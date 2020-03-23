from django.contrib import admin
from .models import Board, Associate, Dependant, Blog


# Register your models here.
admin.site.register(Board)

admin.site.register(Associate)
admin.site.register(Dependant)

admin.site.register(Blog)
