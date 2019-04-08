from django.contrib import admin
from .models import Board, Associate, Dependant


# Register your models here.
admin.site.register(Board)

admin.site.register(Associate)
admin.site.register(Dependant)
