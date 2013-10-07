from django.contrib.auth.views import login
from django.contrib.messages import success, warning, error as message_error
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from amass.videos.models import Organization
from amass.common.forms import UserRegistrationForm
from amass.utils import LoggedInMixin

class Login(View):
    def get(self, request, *args, **kwargs):
        if 'register' in request.GET:
            form = UserRegistrationForm()
            return render(request, 'registration/register.html', {
                        'form': form,
                        'title': u'Register',
                   })
        return login(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'register' in request.POST:
            if 'registration_form' in request.POST:
                form = UserRegistrationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    success(request, "You have successfully registered, please log in.")
                    return HttpResponseRedirect("/")
                else:
                    message_error(request, "Please fix the errors below")
            else:
                form = UserRegistrationForm(initial={
                    'username': request.POST.get('username'),
                    'password1': request.POST.get('password'),
                    })
            return render(request, 'registration/register.html', {
                        'form': form,
                        'title': u'Register',
                })
        return login(request, template_name='index.html', *args, **kwargs)

class OrgListView(LoggedInMixin, ListView):
    model = Organization
    template_name = "videos/organization_list.html"
    context_object_name = 'organizations'

def OrgDetailView(DetailView):

    def get_queryset(self):
        org = get_object_or_404(Organization, name__iexact=self.args[0])
        return org

    def get_context_data(self, **kwargs):
        context = super(OrgDetailView, self).get_context_data(**kwargs)
        context['projects'] = self.org.project_set.all()
        return context

def OrgRegistration(request):

    if request.method == 'POST':
        form = OrgRegistrationForm(request.POST)
        if form.is_valid():
            org = Organization.objects.create(name=form.cleaned_data['name'], address=form.cleaned_data['address'], city=form.cleaned_data['city'] , zipcode=form.cleaned_data['zipcode'] , byline=form.cleaned_data['byline'], description=form.cleaned_data['description'])
            #I think this syntax should be right?
            request.user.organizationrep.organization = org
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
            
    else:
        #blank form
        form = UserRegistrationForm()
        return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
