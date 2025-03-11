from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import re_path, path, include
from django.views.generic import RedirectView
from django.views.static import serve
from dotenv import load_dotenv

from core import settings
from frontend.views import InstructorDetailView, IndexView, KVKKView
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
    re_path(r'^home/$', IndexView.as_view(), name='home'),
    re_path(r'^index', IndexView.as_view(), name="index"),
    re_path(r'^home/$', IndexView.as_view(), name='home'),
    path('kvkk', KVKKView.as_view(), name="kvkk"),

    path('instructors/<slug:slug>', InstructorDetailView.as_view(), name="instructor_detail_view"),
    re_path(r'^$', IndexView.as_view(), name="index_view"),

] + debug_toolbar_urls()
