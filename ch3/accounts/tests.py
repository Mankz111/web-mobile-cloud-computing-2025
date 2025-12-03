from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='cris',
            email='cris@gmail.com',
            password='123456'
        )
        self.assertEqual(user.username, 'cris')
        self.assertEqual(user.email, 'cris@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)



# Create your tests here.
