from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    #location urls
    path('location', views.get_location, name = 'get-location'),
    path('location/new/', views.post_location, name = 'post-location'),
    path('location/<int:pk>/', views.get_location_detail, name = 'get_location_detail'),
    path('location/<name>/', views.search_location, name = 'search_location_detail'),
    path('location/<int:pk>/edit/', views.put_location, name = 'put_location'),
    path('location/<int:pk>/delete/', views.delete_location, name = 'delete_location'),

    # department urls
    path('department', views.get_department, name = 'get-department'),
    path('department/new/', views.post_department, name = 'post-department'),
    path('department/<int:pk>/', views.get_department_detail, name = 'get_department_detail'),
    path('department/<name>/', views.search_department, name = 'search_department_detail'),
    path('department/<int:pk>/edit/', views.put_department, name = 'put_department'),
    path('department/<int:pk>/delete/', views.delete_department, name = 'delete_department'),

    # category urls
    path('category', views.get_category, name = 'get-category'),
    path('category/new/', views.post_category, name = 'post-category'),
    path('category/<int:pk>/', views.get_category_detail, name = 'get_category_detail'),
    path('category/<name>/', views.search_category, name = 'search_category_detail'),
    path('category/<int:pk>/edit/', views.put_category, name = 'put_category'),
    path('category/<int:pk>/delete/', views.delete_category, name = 'delete_category'),

    # subcategory urls
    path('subcategory', views.get_subcategory, name = 'get-subcategory'),
    path('subcategory/new/', views.post_subcategory, name = 'post-subcategory'),
    path('subcategory/<int:pk>/', views.get_subcategory_detail, name = 'get_subcategory_detail'),
    path('subcategory/<name>/', views.search_subcategory, name = 'search_subcategory_detail'),
    path('subcategory/<int:pk>/edit/', views.put_subcategory, name = 'put_subcategory'),
    path('subcategory/<int:pk>/delete/', views.delete_subcategory, name = 'delete_subcategory'),
]
