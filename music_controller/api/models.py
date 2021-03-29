from django.db import models
import string
import random

# random and unique 8-digit code generation


def generate_unique_code():
    length = 6
    while True:
        # query and look at all the rooms in our databases unitl we randomly generate a new, unique code
        # ASCII uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


# Create your models here.
'''
Rows/tables to store information --> database.
When we create a table, we create a model instead. Django will perform the database operations for us.
Django = layer of abstraction for databases.
'''

# Room model. Group similar users together in a room. One person hosts the music and others can join and change music.


class Room(models.Model):
    # Tim: What is a room? What compromises or make up a room?
    # Joseph: A room has people, music speaker/player, a host, non-host people, a code to get in.
    # stores a bunch of characters

    # other fields for CharField: https://www.geeksforgeeks.org/charfield-django-models/#:~:text=CharField%20is%20used%20for%20storing,it%20is%20required%20to%20store.
    code = models.CharField(max_length=8, default="", unique=True)
    # one host cannot have multiple rooms
    # holds some information that links back to the host, keeps track who the host is
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(
        null=False, default=False)  # null means we must pass a value
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    # Fat models and thin views --> put most of the logic on the models.
