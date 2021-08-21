"""bonds_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from bonds_app.views import (hello_world,
                             # BondListView,
                             # BondRetrieveView,
                             BondListCreateView,
                             BondRetrieveUpdateView)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('hello-world', hello_world, name='hello-world'),
    # path('bond-list/', BondListView.as_view(), name='bond-list'),
    # path('bond/<int:pk>', BondRetrieveView.as_view(), name='bond-retrieve'),
    path('api/bond/list-create/', BondListCreateView.as_view(), name='bond-list-create'),
    path('api/bond/<int:pk>/retrieve-update/', BondRetrieveUpdateView.as_view(),
         name='bond-retrieve-update')
]
