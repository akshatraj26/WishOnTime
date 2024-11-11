# WishOnTime

WishOnTime is a Django-based web application that allows users to schedule birthday wishes for friends and loved ones. Users can register birthdays, set a personalized message, and the app will send a wish on the specified date.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Email Configuration](#email-configuration)
- [Database Migrations](#database-migrations)
- [Usage](#usage)
- [Screenshots](#screenshots)

## Features

- Register birthdays with custom messages.
- Automatically sends birthday wishes via email.
- Manage and view all scheduled birthdays.
  
## Technologies

- Django
- Python
- Tailwind CSS & Bootstrap
- Crispy Forms

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wishontime.git
cd wishontime
```

### 2. Set up Virtual Environment

#### For Windows:
```bash
python -m venv env
.\env\Scripts\activate
```

#### For macOS and Linux:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure you have all necessary dependencies like Django and Crispy Forms by checking your `requirements.txt`.

## Email Configuration

To configure the email backend, add the following settings to your `settings.py` file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # or the SMTP server you're using
EMAIL_PORT = 587  # or the correct port for your SMTP provider
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'akshatraj2607@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your-app-password'  # Your email password or app password

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

### Creating an App Password for Gmail SMTP

If you are using Gmail, you need to generate an app password to use for the `EMAIL_HOST_PASSWORD` instead of your regular Google account password. Here’s how you can create one:

1. **Enable 2-Step Verification:**
   - Go to your Google account: [Google Account](https://myaccount.google.com/)
   - Under **Security**, turn on **2-Step Verification**.
   
2. **Generate an App Password:**
   - After enabling 2-Step Verification, go to the **App Passwords** section under **Security**.
   - Select **Mail** as the app and **Other** as the device, then give it a name (e.g., "Django App").
   - Click **Generate**, and Google will give you a 16-character password.
   - Use this password for the `EMAIL_HOST_PASSWORD` in your `settings.py`.

## Database Migrations

To set up the database:

1. **Make Migrations**

   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

## Usage

1. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

2. Visit the application in your browser at `http://127.0.0.1:8000/`.

3. Use the navigation bar to add, view, and manage scheduled birthdays.

## Screenshots

Here are some screenshots of the application:

- ![Screenshot 1](./screenshots/Screenshot%20(101).png)
- ![Screenshot 2](./screenshots/Screenshot%20(102).png)
- ![Screenshot 3](./screenshots/Screenshot%20(103).png)
- ![Screenshot 4](./screenshots/Screenshot%20(104).png)
- ![Screenshot 5](./screenshots/Screenshot%20(105).png)

## Contributing

Contributions are welcome! If you have suggestions or would like to add new features, please submit a pull request.

---

### License

This project is open-source and available under the MIT License.
