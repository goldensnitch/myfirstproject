from django.contrib import admin
from .models import Board, Associate, Dependant, Blog, Timesheet


# Register your models here.
admin.site.register(Board)

admin.site.register(Associate)
admin.site.register(Dependant)
admin.site.register(Timesheet)

admin.site.register(Blog)
