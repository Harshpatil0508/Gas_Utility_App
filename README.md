# Gas_Utility_App
# Service Requests Management System

## Overview
This Django project provides a web application for managing service requests for a gas utility company. It allows customers to submit service requests online, track the status of their requests, and view their account information. Additionally, customer support representatives have access to a tool to manage requests and provide support to customers.

## Features
- **Service Requests:** Customers can submit service requests online. This includes selecting the type of service request, providing details about the request, and attaching files.
- **Request Tracking:** Customers can track the status of their service requests. This includes viewing the status, submission date, and resolution date (if resolved).
- **Account Information:** Customers can view their account information.
- **Admin Access:** Staff users (admin) have access to manage service requests, including updating the resolved date.

## Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages using `pip install -r requirements.txt`.
4. Run database migrations using `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.

## Usage
- Access the application at `127.0.0.1`.
- Customers can log in or sign up to access the service request features.
- Admin users can log in to manage service requests, including updating the resolved date.

## Configuration
- Customize the `settings.py` file to adjust project settings, such as database configuration, timezone, etc.
- Ensure proper permissions are set for file uploads and access.

## Dependencies
- Python 3.9.12
- Django 4.2.11


