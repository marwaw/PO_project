from django.contrib import admin
from .model.Deklaracja import Deklaracja
from .model.FormaStudiow import FormaStudiow
from .model.JezykRealizacji import JezykRealizacji
from .model.NauczycielAkademicki import NauczycielAkademicki
from .model.PowiadomienieOWyborzeTematu import PowiadomienieOWyborzeTematu
from .model.StopienStudiow import StopienStudiow
from .model.Student import Student
from .model.Temat import Temat
from .model.TypPracy import TypPracy

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
