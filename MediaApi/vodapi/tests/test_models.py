from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test Creating new user with an email is successful"""
        email = 'vrushangprivatemail@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
