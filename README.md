# Hospital Staff Management API

This project is a RESTful API for managing hospital staff members, including adding, viewing, and updating staff details. It is built using Flask, SQLAlchemy, and PostgreSQL, with Pydantic for data validation.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Developer's Note](#developers-note)
- [License](#license)

## Features
- Add new staff members
- View all staff members
- Retrieve details of a specific staff member
- Update staff member information
- Role-based access control

## Prerequisites
The following software and tools are required to set up and run the project:
- **Python 3.12.4**: The project was developed and tested using this specific version of Python.
- **PostgreSQL 16.3**: Used as the relational database management system.
- **Git**: Required for cloning the project repository.

## Setup

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

```sh
git clone <repository_url>
cd hospital_staff_management
2. Create a Virtual Environment
Create a virtual environment to manage dependencies:
python -m venv venv
Activate the virtual environment:
On Windows:
.\venv\Scripts\activate
On macOS and Linux:
source venv/bin/activate
3. Install Dependencies
Install the required Python packages:
pip install -r requirements.txt
4. Set Up PostgreSQL Database
Ensure PostgreSQL is installed and running.
Create a new PostgreSQL database:
CREATE DATABASE hospital_db;
Update the database URI in app.py:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost:5432/hospital_db'
Replace <username> and <password> with your PostgreSQL credentials.

Running the Application
To run the application, use the following command:

python -m app.app
The application will start, and you can access the API at http://127.0.0.1:5000.
Testing:
You can use Postman or similar tools to test the API endpoints. Ensure that the PostgreSQL database is set up and the application is running before testing.
Developer's Note:
This project was developed as part of a technical assessment to demonstrate skills in building RESTful APIs using Flask, managing databases with SQLAlchemy, and ensuring robust data validation with Pydantic. The project adheres to best practices in code structure and security, and includes comprehensive documentation to aid in understanding and using the API.
license:
This `README.md` file provides comprehensive guidance on setting up, running, and understanding the Hospital Staff Management API project. It includes specific software requirements, setup instructions, and a note from the developer, ensuring that potential employers and collaborators can easily get started with the project.
