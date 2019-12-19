"""Defines url patterns for learning_logs."""

from django.urls import path

from . import views

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload'),
    path('check/', views.check, name='check'),
    path('ok2check/', views.ok2check, name='ok2check'),
    path('downloadresult/', views.downloadresult, name='downloadresult'),
    
    # Show all topics.
    # url(r'^topics/$', views.topics, name='topics'),
    
    # # Detail page for a single topic.
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    
    # # Page for adding a new topic.
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    # # Page for adding a new entry.
    # url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    
    # # Page for editing an entry.
    # url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    #     name='edit_entry'),
]