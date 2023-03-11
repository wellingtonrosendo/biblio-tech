# -*- coding: utf-8 -*-
from flask import Flask

# import routers
from project.routers.category_router import category_router
from project.repositories.base_repository import mysql_db

app = Flask(__name__)

app.config["DATABASE"] = mysql_db


@app.before_request
def _db_connect():
    mysql_db.connect()


@app.teardown_request
def _db_close(exc):
    if not mysql_db.is_closed():
        mysql_db.close()


app.register_blueprint(category_router)
