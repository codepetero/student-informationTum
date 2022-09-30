from django.test import TestCase
from django.urls import reverse

class TestViews (TestCase):

    def should_show_register_page(self):
        response=self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def should_show_login_page(self):
        response=self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def should_show_signup_user(self):
        self.user={
            "username":"username",
            "email":"email@gmail.com",
            "password":"password",
            "password2":"password2"
        }
        response=self.client.post(reverse("register", self.user))
        self.assertEquals(response.status_code, 302)

    def should_not_sigup_user_with_taken_username(self):
        self.user={
            "username":"username",
            "email":"email@gmail2.com",
            "password":"password",
            "password2":"password2"
        }
        self.client.post(reverse("register", self.user))
        response=self.client.post(reverse("register", self.user))
        self.assertEquals(response.status_code, 409)
        



