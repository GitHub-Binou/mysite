from django.shortcuts import render, redirect, get_object_or_404
from quora.events.models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from quora.events.forms import EventForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def _events(request, events):
    paginator = Paginator(events, 10)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(
        request,
        'events/events.html',
        {'events': events}
    )


def events(request):
    all_events = Event.get_is_active()
    return _events(request, all_events)


def event(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, 'events/event.html', {'event': event})


@login_required
def write(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = Event()
            event.create_user = request.user
            event.title = form.cleaned_data.get('title')
            event.content = form.cleaned_data.get('content')
            event.save()
            return redirect('/events/')
    else:
        form = EventForm()
    return render(request, 'events/write.html', {'form': form})


@login_required
def edit(request, id):
    event = get_object_or_404(Event, pk=id)
    if request.POST:
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/events/')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit.html', {'form': form})