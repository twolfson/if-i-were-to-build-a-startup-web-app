import time
from django.conf import settings
from django.utils.http import http_date

LOGGED_IN_COOKIE_NAME = "logged_in"
LOGGED_IN_ACTIVE_VALUE = "1"


# Allow to detect React app when logged in or not
#   https://docs.djangoproject.com/en/4.2/topics/http/middleware/
#   https://stackoverflow.com/a/20902690/1960509
# DEV: django-allauth signals don't support writing to response
#   This is prob for the best though, since Django Admin login is possible too
def logged_in_cookie_middleware(get_response):
    def middleware(request):
        # Let request run as per normal
        response = get_response(request)
        cookie_present = request.COOKIES.get(LOGGED_IN_COOKIE_NAME)
        user_is_authenticated = request.user.is_authenticated

        # On the path of the response, if we're still auth'd add a cookie
        # DEV: We might want to set cookie on every response, to keep the expiry fresh
        if user_is_authenticated and (settings.SESSION_SAVE_EVERY_REQUEST or not cookie_present):
            # Reuse content from sessions, https://github.com/django/django/blob/4.2.6/django/contrib/sessions/middleware.py#L48-L76  # noqa:E501
            if request.session.get_expire_at_browser_close():
                max_age = None
                expires = None
            else:
                max_age = request.session.get_expiry_age()
                expires_time = time.time() + max_age
                expires = http_date(expires_time)
            if response.status_code < 500:
                response.set_cookie(
                    LOGGED_IN_COOKIE_NAME,
                    LOGGED_IN_ACTIVE_VALUE,
                    max_age=max_age,
                    expires=expires,
                    domain=settings.SESSION_COOKIE_DOMAIN,
                    path=settings.SESSION_COOKIE_PATH,
                    secure=settings.SESSION_COOKIE_SECURE or None,
                    # Override so browser can read, but no session theft risk
                    httponly=False,
                    samesite=settings.SESSION_COOKIE_SAMESITE,
                )
        # Otherwise, remove the cookie
        elif not user_is_authenticated and cookie_present:
            response.delete_cookie(
                LOGGED_IN_COOKIE_NAME,
                # Reuse content from sessions, https://github.com/django/django/blob/4.2.6/django/contrib/sessions/middleware.py#L37-L42  # noqa:E501
                path=settings.SESSION_COOKIE_PATH,
                domain=settings.SESSION_COOKIE_DOMAIN,
                samesite=settings.SESSION_COOKIE_SAMESITE,
            )
        return response

    return middleware
