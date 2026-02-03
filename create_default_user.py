#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visualizer.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

USERNAME = 'test'
PASSWORD = 'testpass'

user, created = User.objects.get_or_create(username=USERNAME)
if created:
    user.set_password(PASSWORD)
    user.save()
    print(f'Created user {USERNAME}')
else:
    print(f'User {USERNAME} already exists')

token, _ = Token.objects.get_or_create(user=user)
print('Token:', token.key)
