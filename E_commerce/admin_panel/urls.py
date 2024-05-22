from django.urls import path
from . import views


urlpatterns = [
    path('',views.admin_panel,name='admin_panel'),
    path('admin_users/',views.admin_users,name='admin_users'),
    path('admin_products/',views.admin_products,name='admin_products'),
    path('add_product/',views.add_product,name='add_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('admin_category/',views.admin_category,name='admin_category'),
    path('admin_userprofile/<int:id>/',views.admin_userprofile,name='admin_userprofile'),
    path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
]
