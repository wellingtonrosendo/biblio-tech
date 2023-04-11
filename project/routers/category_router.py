# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from project.services.category_service import CategoryService


category_router = Blueprint('category_router', __name__)


@category_router.route("/category", methods=["GET"])
def get_all_category():
    category = CategoryService().list_categories()
    return category


@category_router.route("/category/<id>", methods=["GET"])
def get_category(id):
    category = CategoryService().get_category(id)
    return category


@category_router.route("/category", methods=["POST"])
def create_category():
    data = json.loads(request.data)
    return CategoryService().create_category(data)


@category_router.route("/category/<id>", methods=["PUT"])
def update_category(id):
    data = json.loads(request.data)
    category = CategoryService().update_category(id, data)
    return category


@category_router.route("/category", methods=["DELETE"])
def delete_category(data):
    data = json.loads(request.data)
    category = CategoryService().delete_category(data)
    return category
