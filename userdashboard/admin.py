from django.contrib import admin
from .models import Investments,Transactions,Packages

# Register your models here.

admin.site.register(Investments)
admin.site.register(Transactions)
admin.site.register(Packages)
