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

########################### 版本一 ##################################
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


########################### 版本二 ##################################
# 使用api_view
from  rest_framework.decorators import api_view
from rest_framework  import status
from rest_framework.response import Response

@api_view(["GET","POST"])
def idc_list_v2(request,*args,**kwargs):

	if request.method == "GET":
		queryset = Idc.objects.all()
		serializer = IdcSerializers(queryset,many=True)
		return Response(serializer.data)

	elif request.method == "POST":
		serializer =  IdcSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def idc_detail_v2(request,pk,*args,**kwargs):
	try:
		idc = Idc.objects.get(pk=pk)
	except Idc.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializer = IdcSerializers(idc)
		return Response(serializer.data)

	elif request.method == "PUT":
		serializer = IdcSerializers(idc,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
	elif request.method == "DELETE":
		idc.delete()
		return  Response(status=status.HTTP_204_NO_CONTENT)
####################### api_view 路由 #################

from rest_framework.reverse import reverse
@api_view(["GET"])
def api_root(request,format=None,*args,**kwargs):

	return Response({
		"idcs":reverse("idc_list_v6",request=request,format=format)
	})



########################### 版本三 ##################################

from rest_framework.views import APIView
from django.http import Http404
class IdcList(APIView):

	def get(self,request,format=None):
		queryset = Idc.objects.all()
		serializer = IdcSerializers(queryset,many=True)
		return Response(serializer.data)


	def post(self,request,format=None):
		serializer =  IdcSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class IdcDetailList(APIView):

	def get_object(self,pk):
		try:
			return Idc.objects.get(pk=pk)
		except Idc.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		idc = self.get_object(pk)
		serializer = IdcSerializers(idc)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		idc = self.get_object(pk)
		serializer = IdcSerializers(idc,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

	def delete(self,request,pk,format=None):
		idc = self.get_object(pk)
		idc.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)

########################### 版本四 ##################################

from rest_framework import mixins,generics

class IdcListV4(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):

	queryset = Idc.objects.all()
	serializer_class =  IdcSerializers

	def get(self,request,*args,**kwargs):

		return self.list(request, *args, **kwargs)

	def post(self,request,*args,**kwargs):

		return self.create(request, *args, **kwargs)


class IdcDetailV4(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

	queryset = Idc.objects.all()
	serializer_class =  IdcSerializers

	def get(self,request,pk,*args,**kwargs):

		return self.retrieve(request, *args, **kwargs)

	def put(self,request,*args,**kwargs):

		return self.update(request, *args, **kwargs)

	def delete(self,request,*args,**kwargs):

		return self.destroy(request,*args,**kwargs)



########################### 版本五 高级混合版本 ##################################

class IdcListV5(generics.ListCreateAPIView):
	queryset = Idc.objects.all()
	serializer_class =  IdcSerializers


class IdcDetailV5(generics.RetrieveUpdateDestroyAPIView):
	queryset = Idc.objects.all()
	serializer_class =  IdcSerializers


########################### 版本六  视图集 ##################################
from rest_framework import viewsets

class IdcListViewSetV6(
				viewsets.GenericViewSet,
				mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
				mixins.UpdateModelMixin,
                mixins.CreateModelMixin):
	queryset = Idc.objects.all()
	serializer_class = IdcSerializers


########################### 版本六  视图集 ##################################
class IdcViewSetV7(viewsets.ModelViewSet):
	# viewsets.ReadOnlyModelViewSet 继承此类的时候，就是只读,get属性
	queryset = Idc.objects.all()
	serializer_class =  IdcSerializers




















