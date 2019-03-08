# -*- coding: utf-8 -*-
from django.db import models

from idcs.models import Idc


class Cabinet(models.Model):

	idc =  models.ForeignKey(verbose_name='所在机房',to=Idc)
	name = models.CharField(verbose_name="机柜标签",max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		db_table = "resource_cabinet"
		ordering = ["id",]












