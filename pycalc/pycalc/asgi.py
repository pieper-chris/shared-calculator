"""
ASGI config for pycalc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django # added
from channels.asgi import get_channel_layer # added
from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pycalc.settings')
# added below  (and import channels.asgi) via  https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django
channel_layer = get_channel_layer()
#django.setup() # added
#application = get_asgi_application()

