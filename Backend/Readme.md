# Employee Management System
## Overview

This repository contains the implementation of the Employee Management System, a full-stack web application built using Vue.js for the frontend and Django for the backend. The system allows users to manage companies, departments, and employees with full CRUD (Create, Read, Update, Delete) functionality. Additionally, it includes features for handling the onboarding process of new employees and implementing role-based access control for secure data management with JWT Tokens .

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Security Measures](#security-measures)


## Installation
### - backend
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

#### 3. Clone the project

```sh      
git clone https://github.com/AhmedTarek111/Employee-Management-system.git
```

#### 4. Install the packges
##### 1.
```sh      
cd Employee-Management-system
```
##### 2.
```sh      
cd Employee-Management-system
```
##### 3.
  ```sh      
cd backend
```
##### 4.
  ```sh      
pip install -r requirements.txt
```
##### 5.
  ```sh      
python manage.py runserver
```

## Frontend

#### 1
```sh
cd .. 
```

#### 2

```sh
    cd Frontend
```
#### 3

```sh
   npm install
```
#### 4

```sh
npm run serve
```

## Features

### Backend
## Project Structure

The backend of the Employee Management System is organized into three Django apps: Account, Company, and Employee.

- **Account App**: Manages user authentication and registration. It includes models, views, serializers, and URLs related to user accounts.
   
- **Company App**: Handles company-related data such as company details and departments. It includes models, views, serializers, and URLs for CRUD operations on companies and departments.
   
- **Employee App**: Manages employee-related data including employee details and employment status. Similar to the Company app, it includes models, views, serializers, and URLs for managing employees.



1. **Models**
    - **User Accounts**: User Name, Email Address (Login ID), Role
    - **Company**: Company Name, Number of Departments, Number of Employees 
 
    - **Department**: Company (one to many relation), Department Name, Number of Employees
    - **Employee**: Company (one to many relation )  , Department(one to many relation ), Employee Status, Employee Name, Email Address, Mobile Number, Address, Designation, Hired On, Days Employed
           **in employee model i over ride the save function to check if the department when update or change or create to if the the choosen department is realted to this company or not if not it raised error and to make the mobile number in international format and check if count the days of employee if the status of the employee is Hired**

2. **Validations & Business Logic**
    - Validate required fields
    - Validate email 
    - Validate mobile ( i install external package to handel the number to internationl format )
    - Auto-calculate department and employee counts : i make signals to handel this part when any changes happed it automatically changed in the database filed
    - Handle cascading deletions (on delete the company it delete all departments and employees in this ) ,(on delete the department it delete the employee that related to this department )
    - Error handling and appropriate error messages (i make status code for each part to handel error )

3. **authentication and authorization**
    - i use jwt tokens to make the requests and all opearions secure
    - i make the django authenticaion in django with AbstractUser to add role field and use the default django permissions and groups 
    - when user sign up and choose the his role it automatically assign to group related to it for example role employee assign to groups permissions employee
    - user can login in with email or username 
4. **Security & Permissions**
    - Role-based access control i make it with django admin into 3 groups (admin , employee , manager)
    - Secure authentication and authorization (e.g., Sessions, Tokens)

5. **Apps Views files for Logic**
    ### Accounts App
    - i use the ApiView to handel the sign up from scratch 
    
    ### company App
    - i  use class based view because the logic not complex 
    
    ### employee App
    - i  use class based view because the logic not complex 
    - i use apiview in method get to get the realted department that related to the choosen company by pass the company id 
    
    

5. **APIs**
    - CRUD operations for Company, Department, and Employee models
    - RESTful conventions
    - Secure data handling with jwt tokens 
    - API documentation with swagger 

### Frontend
1. **User Interface (UI)**
    - Login Page it handle with handel tokens 
    - Company Management: List, View, Edit, Delete ,Create Companies
    - Department Management: List, View, Edit, Delete, Create Departments
    - Employee Management: List, View, Create, Edit, Delete Employees

2. **Validations**
    - Validate required fields
    - Validate email and mobile formats
    - Department field linked to selected company

3. **Employee Report (Bonus)**
    - Detailed employee report including name, email, mobile number, position, hired date, days employed, company, department




## Usage

1. Open your browser and navigate to `http://localhost:8080` for the frontend.
2. Use the superuser credentials to log in `http://localhost:8080` .
3. after sign in thier is the home page that display the companies management, departments management, and employees management using .

## API Documentation
- i made the API docs with Swagger
- The API supports CRUD operations for all models. Detailed documentation can be found after run the project  in the url `http://127.0.0.1:8000/ swagger/`.
- if you want to check the endpoint externaly change the permissions class in the views files to Allowall

## Security Measures

- i use django admin groups to into 3 groups (manager ,employee ,admin)
- Secure authentication and authorization i use JWT tokens for security

## Completion Checklist

- [done] Backend models and validations
- [done] CRUD operations
- [done] Role-based access control
- [done] API documentation
- [done] Frontend UI and validations
- [done] API integration
- [] Logging (Bonus)
- [] User account management (Bonus)
- [] Summary dashboard (Bonus)
- [] Employee report (Bonus)
- [x] Workflow (Bonus)
- [x] Unit and integration tests (Bonus)


