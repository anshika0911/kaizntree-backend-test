from django.urls import path
from . import views
from .views import CategoriesListCreateAPIView, CategoriesRetrieveUpdateDestroyAPIView,DataListCreateAPIView,DataRetrieveUpdateDestroyAPIView,ItemsListCreateAPIView, ItemsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('data/', DataListCreateAPIView.as_view(), name='data-list-create'),
    path('data/<int:pk>/', DataRetrieveUpdateDestroyAPIView.as_view(), name='data-detail'),
    path('categories/', CategoriesListCreateAPIView.as_view(), name='categories-list-create'),
    path('categories/<int:pk>/', CategoriesRetrieveUpdateDestroyAPIView.as_view(), name='categories-detail'),
    path('items/', ItemsListCreateAPIView.as_view(), name='items-list-create'),
    path('items/<int:pk>/', ItemsRetrieveUpdateDestroyAPIView.as_view(), name='items-detail'),
    path('login/', views.login_api, name='login_api'),
    path('dashboard/', views.item_dashboard_api, name='item_dashboard_api'),
    path('get_items/', ItemsListCreateAPIView.as_view(), name='item_dashboard'),
]

