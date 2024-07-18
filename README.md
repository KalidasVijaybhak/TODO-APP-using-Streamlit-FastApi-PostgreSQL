# FastAPI TODO App with PostgreSQL

This repository contains a simple TODO application built with FastAPI and PostgreSQL. It allows you to manage tasks with basic CRUD operations (Create, Read, Update, Delete).

## Features

- Add new tasks
- Mark tasks as completed
- Delete  tasks
- Delete completed tasks


## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Set up the PostgreSQL database:

   Install PostgreSQL if you haven't already
   Open the PostgreSQL shell or your preferred SQL client
   Run the following commands:
   ```bash
   CREATE DATABASE todo_db;
   CREATE USER fastapi_user WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE todo_db TO fastapi_user;
   GRANT ALL PRIVILEGES ON SCHEMA public TO fastapi_user;


4. Configure the database connection:

   Open database.py
   Update the DATABASE_URL with your PostgreSQL credentials:
   
   ```python
   DATABASE_URL = "postgresql://fastapi_user:password@localhost/todo_db"

5. Running the Application

   Start the FastAPI server:
   ```python
   uvicorn backend:app --reload
   
6. Running the FrontEnd

    ```python
   streamlit run main.py
   
   
   
