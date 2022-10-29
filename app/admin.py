from django.contrib import admin

from app.forms import UserMaskAdmin

from .models import User, Patient, Scheduling


class UserMask(admin.ModelAdmin):
    form = UserMaskAdmin

    class Media:
        js=(
            "jquery.mask.min.js",
            "custom.js",
            )

admin.site.register(User)
admin.site.register(Patient, UserMask)
admin.site.register(Scheduling)
