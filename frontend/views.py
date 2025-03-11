import logging
import sys

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic.base import View
from dotenv import load_dotenv

from frontend.tasks import get_frontend_data, get_testimonials_data, get_instructors_data
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
        # all_slides = cache.get("all_slides", None)
        # all_testimonials = cache.get("all_testimonials", None)
        # all_instructors = cache.get("all_instructors", None)
        #
        # if True or all_testimonials is None:
        #     all_courses = TestimonialSerializer(Testimonial.objects.all(), many=True).data
        #     cache.set("all_testimonials", all_courses, 1800)
        # if True or all_slides is None:
        #     all_slides = SlideSerializer(Slide.objects.all(), many=True).data
        #     cache.set("all_slides", all_slides, 1800)
        #
        # if True or all_instructors is None:
        #     all_instructors = InstructorSerializerForPublic(Instructor.objects.all(), many=True).data
        #     cache.set("all_instructors", all_instructors, 1800)

        context = {
            "frontend": cache.get("frontend", get_frontend_data()),
            "testimonials": cache.get("testimonials", get_testimonials_data()),
            "instructors": cache.get("instructors", get_instructors_data()),
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
