from django.db import models

class Named(models.Model):
    """Abstract base class for something that has a name"""

    name = models.CharField(max_length=200, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

class ProjectType(Named):
    """Class representing types of projects"""
    pass

class EquipmentType(Named):
    """Class representing types of equipment"""
    pass