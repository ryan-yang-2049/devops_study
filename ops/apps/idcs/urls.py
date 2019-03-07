# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from idcs import views

# ############################## 版本一 ##############################
# urlpatterns = [
#
# 	url(r'idcs/$',views.idc_list,name="idc_list"),
# 	url(r'id/(?P<pk>\d+)/$',views.idc_detail,name="idc_detail"),
# ]
#
#
# ############################## 版本二 ##############################

#
# urlpatterns = [
#
# 	url(r'^$',views.api_root,name="idc_list_v2"),
# 	url(r'idcs/$',views.idc_list_v2,name="idc_list_v2"),
# 	url(r'idcs/(?P<pk>\d+)/$',views.idc_detail_v2,name="idc_detail_v2"),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
# # 盖行代码，使得浏览器端可以使用
# #       http://127.0.0.1:8000/idcs/
# #       http://127.0.0.1:8000/idcs.json
# #       http://127.0.0.1:8000/idcs.api
# #       http://127.0.0.1:8000/idcs/2.json
# #       http://127.0.0.1:8000/idcs/2.api
#
# ############################## 版本三 ##############################
#
# urlpatterns = [
# 	url(r'^$', views.api_root, name="idc_list_v3"),
# 	url(r'idcs/$', views.IdcList.as_view(), name="idc_list_v3"),
# 	url(r'idcs/(?P<pk>\d+)/$',views.IdcDetailList.as_view(),name="idc_detail_v3"),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
#
#
#
# ############################## 版本四 ##############################
# urlpatterns = [
# 	url(r'^$', views.api_root, name="idc_list_v4"),
# 	url(r'idcs/$', views.IdcListV4.as_view(), name="idc_list_v4"),
# 	url(r'idcs/(?P<pk>\d+)/$',views.IdcDetailV4.as_view(),name="idc_detail_v4"),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

############################## 版本五 ##############################
# urlpatterns = [
# 	url(r'^$', views.api_root, name="idc_list_v5"),
# 	url(r'^idcs/$', views.IdcListV5.as_view(), name="idc_list_v5"),
# 	url(r'^idcs/(?P<pk>\d+)/$',views.IdcDetailV5.as_view(),name="idc_detail_v5"),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# ############################## 版本六 ##############################
#
# idc_list = views.IdcListViewSetV6.as_view({
# 	'get':'list',
# 	'post':'create',
# })
# idc_detail = views.IdcListViewSetV6.as_view({
# 	'get':'retrieve',
# 	'put':'update',
# 	'delete':'destroy',
# })
#
#
# urlpatterns = [
# 	url(r'^$', views.api_root, name="api_root_v6"),
# 	url(r'^idcs/$', idc_list, name="idc_list_v6"),
# 	url(r'^idcs/(?P<pk>\d+)/$',idc_detail,name="idc_detail_v5"),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# ############################## 版本七 ##############################

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register("idcs",views.IdcViewSetV7)
#
#
# urlpatterns = [
# 	url(r'^',include(router.urls))
# ]






