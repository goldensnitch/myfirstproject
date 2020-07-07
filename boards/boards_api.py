from rest_framework import serializers
from .models import Associate, Timesheet
from rest_framework import viewsets

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


class AssociateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Associate
		fields = ['id','First_Name','Last_Name','Date_of_Birth']


class AssociateViewSet(viewsets.ModelViewSet):
	queryset = Associate.objects.all()
	serializer_class = AssociateSerializer





class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = ['id', 'Associate','Date','Details', 'Hours']


class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all().order_by('Associate', '-Date')
    serializer_class = TimesheetSerializer
    authentication_classes = (TokenAuthentication, ) 
    permission_classes = (IsAuthenticated, )





class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

