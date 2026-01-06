# Python Lesson 04

## Memo: Django Development Environment Setup

### Prerequisites
- Python 3.13.5
- Virtual environment (`.venv`)

### Initial Setup Commands

| Command | Description |
|---------|-------------|
| `python3 -m venv .venv` | Create virtual environment |
| `source .venv/bin/activate` | Activate virtual environment (macOS/Linux) |
| `pip install django qrcode[pil]` | Install required packages |

### Django Project Structure

```bash
# Create Django project in current directory
django-admin startproject mysite .

# Create Django app
python manage.py startapp restaurant_menu
```

**Key differences:**
- `django-admin startproject mysite .` - Creates project in current directory (note the `.` at the end)
- `django-admin startproject mysite` - Creates project in new `mysite/` subdirectory
- `python manage.py startapp <app_name>` - Creates a new app within the project

### Project Structure
```
python-lesson-04/
├── manage.py              # Django management script
├── mysite/                # Project configuration
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing
│   └── wsgi.py
└── restaurant_menu/       # App directory
    ├── models.py          # Database models
    ├── views.py           # View logic
    ├── urls.py            # App-specific URLs
    └── migrations/        # Database migrations
```

### Common Commands

```bash
# Run development server
python manage.py runserver

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Package Management

```bash
# Save installed packages
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

**Note:** Always work within the virtual environment to avoid conflicts with global packages.
