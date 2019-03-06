# -*- coding: utf-8 -*-
from django.conf.urls import url,include

from idcs import views

urlpatterns = [

	url(r'idcs/',views.idc_list,name="idc_list")
]








