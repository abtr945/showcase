from django.shortcuts import render_to_response
from django.template import RequestContext

from app.project.models import Project

def home(request):
   projects = Project.objects.all()
   return render_to_response('main.html', {'projects': projects}, context_instance=RequestContext(request))
