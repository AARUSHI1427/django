from django.contrib import admin
from first_app.models import AccessRecord,Topic,webpage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(webpage)
