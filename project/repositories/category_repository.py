from peewee import DateField, CharField
from project.repositories.base_repository import BaseRepository
from uuid import uuid4
from playhouse.shortcuts import model_to_dict, dict_to_model


class CategoryRepository(BaseRepository):

    id = CharField()
    name = CharField()
    created_at = DateField()
    updated_at = DateField()
    deleted_at = DateField()

    class Meta:
        table_name = 'category'

    def list_category(self):
        categories = list(CategoryRepository().select().dicts())
        return categories

    def get_category(self, id):
        category = CategoryRepository().select().where(
            CategoryRepository.id == id
        ).dicts().first()
        return category

    def create_category(self, data):
        data["id"] = uuid4()
        create_category = CategoryRepository().create(**data)
        return create_category

    def update_category(self, category, data):
        for key in data.keys():
            category[key] = data[key]
        category = dict_to_model(CategoryRepository, category)
        category.save()
        return category.id

    def delete_category(self, data):
        print(data)
        return {}
