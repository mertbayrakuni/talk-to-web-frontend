import logging
import os

import requests
from celery import shared_task
from django.core.cache import cache
from django.utils import timezone
from requests.auth import HTTPBasicAuth


@shared_task
def clear_cache():
    cache.clear()

def my_request(endpoint):
    try:
        panel_url = os.getenv("PANEL_ROOT")
        basic = HTTPBasicAuth(os.getenv("INFO_USERNAME"), os.getenv("INFO_USER_PASSWORD"))
        resp = requests.get(f"{panel_url}/api/{endpoint}", auth=basic)
        if resp:
            return resp.json()
    except Exception as e:
        logging.exception(f"Error in endpoint {endpoint}. {e}")
        return None


def get_blog_posts_by_groups():
    blog_posts = my_request("blog-post/by-groups")

    if blog_posts:
        cache.set("blog_posts_by_groups", blog_posts, timeout=3600)
    else:
        logging.error("get_blog_posts_by_groups return None")


def get_popular_blog_posts():
    popular_blog_posts = my_request("blog-post/popular")

    if popular_blog_posts:
        cache.set("popular_blog_posts", popular_blog_posts, timeout=3600)
    else:
        logging.error("get_popular_blog_posts return None")


def get_blog_posts():
    resp_json = my_request("blog-post")
    blog_posts = resp_json["data"]

    if blog_posts:
        cache.set("blog_posts", blog_posts, timeout=3600)
    else:
        logging.error("get_blog_posts return None")


def get_blog_tags():
    resp_json = my_request("blog-tag")
    blog_tags = resp_json["data"]
    cache.set("blog_tags", blog_tags)

    if blog_tags:
        cache.set("blog_tags", blog_tags, timeout=3600)
    else:
        logging.error("get_blog_tags return None")


def get_service_packets():
    panel_url = os.getenv("PANEL_ROOT")
    resp = requests.get(f"{panel_url}/api/service-packet")
    if resp:
        resp_json = resp.json()

        service_packets = resp_json["data"]

        if service_packets:
            cache.set("service_packets", service_packets, timeout=3600)

    logging.error("get_service_packets return None")


def get_slides():
    resp_json = my_request("slides")
    slides = resp_json["data"]

    if slides:
        cache.set("slides", slides, timeout=3600)
    else:
        logging.error("get_slides return None")


def get_testimonials_data():
    resp_json = my_request("testimonials")
    testimonials = resp_json["data"]

    if testimonials:
        cache.set("testimonials", testimonials, timeout=3600)
    else:
        logging.error("get_testimonials return None")

def get_instructors_data(slug=None):
    if slug is None:
        resp_json = my_request("instructors")
        instructors = resp_json["data"]

        if instructors:
            cache.set("instructors", instructors, timeout=3600)
        else:
            logging.error("get_instructors return None")
    else:
        instructors = my_request(f"instructor?slug={slug}")["data"]
        if instructors and isinstance(instructors, list):
            cache.set(f"instructor-{slug}", instructors[0], timeout=3600)
        else:
            logging.error(f"get_instructor_with_slug={slug} return None")

def get_frontend_data():
    resp_json = my_request("frontend")
    if resp_json is None:
        logging.error("get_frontend_data return None")
        return

    frontend = resp_json["data"]
    if isinstance(frontend, list):
        frontend = frontend[0]

    if frontend:
        cache.set("frontend", frontend, timeout=3600)
    else:
        logging.error("get_services return None")

def get_services():
    resp_json = my_request("services")
    services = resp_json["data"]
    if services:
        cache.set("services", services, timeout=3600)
    else:
        logging.error("get_services return None")


def get_about_page():
    about_page = my_request("about-page/1")
    if about_page:
        cache.set("about_page", about_page)
    else:
        logging.error("get_about_page return None")

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
def update_service_packets():
    t1 = timezone.now()
    get_service_packets()
    t2 = timezone.now()
    logging.info(f"get_service_packets is worked successfully in {(t2 - t1).total_seconds()}")


@shared_task
def update_blog_posts():
    t1 = timezone.now()
    get_blog_posts()
    t2 = timezone.now()
    logging.info(f"get_blog_posts is worked successfully in {(t2 - t1).total_seconds()}")


@shared_task
def update_popular_blog_posts():
    t1 = timezone.now()
    get_popular_blog_posts()
    t2 = timezone.now()
    logging.info(f"get_popular_blog_posts is worked successfully in {(t2 - t1).total_seconds()}")


@shared_task
def update_blog_posts_by_groups():
    t1 = timezone.now()
    get_blog_posts_by_groups()
    t2 = timezone.now()
    logging.info(f"get_blog_posts_by_groups is worked successfully in {(t2 - t1).total_seconds()}")


@shared_task
def update_blog_tags():
    t1 = timezone.now()
    get_blog_tags()
    t2 = timezone.now()
    logging.info(f"get_blog_tags is worked successfully in {(t2 - t1).total_seconds()}")


@shared_task
def update_testimonials():
    t1 = timezone.now()
    get_testimonials_data()
    t2 = timezone.now()
    logging.info(f"get_testimonials is worked successfully in {(t2 - t1).total_seconds()}")


