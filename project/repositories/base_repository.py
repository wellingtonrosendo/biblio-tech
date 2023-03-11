# -*- coding: utf-8 -*-
from peewee import MySQLDatabase, Model
from project.config import Server


mysql_db = MySQLDatabase(Server().MYSQL_DATABASE, user=Server().MYSQL_USER,
                         password=Server().MYSQL_PASSWORD, host=Server().MYSQL_HOST, port=Server().MYSQL_PORT)


class BaseRepository(Model):

    class Meta:
        database = mysql_db
