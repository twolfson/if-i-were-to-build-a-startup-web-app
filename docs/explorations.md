# Explorations
Through the process of writing out this repository, we had times where we wanted to sanity check thoughts or possibly test various ideas.

This is a high level summary of what we explored and what we learned

## 1. django-contrib-auth-forms
Folder: [explorations/1-django-contrib-auth-forms](../explorations/1-django-contrib-auth-forms)

As mentioned in [Web Framework Analysis](web-framework.md), I believed that Django had strong out of the box auth support. I'm learning that's technically true, with a big asterisk.

The drawback is the Django auth content is largely configured for internal only users by default. And fighting against that is kind of sticky/annoying.

> Django is still ahead of others with a User model standard and permissions to use out of the gate. e.g. Rails still offers [Devise][] but it's an implied rather than explicit standard. [Passport (JS)][] is entirely handwaving over how users get defined/set up.

[Devise]: https://www.digitalocean.com/community/tutorials/how-to-set-up-user-authentication-with-devise-in-a-rails-7-application#step-4-creating-the-user-model-with-devise
[Passport (JS)]: https://www.passportjs.org/howtos/password/

<!-- TODO: Update web-framework to give more points to other repos due to best option prob being a third party library in all cases -->

To elaborate further:

- User creation is only done through CLI or Django Admin, no forms/views/URLs to extend for your app
    - User creation methods: https://docs.djangoproject.com/en/4.2/topics/auth/default/#creating-users
    - Enumerated provided forms/views: https://docs.djangoproject.com/en/4.2/topics/auth/default/#using-the-views
- The only articles I found for user creation extend the form that's only used by Django Admin's "Add User" page
    - Article: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
    - Django Admin usage: https://github.com/django/django/blob/4.2.1/django/contrib/auth/admin.py#L74
- So that's only user creation (aka sign up), and probably the worst offender
- But dealing with the other ones feels like you're fighting the system rather than using a framework
    - There's limited/no documentation for the field names for the forms, which isn't good for custom styling
        - e.g. Login interfaces with [`username` and `password`](https://github.com/django/django/blob/4.2.1/django/contrib/auth/forms.py#L205-L210) but that's not in the docs
        - https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView
        - https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
    - On logout, you're navigated to a Django Admin page (until you set `LOGOUT_REDIRECT_URL` in `settings.py`)
    - and the "Log in again" URL navigates to Django Admin, not the /login route set up

![Django default logout page](screenshots/explorations/1-django-contrib-auth-forms/default-logout-screen.png)

My theory on why this is the set up, is [Django is quite upfront about its history](https://www.djangoproject.com/start/overview/):

> Django was invented to meet fast-moving newsroom deadlines, while satisfying the tough requirements of experienced web developers.

With a newsroom model, I'd wager the data model is oriented around internal users, not self-serve sign up (guessing this was pre-paywall days).

Maybe someone else has further clarity though.

I did get sign up and login working though, so that was nice.

There was also circuitous learning around Django forms themselves for me (majority of past work has been [Django REST Framework](https://www.django-rest-framework.org/)) but I still don't have full resolution on the good and bad (especially on a trivial app).

# 2. django-allauth
Folder: [explorations/2-django-allauth](../explorations/2-django-allauth)

This went **a lot** smoother than the `django.contrib.auth` counterpart. It wasn't an instant setup still, but it had reasonable docs, discoverable code, and never felt like I was fighting it (though it did confuse me/feel unintuitive sometimes).

The good:
- Lots of functionality which I can opt-in to using for the most part
    - e.g. Can do just sign up + login, then add email verification, then add more
- Intuitive and legible code

The bad:
- Opinions are just different from mine around UX for a web app at times
    - `"mandatory"` email confirmation page does not identify user until verification is completed (so can't tell user the email to go check)
        - This is prob easily updated through a `views.py` override
    - The confirm email page doesn't show `messages` from what I can tell
- `urls`, `views`, and `templates` naming not consistent, so a lot of reading to find what `template` you need to update

Notable:
- When using `email` as login identifier and allowing `first_name` auth, `username` defaults to `first_name`
    - I've realized that this is a feature, not a bug though. On social platforms, people identify in URLs through `username`, which is distinct from `email`
- `@verified_email_required` does not redirect people to a different page, instead the prompt is just served from the same page

Recommendations:
- Copy all templates into your folder to start
    - Why: Overrides are inevitable for content changes, both in terms of styling as well as text (copy)
- Enumerate all form fields upfront in your own `forms.py`
    - Why: The docs don't state this, so it's a bit of digging to get them. I've found digging is a context switch though
- Enumerate all template <> views or URL mappings upfront (same reason as forms)
- Enumerate all URLs and selectively disable to get startup running ASAP
    - i.e. Prob don't need change password or email at the start, but sign up + login + verify email seem good to have
- Set up `Site` and `SocialApp` configurations via migrations, to easily cover all environments
- `ACCOUNT_EMAIL_VERIFICATION = "mandatory"` requires updating 5 pages (i.e. confirmation prompt + reset password flow)
    - Consider using `"optional"` with convention around `@verified_email_required` instead