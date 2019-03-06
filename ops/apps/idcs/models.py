from django.db import models

# Create your models here.


class Idc(models.Model):
	name = models.CharField(verbose_name='机房名称',max_length=32)
	address = models.CharField(verbose_name='机房地址',max_length=256)
	phone = models.CharField(verbose_name='联系人',max_length=15)
	email = models.EmailField(verbose_name='邮件地址',default="null")
	letter = models.CharField(verbose_name="I机房简称",max_length=5)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'resourse_idc'