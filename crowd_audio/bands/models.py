from django.db import models

# Create your models here.


class Band(models.Model):
	name = models.CharField(max_length=255)
	owner = models.ForeignKey('users.User', related_name="owned_bands")
	members = models.ManyToManyField('users.User', related_name="bands")

	def __unicode__(self):
		return self.name
