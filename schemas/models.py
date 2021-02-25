from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Schema(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)

    class SeparatorType(models.TextChoices):
        COMMA = 'CM', _('Comma (,)')
        SEMICOLON = 'SM', _('Semicolon (;)')
        TAB = 'TB', _('Tab (\\t)')
        PIPE = 'PP', _('Pipe (|)')

    column_separator_type = models.CharField(
        max_length=2,
        db_index=True,
        choices=SeparatorType.choices,
        default=SeparatorType.COMMA,
    )

    class CharacterType(models.TextChoices):
        DOUBLE = 'DQ', _('Double quote (")')
        SINGLE = 'SQ', _('Single quote (\')')

    string_character_type = models.CharField(
        max_length=2,
        db_index=True,
        choices=CharacterType.choices,
        default=CharacterType.DOUBLE,
    )

    def __str__(self):
        return self.name


class ColumnTypes(models.Model):
    name = models.CharField(max_length=128)
    with_extra_from_to = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=128)
    type = models.ForeignKey(ColumnTypes, on_delete=models.CASCADE, blank=True)
    with_extra_from_to = models.BooleanField(default=False)
    extra_from = models.PositiveIntegerField(blank=True)
    extra_to = models.PositiveIntegerField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Dataset(models.Model):
    class StatusType(models.TextChoices):
        READY = 'RD', _('Ready')
        PROCESSING = 'PR', _('Processing')

    status_type = models.CharField(
        max_length=2,
        db_index=True,
        choices=StatusType.choices,
        default=StatusType.PROCESSING,
    )

    file = models.FileField(upload_to='schemas/%Y/%m/%d', blank=True)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, blank=True)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.created
