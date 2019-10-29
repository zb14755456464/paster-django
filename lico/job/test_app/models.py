# Copyright 2019-present Lenovo
# Confidential and Proprietary


from django.db import models
from django.db.models import CharField, IntegerField


class Human(models.Model):
    name = CharField(max_length=100, null=False)
    age = IntegerField()
