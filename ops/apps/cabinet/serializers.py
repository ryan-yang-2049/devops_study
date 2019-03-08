# -*- coding: utf-8 -*-
from rest_framework import serializers

from idcs.serializers import IdcSerializers

from cabinet.models import Cabinet
from idcs.models import Idc
class CabinetSerializer(serializers.Serializer):

	# 多对一或者一对多或多对多,通过many去指定，通过queryset去指定表，通过PrimaryKeyRelatedField 主键去关联的

	idc = serializers.PrimaryKeyRelatedField(many=False,queryset=Idc.objects.all(),help_text="所在机房")
	name = serializers.CharField(required=True,label="机柜标签",help_text="机柜标签")

	# day05 04序列化高级用法
	def to_representation(self, instance):
		idc_obj = instance.idc
		ret = super(CabinetSerializer,self).to_representation(instance)
		ret["idc"] = {
			"id":idc_obj.id,
			"name":idc_obj.name
		}

		return ret

	def to_internal_value(self, data):
		print(data)
		return super(CabinetSerializer,self).to_internal_value(data)

	# 反序列化
	def create(self, validated_data):
		print(validated_data)
		return Cabinet.objects.create(**validated_data)





