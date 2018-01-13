from django.contrib import admin
from .model.models import Deklaracja, FormaStudiow, Nauczycielakademicki

class DeklaracajAdmin(admin.ModelAdmin):
    pass


class FormaStudiowAdmin(admin.ModelAdmin):
    pass

class NauczycielakademickiAdmin(admin.ModelAdmin):
    pass

admin.register(Deklaracja, DeklaracajAdmin)
admin.register(FormaStudiow, FormaStudiowAdmin)
admin.register(Nauczycielakademicki, NauczycielakademickiAdmin)
