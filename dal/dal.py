import mysql.connector


class DataAccessLayer:
    def __init__(self, user, password, database):
        try:
            self.mydb = mysql.connector.connect(
                user=user,
                password=password,
                database=database
            )
            self.mycursor = self.mydb.cursor()  # Initialize the cursor here
            print("Database connection established.")
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            self.mydb = None  # Set to None if connection fails
            self.mycursor = None  # Also set cursor to None

    def disconnect(self):
        if self.mydb:
            self.mycursor.close()
            self.mydb.close()
            print("Database connection closed.")

    def authenticate_user(self, username, password):
        try:
            args = [username, password]
            print(f"Calling AuthenticateUser with args: {args}")

            self.mycursor.callproc('AuthenticateUser', args)
            results = self.mycursor.stored_results()
            for result in results:
                data = result.fetchall()
                if data:
                    user_id = data[0][0]
                    username = data[0][1]
                    user = {'user_id': user_id, 'username': username}
                    print(f"User: {user}")
                    return user
            print("AuthenticateUser returned None. Possible error.")
            return None
        except mysql.connector.Error as err:
            print(f"Stored procedure execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return None
        except Exception as e:
            print(f"Python exception in call_authenticate_user: {e}")
            return None

    def create_user(self, username, password):
        try:
            args = [username, password]
            print(f"Calling CreateUser with args: {args}")

            self.mycursor.callproc('CreateUser', args)
            self.mydb.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Stored procedure execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return False
        except Exception as e:
            print(f"Python exception in call_create_user: {e}")
            return False

