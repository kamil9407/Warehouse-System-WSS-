from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path('create-report/', views.generate_pdf, name='create_report'),
    
    path('all-report', views.create_whole_report, name = 'all_report'),

    path('list/', views.ware_list_view, name='ware_list'),

    path('detail/<int:pk>/', views.ware_detail_view, name='ware_detail'),
]