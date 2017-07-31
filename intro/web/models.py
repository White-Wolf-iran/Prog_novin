# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HeaderTitle(models.Model):
	text = models.CharField('title', max_length=70)
	def __unicode__(self):
		return self.text

class WelcomeText(models.Model):
	welcome = models.CharField('text', max_length=100)
	def __unicode__(self):
		return self.welcome