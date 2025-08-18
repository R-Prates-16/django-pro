from django.contrib import admin
from django.urls import path
from mycontacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('contact/<int:contact_id>/', views.detail, name='detail'),
    path('contact/<int:contact_id>/edit/', views.edit, name='edit'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
]
