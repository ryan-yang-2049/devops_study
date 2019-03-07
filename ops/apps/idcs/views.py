<<<<<<< HEAD
from rest_framework import viewsets

from idcs.models import Idc
from idcs.serializers import IdcSerializers



class IdcViewSet(viewsets.ModelViewSet):
	"""
	retrive:
		返回指定IDC信息
	list :
		返回IDC列表
	update :
		更新IDC信息
	destroy :
		删除IDC记录
	create :
		创建IDC记录
	partial_update :
		更新部分字段
	"""

	queryset = Idc.objects.all()
	serializer_class =  IdcSerializers











=======
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
>>>>>>> 28de3e67c806bd548f32ba1fec70e7e0ab4fa46f


# 转 JSON
class JSONResponse(HttpResponse):

<<<<<<< HEAD

=======
	def __init__(self, data, **kwargs):
		kwargs.setdefault('content_type', 'application/json')
		content = JSONRenderer().render(data)
		super(JSONResponse, self).__init__(content=content, **kwargs)  # 等价于 HttpResponse(content)


def idc_list(request, *args, **kwargs):
	if request.method == "GET":
		queryset = Idc.objects.all()
		serializer = IdcSerializers(queryset, many=True)
		return  JSONResponse(serializer.data)
	elif request.method == "POST":
		data = JSONParser().parse(request)
		serializer = IdcSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
	return HttpResponse("OK.......")


def idc_detail(request,pk,*args,**kwargs):
	try:
		idc = Idc.objects.get(pk=pk)
	except Idc.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == "GET":
		serializer = IdcSerializers(idc)
		return JSONResponse(serializer.data)

	elif request.method == "PUT":

		content = JSONParser().parse(request)
		serializer = IdcSerializers(idc,data=content)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)

		return JSONResponse(serializer.errors,status=400)

	elif request.method == "DELETE":
		idc.delete()
		return  HttpResponse(status=204)








>>>>>>> 28de3e67c806bd548f32ba1fec70e7e0ab4fa46f





