from django.contrib import admin
from .models import Board, Associate, Dependant, Blog, BlogComment, Timesheet, Task


# Register your models here.
admin.site.register(Board)

admin.site.register(Associate)
admin.site.register(Dependant)
admin.site.register(Timesheet)

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Task)

