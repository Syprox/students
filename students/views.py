# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    
    title = 'Welcome!'
    if request.user.is_authenticated():
        title = 'Welcome %s' %(request.user)
    
    context = {
               "title":title,
               }
    
    return render(request, "/studentsdb/templates/groups.html",context)

#Views for Students

def students_list(request):
    return render(request, "students/students_list.html", {})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def groups_list(request):
    return render(request, "students/groups_list.html", {})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(reqest, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

# Views for journal

def journal(request):
    return render(request, "students/journal.html", {})

def journal_student(request, sid):
    return HttpResponse('<h1>Journal Student</h1>')

def journal_group(request, gid):
    return HttpResponse('<h1>Journal Group</h1>')

