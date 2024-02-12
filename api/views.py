from rest_framework import generics
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render
from .forms import LoginForm
from rest_framework import generics
from rest_framework import filters
from .models import Data
from .serializers import DataSerializer
from .models import Categories
from .serializers import CategoriesSerializer
from .models import Items
from .serializers import ItemsSerializer
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate

def login_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User is authenticated, perform further actions
            # For example, set session variables or redirect to another page
            return HttpResponse('User authenticated successfully')
        else:
            # User authentication failed, handle accordingly
            return HttpResponse('Invalid username or password')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('items')
        else:
                # Handle invalid credentials
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def item_dashboard_api(request):
    return render(request, 'item_dashboard.html')

def item_dashboard(request):
    items = Items.objects.all().select_related('Categories')   # Get all items and convert to dictionary
    return JsonResponse(list(items), safe=False)

class DataListCreateAPIView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class CategoriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ItemsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sku', 'category_id__name']  # Adjust field name for searching
    ordering_fields = ['sku', 'in_stock', 'available_stock']

class ItemsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
