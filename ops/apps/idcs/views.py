from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from idcs.models import Idc
from idcs.serializers import IdcSerializers

# 转 JSON
class JSONResponse(HttpResponse):

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













