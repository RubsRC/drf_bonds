from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from bonds_app.views import (hello_world,
                             BondListCreateView,
                             BondRetrieveUpdateView)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('hello-world', hello_world, name='hello-world'),
    path('api/bond/list-create/', BondListCreateView.as_view(), name='bond-list-create'),
    path('api/bond/<int:pk>/retrieve-update/', BondRetrieveUpdateView.as_view(),
         name='bond-retrieve-update')
]
