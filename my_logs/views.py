from django.http.response import Http404
from django.shortcuts import render,redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'my_logs/index.html')


@login_required
def topics(request):
    """show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request , 'my_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    "显示单个主题及其所有的条目"
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
      raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'my_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题。"""
    if request.method != 'POST':
          # 未提交数据：创建一个新表单。
        form = TopicForm()
    else:
          # POST提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('my_logs:topics')

      # 显示空表单或指出表单数据无效。
    context = {'form': form}
    return render(request, 'my_logs/new_topic.html', context)

@login_required
def new_entry(request,topic_id):
    """在特定主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
      raise Http404
    if request.method != 'POST':
          # 未提交数据：创建一个新表单。
        form = EntryForm()
    else:
          # POST提交的数据：对数据进行处理。
        form = EntryForm(data=request.POST)
       
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('my_logs:topic',topic_id = topic_id)

      # 显示空表单或指出表单数据无效。
    context = {'topic':topic, 'form': form}
    return render(request, 'my_logs/new_entry.html', context)

@login_required
def edit_entry(request,entry_id):
    """在特定主题中添加新条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
          # 未提交数据：创建一个新表单。
        form = EntryForm(instance=entry)
    else:
          # POST提交的数据：对数据进行处理。
        form = EntryForm(instance=entry, data=request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('my_logs:topic',topic_id = topic.id)

      # 显示空表单或指出表单数据无效。
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'my_logs/edit_entry.html', context)