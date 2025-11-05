# Garden Manager App 🌱

Welcome to the **Garden Manager** app! This is a Tkinter-based application for managing gardens, plants, and users. You can create and manage gardens, add/remove plants, and manage users assigned to gardens.

## Features
- **Log in/Create User**: Easily log into your account or create a new one.
- **Garden Management**: Add new gardens, view all gardens, and manage which plants are assigned to which gardens.
- **Plant Management**: Add and view plants assigned to a garden.
- **User Management**: View and manage which users are assigned to a garden.
  
### Upcoming Features (Work in Progress)
- **Update Plant**: Add the ability to update plant details.
- **Remove User from Garden**: This feature is currently not working, but it's on the roadmap.
- **Update Garden**: Add the ability to update garden details.
- **Update User**: Add the ability to update user details.
- **View All Gardens**: Currently, gardens are only shown when you interact with them.
- **View All My Plants**: Add the ability to list of all plants you have worked with/added, not just the ones in a garden.
- **Add images for plants**: Add the ability to add images for plants

## Requirements
Before running the app, make sure you have the following Python packages installed:

### Required Packages
- `tkinter` (for the UI)
- `mysql-connector-python` (for database interaction)
- `python-dotenv` (for loading environment variables from a `.env` file)

You can install them using `pip`:
`pip install tkinter mysql-connector-python python-dotenv`
OR

Install the Dependencies through the requirements text file:
Run the following command in your terminal:
`pip install -r requirements.txt`

### Environment Variables
To connect to the database, configure the provided .env file that contains the following information:

- DB_USER: Your MySQL username

- DB_PASSWORD: Your MySQL password

- DB_DATABASE: The name of your database (in the provided SQL file, the DB name is garden)

Example .env file:
DB_USER=your_username
DB_PASSWORD=your_password
DB_DATABASE=garden_manager_db

### How to Run the App

- Configure the .env File:
    Update the .env file in the project directory with your database credentials.
- Ensure that dependencies are installed
    `pip install -r requirements.txt`
- Run the Application:
    Start the app by running main.py `python main.py` or `python3 main.py`

This will launch the Tkinter GUI where you can log in, create a new user, and manage your garden and plants.

There is test user information inserted into the DB that can be used for login:
user1, password: password1
user2, password: password2
user3, password: password3
user4, password: password4
user5, password: password5
user6, password: password6
user7, password: password7
user8, password: password8
user9, password: password9
user10, password: password10


### Using the App

- After logging in, the user is brought to their Gardens tab. If there are gardens associated with the user, they will populate on the screen.
**Adding a new garden**: Type the desired garden name into the text box to the left of Create Garden button. Press the Create Garden button to add the garden. 
**Deleting a garden**: Select the name of the garden you wish to delete by clicking on the garden name and then press Delete Garden. A pop up will display a confirmation message and then a success message upon successful deletion of the garden.

- When accessing the plants tab, use the dropdown selector next to the View Plants in Garden text in order to view plants within a garden.
**Adding a new plant**: Select the garden to add the new plant to, enter the plant name, select the type from the dropdown, enter the year in YYYY-MM-DD format, and the quantity planted. Press "Add Plant". Select the garden from View Plants in Garden option to view the newly added plant entry.
**Removing a plant**: Select the name of the plant you wish to delete by clicking on the plant name and then press "Remove Selected Plant". Select the garden from View Plants in Garden dropdown to see an updated list of plants. 

-When accessing the users tab, use the dropdown to select a garden to see all of the users assigned to the garden that your account is associated with.
**Add User to Garden**: At this time, this feature is not user friendly, since you have to add the User id of the user you would like to add to the garden. I will be working on adding user by username in this section rather than by ID.
**Remove Selected User**: At this time, this feature isn't functioning. If it was, you could select the username from the list and press Remove Selected User button.

### Known Issues
Delete User from Garden: This feature is not working at the moment. It's currently on hold and will be worked on in the future.

Missing Features: As mentioned, there are several features like updating plants, gardens, and users that were planned but not implemented before the deadline. I will work on them during my break from class this summer.

Accessibility Concerns: I did not have the time to check the colors of the app in a contrast checker or assess my app for accessibility. This is another aspect that I would like to focus on during my updates. 

## File Structure

garden_manager/
├── views/
│   ├── plants_tab.py
│   ├── gardens_tab.py
│   └── users_tab.py
|   ├── view.py
├── bll/
│   ├── bll.py
├── dal/
│   ├── dal.py
|   ├── gardens_dal.py
|   ├── plants_dal.py
├── .env
├── main.py
├── requirements.txt
└── README.md


