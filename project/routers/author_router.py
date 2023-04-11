# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from project.services.author_service import AuthorService


author_router = Blueprint('author_router', __name__)


@author_router.route("/author", methods=["GET"])
def get_author():
    author = AuthorService().get_author()
    return author


@author_router.route("/author", methods=["POST"])
def create_author():
    data = json.loads(request.data)
    author = AuthorService().create_author(data)
    return author


@author_router.route("/author", methods=["PUT"])
def update_author():
    data = json.loads(request.data)
    author = AuthorService().update_author(data)
    return author


@author_router.route("/author", methods=["DELETE"])
def delete_author():
    data = json.loads(request.data)
    author = AuthorService().delete_author(data)
    return author
