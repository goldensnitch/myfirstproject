from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics' ,on_delete=models.DO_NOTHING)

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name= 'posts',on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.DO_NOTHING)

State_Choices = (
('Assam','Assam'),
('Tamil Nadu', 'Tamil Nadu'),
)
City_Choices = (
('Guwahati', 'Guwahati'),
('Chennai', 'Chennai'),
)
Relationship_Choices = (
('Father', 'Father'),
('Mother', 'Mother'),
('Brother', 'Brother'),
('Sister', 'Sister'),
)
RequestType_Choices = (
('Ad-hoc', 'Ad-hoc'),
('Tender', 'Tender'),
)
RequestStatus_Choices = (
('New Request', 'New Request'),
('Quote In Progress', 'Quote In Progress'),
('Quote Sent', 'Quote Sent'),
)

class Associate(models.Model):
    First_Name = models.CharField(max_length=50, blank=False)
    Last_Name = models.CharField(max_length=50, blank=False)
    Date_of_Birth = models.DateField(blank=False)
    FatherName = models.CharField("Father\'s Name", max_length=100, blank=True)
    MotherName = models.CharField("Mother\'s Name", max_length=100, blank=True)
    Address_Line_1 = models.CharField(max_length=255, blank=True)
    Address_Line_2 = models.CharField(max_length=255, blank=True)
    City = models.CharField(max_length=50, choices=City_Choices, default='Chennai', blank=False)
    State = models.CharField(max_length=50, choices=State_Choices, default='Tamil Nadu', blank=False)
    Pin_Code = models.CharField(max_length=6, blank=True)
    PF = models.CharField(max_length=20, blank=True)
    ESI = models.CharField(max_length=20, blank=True)
    PAN = models.CharField(max_length=10, blank=True)
    Aadhar = models.CharField(max_length=20, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Associates')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name
    def Display_Name(self):
        return self.First_Name + ' ' + self.Last_Name

class Dependant(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    Relationship = models.CharField(max_length=50, choices=Relationship_Choices, default='Father', blank=False)
    Date_of_Birth = models.DateField(blank=False)
    Associate = models.ForeignKey(Associate, on_delete=models.CASCADE, related_name='Dependants')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Dependants')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Name

class Client(models.Model):
    Name = models.CharField(max_length=255, blank=False, unique=True)
    Address_Line_1 = models.CharField(max_length=255, blank=True)
    Address_Line_2 = models.CharField(max_length=255, blank=True)
    City = models.CharField(max_length=50, choices=City_Choices, default='Chennai', blank=False)
    State = models.CharField(max_length=50, choices=State_Choices, default='Tamil Nadu', blank=False)
    Pin_Code = models.CharField(max_length=6, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Clients')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Name

class Request(models.Model):
    ID = models.AutoField(primary_key=True)
    Client = models.ForeignKey(Client, blank=False, on_delete=models.DO_NOTHING, related_name='Requests')
    Project = models.CharField(max_length=255, blank=False)
    Details = models.TextField(max_length=4000, blank=False)
    Type = models.CharField(max_length=50, choices=RequestType_Choices, default='Ad-hoc', blank=False)
    Status = models.CharField(max_length=50, choices=RequestStatus_Choices, default='New', blank=False)
    Quote_Date = models.DateField(blank=False)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Requests')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.ID + '-' + self.Project






