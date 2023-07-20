from django.contrib import admin
from django.contrib.auth.models import User, Permission
from django.contrib.auth.hashers import make_password
from vehiculo.models import Vehiculo

# Register your models here.

admin.site.register(Vehiculo)
# admin.site.unregister(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'has_visualizar_catalogo_permission')
#     list_display_links = ("username", )
#     search_fields = ("username", "first_name", "last_name")
    
#     def has_visualizar_catalogo_permission(self, obj):
#         return obj.has_perm('vehiculo.visualizar_catalogo')
    
#     has_visualizar_catalogo_permission.boolean = True
#     has_visualizar_catalogo_permission.short_description = 'Visualizar Catálogo'
    
#     def save_model(self, request, obj, form, change):
#         # Encriptar la contraseña antes de guardar el usuario
#         obj.password = make_password(form.cleaned_data.get('password'))
#         super().save_model(request, obj, form, change)