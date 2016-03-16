"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'students.views.students_list', name='home'),
    
    #url(r'^home/$', 'studentsdb.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    
    # urls for students
    url(r'^students/$', 'students.views.students_list', name='students_list'),
    url(r'^students/add/$', 'students.views.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students_edit', name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students_delete', name='students_delete'),
    
    # urls for groups
    url(r'^groups/$', 'students.views.groups_list', name='groups_list'),
    url(r'^groups/add/$', 'students.views.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups_delete', name='groups_delete'),
    
    # urls for attendence
    url(r'^journal/$', 'students.views.journal', name='journal'),
    url(r'^journal/(?P<sid>\d+)/$', 'students.views.journal_student', name='journal_student'),
    url(r'^journal/(?P<gid>\d+)/$', 'students.views.journal_group', name='journal_group'),
]
