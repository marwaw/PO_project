from django.contrib import admin
from .model import Deklaracja
from .model import FormaStudiow
from .model import JezykRealizacji
from .model import NauczycielAkademicki
from .model import PowiadomienieOWyborzeTematu
from .model import StopienStudiow
from .model import Student
from .model import Temat
from .model import TypPracy

class DeklaracjaAdmin(admin.ModelAdmin):
    pass

class FormaStudiowAdmin(admin.ModelAdmin):
    pass

class JezykRealizacjiAdmin(admin.ModelAdmin):
    pass

class NauczycielAkademickiAdmin(admin.ModelAdmin):
    pass

class PowiadomienieOWyborzeTematuAdmin(admin.ModelAdmin):
    pass

class StopienStudiowAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

class TematAdmin(admin.ModelAdmin):
    pass

class TypPracyAdmin(admin.ModelAdmin):
    pass

admin.register(Deklaracja, DeklaracjaAdmin)
admin.register(FormaStudiow, FormaStudiowAdmin)
admin.register(JezykRealizacji, JezykRealizacjiAdmin)
admin.register(NauczycielAkademicki, NauczycielAkademickiAdmin)
admin.register(PowiadomienieOWyborzeTematu, PowiadomienieOWyborzeTematuAdmin)
admin.register(StopienStudiow, StopienStudiowAdmin)
admin.register(Student, StudentAdmin)
admin.register(Temat, TematAdmin)
admin.register(TypPracy, TypPracyAdmin)
