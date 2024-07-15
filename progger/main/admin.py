from django.contrib import admin

from .forms import EquipmentForm
from .models import Equipment


class EquipmentRegisterAdmin(admin.ModelAdmin):
    list_display = ["title", "amount"]
    #list_display = [field.name for field in Equipment._meta.fields]
    #fields = ["title"]
    #list_filter = ["title"]
    #search_fields = ["title"]

    #exclude = ["title"]
    #inlines = [FieldMappingInline]

    class Meta:
        model = EquipmentForm


admin.site.register(Equipment, EquipmentRegisterAdmin)
