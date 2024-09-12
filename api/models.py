from django.db import models
from datetime import date

# Create your models here.

class BenefitType(models.TextChoices):
    VOUCHER = "voucher", "Voucher"
    CASHBACK = "cashback", "Cashback"

class ValidityType(models.TextChoices):
    QUANTITY = "quantity", "Quantity"
    TENURE = "tenure", "Tenure"

def default_amount_options():
    return [10000, 20000, 50000]

def default_tenure_options():
    return [6, 12, 24]

class Plan(models.Model):
    planId = models.AutoField(primary_key=True)
    planName = models.CharField(max_length=500, default="This is not a valid plan. Allow us some time to fix this!")
    benefitType = models.CharField(max_length=50, choices=BenefitType.choices, default=BenefitType.VOUCHER)
    benefitPercentage = models.IntegerField(default=1)
    amountOptions = models.JSONField(default=default_amount_options, editable=False)
    tenureOptions = models.JSONField(default=default_tenure_options , editable=False)

    def __str__(self):
        return self.planName

class Promo(models.Model):
    promoId = models.AutoField(primary_key=True)
    planId = models.ForeignKey(Plan, related_name="promos", on_delete=models.CASCADE)
    promoName = models.CharField(max_length=500, default="This is not a valid promo. Allow us some time to fix this!")
    validityType = models.CharField(max_length=50, choices=ValidityType.choices, default=ValidityType.QUANTITY)
    quantity = models.IntegerField(null=True)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    benefitPercentage = models.IntegerField(default=1)

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=200)
    userMail = models.CharField(max_length=200)

    def __str__(self):
        return self.userName
    
class UserSelectedPlans(models.Model):
    id = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    planID = models.ForeignKey(Plan, on_delete=models.CASCADE)
    promoID = models.IntegerField()
    selectedAmount = models.IntegerField(null=True)
    selectedTenure = models.IntegerField(null=True)
    startDate = models.DateField(default=date.today)
    depositedAmount = models.IntegerField(default=0)

