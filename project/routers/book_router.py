# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from project.services.movie_service import MovieService


movie_router = Blueprint('file_router', __name__)


@movie_router.route("/movie", methods=["GET"])
def get_movie():
    movie = MovieService().get_movie()
    return movie


@movie_router.route("/movie", methods=["POST"])
def create_movie(data):
    data = json.loads(request.data)
    movie = MovieService().create_movie(data)
    return movie


@movie_router.route("/movie", methods=["PUT"])
def update_movie(data):
    data = json.loads(request.data)
    movie = MovieService().update_movie(data)
    return movie


@movie_router.route("/movie", methods=["DELETE"])
def delete_movie(data):
    data = json.loads(request.data)
    movie = MovieService().delete_movie(data)
    return movie
