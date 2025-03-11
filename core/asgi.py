import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# Initialize Django before importing any apps or middleware.
import django
django.setup()
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from course import routing as course_routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            course_routing.websocket_urlpatterns
        )),
})

