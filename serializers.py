from rest_framework import serializers
from .models import Room, facilities

class FacilitySerializers(serializers.ModelSerializer):

    class Meta:

        model = facilities
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    itemRows = FacilitySerializers(read_only=True, many=True)
    class Meta:

        model = Room
        fields = "__all__"


# class PostformSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = facilities, Room
#         fields = ["Floor_name","no_rooms","Name"]
#
#     def clean(self):
#
#         super(PostformSerializers, self).clean()
#
#         roomName = self.cleaned_data.get('roomName')
#         occupancy = self.cleaned_data.get('occupancy')
#         if roomName == None:
#             self._errors['roomName'] = self.error_class([
#                 'Please enter a room name'])
#         if len(roomName) < 30:
#             self._errors['roomName'] = self.error_class([
#                 'Please enter a name less than 30 characters'])
#         if occupancy== None:
#             self._errors['username'] = self.error_class([
#                 'Please enter occupancy'])
#
#         return self.cleaned_data