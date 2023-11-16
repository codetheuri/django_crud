# Simple Django CRUD Application

This is a simple Django CRUD (Create, Read, Update, Delete) application that allows you to manage a list of items. It includes basic functionalities for creating, reading, updating, and deleting items.

## Features

- **CRUD Operations:** Add, delete, update, and view items.
- **Django Framework:** Built using the Django web framework.
- **Bootstrap Styling:** Basic styling using Bootstrap for a clean and responsive user interface.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) (>= 3.6)
- [Django](https://www.djangoproject.com/)
- [Virtualenv](https://virtualenv.pypa.io/) (recommended)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
Navigate to the project directory:  
    cd your-repository
Create and activate a virtual environment (optional but recommended):    
    
     python -m venv venv
    
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install dependencies:
      
      pip install -r requirements.txt
Run migrations to create the necessary database tables:      
 
    python manage.py migrate
Create a superuser to access the Django admin interface:

    python manage.py createsuperuser
Start the development server:
   
    python manage.py runserver
Access the application in your browser at http://localhost:8000.

Usage
Visit the homepage to view the list of items.
Navigate to the "Add Item" section to add new items.
Click on items to view details, update, or delete them.
Django Admin Interface
Access the Django admin interface at http://localhost:8000/admin using the superuser credentials created
