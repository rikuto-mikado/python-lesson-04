# Python Lesson 04

## What I Learned

-
-
-

## Challenges

-
-
-

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