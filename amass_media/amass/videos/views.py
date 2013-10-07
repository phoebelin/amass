from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from amass.videos.models import Project, Organization
from amass.videos.forms import ProjectForm
from django.db.models import Q

import logging
log = logging.getLogger()

def home(request):
    context = RequestContext(request, {'title': 'Home'})
    return render_to_response('index.html', context)

#generic view of a user page showing all of his videos
class VideographerListView(ListView):

    model = Organization
    context_object_name = "videographer_list"
    template_name = ""

def ProjectListView(request):
    """
    log.info("start")
    #if the authenticated user is an orgrep, we will only list the org's own projects.
    if request.user.is_authenticated() and request.user.creator.all():
        projs = request.user.creator.all()
        log.info(request.user.is_authenticated())
        log.info(request.user.creator.all())
        log.info("edit")
        return render_to_response('project_list_for_org.html', {'projects':projs}, context_instance=RequestContext(request))

    #unauthenticated users and authenticated videographers will be show a default projects page with ability to search
    else:
    """

    orgrep = False
    if request.user.is_authenticated(): #and user orgrep field is true- to be implemented
        orgrep = True

    #replace 'search_name' with whatever we use in the template
    project_filter = 'project'
    budget_filter = 'budget'
    status_filter = 'search_name3'

    searched = False
    param = "criteria"
    #for param in search_params:
    if param in request.GET and request.GET[param]:
            value = request.GET[param]
            field = request.GET['search']
            if value == project_filter:
                #projs = Project.objects.get(Q(name__iexact = field))
                projs = get_list_or_404(Project, Q(name__iexact = field))       
            elif value == budget_filter:
                #projs = Project.objects.filter(budget__lte = field)
                projs = get_list_or_404(Project, budget__gte = field)
            elif value == status_filter:
                projs = Project.objects.filter(status = value)
            searched = True

    if searched == False:
        projs = Project.objects.order_by('-posted_date')[0:10]
    log.info("detail")
    log.info(projs[0].id)
    
    return render_to_response('project_list.html', {'projects':projs, 'orgrep':orgrep}, context_instance=RequestContext(request))

class ProjectList(ListView):
    model = Project
    context_object_name = "projects"

class ProjectDetail(DetailView):
    context_object_name = 'project'

    def get_queryset(self):
        log.info(Project.objects.filter(id__exact=self.kwargs['pk'])[0].creator.username)
        self.project = get_object_or_404(Project, id__exact=self.kwargs['pk'])
        return Project.objects.filter(id__exact=self.kwargs['pk'])
        #self.project = get_object_or_404(Project, id__exact=self.kwargs['pk'])
        #return self.project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        log.info(self.project.creator.username)
        context['username'] = self.project.creator.username
        if self.request.user == self.project.creator:
            context['orgrep'] = True
        else:
            context['orgrep'] = False
        return context

class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = '/projects'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        project = form.save(commit=False)
        project.creator = self.request.user
        project.status = Project.STATUS_PENDING
        project.save()
        return super(ProjectCreate, self).form_valid(form)

class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = '/projects'

def ProjectRegistration(request):

    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        if form.is_valid():    
            project = Project.objects.create(organization=request.user.organizationrep.organization, types=form.cleaned_data['types'], status=STATUS_PENDING, budget=form.cleaned_data['budget'], description=form.cleaned_data['description']) 
        else:
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

    else:
        #blank form
        form = UserRegistrationForm()
        return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
def UserRegistration(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')

    if request.method == 'POST':
        form = VideographerRegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.clean_data['username'], email=form.clean_data['email'], password=form.clean_data['password'])

            if form.cleaned_data['videographer_or_rep']:
                videographer = Videographer.objects.create(user=user)
            else:
                orgrep = OrganizationRep.objects.create(user=user)
            return HttpResponseRedirect('/profile/')

        else:
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

    else:
        #blank form
        form = UserRegistrationForm()
        return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

def Follow(request):
    log.info("mem")
    if request.user.is_authenticated():
        if request.POST["followBool"] == True:
            proj = Project.objects.get(id = request.POST["projectId"])
            request.user.userprofile.projectFollowing.add(proj)
            return HttpResponse()
        else:
            proj = Project.objects.get(id = request.POST["projectId"])
            request.user.userprofile.projectFollowing.remove(proj)
            return HttpResponse()
    else: #and user orgrep field is true- to be implemented
        log.info('no form yet')
        #form = UserRegistrationForm()
        #return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
