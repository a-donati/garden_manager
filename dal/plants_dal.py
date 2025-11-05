import mysql.connector

class PlantsDAL:
    def __init__(self, db_connection):
        self.mydb = db_connection.mydb
        self.mycursor = db_connection.mycursor  
    
    # Add plant to garden
    def call_add_plant_to_garden_procedure(self, garden_id, plant_name, plant_type, user_id, date_added, quantity):
        try:
            args = [garden_id, plant_name, plant_type,
                    user_id, date_added, quantity]
            print(f"Calling AddPlantToGarden with args: {args}")

            self.mycursor.callproc('AddPlantToGarden', args)
            self.mydb.commit()
            return True

        except mysql.connector.Error as err:
            print(f"Stored procedure execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return False
        except Exception as e:
            print(
                f"Python exception in call_add_plant_to_garden_procedure: {e}")
            return False
        
    # Get plant ID by name
    def get_plant_id_by_name(self, plant_name):
        try:
            self.mycursor.execute("SELECT GetPlantIdByName(%s)", (plant_name,))
            result = self.mycursor.fetchone()
            # Return the plant ID or None if not found
            return result[0] if result else None
        except mysql.connector.Error as err:
            print(f"Error calling function: {err}")
            return None
        except Exception as e:
            print(f"Python exception in get_plant_id_by_name: {e}")
            return None
    
    # Update plant
    def update_plant(self, plant_id, plant_name, plant_type, image_path):
        try:
            args = [plant_id, plant_name, plant_type, image_path]
            print(f"Calling UpdatePlant with args: {args}")
            self.mycursor.callproc('UpdatePlant', args)
            self.mydb.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Stored procedure execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return False
        except Exception as e:
            print(f"Python exception in call_update_plant: {e}")
            return False
   
    def remove_plant_from_garden(self, garden_id, plant_id, user_id):
        try:
            self.mycursor.callproc('RemovePlantFromGarden', (garden_id, plant_id, user_id))
            self.mydb.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error removing plant: {err}")
            return False
