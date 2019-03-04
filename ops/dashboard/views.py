from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, loader


# 23:33

class Test(object):
	http_method_names = ["get", 'post', 'put', 'delete']
	def as_view(self):
		def view(request, *args, **kwargs):
			self.request = request
			self.args = args
			self.kwargs = kwargs
			return self.dispatch(request, *args, **kwargs)
		return view

	# 分配视图
	def dispatch(self, request, *args, **kwargs):
		if request.method.lower() not in self.http_method_names:
			return self.http_method_not_allowed()
		handle = getattr(self, request.method.lower())
		return handle(request, *args, **kwargs)

	# 没有请求的方法
	def http_method_not_allowed(self, *args, **kwargs):
		pass

	def get(self, request, *args, **kwargs):
		# 返回用户列表
		return HttpResponse("ok")

	def post(self, request, *args, **kwargs):
		# 修改用户信息
		return HttpResponse("ok")

	def put(self, request, *args, **kwargs):
		# 创建用户
		return HttpResponse("ok")

	def delete(self, request, *args, **kwargs):
		# 删除用户
		return HttpResponse("ok")
# 14:01

import logging

logger = logging.getLogger("reboot")



from django.views import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
class MyView(View):
	per_page_num = 10

	def get(self, request, *args, **kwargs):
		logger.debug("这是第一条日志")
		try:
			page = int(request.GET.get("page",1))
		except:
			page = 1

		end = page * self.per_page_num
		start = end - self.per_page_num
		queryset = User.objects.all()[start:end]
		data = list(queryset.values("username","email"))

		return JsonResponse(data,safe=False)
