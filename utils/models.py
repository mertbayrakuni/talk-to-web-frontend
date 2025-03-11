import logging
import uuid
from collections import OrderedDict

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    is_active = models.BooleanField(default=True, blank=True, null=True, verbose_name=_("Is Active?"))
    is_deleted = models.BooleanField(default=False, blank=True, null=True, verbose_name=_("Is Deleted?"))

    created_by = models.ForeignKey('user.User', on_delete=models.RESTRICT, blank=True, null=True,
                                   related_name='created_by_%(class)s_related', verbose_name=_("Created By"))
    updated_by = models.ForeignKey('user.User', on_delete=models.RESTRICT, blank=True, null=True,
                                   related_name='updated_by_%(class)s_related', verbose_name=_("Updated By"))
    deleted_by = models.ForeignKey('user.User', on_delete=models.RESTRICT, blank=True, null=True,
                                   related_name='deleted_by_%(class)s_related', verbose_name=_("Deleted By"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name=_("Deleted At"))
    objects = models.Manager()
    class Meta:
        abstract = True

    @classmethod
    def get_instance(cls, data):
        try:
            if data is None:
                return None
            elif (isinstance(data, dict) or isinstance(data, OrderedDict)) and "id" in data:
                return cls.objects.filter(id=data["id"]).first()
            else:
                return cls.objects.filter(id=data).first()
        except Exception as e:
            logging.exception(e)
            return None

    @classmethod
    def get_pk_type(cls):
        for field in cls._meta.fields:
            field_name = field.name
            field_type = field.get_internal_type()
            if field_name == "id":
                return field_type

    def save(self, *args, **kwargs):
        super(BaseModel, self).save(*args, **kwargs)


class BaseModel2(models.Model):
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    created_by = models.ForeignKey('user.User', on_delete=models.RESTRICT, blank=True, null=True,
                                   related_name='created_by_%(class)s_related')
    updated_by = models.ForeignKey('user.User', on_delete=models.RESTRICT, blank=True, null=True,
                                   related_name='updated_by_%(class)s_related')
    deleted_by = models.ForeignKey('user.User', on_delete=models.RESTRICT, blank=True, null=True,
                                   related_name='deleted_by_%(class)s_related')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    class Meta:
        abstract = True

    @classmethod
    def get_pk_type(cls):
        for field in cls._meta.fields:
            field_name = field.name
            field_type = field.get_internal_type()
            if field_name == "id":
                return field_type

    @classmethod
    def get_instance(cls, data):
        try:
            if data is None:
                return None
            elif (isinstance(data, dict) or isinstance(data, OrderedDict)) and "id" in data:
                return cls.objects.filter(id=data["id"]).first()
            else:
                return cls.objects.filter(id=data).first()
        except Exception as e:
            logging.exception(e)
            return None

    def save(self, *args, **kwargs):
        super(BaseModel2, self).save(*args, **kwargs)
