from project.repositories.author_repository import AuthorRepository
from project.repositories.base_repository import mysql_db
import logging


class AuthorService():
    def get_author(self):
        author = AuthorRepository().get_author()
        return {"author": author}

    def create_author(self, data):
        with mysql_db.atomic() as transaction:
            try:
                author = AuthorRepository().create_author(data)
                return {"author": author}
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return ex

    def update_author(self, data):
        with mysql_db.atomic() as transaction:
            try:
                author = AuthorRepository().update_author(data)
                return {"author": author}
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return ex

    def delete_author(self, id):
        author = AuthorRepository().delete_author(id)
        return {"author": author}
