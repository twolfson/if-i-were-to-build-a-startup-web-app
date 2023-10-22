# Allow to detect React app when logged in or not
#   https://docs.djangoproject.com/en/4.2/topics/http/middleware/
#   https://stackoverflow.com/a/20902690/1960509
# DEV: django-allauth signals don't support writing to response
#   This is prob for the best though, since Django Admin login is possible too
def logged_in_cookie_middleware(get_response):
    def middleware(request):
        # Let request run as per normal
        response = get_response(request)

        # On the path of the response, if we're still auth'd add a cookie
        # DEV: We might want to set cookie on every response, to keep the expiry fresh
        print(request.COOKIES.get("sessionid"))
        if request.user.is_authenticated() and not request.COOKIES.get('logged_in'):
            response.set_cookie("logged_in", "1")
        # Otherwise, remove the cookie
        elif not request.user.is_authenticated() and request.COOKIES.get('logged_in'):
            response.delete_cookie("logged_in")
        return response
    return middleware
