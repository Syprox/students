# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf import settings
from django.shortcuts import render


# Create your views here.
def home(request):
    
    title = 'Welcome!'
    if request.user.is_authenticated():
        title = 'Welcome %s' %(request.user)
    
    context = {
               "title":title,
               }
    
    return render(request, "/studentsdb/templates/groups.html",context)