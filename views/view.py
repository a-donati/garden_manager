import tkinter as tk
from tkinter import ttk, messagebox
from bll.bll import BusinessLogicLayer
from dal.dal import DataAccessLayer
from views.plants_tab import PlantsTab 
from views.gardens_tab import GardensTab
from views.users_tab import UsersTab
import os
from dotenv import load_dotenv

class GardenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Garden Manager")
        self.root.geometry("800x800")
        
        # Load environment variables from .env file
        load_dotenv()

        # Grab the database credentials from the environment variables
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_database = os.getenv('DB_DATABASE')
        if not db_user or not db_password or not db_database:
                messagebox.showerror("Error", "Database credentials are missing from the .env file.")
                return

        config = {'user': db_user, 'password': db_password, 'database': db_database}
        self.data_access_layer = DataAccessLayer(**config)
        self.bll = BusinessLogicLayer(self.data_access_layer)

        self.username = None
        self.user_id = None

        self.build_login_screen()
        
        # config = {'user': 'root', 'password': 'db123456', 'database': 'garden'}
        # self.data_access_layer = DataAccessLayer(**config)
        # self.bll = BusinessLogicLayer(self.data_access_layer)

        # self.username = None
        # self.user_id = None

        # self.build_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def build_login_screen(self):
        self.clear_screen()

        # Welcome message with intro text
        welcome_message = "Welcome to Garden Manager - A garden database management app.\nCreate an account or log in to start managing your gardens & plants."
        intro_label = tk.Label(self.root, text=welcome_message, font=("Helvetica", 12), justify='center')
        intro_label.pack(pady=20)

        # Optional flower emojis or an image above the login
        emoji_label = tk.Label(self.root, text="🌸🌼🌻", font=("Helvetica", 24), justify='center')
        emoji_label.pack(pady=10)

        # Username and Password fields
        tk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Login and Create User buttons
        ttk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        ttk.Button(self.root, text="Create User", command=self.create_user).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_data = self.bll.authenticate_user(username, password)
        if user_data:
            self.user_id = user_data['user_id']
            self.username = username
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def create_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success = self.bll.create_user(username, password)
        if success:
            messagebox.showinfo("Success", "User created. You can now log in.")
        else:
            messagebox.showerror("Error", "Username may already exist.")

    def show_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Welcome, {self.username}!", font=("Helvetica", 14)).pack(pady=10)
        # Log Out button in top-left corner
        self.logout_button = ttk.Button(self.root, text="Log Out", command=self.logout)
        self.logout_button.place(x=10, y=10)  

        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both')
        notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

        self.garden_tab = ttk.Frame(notebook)
        self.plant_tab = ttk.Frame(notebook)
        self.users_tab = ttk.Frame(notebook)

        notebook.add(self.garden_tab, text="Gardens")
        notebook.add(self.plant_tab, text="Plants")
        notebook.add(self.users_tab, text="Users")

        self.build_garden_tab()
        self.build_plant_tab()
        self.build_users_tab()

    def logout(self):
        # Clear the session (username and user_id) and go back to login screen
        self.username = None
        self.user_id = None
        self.build_login_screen()

    def on_tab_changed(self, event):
        selected_tab = event.widget.tab(event.widget.index("current"))["text"]
        
        if selected_tab == "Plants":
            self.plants_tab.refresh_plant_garden_dropdown()
            self.plants_tab.refresh_plant_list()  
        if selected_tab == "Users":
            self.users_tab.refresh_garden_dropdown()
            self.users_tab.refresh_user_list()

    def build_garden_tab(self):

        self.gardens_tab = GardensTab(self.garden_tab, self.bll, self.user_id, self.plant_tab)

    def view_plants_in_garden(self, garden_name):
        # Get garden ID and plant list from BLL
        garden_id = self.bll.get_garden_id_by_name(garden_name, self.user_id)
        plants = self.bll.get_plants_for_garden(garden_id)

        # Create new window
        plant_window = tk.Toplevel(self.root)
        plant_window.title(f"Plants in {garden_name}")
        plant_window.geometry("400x300")

        if not plants:
            tk.Label(plant_window, text="No plants found in this garden.").pack(pady=10)
            return

        for plant in plants:
            info = f"{plant['plant_name']} ({plant['plant_type']})"
            tk.Label(plant_window, text=info).pack(anchor='w', padx=10, pady=2)

    def build_plant_tab(self):
        # Initialize the PlantsTab and pass the BLL and parent frame
        self.plants_tab = PlantsTab(self.plant_tab, self.bll, self.user_id)
        
        # Call the function to refresh the garden dropdown list
        self.plants_tab.refresh_plant_garden_dropdown()

    def build_users_tab(self):
        self.users_tab = UsersTab(self.users_tab, self.bll, self.user_id)
        
    def refresh_plant_dropdown(self):
        self.plants_tab.refresh_plant_garden_dropdown()
        


