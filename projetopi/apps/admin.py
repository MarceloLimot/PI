from django.contrib import admin

from .models import App, LoginFunc, LoginDonat, LoginDoador

admin.site.register(App)
admin.site.register(LoginFunc)
admin.site.register(LoginDonat)
admin.site.register(LoginDoador)
