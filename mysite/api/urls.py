from django.urls import path
from . import views

urlpatterns = [
    path('bloposts/', views.BlogPostListCreate.as_view(), name='blogpost-view-create')
]