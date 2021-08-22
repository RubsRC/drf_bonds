from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from bonds_app.views import (hello_world,
                             UserList,
                             UserDetail,
                             BondListCreateView,
                             BondRetrieveUpdateView)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('hello-world', hello_world, name='hello-world'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('api/bonds/', BondListCreateView.as_view(), name='bond-list-create'),
    path('api/bonds/<int:pk>/', BondRetrieveUpdateView.as_view(),
         name='bond-retrieve-update')
]
