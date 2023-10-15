from django.test import Client, TestCase
from django.contrib.auth.models import User


class SignUpFormViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        del self.client

    def test_submit_valid(self):
        """Submitting sign up with valid data, creates a user as expected"""
        # DEV: It's tempting to load the page + fill in fields, but if this were an API, we wouldn't have that luxury
        #   It's okay to hardcode the fields here
        response = self.client.post(
            "/signup/",
            {
                "email": "hello@world.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "abcxyz123",
                "password2": "abcxyz123",
            },
        )

        if response.status_code != 302:
            raise AssertionError(f"Encountered {response.status_code}, {response.context['form'].errors}")

        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()  # Get only user in DB (errors out if not 1)
        # We're trusting django-allauth to select the `username`
        #   It's useful to allow it to be different from email for social purposes
        self.assertEqual(user.username, "test")  # This doubles as lowercase check
        self.assertEqual(user.email, "hello@world.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")

    def test_submit_invalid(self):
        """Submitting sign up with invalid data, shows errors"""
        response = self.client.post(
            "/signup/",
            {
                "password1": "password",
                "password2": "password",
            },
        )
        self.assertIn("This password is too common.", str(response.content))

    def test_submit_missing(self):
        """Submitting sign up with missing data, shows errors"""
        response = self.client.post(
            "/signup/",
            {},
        )

        self.assertFormError(response.context["form"], "first_name", "This field is required.")
        self.assertFormError(response.context["form"], "last_name", "This field is required.")
