from django.test import Client, TestCase


class SignUpFormViewTestCase(TestCase):
    def test_submit_valid(self):
        """Submitting sign up with valid data, creates a user as expected"""
        client = Client()
        # DEV: It's tempting to load the page + fill in fields, but if this were an API, we wouldn't have that luxury
        #   It's okay to hardcode the fields here
        response = client.post("/signup/", {
            "email": "hello@world.com",
            "password1": "password",
            "password2": "password",
            # TODO: Test first and last name are required
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()  # Get only user in DB (errors out if not 1)
        # TODO: Fix this
        # self.assertEqual(user.username, "hello@world.com")
        self.assertEqual(user.email, "hello@world.com")

    def test_submit_invalid(self):
        """Submitting sign up with invalid data, shows errors"""
        pass

    # TODO: Test case coercion
    # TODO: Enforce casing from Django Admin as well?
