FastAPI TODO App with PostgreSQL
This repository contains a simple TODO application built with FastAPI and PostgreSQL. It allows you to manage tasks with basic CRUD operations (Create, Read, Update, Delete).

Features
Add new tasks
Mark tasks as completed
Retrieve all tasks
Delete tasks
Clear all tasks
Setup
Prerequisites
Python 3.8+
PostgreSQL
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <repository_name>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the database:

Create a PostgreSQL database named todo_db.
Create a user with privileges on todo_db.
Update the database URL in database.py with your PostgreSQL credentials.
Run the application:

bash
Copy code
uvicorn main:app --reload
Open your browser and go to http://localhost:8000 to access the FastAPI Swagger UI.

Usage
Use the Swagger UI or any API testing tool (e.g., Postman) to interact with the API endpoints.
Detailed API documentation is available at http://localhost:8000/docs.
API Endpoints
POST /add_entry: Add a new task.
POST /add_complete_entry/{index}: Mark a task as completed.
GET /get_completed_entries: Retrieve all completed tasks.
GET /get_entries: Retrieve all tasks.
DELETE /delete_entry/{index}: Delete a specific task.
DELETE /delete_completed_entry/{index}: Delete a completed task.
DELETE /clear_entries: Clear all tasks.
DELETE /clear_completed_entries: Clear all completed tasks.
Contributing
Contributions are welcome! Please feel free to fork the repository and submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
