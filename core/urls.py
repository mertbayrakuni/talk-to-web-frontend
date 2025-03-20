from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import re_path, path, include
from django.views.generic import RedirectView
from django.views.static import serve
from dotenv import load_dotenv

from core import settings
from frontend.views import InstructorDetailView, IndexView, KVKKView, AlumniDetailView, BusinessLearningView, \
    ContractedInstitutionsView, FQAView, HumanResourcesView, WriteToUsView, CourseGroupDetailView
from frontend.views import handler404, handler500


load_dotenv()



favicon_view = RedirectView.as_view(url='/media/images/favicon.ico', permanent=True)
urlpatterns = [
    re_path(r"favicon\.ico$", favicon_view),
    re_path(r"^404", handler404, name="handler404"),
    re_path(r"^500", handler500, name="handler500"),
    path('admin/logs/', include('log_viewer.urls')),
    path('admin/', admin.site.urls, name="admin"),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,
                                              'show_indexes': settings.DEBUG}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,
                                             'show_indexes': settings.DEBUG}),


    re_path(r'^index', IndexView.as_view(), name="index"),
    re_path(r'^home', IndexView.as_view(), name='home'),
    path('kvkk', KVKKView.as_view(), name="kvkk"),
    path('business-learning', BusinessLearningView.as_view(), name="business_learning"),
    path('contracted-institutions', ContractedInstitutionsView.as_view(), name="contracted_institutions"),
    path('fqa', FQAView.as_view(), name="fqa"),
    path('human-resources', HumanResourcesView.as_view(), name="human_resources"),
    path('write-to-us', WriteToUsView.as_view(), name="write_to_us"),

    path('instructors/<slug:slug>', InstructorDetailView.as_view(), name="instructor_detail_view"),
    path('egitmenlerimiz/<slug:slug>', InstructorDetailView.as_view(), name="instructor_detail_view2"),

    path('upcoming-courses/<slug:slug>', CourseGroupDetailView.as_view(), name="course_group_detail_view2"),
    path('egitimler/<slug:slug>', CourseGroupDetailView.as_view(), name="course_group_detail_view2"),

    path('alumni/<slug:slug>', AlumniDetailView.as_view(), name="alumni_detail_view"),
    path('mezunlarimiz/<slug:slug>', AlumniDetailView.as_view(), name="mezunlarimiz_detail_view"),
    re_path(r'^$', IndexView.as_view(), name="index_view"),

] + debug_toolbar_urls()
