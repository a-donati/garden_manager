# plants_tab.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class PlantsTab:
    def __init__(self, parent, bll, user_id):
        self.parent = parent
        self.bll = bll
        self.user_id = user_id  
        self.plant_garden_var = tk.StringVar()
        
        # Initialize UI components for the plants tab
        self.init_plant_ui()

    def init_plant_ui(self):
        frame = ttk.Frame(self.parent)
        frame.pack(padx=10, pady=10)

        self.plant_entries = {}

        labels = [
            "Garden", "Name", "Type",
            "Planted Date (YYYY-MM-DD)", "Quantity"
        ]

        for idx, label in enumerate(labels):
            ttk.Label(frame, text=label + ":").grid(row=idx, column=0, sticky="e", padx=5, pady=2)

            if label == "Type":
                plant_type_combobox = ttk.Combobox(frame, values=["Flower", "Vegetable"], state="readonly")
                plant_type_combobox.grid(row=idx, column=1, padx=5, pady=2)
                self.plant_entries[label] = plant_type_combobox
            else:
                entry = ttk.Entry(frame)
                entry.grid(row=idx, column=1, padx=5, pady=2)
                self.plant_entries[label] = entry

        self.plant_garden_dropdown = ttk.Combobox(frame, textvariable=self.plant_garden_var)
        self.plant_garden_dropdown.grid(row=0, column=1, padx=5, pady=2)

        ttk.Button(frame, text="Add Plant", command=self.add_plant).grid(row=len(labels), column=0, columnspan=2, pady=10)

        # View filter UI BELOW add plant section, above the treeview
        ttk.Label(frame, text="View Plants in Garden:").grid(row=len(labels)+1, column=0, sticky="e", padx=5, pady=5)
        self.view_garden_var = tk.StringVar()
        self.view_garden_dropdown = ttk.Combobox(frame, textvariable=self.view_garden_var, state="readonly")
        self.view_garden_dropdown.grid(row=len(labels)+1, column=1, padx=5, pady=5)
        self.view_garden_dropdown.bind("<<ComboboxSelected>>", self.on_view_garden_selected)

        # Shared treeview
        self.plant_tree = ttk.Treeview(frame, columns=("Name", "Type", "Date", "Quantity"), show="headings")
        for col in self.plant_tree["columns"]:
            self.plant_tree.heading(col, text=col)
        self.plant_tree.grid(row=len(labels)+2, column=0, columnspan=2, pady=10)
        
        ttk.Button(frame, text="Remove Selected Plant", command=self.remove_selected_plant).grid(row=len(labels)+3, column=0, columnspan=2, pady=10)

    def on_view_garden_selected(self, event):
        self.refresh_plant_list()
        
    def refresh_plant_garden_dropdown(self):
        gardens = self.bll.get_gardens_for_user(self.user_id)
        garden_names = [garden['garden_name'] for garden in gardens]

        # Populate dropdowns
        self.plant_garden_dropdown['values'] = garden_names
        self.view_garden_dropdown['values'] = garden_names

        if garden_names:
            self.view_garden_var.set(garden_names[0])
            self.on_view_garden_selected(None)

    def add_plant(self):
        garden_name = self.plant_garden_var.get()
        name = self.plant_entries["Name"].get()
        plant_type = self.plant_entries["Type"].get()
        date_planted = self.plant_entries["Planted Date (YYYY-MM-DD)"].get()
        quantity = self.plant_entries["Quantity"].get()

        garden_id = self.bll.get_garden_id_by_name(garden_name)

        if not garden_id:
            messagebox.showerror("Error", "Invalid garden selected.")
            return

        if all([garden_name, name, plant_type, date_planted, quantity]):
            success, message = self.bll.add_plant_to_garden(
                garden_id, name, plant_type, self.user_id, date_planted, quantity
            )
            if success:
                self.clear_plant_entries()

                # Refresh plant list based on selected view dropdown
                self.on_view_garden_selected(None)
            else:
                messagebox.showerror("Error", message)
    def remove_selected_plant(self):
        print("remove_selected_plant() called") 
        sel = self.plant_tree.selection()
        print("Selected:", sel)  
        if not sel:
            messagebox.showwarning("Select Plant", "Please select a plant to remove.")
            return

        # Extract plant name from the first column of the selected row
        plant_name = self.plant_tree.item(sel[0], 'values')[0]
        print("Selected row values:", self.plant_tree.item(sel[0], 'values'))

        garden_name = self.view_garden_var.get()
        # get_plant_id = self.bll.get_plant_id_by_name(garden_name)
        success, msg = self.bll.remove_plant_by_name(plant_name, garden_name, self.user_id)
        if success:
            self.refresh_plant_list()
        else:
            messagebox.showerror("Error", msg)

    def clear_plant_entries(self):
        for label, entry in self.plant_entries.items():
            if isinstance(entry, ttk.Combobox):
                entry.set('')  # Clear dropdown
            else:
                entry.delete(0, tk.END)  # Clear text entry

    def refresh_plant_list(self):
        # Clear existing entries in the treeview
        self.plant_tree.delete(*self.plant_tree.get_children())

        garden_name = self.view_garden_var.get()
        all_plants = self.bll.get_plants_in_garden(self.user_id)

        # Filter plants based on the selected garden
        plants = [plant for plant in all_plants if plant['garden_name'] == garden_name]

        if not plants:
            # If no plants are found, display a message in the treeview
            self.plant_tree.insert("", "end", values=("No plants found", "", "", ""))
        else:
            # Insert plant data into the treeview
            for plant in plants:
                self.plant_tree.insert("", "end", values=(
                    plant['plant_name'],
                    plant['plant_type'],
                    plant['date_added'],
                    plant['quantity']
                ))

