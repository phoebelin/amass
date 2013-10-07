from django.contrib import admin

from amass.common.models import ProjectType, EquipmentType
from amass.videos.models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    pass

class ProjectTypeAdmin(admin.ModelAdmin):
    pass

class EquipmentTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
