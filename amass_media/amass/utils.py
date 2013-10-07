from django.http import Http404

class LoggedInMixin(object):
    """ A mixin requiring a user to be logged in."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() :
            raise Http404
        return super(LoggedInMixin, self).dispatch(request, *args, **kwargs)
