"""
    Modeller için Test.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


# def create_user(email='user@example.com', password='testpass123'):
#     """Yeni bir kullanıcı oluşturun ve geri döndürün."""
#     return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """E-posta adresiyle kullanıcı oluşturma testi başarılı oldu."""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # def test_new_user_email_normalized(self):
    #     """Yeni kullanıcılar için test e-postası normalleştirilmiştir."""
    #     sample_emails = [
    #         ['test1@EXAMPLE.com', 'test1@example.com'],
    #         ['Test2@Example.com', 'Test2@example.com'],
    #         ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
    #         ['test4@example.COM', 'test4@example.com'],
    #     ]
    #     for email, expected in sample_emails:
    #         user = get_user_model().objects.create_user(email, 'sample123')
    #         self.assertEqual(user.email, expected)

    # def test_new_user_without_email_raises_error(self):
    #     """E-posta adresi olmadan kullanıcı oluşturmanın ValueError hatası verdiğini test edin."""
    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user('', 'test123')

    # def test_create_superuser(self):
    #     """Süper kullanıcı oluşturmayı test edin."""
    #     user = get_user_model().objects.create_superuser(
    #         'test@example.com',
    #         'test123',
    #     )

    #     self.assertTrue(user.is_superuser)
    #     self.assertTrue(user.is_staff)

    # def test_create_recipe(self):
    #     """recipe oluşturma testi başarılı oldu."""
    #     user = get_user_model().objects.create_user(
    #         'test@example.com',
    #         'testpass123',
    #     )
    #     recipe = models.Recipe.objects.create(
    #         user=user,
    #         title='Sample recipe name',
    #         time_minutes=5,
    #         price=Decimal('5.50'),
    #         description='Sample receipe description.',
    #     )

    #     self.assertEqual(str(recipe), recipe.title)

    # def test_create_tag(self):
    #     """Tag oluşturma testi başarılı oldu."""
    #     user = create_user()
    #     tag = models.Tag.objects.create(user=user, name='Tag1')

    #     self.assertEqual(str(tag), tag.name)

    # def test_create_ingredient(self):
    #     """ingredient oluşturma testi başarılı oldu."""
    #     user = create_user()
    #     ingredient = models.Ingredient.objects.create(
    #         user=user,
    #         name='Ingredient1'
    #     )

    #     self.assertEqual(str(ingredient), ingredient.name)

    # @patch('core.models.uuid.uuid4')
    # def test_recipe_file_name_uuid(self, mock_uuid):
    #     """Image yolunu oluşturmayı test edin."""
    #     uuid = 'test-uuid'
    #     mock_uuid.return_value = uuid
    #     file_path = models.recipe_image_file_path(None, 'example.jpg')

    #     self.assertEqual(file_path, f'uploads/recipe/{uuid}.jpg')
