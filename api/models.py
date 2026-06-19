from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Loan(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paid', 'Paid'),
        ('defaulted', 'Defaulted'),
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='loans'
        )
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=4)
    term_months = models.IntegerField()
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='active'
    )
    disbursed_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.id}: {self.user.email} - Kshs. {self.principal_amount}"
    
class Repayment(models.Model):
    loan = models.ForeignKey(
        Loan, 
        on_delete=models.CASCADE,
        related_name='repayments'
    )
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repayment {self.id}: Loan {self.loan.id} - Kshs. {self.amount_paid}"