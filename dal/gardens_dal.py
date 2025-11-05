import mysql.connector


class GardensDAL:
    def __init__(self, db_connection):
        self.mydb = db_connection.mydb
        self.mycursor = db_connection.mycursor
    
    def create_garden(self, garden_name, owner_id):
        try:
            args = [garden_name, owner_id]
            print(f"Calling CreateGarden with args: {args}")

            self.mycursor.callproc('AddGarden', args)
            self.mydb.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Stored procedure execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return False
        except Exception as e:
            print(f"Python exception in call_create_garden: {e}")
            return False

    def add_user_to_garden(self, user_id, garden_id):
        try:
            args = [user_id, garden_id]
            print(f"Calling AddUserToGarden with args: {args}")

            self.mycursor.callproc('AddUserToGarden', args)
            self.mydb.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Stored procedure execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return False
        except Exception as e:
            print(f"Python exception in call_add_user_to_garden: {e}")
            return False

    def remove_user_from_garden(self, user_id, garden_id):
        print(f"Executing SQL to remove user ID {user_id} from garden ID {garden_id}")
        
        try:
            # Assuming this is the query for removing the user from the garden
            cursor = self.db_connection.cursor()
            cursor.callproc('RemoveUserFromGarden', (user_id, garden_id))

            # Fetch the result of the stored procedure call
            result = cursor.fetchone()
            if result:
                print(f"Stored procedure result: {result[0]}")

            self.db_connection.commit()
            
            if cursor.rowcount > 0:
                print(f"Successfully removed {cursor.rowcount} user(s).")
                return True
            else:
                print(f"No user found with user_id {user_id} in garden_id {garden_id}")
                return False
        
        except Exception as e:
            print(f"Error occurred while removing user: {e}")
            return False
        
    def get_gardens_for_user(self, user_id):
        try:
            # Get the username corresponding to the user_id
            self.mycursor.execute(
                'SELECT username FROM Users WHERE user_id = %s', (user_id,))
            user = self.mycursor.fetchone()

            if user is None:
                print(f"No user found with ID {user_id}")
                return []

            username = user[0]  # Get the username from the result

            # Query UserGardens view using the username
            query = 'SELECT garden_name FROM Gardens WHERE owner_id = %s'
            self.mycursor.execute(query, (user_id,))
            gardens = []
            results = self.mycursor.fetchall()  # Fetch all results directly
            for row in results:
                gardens.append({
                    'garden_name': row[0]
                })
            
            print(f"Gardens for user ID {user_id}: {gardens}")
            return gardens
        except mysql.connector.Error as err:
            print(f"Query execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return []
        except Exception as e:
            print(f"Python exception in get_gardens_for_user: {e}")
            return []

    def get_plants_in_garden(self, user_id):
        try:
            print(f"Fetching plants for user_id: {user_id}")

            query = 'SELECT * FROM GetPlantsInGarden WHERE user_id = %s'
            self.mycursor.execute(query, (user_id,))  # Pass user_id as a tuple
            plants = self.mycursor.fetchall()  # Fetch all results directly

            # Process the results
            results = []
            if plants:
                for row in plants:
                    results.append({
                        'garden_name': row[1],
                        'plant_name': row[2],
                        'plant_type': row[3],
                        'image_path': row[4],
                        'date_added': row[5],
                        'quantity': row[6],
                        # Adjust index based on the new view definition
                        'username': row[8]
                    })
            print(f"Plants: {results}")
            return results
        except mysql.connector.Error as err:
            print(f"SQL execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return []
        except Exception as e:
            print(f"Python exception in get_plants_in_garden: {e}")
            return []

    def get_users_in_garden(self, garden_name):
        try:
            print(f"Fetching users for garden: {garden_name}")
            self.mycursor.callproc('GetGardenUsers', [garden_name])

            results = []
            for result in self.mycursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    results.append({'username': row[0]})  # assuming row[0] is username

            print(f"Users: {results}")
            return results

        except mysql.connector.Error as err:
            print(f"SQL execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return []
        except Exception as e:
            print(f"Python exception in get_users_in_garden: {e}")
            return []




    def get_garden_id_by_name(self, garden_name):
        try:
            # Call the stored procedure to get the garden ID
            self.mycursor.execute("SELECT GetGardenId(%s)", (garden_name,))
            result = self.mycursor.fetchone()
            return result[0] if result else None
        except mysql.connector.Error as err:
            print(f"Error executing stored procedure: {err}")
            return None
        except Exception as e:
            print(f"Python exception in get_garden_id_by_name: {e}")
            return None
    # def get_garden_id_by_name(self, garden_name, user_id):
    #     try:
    #         # Modify the stored procedure call to consider both garden_name and user_id
    #         self.mycursor.execute("SELECT GetGardenId(%s, %s)", (garden_name, user_id))
    #         result = self.mycursor.fetchone()
    #         return result[0] if result else None
    #     except mysql.connector.Error as err:
    #         print(f"Error executing stored procedure: {err}")
    #         return None
    #     except Exception as e:
    #         print(f"Python exception in get_garden_id_by_name: {e}")
    #         return None

    def delete_garden(self, garden_id):
        # SQL query to delete the garden by ID
        query = "DELETE FROM gardens WHERE garden_id = %s"
        params = (garden_id,)
        
        # Execute the query
        try:
            self.mycursor.execute(query, params)
            self.mydb.commit()
            return True
        except Exception as e:
            print(f"Error deleting garden: {e}")
            return False
