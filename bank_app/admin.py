from django.contrib import admin

# Register your models here.
from bank_app.models import Branch, District, Member

admin.site.register(Branch)
admin.site.register(District)
admin.site.register(Member)
