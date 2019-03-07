# -*- coding: utf-8 -*-

# 进行序列化的模块
from rest_framework import  serializers

from idcs.models import Idc
class IdcSerializers(serializers.Serializer):
	"""
	IDC 序列化类
	"""
	# 序列化字段,序列化后的类型是返回给前端的类型

	id      = serializers.IntegerField(read_only=True)  # read_only 只读，提交ID忽略
	name    = serializers.CharField(required=True,max_length=32,
	                                label="机房名称",
	                                help_text="机房名称",
	                                error_messages={"blank":"机房名称不能为空","required":"这个字段为必要字段"})  # require 必须传递,直接在程序段限制长度，不用去数据库校验长度
	address = serializers.CharField(required=True,max_length=256,label="机房地址",help_text="机房地址")
	phone   = serializers.CharField(required=True,max_length=15,label="联系电话",help_text="联系电话")
	email   = serializers.EmailField(required=True,label="联系邮箱",help_text="联系邮箱")
	letter  = serializers.CharField(required=True,max_length=5,label="机房简称",help_text="机房简称")


	def create(self, validated_data):

		# 传ID表示修改，不传ID 表示创建
		return  Idc.objects.create(**validated_data)


	def update(self, instance, validated_data):
		instance.name = validated_data.get("name",instance.name)
		instance.address = validated_data.get("name",instance.address)
		instance.phone = validated_data.get("name",instance.phone)
		instance.email = validated_data.get("name",instance.email)
		instance.save()

		return instance








