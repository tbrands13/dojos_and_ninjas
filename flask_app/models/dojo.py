from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def pick_one_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_and_ninjas').query_db(query, data)
        print(results)

        dojo = cls(results[0])

        for db_row in results:
            ninja_data = {
                "id": db_row["id"],
                "first_name": db_row["first_name"],
                "last_name": db_row["last_name"],
                "age": db_row["age"],
                "dojo_id": db_row["dojo_id"],
                "created_at": db_row["created_at"],
                "updated_at": db_row["updated_at"]
            }

            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo


    @classmethod
    def make_dojo(cls,data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s,  NOW(), NOW());'
        results = connectToMySQL('dojo_and_ninjas').query_db(query, data)
        return results


    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))

        return dojos

