# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from project.services.book_service import BookService


book_router = Blueprint('book_router', __name__)


@book_router.route("/book", methods=["GET"])
def get_all_book():
    book = BookService().list_book()
    return book


@book_router.route("/book/<id>", methods=["GET"])
def get_book(id):
    category = BookService().get_book(id)
    return category


@book_router.route("/book", methods=["POST"])
def create_book(data):
    data = json.loads(request.data)
    book = BookService().create_book(data)
    return book


@book_router.route("/book", methods=["PUT"])
def update_book(data):
    data = json.loads(request.data)
    book = BookService().update_book(data)
    return book


@book_router.route("/book", methods=["DELETE"])
def delete_book(data):
    data = json.loads(request.data)
    book = BookService().delete_book(data)
    return book


@book_router.route("/book/author", methods=["GET"])
def get_book_author():
    query_string = request.args.get("name")
    book = BookService().get_book_author(query_string)
    return book
