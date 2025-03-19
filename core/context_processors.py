from django.core.cache import cache

from core.settings import ROOT, API_ROOT
from frontend.tasks import get_frontend_data


def global_settings(request):

    my_context = {
        'ROOT': ROOT,
        'API_ROOT': API_ROOT,
        "frontend": cache.get("frontend", get_frontend_data()),
    }


    return my_context
