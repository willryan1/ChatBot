"""
WSGI config for chat_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

project_home = u'/Users/willryan/PycharmProjects/django_chat_try/chat_app'
if project_home not in sys.path:
    sys.path.append(project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'chat_app.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = get_wsgi_application()
