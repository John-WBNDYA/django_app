# My Django Project

## Requirements
- Python 3.x
- Virtualenv
- Docker

## Setup

To build and run the app using venv, follow these steps:

### Using Virtualenv
1. Clone the repository to your local machine

2. Create a new venv environment using the requirements.txt files:

   ```
   python -m venv
   source venv/scripts/activate
   pip install -r requirements.txt
   ```
3. Start the development server:

    change directory to manage.py file
   ```
   python manage.py runserver
   ```

4. Navigate to 'https://localhost:800' in your web browser

### Using Docker

To build and run the app using docker, follow these steps:

1. Clone the repository to your local machine
2. Build the Docker image:
   ```
   docker build -t my-django-app
   ```
3. Start the Docker container:
   ```
   docker run -p 8000:8000 my-django-app
   ```
4.  Navigate to 'https://localhost:800' in your web browser


## Environment Variables
Ensure you create a `.env` file with the required environment variables such as database settings, secret key, etc. This file should not be committed to the repository.
