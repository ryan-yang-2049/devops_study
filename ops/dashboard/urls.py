# -*- coding: utf-8 -*-
"""
__title__ = 'urls.py'
__author__ = 'yangyang'
__mtime__ = '2019-03-02'
"""
from django.conf.urls import url, include
from .views import MyView

urlpatterns = [
	url(r'user/',MyView.as_view())
]










