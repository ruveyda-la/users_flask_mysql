# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:

    db="users"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
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



