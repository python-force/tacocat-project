import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('tacos.db')

class User(UserMixin, Model):
    pub_date = DateTimeField(default=datetime.datetime.now)
    email = CharField(unique=True)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE
        order_by = ('-pub_date',)


    @classmethod
    def create_user(cls, email, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password))
        except IntegrityError:
            raise ValueError("User already exists")


class Taco(Model):
    pub_date = DateTimeField(default=datetime.datetime.now)
    protein = CharField(max_length=30)
    shell = CharField(max_length=30)
    cheese = BooleanField(default=False)
    extras = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-pub_date',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco], safe=True)
    DATABASE.close()