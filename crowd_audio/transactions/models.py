from django.db import models


class Transaction(models.Model):
	key = models.TextField()
	extra_data = models.TextField()

	def __unicode__(self):
		return self.key