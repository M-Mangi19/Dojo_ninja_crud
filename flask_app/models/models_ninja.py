from flask_app.config.mysqlconnection import connectToMySQL


db = 'dojos_and_ninjas_schema'

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        data = {'id':ninja_id}
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUE ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
                """
        results = connectToMySQL(db).query_db(query, data)
        return results


    @classmethod
    def update(cls, form_data, ninja_id):
        query = f"UPDATE ninjas SET name = %(first_name)s, %(last_name)s %(age)s WHERE id = {ninja_id}"
        results = connectToMySQL(db).query_db(query, form_data)
        return results


    @classmethod
    def delete(cls, data):
        query = "DELETE from ninjas WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results


    @classmethod
    def save( cls, data):
        query = """INSERT INTO ninjas ( first_name, last_name, age)
                    VALUES (%(first_name)s, %(last_name)s, %(age)s);
                """
        return connectToMySQL('ninjas').query_db(query, data)
