from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import Menu
from .serializers import MenuItemSerializer

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=10)
        self.assertEqual(item.__str__(), "IceCream : 80")
        
class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title="Pizza", price=10, inventory=10)
        Menu.objects.create(title="Hamburger", price=20, inventory=10)
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        
    def test_get_all(self):
        url = reverse('menu-items')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        serialized_data = MenuItemSerializer(Menu.objects.all(), many=True)
        
        self.assertEqual(response.data, serialized_data.data)
        
        
