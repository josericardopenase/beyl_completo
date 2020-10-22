from django.contrib import admin
from .models  import Plan, PlanInclude, PlanFeature


class PlanIncludeInline(admin.TabularInline):
    model = PlanInclude
    extra = 0


class PlanAdmin(admin.ModelAdmin):
    inlines = [PlanIncludeInline,]

admin.site.register( Plan , PlanAdmin )
admin.site.register(PlanFeature)