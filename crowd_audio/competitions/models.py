from django.db import models

# Create your models here.


class Competition(models.Model):
	band = models.ForeignKey('bands.Band', related_name="competitions")
	type = models.ForeignKey('CompetitionType', related_name="competitions")
	funding = models.CharField(max_length=255, choices=[('crowd', 'Crowd Fund'), ('personal', 'Personally Fund')])

	def __unicode__(self):
		return "%s competion: %d" % (self.band.name, self.id)


class CompetitionType(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=7)

	def __unicode__(self):
		return self.name


class CompetitionProfile(models.Model):
	competition = models.ForeignKey(Competition)
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name