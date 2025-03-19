import logging
import sys

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic.base import View
from dotenv import load_dotenv

from frontend.tasks import get_frontend_data, get_testimonials_data, get_instructors_data, get_alumni_data
from utils.util import get_file_handler

load_dotenv()
logger = logging.getLogger('assist')
logger.setLevel(logging.DEBUG)
logger.addHandler(get_file_handler(filename="frontend.log"))


def handler404(request, exception="", template_name='frontend/page-404.html'):
    type_, value, traceback = sys.exc_info()
    context = {
        "name": "404",
        "message": f"PAGE NOT FOUND! {value}"
    }

    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request), status=404)


def handler500(request, exception="", template_name='frontend/page-500.html'):
    type_, value, traceback = sys.exc_info()
    context = {
        "name": "500",
        "message": f"500 Internal Server Error !=== > {value}"
    }

    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request), status=500)


def handler501(request, exception="", template_name='frontend/errorPage501.html'):
    type_, value, traceback = sys.exc_info()
    context = {
        "name": "501",
        "message": f"501 Not Implemented !=== > {value}"
    }
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


class IndexView(View):
    def get(self, request):
        context = {
            "frontend": cache.get("frontend", get_frontend_data()),
            "news": cache.get("news", get_frontend_data()),
            "testimonials": cache.get("testimonials", get_testimonials_data()),
            "instructors": cache.get("instructors", get_instructors_data()),
            "alumni": cache.get("alumni", get_alumni_data()),
        }

        template = loader.get_template(f'frontend/index.html')
        return HttpResponse(template.render(context, request))


class InstructorDetailView(View):
    def get(self, request, slug):
        instructor = cache.get(f"instructor-{slug}", get_instructors_data(slug))
        if instructor is None:
            raise Http404

        context = {
            'instructor': instructor,
        }

        template = loader.get_template(f'frontend/instructor_detail.html')
        return HttpResponse(template.render(context, request))


class KVKKView(LoginRequiredMixin, View):
    def get(self, request, page_name=None):
        context = {
            "active": ["#kvkk_li"]
        }

        template = loader.get_template(f'frontend/kvkk.html')
        return HttpResponse(template.render(context, request))


class AlumniDetailView(View):
    def get(self, request, slug):
        alumni = cache.get("alumni", get_alumni_data())
        alumna = cache.get(f"alumni-{slug}", get_alumni_data(slug))
        if alumna is None:
            raise Http404

        context = {
            'alumna': alumna,
            'alumni': alumni
        }

        template = loader.get_template(f'frontend/alumni.html')
        return HttpResponse(template.render(context, request))

