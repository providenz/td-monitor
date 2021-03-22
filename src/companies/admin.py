from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "siret", "td_id", "created", "is_verified")

    def is_verified(self, obj):
        return obj.status == Company.STATUS.verified

    is_verified.short_description = "Vérifiée"
    is_verified.boolean = True
