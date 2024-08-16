from django.urls import path
from app import views
urlpatterns = [
path('contact/', views.contact_view, name='contact'),
path('thanks/', views.thanks_view, name='thanks'),
path('test/', views.test_view, name='test'),
    path('contact/', views.contact_view, name='contact')
]
