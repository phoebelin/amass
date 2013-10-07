from django.db import models
from django.contrib.auth.models import User
from amass.common.models import Named, EquipmentType

class Equipment(Named):
    type = models.ForeignKey(EquipmentType)
    owner = models.ForeignKey(User, null=True)

class Loan(models.Model):
    borrowed = models.DateField(auto_now_add=True)
    returned = models.DateField(null=True, blank=True)
