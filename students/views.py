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
    students=(
              {'id': 1,
               'first_name': u'Віталій',
               'last_name': u'Подоба',
               'ticket': 325,
               'image': 'img/me.jpg'},
              {'id': 2,
               'first_name': u'Андрій',
               'last_name': u'Корост',
               'ticket': 35,
               'image': 'img/piv.jpg'},
              {'id': 3,
               'first_name': u'Вадим',
               'last_name': u'Петренко',
               'ticket': 5,
               'image': 'img/podoba3.jpg'}
              )
    
    return render(request, "students/students_list.html", {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def groups_list(request):
    groups=(
            {'id': '1',
             'name': 'МтМ-21',
             'lider': 'Віталій Подоба'
             },
            {'id': '2',
             'name': 'МтМ-22',
             'lider': 'Корост Андрій'
             },
            {'id': '3',
             'name': '91ДПМ',
             'lider': 'Воронкіна Діана'
             },
            {'id': '4',
             'name': '91ДР',
             'lider': 'Лапіна Владислава'
             }
            )
    return render(request, "students/groups_list.html", {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(reqest, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

def groups_lider(request, gid):
    return HttpResponse('<h1>Edit Group %s Lider</h1>' % gid)

# Views for journal

def journal(request):
    return render(request, "students/journal.html", {})

def students_journal(request, sid):
    return HttpResponse('<h1>Journal Student %s</h1>' % sid)

def groups_journal(request, gid):
    return HttpResponse('<h1>Group %s Journal</h1>' % gid)

