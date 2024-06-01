# Employee Management System

## Overview

This repository contains the implementation of the Employee Management System, a full-stack web application built using Vue.js for the frontend and Django for the backend. The system allows users to manage companies, departments, and employees with full CRUD (Create, Read, Update, Delete) functionality. Additionally, it includes features for handling the onboarding process of new employees and implementing role-based access control for secure data management with JWT Tokens.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Security Measures](#security-measures)

## Features

### Backend
The backend of the Employee Management System is organized into three Django apps: Account, Company, and Employee.

1. **Models**
    - **User Accounts**: User Name, Email Address (Login ID), Role
    - **Company**: Company Name, Number of Departments, Number of Employees
    - **Department**: Company (one to many relation), Department Name, Number of Employees
    - **Employee**: Company (one to many relation), Department (one to many relation), Employee Status, Employee Name, Email Address, Mobile Number, Address, Designation, Hired On, Days Employed

2. **Validations & Business Logic**
    - Validate required fields
    - Validate email
    - Validate mobile (using external package to handle the number in international format)
    - Auto-calculate department and employee counts using signals
    - Handle cascading deletions
    - Error handling with appropriate status codes

3. **Authentication and Authorization**
    - JWT tokens for secure requests and operations
    - Custom Django authentication using `AbstractUser` to add role field
    - Role-based access control with Django permissions and groups

4. **Security & Permissions**
    - Role-based access control with three groups (admin, employee, manager)
    - Secure authentication and authorization (JWT Tokens)

5. **Views**
    - **Accounts App**: APIView for signup, user creation, and update operations; home page view for employee count
    - **Company App**: Class-based views for CRUD operations on companies and departments
    - **Employee App**: Class-based views for CRUD operations on employees, APIView to get departments related to a company, and views to get hired employees and employees related to a specific company

6. **APIs**
    - CRUD operations for Company, Department, and Employee models
    - RESTful conventions
    - Secure data handling with JWT tokens
    - API documentation with Swagger

### Frontend
1. **User Interface (UI)**
    - Login Page with token handling
    - Company Management: List, View, Edit, Delete, Create Companies
    - Department Management: List, View, Edit, Delete, Create Departments
    - Employee Management: List, View, Create, Edit, Delete Employees

2. **Validations**
    - Validate required fields
    - Validate email and mobile formats
    - Department field linked to the selected company

3. **Employee Report (Bonus)**
    - Detailed employee report including name, email, mobile number, position, hired date, days employed, company, department

## Installation

### Backend

#### 1. Create a Virtual Environment

Create a virtual environment using the `venv` module. Run the following command in the root directory of the project:

On macOS/Linux:
```sh
python3 -m venv venv
```

On Windows:
```sh
python -m venv venv
```

#### 2. Activate the Virtual Environment

Activate the virtual environment 

On macOS/Linux:
```sh
source venv/bin/activate
```

On Windows:
```sh
cd venv\Scripts\activate
```

#### 3. Clone the Project

```sh      
git clone https://github.com/AhmedTarek111/Employee-Management-system.git
```

#### 4. Install the Packages
##### 1.
```sh      
cd Employee-Management-system
```
##### 2.
```sh      
cd backend
```
##### 3.
  ```sh      
pip install -r requirements.txt
```
##### 4.
  ```sh      
python manage.py runserver
```

### Frontend

#### 1. Navigate to the Frontend Directory
```sh
cd .. 
```

#### 2. Move into the Frontend Directory
```sh
cd Frontend
```

#### 3. Install Dependencies
```sh
npm install
```

#### 4. Run the Frontend Development Server
```sh
npm run serve
```

## Usage

1. Open your browser and navigate to `http://localhost:8080` for the frontend.
2. The login page will appear. Sign up or log in with credentials (e.g., username: admin, password: 1234).
3. Use the superuser credentials to log in.
4. After signing in, the home page will display options for managing companies, departments, and employees.

## API Documentation

- The API documentation is generated with Swagger.
- The API supports CRUD operations for all models. Detailed documentation can be found at `http://127.0.0.1:8000/swagger/` after running the project.
- For external endpoint checks, change the permission class in the views files to AllowAll.

## Security Measures

- Django admin groups for role-based access control (manager, employee, admin)
- Secure authentication and authorization using JWT tokens

## Completion Checklist

- [x] Backend models and validations
- [x] CRUD operations
- [x] Role-based access control
- [x] API documentation
- [x] Frontend UI and validations
- [x] API integration
- [x] User account management (Bonus)
- [x] Summary dashboard (Bonus)
- [x] Employee report (Bonus)
- [ ] Logging (Bonus) - Can be implemented if more time is available
- [ ] Workflow (Bonus) - Can be implemented if more time is available
- [ ] Unit and integration tests (Bonus) - Can be implemented if more time is available

---

