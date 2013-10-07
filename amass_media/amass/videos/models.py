from django.db import models
from django.contrib.auth.models import User
from amass.common.models import Named, ProjectType
from django.db.models.signals import post_save

class Project(Named):
    # constants for the status
    STATUS_PENDING = 0
    STATUS_OPEN = 1
    STATUS_UNDERWAY = 2
    STATUS_COMPLETED = 3

    # human readable displays
    STATUS_CHOICES = (
        (STATUS_PENDING, u"Pending"),
        (STATUS_OPEN, u"Open"),
        (STATUS_UNDERWAY, u"Underway"),
        (STATUS_COMPLETED, u"Completed"),
    )

    creator = models.ForeignKey(User, related_name="creator")
    types = models.ManyToManyField(ProjectType)
    status = models.SmallIntegerField(db_index=True, choices=STATUS_CHOICES)
    budget = models.IntegerField(db_index=True)
    posted_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    application_date = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True, auto_now=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    followers = models.ManyToManyField(User, related_name="followers")

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    """Profile for some user on the site"""
    user = models.OneToOneField(User)
    position = models.CharField(max_length=100)
    projectFollowing = models.ManyToManyField(Project)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Video(Named):
    creator = models.ForeignKey(UserProfile)
    project = models.ForeignKey(Project)
    completion_date = models.DateField(auto_now_add=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Organization(Named):
    """Class representing an organization on the site."""

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    byline = models.TextField()
    description = models.TextField()
