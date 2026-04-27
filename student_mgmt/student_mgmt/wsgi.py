"""
WSGI config for student_mgmt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_mgmt.settings')

application = get_wsgi_application()

# Upon running "python manage.py runserver", the WSGI application will be used to serve the app.
# The app is served using the settings defined in "student_mgmt.settings".
# The app is available at "localhost:8000" by default.
# From here, the next file that will be executed is "student_mgmt/urls.py".

