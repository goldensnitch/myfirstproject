from rest_framework import serializers
from .models import Associate, Timesheet
from rest_framework import viewsets

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

User = get_user_model()


class AssociateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Associate
		fields = ['id','First_Name','Last_Name','Date_of_Birth']



class AssociateViewSet(viewsets.ModelViewSet):
	queryset = Associate.objects.all()
	serializer_class = AssociateSerializer



class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class UserDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserDetailsSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer







class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = ['id', 'Associate','Date','Details', 'Hours']



class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all().order_by('Associate', '-Date')
    serializer_class = TimesheetSerializer
    authentication_classes = (TokenAuthentication, ) 
    permission_classes = (IsAuthenticated, )


