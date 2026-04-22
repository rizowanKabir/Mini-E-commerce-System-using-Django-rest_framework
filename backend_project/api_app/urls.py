from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register('products', views.product_list,basename='products')
router.register('order', views.order_list, basename='order')

urlpatterns = router.urls
#[
    #path("admin/", admin.site.urls),
    #path('product/', views.product_list.as_view(),name='product_list'),
    #path('', include(router.urls)),
    #path('product/<int:pk>/', views.product_details.as_view(), name='product_list'),
    #path('order/', views.order_list, name='order_list'),
 
#]
