from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import re_path, path, include
from django.views.generic import RedirectView, TemplateView
from django.views.static import serve
from dotenv import load_dotenv

from core import settings
from frontend.views import InstructorDetailView, IndexView, KVKKView, AlumniDetailView, BusinessLearningView, \
    ContractedInstitutionsView, FQAView, HumanResourcesView, WriteToUsView, CourseGroupDetailView, BlogSitemap, \
    BlogPostsView, UpcomingEducationView, OldEducationView, WhyTalkToWebView, OnBasvuruFormuView, TumEgitimlerView, \
    KurumsalEgitimCozumleriView, KalitePolitikamizView, MusteriPolitikamizView, \
    BilgiGuvenligiPolitikamizView, GizlilikVeCerezPolitikamizView, KosullarVeSartlarView, AboutUsView, \
    TumEtkinliklerlerView, AnlasmaliKurumlarView
from frontend.views import handler404, handler500

load_dotenv()


sitemaps = {
    "blogs": BlogSitemap,
}
favicon_view = RedirectView.as_view(url="/media/images/favicon.ico", permanent=True)
urlpatterns = [
    re_path(r"^sitemap.xml", sitemap, {'sitemaps': sitemaps},
          name='django.contrib.sitemaps.views.sitemap'),

    re_path(r'^robots.txt/$', TemplateView.as_view(template_name='frontend/robot.html')),

    re_path(r"favicon\.ico$", favicon_view),
    re_path(r"^404", handler404, name="handler404"),
    re_path(r"^500", handler500, name="handler500"),
    path("admin/logs/", include("log_viewer.urls")),
    path("admin/", admin.site.urls, name="admin"),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT,
                                              "show_indexes": settings.DEBUG}),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT,
                                             "show_indexes": settings.DEBUG}),


    path("index", IndexView.as_view(), name="index"),
    path("home", IndexView.as_view(), name="home"),
    path("hakkimizda/", AboutUsView.as_view(), name="about_us"),
    path("anlasmali-kurumlar/",AnlasmaliKurumlarView.as_view(), name="anlasmali_kurumlar"),
    path("neden-talk-to-web/", WhyTalkToWebView.as_view(), name="why_talk_to_web_view"),
    path("on-basvuru-formu/", OnBasvuruFormuView.as_view(), name="on_basvuru_formu_view"),
    path("tum-egitimler/", TumEgitimlerView.as_view(), name="tum_egitimler_view"),
    path("tum-etkinlikler/", TumEtkinliklerlerView.as_view(), name="tum_etkinlikler_view"),
    path("kurumsal-egitim-cozumleri/", KurumsalEgitimCozumleriView.as_view(), name="kurumsal_egitim_cozumleri_view"),
    path("kurumsal-basvuru/", WriteToUsView.as_view(), name="bize_yazin_view"),
    path("insan-kaynaklari/", HumanResourcesView.as_view(), name="insan_kaynaklari_view"),
    path("kalite-politikamiz/", KalitePolitikamizView.as_view(), name="kalite_politikamiz_view"),
    path("musteri-politikamiz/", MusteriPolitikamizView.as_view(), name="musteri_politikamiz_view"),
    path("bilgi-guvenligi-politikamiz/", BilgiGuvenligiPolitikamizView.as_view(), name="bilgi_guvenligi_politikamiz_view"),
    path("gizlilik-ve-cerez-politikamiz/", GizlilikVeCerezPolitikamizView.as_view(), name="gizlilik_ve_cerez_politikamiz_view"),
    path("kosullar-ve-sartlar/", KosullarVeSartlarView.as_view(), name="kosullar_ve_sartlar_view"),

    path("kvkk/", KVKKView.as_view(), name="kvkk"),
    path("business-learning/", BusinessLearningView.as_view(), name="business_learning"),
    path("contracted-institutions/", ContractedInstitutionsView.as_view(), name="contracted_institutions"),
    path("sss/", FQAView.as_view(), name="fqa"),


    path("blogs/", BlogPostsView.as_view(), name="blogs_view"),
    path("blogs/<slug:slug>/", BlogPostsView.as_view(), name="blog_private_view"),
    path("instructors/<slug:slug>/", InstructorDetailView.as_view(), name="instructor_detail_view"),
    path("egitmenlerimiz/<slug:slug>/", InstructorDetailView.as_view(), name="instructor_detail_view2"),


    path("tum-egitimler/", CourseGroupDetailView.as_view(), name="all_education"),
    path("yaklasan-egitimler/", UpcomingEducationView.as_view(), name="upcoming_education"),
    path("gecmis-egitimler/", OldEducationView.as_view(), name="old_education"),

    path("egitimler/<slug:slug>/", CourseGroupDetailView.as_view(), name="course_group_detail_view2"),

    path("alumni/<slug:slug>/", AlumniDetailView.as_view(), name="alumni_detail_view"),
    path("mezunlarimiz/<slug:slug>/", AlumniDetailView.as_view(), name="mezunlarimiz_detail_view"),
    path("", IndexView.as_view(), name="index_view"),

] + debug_toolbar_urls()
