from django.urls import path
from .views import (
    # ListProductApiView,
    # CreateProductAPIView,
    # RetrieveProductAPIView,
    # UpdateProductAPIView,
    # DestroyProductAPIView,
    ListCreateProductAPIView,
    RetrieveUpdateDestroyProductAPIView
)

urlpatterns = [
    path('list-create/', ListCreateProductAPIView.as_view(), name='list-create'),
    path('rad/<int:id>/', RetrieveUpdateDestroyProductAPIView.as_view(),
         name='rad'),

    # path('list/', ListProductApiView.as_view(), name='list'),
    # path('create/', CreateProductAPIView.as_view(), name='create'),
    # path('retrieve/<int:id>/', RetrieveProductAPIView.as_view(), name='retrieve'),
    # path('update/<int:id>/', UpdateProductAPIView.as_view(), name='update'),
    # path('destroy/<int:id>/', DestroyProductAPIView.as_view(), name='destroy'),

]
