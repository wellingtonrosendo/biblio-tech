from project.repositories.category_repository import CategoryRepository
from project.repositories.base_repository import mysql_db
import logging


class CategoryService():

    def list_categories(self):
        categories = CategoryRepository().list_category()
        return {"categories": categories}

    def get_category(self, public_id):
        category = CategoryRepository().get_category(public_id)
        return {"categories": category}

    def create_category(self, data):
        with mysql_db.atomic() as transaction:
            try:
                category = CategoryRepository().create_category(data)
                return {"category": category.public_id}
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return ex

    def update_category(self, id, data):
        with mysql_db.atomic() as transaction:
            try:
                category = CategoryRepository().get_category(id)
                upd_category = CategoryRepository().update_category(category, data)
                print(upd_category)
                return {"category": upd_category}
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return ex

    def delete_category(self, id):
        category = CategoryRepository().get_category(id)
        result = CategoryRepository().delete_category(category)
        return {"category": result}
