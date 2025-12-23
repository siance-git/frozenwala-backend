from django.db import models

# Create your models here.
class Walet(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    wallet_value = models.FloatField(default=0.0)


class WalletTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    transaction_id = models.BigIntegerField(null=True, blank=True)
    opening_bal = models.DecimalField(max_digits=13, decimal_places=2)
    credit_bal = models.DecimalField(max_digits=13, decimal_places=2)
    debit_bal = models.DecimalField(max_digits=13, decimal_places=2)
    closing_bal = models.DecimalField(max_digits=13, decimal_places=2)
    transaction_type = models.CharField(max_length=155)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'wallet_transaction' 


class PurchaseBenefit(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50,default='1')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefit_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"PurchaseBenefit #{self.id}"


from django.db import models

class InstallationBenefit(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50, default='1')

    def __str__(self):
        return f"Installation Benefit - {self.price} "


class ReferralBenefit(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50, default='1')

    def __str__(self):
        return f"Referral Benefit - {self.price} "
