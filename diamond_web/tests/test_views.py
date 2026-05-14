from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class HomeViewTest(TestCase):
    def setUp(self):
        # 1. Buat user test
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'  # password tidak dipakai di force_login
        )
        # 2. Force login sebelum setiap test method
        self.client.force_login(self.user)

    def test_home_page_returns_200(self):
        response = self.client.get(reverse('diamond_web:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diamond_web/home.html')

    def test_protected_view_redirects_when_not_logged_in(self):
        # Logout dulu untuk test behavior saat belum auth
        self.client.logout()
        response = self.client.get(reverse('diamond_web:ticket_list'))
        self.assertEqual(response.status_code, 302)  # Redirect ke login