import datetime

from peewee import CharField, Model, DateTimeField

from db import mydatabase


class LinkEntity(Model):
    local_address = CharField()
    real_address = CharField()
    name = CharField(null=True)
    author = CharField(null=True)
    deadline = DateTimeField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydatabase
