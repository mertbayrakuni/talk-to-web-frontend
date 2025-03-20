import logging
import os

import requests
from celery import shared_task
from django.core.cache import cache
from django.utils import timezone
from requests.auth import HTTPBasicAuth

from core.settings import API_ROOT
from utils.util import get_file_handler

logger = logging.getLogger('frontend_tasks')
logger.setLevel(logging.DEBUG)
logger.addHandler(get_file_handler(filename="frontend_tasks.log"))


@shared_task
def clear_cache():
    cache.clear()

def my_request(endpoint):
    try:
        basic = HTTPBasicAuth(os.getenv("INFO_USERNAME"), os.getenv("INFO_USER_PASSWORD"))
        resp = requests.get(f"{API_ROOT}/api/{endpoint}", auth=basic)
        if resp:
            return resp.json()
    except Exception as e:
        logger.error(f"Error in endpoint {endpoint}. {e}")
        return None


def get_blog_posts_by_groups():
    blog_posts = my_request("blog-post/by-groups")

    if blog_posts:
        cache.set("blog_posts_by_groups", blog_posts, timeout=3600)
    else:
        logger.error("get_blog_posts_by_groups return None")



def get_slides():
    resp_json = my_request("slides")
    slides = resp_json["data"]

    if slides:
        cache.set("slides", slides, timeout=3600)
    else:
        logger.error("get_slides return None")


def get_testimonials_data():
    resp_json = my_request("testimonials")
    testimonials = resp_json["data"]

    if testimonials:
        cache.set("testimonials", testimonials, timeout=3600)
    else:
        logger.error("get_testimonials return None")


def get_instructors_data(slug=None):
    if slug is None:
        resp_json = my_request("instructors")
        instructors = resp_json["data"]

        if instructors:
            cache.set("instructors", instructors, timeout=3600)
        else:
            logger.error("get_instructors return None")
    else:
        instructor = my_request(f"instructors/{slug}")
        if instructor:
            cache.set(f"instructor-{slug}", instructor, timeout=3600)
        else:
            logger.error(f"get_instructor_with_slug={slug} return None")


def get_course_groups_data(slug=None):
    if slug is None:
        resp_json = my_request("course-groups")
        course_groups = resp_json["data"]

        if course_groups:
            cache.set("course-groups", course_groups, timeout=3600)
        else:
            logger.error("get_course_groups return None")
    else:
        course_group = my_request(f"course-groups/{slug}")
        if course_group:
            cache.set(f"course-group-{slug}", course_group, timeout=3600)
        else:
            logger.error(f"get_instructor_with_slug={slug} return None")


def get_alumni_data(slug=None):
    if slug is None:
        resp_json = my_request("alumni")
        alumni = resp_json["data"]

        if alumni:
            cache.set("alumni", alumni, timeout=3600)
        else:
            logger.error("get_alumni return None")
    else:
        alumni = my_request(f"alumni/{slug}")
        if alumni:
            if isinstance(alumni, list):
                cache.set(f"alumni-{slug}", alumni[0], timeout=3600)
            else:
                cache.set(f"alumni-{slug}", alumni, timeout=3600)
        else:
            logger.error(f"get_alumni_with_slug={slug} return None")

def get_frontend_data():
    resp_json = my_request("frontend")
    if resp_json is None:
        logger.error("get_frontend_data return None")
        return

    frontend = resp_json["data"]
    if isinstance(frontend, list):
        frontend = frontend[0]

    if frontend:
        cache.set("frontend", frontend, timeout=3600)
    else:
        logger.error("get_services return None")

def get_services():
    resp_json = my_request("services")
    services = resp_json["data"]
    if services:
        cache.set("services", services, timeout=3600)
    else:
        logger.error("get_services return None")


def get_about_page():
    about_page = my_request("about-page/1")
    if about_page:
        cache.set("about_page", about_page)
    else:
        logger.error("get_about_page return None")

@shared_task
def update_about_page():
    t1 = timezone.now()
    get_about_page()
    t2 = timezone.now()
    logging.info(f"get_about_page is worked successfully in {(t2 - t1).total_seconds()}")


@shared_task
def update_slides():
    t1 = timezone.now()
    get_slides()
    t2 = timezone.now()
    logging.info(f"get_slides is worked successfully in {(t2 - t1).total_seconds()}")


@shared_task
def update_services():
    t1 = timezone.now()
    get_services()
    t2 = timezone.now()
    logging.info(f"get_services is worked successfully in {(t2 - t1).total_seconds()}")



@shared_task
def update_testimonials():
    t1 = timezone.now()
    get_testimonials_data()
    t2 = timezone.now()
    logging.info(f"get_testimonials is worked successfully in {(t2 - t1).total_seconds()}")


