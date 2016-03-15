# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def students_list(request):
    return render(request, "students/students_list.html",{})

def home(request):
    
    title = 'Welcome!'
    if request.user.is_authenticated():
        title = 'Welcome %s' %(request.user)
    
    context = {
               "title":title,
               }
    
    return render(request, "/studentsdb/templates/groups.html",context)

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')