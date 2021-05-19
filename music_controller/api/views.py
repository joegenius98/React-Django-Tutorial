from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# /hello and /hi are examples of endpoints --> location of web server


# not only view, but create room (that's what generics does)
# generics.ListAPIView is an already-created view that returns to us all of the different rooms
# vs. generics.createAPIView allowed us to add information to the database
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()  # we want to return all of the room objects
    # How do I convert all the rooms to some format that I cna actually return? We use RoomSerializer
    serializer_class = RoomSerializer
# We now need a path to get to this function.
