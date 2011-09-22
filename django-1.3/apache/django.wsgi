import os, sys

projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if path not in sys.path:
    sys.path.append(path)

if projectPath not in sys.path:
    sys.path.append(projectPath)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()