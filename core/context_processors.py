from django.core.cache import cache

from core.settings import ROOT, API_ROOT
from frontend.tasks import get_frontend_data, get_recent_blog_posts


def global_settings(request):

    my_context = {
        'ROOT': ROOT,
        'API_ROOT': API_ROOT,
        "frontend": cache.get("frontend", get_frontend_data()),
        "recent_blog_posts": cache.get("recent_blog_posts", get_recent_blog_posts()),
    }


    return my_context
