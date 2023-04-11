
from peewee import CharField, DateField, fn
from project.repositories.base_repository import BaseRepository
from playhouse.shortcuts import dict_to_model, model_to_dict
from uuid import uuid4


class AuthorRepository(BaseRepository):

    id = CharField()
    name = CharField()
    created_at = DateField()
    updated_at = DateField()
    deleted_at = DateField()

    class Meta:
        table_name = 'author'

    def get_author(self):
        author = list(AuthorRepository().select().dicts())
        return author

    def create_author(self, data):
        data["id"] = uuid4()
        try:
            author = AuthorRepository().create(**data)
            print(author)
            return {"sucesso": "Autor cadastrado com sucesso", "autor": author}
        except Exception as ex:
            print(ex)
            return {"erro": "Erro ao cadastrar", "status": ex}

    def update_author(self, author, data):
        author_dict = model_to_dict(author)
        try:
            for key in data.keys():
                author_dict[key] = data[key]
            author = dict_to_model(AuthorRepository, author_dict)
            author.save()
            return {"sucesso": "Autor arualizado com sucesso", "autor": author}
        except Exception as ex:
            return {"erro": "Erro ao atualizar", "status": ex}

    def delete_author(self, data):
        return {}
