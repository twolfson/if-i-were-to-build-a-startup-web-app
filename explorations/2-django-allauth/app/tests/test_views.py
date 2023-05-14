from django.test import Client, TestCase
from django.contrib.auth.models import User


class SignUpFormViewTestCase(TestCase):
    def test_submit_valid(self):
        """Submitting sign up with valid data, creates a user as expected"""
        client = Client()
        # DEV: It's tempting to load the page + fill in fields, but if this were an API, we wouldn't have that luxury
        #   It's okay to hardcode the fields here
        response = client.post(
            "/signup/",
            {
                "email": "hello@world.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "abcxyz123",
                "password2": "abcxyz123",
                # TODO: Test first and last name are required
            },
        )

        if response.status_code != 302:
            raise AssertionError(f"Encountered {response.status_code}, {response.context['form'].errors}")

        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()  # Get only user in DB (errors out if not 1)
        self.assertEqual(user.username, "hello@world.com")
        self.assertEqual(user.email, "hello@world.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")

    def test_submit_invalid(self):
        """Submitting sign up with invalid data, shows errors"""
        pass

    # TODO: Test case coercion
    # TODO: Enforce casing from Django Admin as well?
