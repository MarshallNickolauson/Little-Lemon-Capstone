from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer