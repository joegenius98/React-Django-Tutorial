from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')
        # id = primary key that can identify a model amongst all the other models, usually an integer. Automatically
        # created when we insert a new room into our database.
