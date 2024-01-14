from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/', views.register_user, name='register'),
    path('view/<int:pk>', views.view_customer, name='viewcustomer'),
    path('delete/<int:pk>', views.delete_customer, name='deletecustomer'),
    path('addcustomer', views.add_customer, name='addcustomer'),
    path('update/<int:pk>', views.update_customer, name='updatecustomer'),
]