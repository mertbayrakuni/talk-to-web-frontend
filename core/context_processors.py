from django.core.cache import cache

from core.settings import ROOT, API_ROOT
from frontend.tasks import get_frontend_data, get_recent_blog_posts, get_last_three_course_groups, \
    get_testimonials_data, get_all_course_groups_data, get_instructors_data, get_alumni_data


def global_settings(request):

    my_context = {
        'ROOT': ROOT,
        'API_ROOT': API_ROOT,
        "frontend": cache.get("frontend", get_frontend_data()),
        "testimonials": cache.get("testimonials", get_testimonials_data()),
        "all_course_groups":  cache.get("all-course-groups", get_all_course_groups_data()),
        "news": cache.get("news", get_frontend_data()),
        "instructors": cache.get("instructors", get_instructors_data()),
        "alumni": cache.get("alumni", get_alumni_data()),
        "recent_blog_posts": cache.get("recent_blog_posts", get_recent_blog_posts()),
        "last_three_course_groups": cache.get("last_three_course_groups", get_last_three_course_groups()),
    }
    return my_context
