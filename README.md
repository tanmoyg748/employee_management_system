# Employee Management System

A simple **Employee Management System** built with Django. This project helps you manage employee information such as name, email, and salary.

## Features

- View the list of all employees
- Add a new employee
- View individual employee details
- Edit employee information
- Delete an employee
- Store employee data in an SQLite database
- Use AJAX (Fetch API) to delete an employee without reloading the page
- Use Bootstrap 5.3.3 for the employee list page

## Technologies Used

- Python
- Django 6.1.1
- SQLite3
- HTML
- JavaScript
- Bootstrap 5.3.3

## Project Structure

```text
employee_management/
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── employees/
│   ├── migrations/
│   ├── static/
│   │   └── employees/
│   │       └── js/
│   │           └── employee.js
│   ├── templates/
│   │   └── employees/
│   │       ├── employee_list.html
│   │       ├── employee_form.html
│   │       ├── employee_detail.html
│   │       └── employee_edit.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── db.sqlite3
└── manage.py
```

## How to Run the Project

Follow these steps to run the project on your computer.

### 1. Download or Clone the Project

Download this repository or clone it using Git:

```bash
git clone YOUR_REPOSITORY_URL
```

Then open the project folder in your terminal or VS Code.

### 2. Create a Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate the Virtual Environment

**Windows (CMD):**

```bash
myenv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.\myenv\Scripts\Activate.ps1
```

** macOS / Linux:**

```bash
source myenv/bin/activate
```

### 4. Install Django

```bash
pip install Django==6.1.1
```

### 5. Go to the Project Folder

Make sure your terminal is inside the folder containing `manage.py`.

For example:

```bash
cd employee_management
```

If you are already in that folder, you can skip this step.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open the Project in Your Browser

Visit:

```text
http://127.0.0.1:8000/
```

## How to Use

1. Open the home page to see the employee list.
2. Click **Add Employee** to add a new employee.
3. Click **View** to see an employee's details.
4. Click **Edit** to update employee information.
5. Click **Delete** to remove an employee after confirmation.

## Database

This project uses **SQLite3**, Django's default database. The employee information is stored in the `db.sqlite3` file.

The `Employee` model contains these fields:

| Field | Description |
|---|---|
| `name` | Employee name |
| `email` | Employee email address (must be unique) |
| `salary` | Employee salary |

## Note

- This project is intended for learning and practice.
- Bootstrap is loaded from a CDN, so an internet connection is needed for its styling.
- Do not use the development server or the current development settings for production deployment.
