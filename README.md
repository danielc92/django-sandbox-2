# Project Title
Another sandbox project to test functionality of Django Framework.

# Before you get started
Concepts covered in this project:
- Rendering forms manually
- Rendering many-to-one forms in one page method
- Rendering DateTime fields properly

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/django-sandbox-2.git
```

**This project uses a python 3.7 virtual environment**
```sh
virtualenv --python=/path/to/python3bin venv
source venv/bin/activate
pip install django
```

**To create the database for the first time**
```sh
cd path/to/this/project (where manage.py resides)
python manage.py makemigrations
python manage.py migrate
```

# Tests
- Render form contents manually to fine tune appearance
- Render contents of form with many-to-one relationship in a single form without using form.save() method
- Use DateInput to render a DateTime field properly (it does not set type attribute to "date" by default)


# Contributors
- Daniel Corcoran

# Sources
- [Django Documentation](https://docs.djangoproject.com/en/2.2/)