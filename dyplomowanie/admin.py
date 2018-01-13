from django.contrib import admin
from .model.models import Deklaracja, FormaStudiow

class DeklaracajAdmin(admin.ModelAdmin):
    pass


class FormaStudiowAdmin(admin.ModelAdmin):
    pass

admin.register(Deklaracja, DeklaracajAdmin)
admin.register(FormaStudiow, FormaStudiowAdmin)
