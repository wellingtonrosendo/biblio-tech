import jwt
from project.config import Server
from functools import wraps
from flask import Flask, make_response, jsonify, request
from playhouse.shortcuts import model_to_dict
from project.repositories.api.api_token_repository import ApiTokensRepository


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        authorization = request.headers.get('Authorization')
        if authorization:
            token = authorization.split(" ")[1]
        elif request.headers.get('token'):
            secret_key = request.headers.get('token')
            if secret_key:
                token = ApiTokensRepository.select().where(
                    ApiTokensRepository.token == secret_key).first()
        elif request.headers.get('x-access-token'):
            secret_key = request.headers.get('x-access-token')
            if secret_key:
                token = ApiTokensRepository.select().where(
                    ApiTokensRepository.token == secret_key).first()
        if not token:
            return make_response(jsonify({'message': 'Token missing.'}), 400)
        try:
            if isinstance(token, str):
                data = jwt.decode(token, Server().SECRET_KEY, 'HS256')
            else:
                data = model_to_dict(token)
                data = data["user"]
        except Exception as ex:
            return make_response(jsonify({'message': 'Token is invalid'}), 401)

        return f(data, *args, **kwargs)
    return decorated


def api_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({'message': 'Token is invalid'}), 401)
        try:
            token = ApiTokensRepository.select().where(
                ApiTokensRepository.token == token).first()
            if not token:
                return make_response(jsonify({'message': 'Token is invalid'}), 401)
            data = token
        except Exception as ex:
            return make_response(jsonify({'message': 'Token is invalid'}), 401)
        return f(data, *args, **kwargs)
    return decorated
