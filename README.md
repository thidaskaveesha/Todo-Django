# Todo-Django

Todo-Django is a small todo application developed using Django framework. It allows users to create, manage, and track their tasks effectively.

## Setup Environment

To set up the environment for Todo-Django, follow these steps:

1. Install Django framework using pip:
    ```bash
    pip install django
    ```

2. Create a new Django project:
    ```bash
    django-admin startproject <your-project-name>
    ```

3. Navigate to the newly created project directory:
    ```bash
    cd <your-project-name>
    ```

4. Create a new Django app within the project:
    ```bash
    python manage.py startapp <name-of-your-app>
    ```

5. Link the newly created app to the project:
    - Open `settings.py` file located in the root folder of your project.
    - Locate the `INSTALLED_APPS` list in the settings file.
    - Add the name of your newly created app as a string to the list.

## Usage

Once the environment is set up, you can start using the Todo-Django application. To run the application, use the following command:

```bash
python manage.py runserver
```

This will start the development server. You can then access the Todo-Django application through your web browser at http://localhost:8000/.

## Features

Todo-Django offers the following features:

- **Task Management**: Create, edit, and delete tasks.
- **Task Status**: Mark tasks as completed or incomplete.
- **Task Prioritization**: Assign priorities to tasks.
- **User Authentication**: Secure user authentication and authorization.
- **Responsive Design**: Works seamlessly on different screen sizes.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
