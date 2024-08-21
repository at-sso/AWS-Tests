# Library Management Web Application in Docker

This project is a Flask-based web application designed to manage users, books, and loans in a library. It includes features for adding, updating, deleting, and viewing these entities. The application can be run locally using Docker.

## Table of Contents

- [Library Management Web Application in Docker](#library-management-web-application-in-docker)
    - [Table of Contents](#table-of-contents)
    - [Project Structure](#project-structure)
    - [Installation](#installation)
        - [Prerequisites](#prerequisites)
        - [Clone the Repository](#clone-the-repository)
    - [Running the Application](#running-the-application)
        - [Using Docker](#using-docker)
    - [Features](#features)

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       ├── base.html
│       ├── books.html
│       ├── index.html
│       ├── loans.html
│       ├── update_book.html
│       ├── update_loan.html
│       ├── update_user.html
│       └── users.html
├── manage.py
├── Dockerfile
└── README.md
```

- **`./app/__init__.py`**: Initializes the Flask app and configures the database.
- **`./app/models.py`**: Defines the database models for Users, Books, and Loans.
- **`./app/routes.py`**: Contains the routes for managing users, books, and loans.
- **`./templates/*`**: Contains the HTML templates used by the application.

## Installation

### Prerequisites

- Docker installed on your machine.

### Clone the Repository

```bash
git clone https://github.com/at-sso/AWS-Tests.git
cd AWS-Tests
```

## Running the Application

### Using Docker

1. [**Build the Docker image:**](run.sh)

   ```bash
   ./zperk.t9/run.sh
   ```

2. **Access the Application:**

   Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Features

You can find the full documentation [here](../zperk.t4/readme.md).
