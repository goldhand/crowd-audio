from django.db import models


class Payment(models.Model):
	competition = models.ForeignKey("competitions.Competition", related_name="payments")
	user = models.ForeignKey("users.User", related_name="payments")
	transaction = models.OneToOneField("transactions.Transaction")
	amount = models.DecimalField(decimal_places=2, max_digits=7)

	def __unicode__(self):
		return self.amount