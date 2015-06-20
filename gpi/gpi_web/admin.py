from django.contrib import admin
from gpi.gpi_web.models import Release, Project



class ReleaseAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Release, ReleaseAdmin)
admin.site.register(Project, ProjectAdmin)
