# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
DATABASE = "users"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def create(cls, data ):
        query = 'INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );'
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_one(cls, data:dict):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)



    @classmethod
    def delete_one(cls, data:dict):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
