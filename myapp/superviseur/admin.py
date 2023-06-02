from django.contrib.gis import admin
from django.utils.translation import gettext_lazy as _

from .models import *

# Register your models here.
admin.site.register(myPolygon)
class polygoneAdmin (admin.GISModelAdmin):
    list_display = ("geom")



admin.site.register(project)
admin.site.register(point)
admin.site.register(client)
admin.site.register(Post)


admin.site.site_title = _("smart for green")
admin.site.site_header = _("smart for green")
admin.site.index_title = _("admni")