from django.core.cache import cache
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.constants import PAYMENT_PENDING, PAYMENT_SUCCESS


@receiver(post_save, sender=None, dispatch_uid='post_save_update_cache')
def post_save_cache(sender, instance, created, raw, **kwargs):
    if raw:
        return

    if sender.__name__ == "AboutPage":
        cache.delete("about_page")

    elif sender.__name__ == "Service":
        cache.delete("services")

    elif sender.__name__ == "ServicePacket":
        cache.delete("service_packets")

    elif sender.__name__ == "Slide":
        cache.delete("slides")

    elif sender.__name__ == "Testimonial":
        cache.delete("testimonials")
    elif sender.__name__ == "Il":
        cache.delete("iller")
    elif sender.__name__ == "Ilce":
        cache.delete("ilceler")

    elif sender.__name__ == "CarModel":
        cache.delete("car_models")

    elif sender.__name__ == "CarMark":
        cache.delete("car_marks")


@receiver(post_save, sender=None, dispatch_uid='post_save_commission')
def post_save_commission(sender, instance, created, raw, **kwargs):
    pass