# gardens_tab.py
import tkinter as tk
from tkinter import ttk, messagebox
from bll.bll import BusinessLogicLayer
from views.plants_tab import PlantsTab


class GardensTab:
    def __init__(self, parent, bll, user_id, plants_tab):
        self.parent = parent
        self.bll = bll
        # self.app = app
        self.user_id = user_id
        self.garden_name_entry = None
        self.garden_listbox = None
        self.plants_tab = plants_tab  # store reference
        self.build_garden_ui()

    def build_garden_ui(self):
        ttk.Label(self.parent, text="Garden Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.garden_name_entry = ttk.Entry(self.parent)
        self.garden_name_entry.grid(row=0, column=1, pady=10)
        # Create Garden button
        ttk.Button(self.parent, text="Create Garden", command=self.create_garden).grid(row=0, column=2, padx=5)
        # Delete Garden button
        ttk.Button(self.parent, text="Delete Garden", command=self.delete_garden).grid(row=1, column=2, padx=5)
        # Display gardens
        ttk.Label(self.parent, text="Your Gardens:").grid(row=1, column=0, columnspan=3)
        self.garden_listbox = tk.Listbox(self.parent, width=50)
        self.garden_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.refresh_garden_list()

    def create_garden(self):
        garden_name = self.garden_name_entry.get()
        success = self.bll.create_garden(garden_name, self.user_id)
        
        if success:
            self.refresh_garden_list()
        else:
            messagebox.showerror("Error", f"Failed to create garden '{garden_name}'")

    def refresh_garden_list(self):
        # Clear existing entries in the listbox
        self.garden_listbox.delete(0, tk.END)

        gardens = self.bll.get_gardens_for_user(self.user_id)

        if not gardens:
            # If no gardens are found, insert a "No gardens found" message
            self.garden_listbox.insert(tk.END, "No gardens found")
        else:
            # Insert each garden name into the listbox
            for garden in gardens:
                self.garden_listbox.insert(tk.END, garden['garden_name'])

    def view_plants_in_garden(self, garden_name):
        garden_id = self.bll.get_garden_id_by_name(garden_name, self.user_id)
        plants = self.bll.get_plants_for_garden(garden_id)

        plant_window = tk.Toplevel(self.parent)
        plant_window.title(f"Plants in {garden_name}")
        plant_window.geometry("400x300")

        if not plants:
            tk.Label(plant_window, text="No plants found in this garden.").pack(pady=10)
            return

        for plant in plants:
            info = f"{plant['plant_name']} ({plant['plant_type']})"
            tk.Label(plant_window, text=info).pack(anchor='w', padx=10, pady=2)
    def delete_garden(self):
        # Get the selected garden from the listbox
        selected_garden = self.garden_listbox.get(tk.ACTIVE)
        
        if not selected_garden:
            messagebox.showerror("Error", "No garden selected.")
            return

        # Confirm the deletion
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the garden '{selected_garden}'?"):
            # Only pass the selected garden name and let the method handle the user ID
            garden_id = self.bll.get_garden_id_by_name(selected_garden)
            
            if garden_id:
                # Delete the garden
                success = self.bll.delete_garden(garden_id)
                
                if success:
                    messagebox.showinfo("Success", f"Garden '{selected_garden}' deleted successfully.")
                    self.refresh_garden_list()  # Refresh the garden list
                    self.plants_tab.refresh_plant_garden_dropdown()  
                else:
                    messagebox.showerror("Error", "Failed to delete the garden.")
            else:
                messagebox.showerror("Error", "Garden not found.")
