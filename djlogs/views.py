from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    """The home page for djlogs"""
    return render(request, 'djlogs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'djlogs/topics.html', context)

def topic(request, topic_id):
    """Show a specific topic and all related entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'djlogs/topic.html', context)