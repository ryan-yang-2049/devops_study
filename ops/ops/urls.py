"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls


from idcs.views import IdcViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register("idcs",IdcViewSet,base_name="idcs")
router.register("users",UserViewSet,base_name="users")



# 接口文档需要安装： python3 -m pip install coreapi

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
	url(r'^',include(router.urls)),
	url(r'^docs/',include_docs_urls("51reboot运维平台接口文档"))
]
