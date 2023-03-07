# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    db="users"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_user(user):
        items = User.get_all()
        is_valid = True
        if len(user['first_name'])<1:
            flash("First name is required.")
            is_valid = False
        if len(user['last_name'])<1:
            flash("Last name is required.")
            is_valid = False
        if len(user['email'])<1:
            flash("First name is required.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        for item in items:
            if item.email == user['email']:
                flash("Email is already registered")
                is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        query = """INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema name you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of results with cls.
        for result in results:
            users.append( cls(result) )
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return result[0]

    @classmethod
    def change(cls,data):
        query="""UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s,
                email=%(email)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete_user(cls,data):
        query="DELETE FROM users WHERE id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return result



