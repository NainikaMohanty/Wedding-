from django.contrib import admin
from application1.models import Registerer
class Registerer_Admin(admin.ModelAdmin):
    list_display=['Name','Mobile_Number','Email','Username','Password','Confirm_password']
admin.site.register(Registerer,Registerer_Admin)

