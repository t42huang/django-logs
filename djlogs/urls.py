"""Defines URL patterns for djlogs."""

from django.urls import path

from . import views

app_name = 'djlogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all topics
    path('topics/', views.topics, name='topics'),

    # Page to display for a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page to add a new topic in
    path('new_topic/', views.new_topic, name='new_topic'),

]