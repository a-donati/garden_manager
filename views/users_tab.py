# plants_tab.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class UsersTab:
    def __init__(self, parent, bll, user_id):
        self.parent = parent
        self.bll = bll
        self.user_id = user_id
        self.init_user_ui()

    def init_user_ui(self):
        frame = ttk.Frame(self.parent)
        frame.pack(padx=10, pady=10)

        # Dropdown to select garden
        ttk.Label(frame, text="View Users Assigned to Garden:").grid(row=0, column=0, sticky="e")
        self.view_garden_var = tk.StringVar()
        self.view_garden_dropdown = ttk.Combobox(frame, textvariable=self.view_garden_var, state="readonly")
        self.view_garden_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.view_garden_dropdown.bind("<<ComboboxSelected>>", self.on_garden_selected)

        # Treeview to show users
        self.user_tree = ttk.Treeview(frame, columns=("Username"), show="headings")
        # self.user_tree.heading("User ID", text="User ID")
        self.user_tree.heading("Username", text="Username")
        self.user_tree.grid(row=1, column=0, columnspan=2, pady=10)

        # Fields to add user to garden
        ttk.Label(frame, text="User ID:").grid(row=2, column=0, sticky="e")
        self.user_id_entry = ttk.Entry(frame)
        self.user_id_entry.grid(row=2, column=1)

        ttk.Button(frame, text="Add User to Garden", command=self.add_user_to_garden).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Remove Selected User", command=self.remove_selected_user).grid(row=4, column=0, columnspan=2, pady=10)

        self.refresh_garden_dropdown()

    def refresh_garden_dropdown(self):
        gardens = self.bll.get_gardens_for_user(self.user_id)
        garden_names = [g['garden_name'] for g in gardens]
        self.view_garden_dropdown['values'] = garden_names
        if garden_names:
            self.view_garden_var.set(garden_names[0])
            self.on_garden_selected(None)

    def on_garden_selected(self, event):
        self.refresh_user_list()

    def refresh_user_list(self):
        self.user_tree.delete(*self.user_tree.get_children())
        garden_name = self.view_garden_var.get()
        garden_id = self.bll.get_garden_id_by_name(garden_name)
        users = self.bll.get_users_in_garden(garden_name)
        for user in users:
            self.user_tree.insert("", "end", values=(user["username"],))

    def add_user_to_garden(self):
        try:
            user_id = int(self.user_id_entry.get())
        except ValueError:
            messagebox.showerror("Error", "User ID must be an integer.")
            return
    
    
        garden_name = self.view_garden_var.get()
        garden_id = self.bll.get_garden_id_by_name(garden_name)
        success = self.bll.add_user_to_garden(user_id, garden_id)
        if success:
            messagebox.showinfo("Success", "User added to garden.")
            self.refresh_user_list()
        else:
            messagebox.showerror("Error", "Failed to add user to garden.")
    def remove_selected_user(self):
        selected_item = self.user_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No user selected.")
            return

        user_values = self.user_tree.item(selected_item, "values")
        if len(user_values) < 1:
            messagebox.showerror("Error", "Unable to get selected user.")
            return

        try:
            user_id = int(user_values[0]) # user id might not be the first column, this feature doesn't work right now 
        except ValueError:
            messagebox.showerror("Error", "Invalid User ID.")
            return

        garden_name = self.view_garden_var.get()
        garden_id = self.bll.get_garden_id_by_name(garden_name)

        if not garden_id:
            messagebox.showerror("Error", "Garden not found.")
            return

        confirm = messagebox.askyesno("Confirm", f"Remove user ID {user_id} from {garden_name}?")
        if confirm:
            success = self.bll.remove_user_from_garden(user_id, garden_id)
            if success:
                messagebox.showinfo("Success", f"User ID {user_id} removed.")
                self.refresh_user_list()
            else:
                messagebox.showerror("Error", "Failed to remove user.")


