from django.db import models

# Create your models here.


class Engineer(models.Model):
	name = models.CharField(max_length=255)
	user = models.ForeignKey('users.User', related_name="engineers")

	def __unicode__(self):
		return self.name
