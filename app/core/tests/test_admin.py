"""
Django Admin testleri.
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Admin site testleri."""

    def setUp(self):
        """Test için gerekli verileri hazırla."""
        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="testpass123"
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="testpass123", name="Test Kullanıcı"
        )

    def test_users_list(self):
        """Admin kullanıcı listesi sayfası çalışıyor mu."""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_edit_user_page(self):
        """Kullanıcı düzenleme sayfası çalışıyor mu."""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Admin kullanıcı ekleme sayfası çalışıyor mu."""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
