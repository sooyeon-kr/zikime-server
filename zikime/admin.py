from django.contrib import admin
from . import models # 👈 해당 model이 존재하는 파일을 import

# admin.site.register(User)
@admin.register(models.CustomUser) # 👈 데코레이터로 등록
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Permission) 
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Serial) 
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Device) 
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Status) 
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Attachment) 
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.History) 
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Regist) 
class CustomUserAdmin(admin.ModelAdmin):
    pass
