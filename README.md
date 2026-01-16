# Python Lesson 04

## What I Learned

### 1. Django Model Field Options

#### ForeignKey `on_delete` Parameter

When creating a `ForeignKey` relationship, the `on_delete` parameter determines what happens to related objects when the referenced object is deleted:

| Option | Behavior |
|--------|----------|
| `PROTECT` | Prevents deletion of the referenced object if related items exist |
| `CASCADE` | Deletes all related items when the referenced object is deleted |
| `SET_NULL` | Sets the foreign key to `NULL` (requires `null=True`) |
| `SET_DEFAULT` | Sets the foreign key to its default value |
| `DO_NOTHING` | Takes no action (may cause integrity errors) |

```python
# Example: Prevent user deletion if they have menu items
author = models.ForeignKey(User, on_delete=models.PROTECT)
```

#### DateTime Field Auto-Update Options

| Field Option | Behavior |
|--------------|----------|
| `auto_now_add=True` | Automatically set to current time only when the object is first created |
| `auto_now=True` | Automatically update to current time every time the object is saved |

```python
date_created = models.DateTimeField(auto_now_add=True)  # Set once on creation
date_updated = models.DateTimeField(auto_now=True)      # Updated on every save
```

### 2. Django Class-Based Views (CBV)

#### The `as_view()` Method

`as_view()` converts a class-based view into a callable view function that Django's URL resolver can use. It is **required** for all class-based views.

```python
# In urls.py
from . import views

urlpatterns = [
    path("", views.MenuList.as_view(), name="home")  # as_view() is required
]
```

### 3. Django Built-in User Model

Django provides a built-in `User` model for authentication and user management:

```python
from django.contrib.auth.models import User

# Use it as a ForeignKey in your models
author = models.ForeignKey(User, on_delete=models.PROTECT)
```

### 4. QR Code Generation with Python

Using the `qrcode` library to generate QR codes:

```python
import qrcode

image = qrcode.make("https://127.0.0.1:8000")
image.save("qr.png")
```

## Challenges

- Understanding when to use `PROTECT` vs `CASCADE` for `on_delete` - it depends on the business logic (should related data be preserved or deleted?)
- Remembering to use `as_view()` for class-based views in URL patterns
- Distinguishing between `auto_now_add` (creation time) and `auto_now` (modification time)

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