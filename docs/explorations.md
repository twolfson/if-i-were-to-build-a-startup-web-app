# Explorations
Through the process of writing out this repository, we had times where we wanted to sanity check thoughts or possibly test various ideas.

This is a high level summary of what we explored and what we learned

## 1. django-contrib-auth-forms
Folder: [explorations/django-contrib-auth-forms](../explorations/django-contrib-auth-forms)

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
