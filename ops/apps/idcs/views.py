

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


from idcs.models import Idc
from idcs.serializers import IdcSerializers


def  idc_list(request,*args,**kwargs):

	if request.method == "GET":
		queryset = Idc.objects.all()
		serializer = IdcSerializers(queryset,many=True)
		content = JSONRenderer().render(serializer.data)
		return  HttpResponse(content,content_type="application/json")
	elif request.method == "POST":
		pass

	return HttpResponse("")




