# bll.py
from dal.dal import DataAccessLayer
from dal.gardens_dal import GardensDAL
import mysql
from dal.plants_dal import PlantsDAL


class BusinessLogicLayer:
    def __init__(self, data_access_layer):
        self.dal = data_access_layer
        self.gardens_dal = GardensDAL(
            data_access_layer)  # Instantiate GardensDAL
        self.plants_dal = PlantsDAL(data_access_layer)

    def authenticate_user(self, username, password):
        user_data = self.dal.authenticate_user(username, password)
        return user_data

    def create_user(self, username, password):
        return self.dal.create_user(username, password)

    def get_gardens_for_user(self, user_id):
        gardens = self.gardens_dal.get_gardens_for_user(user_id)
        return gardens

    def create_garden(self, garden_name, owner_id):
        return self.gardens_dal.create_garden(garden_name, owner_id)
    def delete_garden(self, garden_name):
        return self.gardens_dal.delete_garden(garden_name)
    def add_plant_to_garden(self, garden_id, plant_name, plant_type, user_id, date_added, quantity):
        try:
            args = [garden_id, plant_name, plant_type,
                    user_id, date_added, quantity]
            print(f"Calling AddPlantToGarden with args: {args}")

            # Call the Data Access Layer method
            success = self.plants_dal.call_add_plant_to_garden_procedure(*args)
            if success:
                message = "Plant added successfully."
            else:
                message = "Failed to add plant to garden."

            return success, message  # Return both success and message

        except mysql.connector.Error as err:
            print(f"Stored procedure execution error: {err}")
            print(f"MySQL error code: {err.errno}")
            print(f"MySQL error message: {err.msg}")
            return False, str(err)  # Return False and the error message
        except Exception as e:
            print(f"Python exception in add_plant_to_garden: {e}")
            return False, str(e)  # Return False and the error message

    def get_plants_in_garden(self, garden_id):
        plants = self.gardens_dal.get_plants_in_garden(garden_id)
        return plants

    def update_plant(self, plant_id, plant_name, plant_type, image_path):
        success = self.plants_dal.update_plant(
            plant_id, plant_name, plant_type, image_path)
        if success:
            return success, "Plant updated successfully."
        else:
            return False, "Failed to update plant."

    def remove_plant_from_garden(self, plant_id):
        success = self.plants_dal.remove_plant_from_garden(plant_id)
        if success:
            return success, "Plant removed successfully."
        else:
            return False, "Failed to remove plant."

    def add_user_to_garden(self, user_id, garden_id):
        return self.gardens_dal.add_user_to_garden(user_id, garden_id)

    def remove_user_from_garden(self, user_id, garden_id):
        print(f"Attempting to remove user ID {user_id} from garden ID {garden_id}")
        
        success = self.garden_dal.remove_user_from_garden(user_id, garden_id)
        
        if not success:
            print(f"Failed to remove user ID {user_id} from garden ID {garden_id}")
        else:
            print(f"User ID {user_id} successfully removed from garden ID {garden_id}")
        
        return success

    def get_users_in_garden(self, garden_name):
        return self.gardens_dal.get_users_in_garden(garden_name)

    def update_plant_by_name(self, plant_name, new_name, new_type, new_image_path):
        plant_id = self.plants_dal.get_plant_id_by_name(
            plant_name.lower())  # Call the function with lowercased name
        if plant_id == -1:
            return False, "Plant not found."

        success = self.plants_dal.update_plant(
            plant_id, new_name, new_type, new_image_path)
        if not success:
            return False, "Failed to update plant."
        return True, "Plant updated successfully."


    def remove_plant_by_name(self, plant_name, garden_name, user_id):
        print(f"Removing plant: {plant_name} from garden: {garden_name}, user_id: {user_id}")

        # 1) look up garden_id
        garden_id = self.get_garden_id_by_name(garden_name)
        print(f"Resolved garden_id: {garden_id}")
        if not garden_id:
            print("Garden not found")
            return False, f"Garden '{garden_name}' not found."

        # 2) look up plant_id
        plant_id = self.plants_dal.get_plant_id_by_name(plant_name)
        print(f"Resolved plant_id: {plant_id}")
        if not plant_id:
            print("Plant not found")
            return False, f"Plant '{plant_name}' not found in '{garden_name}'."

        # 3) call the removal proc
        success = self.plants_dal.remove_plant_from_garden(garden_id, plant_id, user_id)
        print(f"Remove success: {success}")
        if not success:
            return False, "Failed to remove plant from database."

        return True, f"Removed '{plant_name}' from '{garden_name}'."



    def get_plant_id_by_name(self, plant_name):
        return self.plants_dal.get_plant_id_by_name(plant_name.lower())
    def get_garden_id_by_name(self, garden_name):
        try:
            # Call stored procedure to get garden ID based on garden name
            result = self.gardens_dal.get_garden_id_by_name(garden_name)
            return result if result else None
        except Exception as e:
            print(f"Error retrieving garden ID: {e}")
            return None
