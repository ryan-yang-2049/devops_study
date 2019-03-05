from django.db import models

# Create your models here.



class Idc(models.Model):
	name        = models.CharField(verbose_name="机房名称",max_length=32)
	address     = models.CharField(verbose_name="机房地址",max_length=256)
	phone       = models.CharField(verbose_name="机房联系电话",max_length=15)
	email       = models.EmailField()
	letter      = models.CharField(verbose_name="idc 字母简称",max_length=5)
























