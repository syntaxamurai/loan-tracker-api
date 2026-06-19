from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Loan, Repayment

admin.site.register(User, UserAdmin)
admin.site.register(Loan)
admin.site.register(Repayment)