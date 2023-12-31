from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_ninja import Ninja

db = 'dojos_and_ninjas_schema'

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        data = {'id':dojo_id}
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos (name)
                VALUE ( %(name)s)
                """
        results = connectToMySQL(db).query_db(query, data)
        return results


    @classmethod
    def update(cls, form_data, dojo_id):
        query = f"UPDATE dojos SET name = %(name)s WHERE id = {dojo_id}"
        results = connectToMySQL(db).query_db(query, form_data)
        return results


    @classmethod
    def delete(cls, data):
        query = "DELETE from dojos WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('ninjas').query_db(query, data)


    @classmethod
    def get_dojo_with_ninjas( cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db['first_name'],
                "last_name" : row_from_db['last_name'],
                "age" : row_from_db["age"],
                "created_at" : row_from_db['ninjas.created_at'],
                "updated_at" : row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo