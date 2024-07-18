markdownCopy# FastAPI TODO App with PostgreSQL

This repository contains a simple TODO application built with FastAPI and PostgreSQL. It allows you to manage tasks with basic CRUD operations (Create, Read, Update, Delete).

## Features

- Add new tasks
- Mark tasks as completed
- Retrieve all tasks
- Retrieve completed tasks
- Delete specific tasks
- Delete completed tasks
- Clear all tasks
- Clear all completed tasks

## Prerequisites

- Python 3.8+
- PostgreSQL

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>

Install dependencies:
bashCopypip install -r requirements.txt

Set up the PostgreSQL database:

Install PostgreSQL if you haven't already
Open the PostgreSQL shell or your preferred SQL client
Run the following commands:
sqlCopyCREATE DATABASE todo_db;
CREATE USER fastapi_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE todo_db TO fastapi_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO fastapi_user;



Configure the database connection:

Open database.py
Update the DATABASE_URL with your PostgreSQL credentials:
pythonCopyDATABASE_URL = "postgresql://fastapi_user:password@localhost/todo_db"




Running the Application

Start the FastAPI server:
bashCopyuvicorn main:app --reload

Open your browser and go to http://localhost:8000/docs to access the Swagger UI and interact with the API.

API Endpoints

POST /add_entry: Add a new task
POST /add_complete_entry/{index}: Mark a task as completed
GET /get_completed_entries: Retrieve all completed tasks
GET /get_entries: Retrieve all tasks
DELETE /delete_entry/{index}: Delete a specific task
DELETE /delete_completed_entry/{index}: Delete a completed task
DELETE /clear_entries: Clear all tasks
DELETE /clear_completed_entries: Clear all completed tasks

Project Structure

main.py: FastAPI application and route definitions
database.py: Database configuration and connection setup
requirements.txt: List of Python dependencies

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
