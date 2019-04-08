from django import forms
from django.forms import widgets
from .models import Topic, Associate, Dependant, Client

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']





class DateInputWid(forms.DateInput):
    input_type = 'date'

class NewAssociateForm(forms.ModelForm):

    class Meta:
        model = Associate
        fields = ['First_Name', 'Last_Name', 'Date_of_Birth', 'FatherName', 'MotherName',
                  'Address_Line_1', 'Address_Line_2', 'City', 'State', 'Pin_Code',
                  'PF', 'ESI', 'PAN', 'Aadhar']
        widgets = {
            'Date_of_Birth': DateInputWid()
        }


class AssociateDetailsForm(forms.ModelForm):
    First_Name = forms.CharField(disabled=True)
  #  Last_Name = forms.CharField(disabled=True)
    class Meta:
        model = Associate
        fields = ['First_Name', 'Last_Name', 'Date_of_Birth', 'FatherName', 'MotherName',
                  'Address_Line_1', 'Address_Line_2', 'City', 'State', 'Pin_Code',
                  'PF', 'ESI', 'PAN', 'Aadhar']
        widgets = {
            'Date_of_Birth': DateInputWid()
        }


class PersonalInfoForm(forms.ModelForm):
    First_Name = forms.CharField(disabled=True)
    class Meta:
        model = Associate
        fields = ['First_Name', 'Last_Name', 'Date_of_Birth', 'FatherName', 'MotherName']
        widgets = {
            'Date_of_Birth': DateInputWid()
        }

class ContactInfoForm(forms.ModelForm):

    class Meta:
        model = Associate
        fields = ['Address_Line_1', 'Address_Line_2', 'City', 'State', 'Pin_Code']
        widgets = {
            'Date_of_Birth': DateInputWid()
        }

class IDProofInfoForm(forms.ModelForm):

    class Meta:
        model = Associate
        fields = ['PF', 'ESI', 'PAN', 'Aadhar']
        widgets = {
            'Date_of_Birth': DateInputWid()
        }

class DependantInfoForm(forms.ModelForm):

    class Meta:
        model = Dependant
        fields = ['Name', 'Relationship', 'Date_of_Birth']
        widgets = {
            'Date_of_Birth': DateInputWid()
        }

class NewClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['Name', 'Address_Line_1', 'Address_Line_2', 'City', 'State', 'Pin_Code']

