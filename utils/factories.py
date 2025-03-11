import random
from datetime import timedelta

import factory
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from factory.django import DjangoModelFactory
from faker import Faker
from slugify import slugify

from attachment.models import Attachment
from country.models import Il, Ilce, MahalleKoy
from user.models import User
from utils.constants import (SUPER_ADMIN, CUSTOMER, MAHALLE)

fake = Faker(["tr_TR"])
Faker.seed(0)


class GeneralModelFactory(DjangoModelFactory):
    @classmethod
    def _setup_next_sequence(cls):
        model = cls._meta.model
        manager = cls._get_manager(model)

        try:
            return 1 + manager.values_list('pk', flat=True).order_by('-pk')[0]
        except IndexError:
            return 0
        except TypeError:
            return 1 + manager.count()

    is_active = True
    is_deleted = False
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)
    deleted_at = None
    created_by = None
    deleted_by = None


class AttachmentFactory(DjangoModelFactory):
    class Meta:
        model = Attachment

    slug = factory.Faker("slug")
    thumbnail = factory.Faker("image_url")
    original = factory.Faker("image_url")
    mime = factory.Faker("mime_type")

    is_public = factory.Faker('pybool')
    is_deleted = False
    created_by_id = None


class IlFactory(GeneralModelFactory):
    class Meta:
        model = Il

    name = factory.Faker("name")


class IlceFactory(GeneralModelFactory):
    class Meta:
        model = Ilce

    name = factory.Faker("name")
    il = factory.SubFactory(IlFactory)


class MahalleKoyFactory(GeneralModelFactory):
    class Meta:
        model = MahalleKoy

    name = factory.Faker("name")
    ilce = factory.SubFactory(IlceFactory)
    il = factory.LazyAttribute(lambda a: a.ilce.il)
    semt_bucak_belde = factory.Faker("name")
    posta_kodu = factory.Faker("name")
    type = MAHALLE


def get_email(first_name, last_name):
    first_name = slugify(first_name)
    last_name = slugify(last_name)
    if User.objects.filter(email__startswith='{}.{}'.format(first_name, last_name).lower()).exists():
        n = User.objects.filter(email__startswith='{}.{}'.format(first_name, last_name).lower()).count()
        return '{}.{}{}@kintshop.com'.format(first_name, last_name, n).lower()
    return '{}.{}@kintshop.com'.format(first_name, last_name).lower()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    full_name = factory.LazyAttribute(lambda a: '{} {}'.format(a.first_name, a.last_name).lower())
    email = factory.LazyAttribute(lambda a: get_email(a.first_name, a.last_name))
    is_superuser = False
    is_staff = False
    password = make_password("kintshop1234")

    date_joined = factory.LazyFunction(timezone.now)


class SuperUserFactory(UserFactory):
    is_superuser = True
    is_staff = True
    role = SUPER_ADMIN


class CustomerUserFactory(UserFactory):
    role = CUSTOMER


def unrolled_iterator(func):
    return factory.Iterator(func(), cycle=False)


def starts_on():
    now = timezone.now()
    my_date = now - timedelta(days=random.randint(1, 3))
    while True:
        yield my_date
        my_date = now - timedelta(days=random.randint(1, 3))


def ends_on():
    now = timezone.now()
    my_date = now + timedelta(days=random.randint(0, 3))
    while True:
        yield my_date
        my_date = now + timedelta(days=random.randint(0, 3))


starts_on_gen = starts_on()
ends_on_gen = ends_on()

address_dict = {
    "id": 367,
    "il": {
        "id": 6,
        "name": "Ankara"
    },
    "vkn": "",
    "ilce": {
        "id": 72,
        "il": 6,
        "name": "Çankaya"
    },
    "tckn": "23243432432",
    "owner": 270,
    "title": "Ev",
    "country": {
        "id": 225,
        "flag": {
            "id": 228,
            "slug": None,
            "original": "http://65.109.128.137:9000/images/flags/originals/tr.svg",
            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/tr.svg"
        },
        "iso2": "TR",
        "iso3": "TUR",
        "name": "Turkey"
    },
    "is_active": True,
    "last_name": "Kozoğlu",
    "first_name": "Şeyma",
    "is_current": True,
    "posta_kodu": "06805",
    "fatura_type": "Bireysel",
    "mahalle_koy": {
        "id": 5424,
        "ilce": 72,
        "name": "Ahlatlıbel Mah.",
        "il_name": "Ankara",
        "ilce_name": "Çankaya",
        "posta_kodu": "06805"
    },
    "pasaport_no": None,
    "company_name": "",
    "mobile_phone": "05555555555",
    "vergi_dairesi": None,
    "street_address": "Ahlatlıbel Mah. Belligün Cad. No:14/8 Ankara/Çankaya",
    "e_fatura_mukellefiyim": None
}

#
# class MailFactory(GeneralModelFactory):
#     class Meta:
#         model = Mail
#
#     vendor = factory.SubFactory(VendorFactory)
#     customer = factory.SubFactory(CustomerUserFactory)
#     order_num = factory.Faker("name")
#     type = random.choice([REGISTRATION_EMAIL,
#                           SUPERADMIN_PASSWORD_RESET_EMAIL,
#                           PASSWORD_RESET_EMAIL,
#                           VENDOR_REGISTRATION_CODE_EMAIL,
#                           VENDOR_INVOICE_EMAIL,
#                           CAMPAIGN_EMAIL,
#                           ORDER_EMAIL])
#     title = factory.Faker("name")
#     template = factory.Faker("name")
#     text = factory.Faker("name")
#     to_email = factory.Faker("email")
#     bcc = factory.Faker("email")
#     cc = factory.Faker("email")
#     from_email = "postmaster@kintyazilim.com",
#     from_user = factory.LazyAttribute(lambda obj: obj.customer.username)
#     attachments = factory.RelatedFactory(AttachmentFactory, factory_related_name='mail')
#     created_by = factory.SubFactory(SuperUserFactory)
#
