import logging
import pprint
import sys

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic.base import View
from dotenv import load_dotenv

from core.settings import API_ROOT
from frontend.tasks import get_frontend_data, get_testimonials_data, get_instructors_data, get_alumni_data, \
    get_course_groups_data, get_blog_posts, get_recent_blog_posts, get_all_course_groups_data
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
        all_course_groups = cache.get("all-course-groups", get_all_course_groups_data())
        context = {

        }


        template = loader.get_template(f'frontend/index.html')
        return HttpResponse(template.render(context, request))

class AboutUsView(View):
    def get(self, request):
        all_course_groups = cache.get("all-course-groups", get_all_course_groups_data())
        context = {

        }

        template = loader.get_template(f'frontend/hakkimizda.html')
        return HttpResponse(template.render(context, request))


class AnlasmaliKurumlarView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/anlasmali_kurumlar.html')
        return HttpResponse(template.render(context, request))


class WhyTalkToWebView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/why_talk_to_web.html')
        return HttpResponse(template.render(context, request))


class TumEtkinliklerlerView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/tum_etkinlikler.html')
        return HttpResponse(template.render(context, request))


class OnBasvuruFormuView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/write_to_us.html')
        return HttpResponse(template.render(context, request))

class TumEgitimlerView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/why_talk_to_web.html')
        return HttpResponse(template.render(context, request))


class KurumsalEgitimCozumleriView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/kurumsal_egitim_cozumleri.html')
        return HttpResponse(template.render(context, request))

class InsanKaynaklariView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/why_talk_to_web.html')
        return HttpResponse(template.render(context, request))
class KalitePolitikamizView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/kalite_politikasi.html')
        return HttpResponse(template.render(context, request))


class MusteriPolitikamizView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/musteri_politikasi.html')
        return HttpResponse(template.render(context, request))


class BilgiGuvenligiPolitikamizView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/bilgi_guvenligi_politikasi.html')
        return HttpResponse(template.render(context, request))


class GizlilikVeCerezPolitikamizView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/why_talk_to_web.html')
        return HttpResponse(template.render(context, request))
class KosullarVeSartlarView(View):
    def get(self, request):
        context = {}
        template = loader.get_template(f'frontend/why_talk_to_web.html')
        return HttpResponse(template.render(context, request))

class InstructorDetailView(View):
    def get(self, request, slug):
        instructor = cache.get(f"instructor-{slug}", get_instructors_data(slug))
        if instructor is None:
            raise Http404

        context = {
            'instructor': instructor,
        }

        template = loader.get_template(f'frontend/instructor.html')
        return HttpResponse(template.render(context, request))

class BlogPostsView(View):
    def get(self, request, slug=None):
        if slug is None:
            blog_posts = cache.get(f"blog_posts", get_blog_posts())
            recent_blog_posts = cache.get(f"recent_blog_posts", get_recent_blog_posts())

            context = {
                'blog_posts': blog_posts,
                'recent_blog_posts': recent_blog_posts

            }

            template = loader.get_template(f'frontend/blogs.html')
            return HttpResponse(template.render(context, request))
        else:
            blog_post = cache.get(f"blog_post-{slug}", get_blog_posts(slug))
            recent_blog_posts = cache.get(f"recent_blog_posts", get_recent_blog_posts())
            context = {
                'blog_post': blog_post,
                'recent_blog_posts': recent_blog_posts,
            }

            template = loader.get_template(f'frontend/blog_private.html')
            return HttpResponse(template.render(context, request))

class CourseGroupDetailView(View):
    def get(self, request, slug=None):
        if slug is None:
            course_groups = cache.get(f"course-groups", get_course_groups_data())

            context = {
                'course_groups': course_groups,
            }

            template = loader.get_template(f'frontend/course_groups.html')
            return HttpResponse(template.render(context, request))

        else:
            course_group = cache.get(f"course-group-{slug}", get_course_groups_data(slug))
            if course_group is None:
                raise Http404

            context = {
                'course_group': course_group,
            }

            template = loader.get_template(f'frontend/course_groups.html')
            return HttpResponse(template.render(context, request))


class UpcomingEducationView(View):
    def get(self, request, slug=None):
        if slug is None:
            course_groups = cache.get(f"course-groups", get_course_groups_data())

            context = {
                'course_groups': course_groups,
            }

            template = loader.get_template(f'frontend/course_groups.html')
            return HttpResponse(template.render(context, request))

        else:
            course_group = cache.get(f"course-group-{slug}", get_course_groups_data(slug))
            if course_group is None:
                raise Http404

            context = {
                'course_group': course_group,
            }

            template = loader.get_template(f'frontend/course_groups.html')
            return HttpResponse(template.render(context, request))


class OldEducationView(View):
    def get(self, request, slug=None):
        if slug is None:
            course_groups = cache.get(f"course-groups", get_course_groups_data())

            context = {
                'course_groups': course_groups,
            }

            template = loader.get_template(f'frontend/course_groups.html')
            return HttpResponse(template.render(context, request))

        else:
            course_group = cache.get(f"course-group-{slug}", get_course_groups_data(slug))
            if course_group is None:
                raise Http404

            context = {
                'course_group': course_group,
            }

            template = loader.get_template(f'frontend/course_groups.html')
            return HttpResponse(template.render(context, request))


class KVKKView(View):
    def get(self, request, page_name=None):
        context = {
            "active": ["#kvkk_li"]
        }

        template = loader.get_template(f'frontend/kvkk.html')
        return HttpResponse(template.render(context, request))

class BusinessLearningView(View):
    def get(self, request, page_name=None):
        context = {
            "active": ["#business_learning"]
        }

        template = loader.get_template(f'frontend/business_learning.html')
        return HttpResponse(template.render(context, request))

class ContractedInstitutionsView(View):
    def get(self, request, page_name=None):
        context = {
            "active": ["#business_learning"]
        }

        template = loader.get_template(f'frontend/contracted_institutions.html')
        return HttpResponse(template.render(context, request))

class FQAView(View):
    def get(self, request, page_name=None):
        context = {
            "active": ["#business_learning"]
        }

        template = loader.get_template(f'frontend/fqa.html')
        return HttpResponse(template.render(context, request))

class HumanResourcesView(View):
    def get(self, request, page_name=None):
        context = {
            "active": ["#business_learning"]
        }

        template = loader.get_template(f'frontend/human_resources.html')
        return HttpResponse(template.render(context, request))

class WriteToUsView(View):
    def get(self, request, page_name=None):
        context = {
            "active": ["#write_to_us"]
        }

        template = loader.get_template(f'frontend/write_to_us.html')
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



class BlogSitemap(View):
    def get(self, request):
        my_response = request.get(f"{API_ROOT}/sitemap.xm")
        return HttpResponse(my_response.getvalue(), content_type='application/xml')
