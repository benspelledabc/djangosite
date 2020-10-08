# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q
from announcements.get_news import get_news, get_version_json, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
# "restart": get_restart_notice isn't really used yet
from django.views.generic import DetailView
from ipware import get_client_ip
from .models import Choice, Poll
from datetime import datetime
import logging

# logger = logging.getLogger(__name__)


def django_pdf(request):
    step_hit_count_by_page(request.path)
    return HttpResponse("Click <a href='/static/content/django.pdf'>here</a> to win!")


def django_pdf_duplicate(request):
    step_hit_count_by_page(request.path)
    return HttpResponse("Click <a href='/static/content/django.pdf'>here</a> to win!")


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        this_moment = datetime.now()
        recent_active_polls = Poll.objects.filter(
            (Q(end_date=this_moment.date()) | Q(end_date__gt=this_moment.date())) &
            (Q(start_date=this_moment.date()) | Q(start_date__lt=this_moment.date()))
        ).order_by('end_date')[:15]
        # ).order_by('-pk')[:15]
        return recent_active_polls

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # i'm not sure what this is for.. but there it is, gone.
        # context['poll_list'] = Poll.objects.all()[:5]
        context['release'] = get_version_json()
        # "copy_year": datetime.now().year
        context['copy_year'] = datetime.now().year
        context['remote_ip'] = self.get_ip_again()

        # logger.warning(f"Testing logger, should be in IndexView for polls...")
        # logger.info("Testing...")

        return context

    # this doesn't work right if behind a proxy (nginx)
    def visitor_ip_address(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def get_ip(self):
        ip, is_routable = get_client_ip(self.request)
        return_value = "1.1.1.1"
        if ip is None:
            # Unable to get the client's IP address
            return_value = "2.2.2.2"
        else:
            # We got the client's IP address
            if is_routable:
                # The client's IP address is publicly routable on the Internet
                return_value = "3.3.3.3"
            else:
                # The client's IP address is private
                return_value = "4.4.4.4"

        return return_value
        # Order of precedence is (Public, Private, Loopback, None)

    def get_ip_again(self):
        return_value = "0.0.0.0"
        request = self.request
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
            request.META['REMOTE_ADDR'] = ip
            return_value = ip
        return return_value


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # i'm not sure what this is for.. but there it is, gone.
        # context['poll_list'] = Poll.objects.all()[:5]
        context['release'] = get_version_json()
        context['copy_year'] = datetime.now().year
        return context


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # i'm not sure what this is for.. but there it is, gone.
        # context['poll_list'] = Poll.objects.all()[:5]
        context['release'] = get_version_json()
        context['copy_year'] = datetime.now().year

        # logger.warning(f"Testing logger, should be in ResultsView for polls...")
        # logger.info("Testing...")

        return context


def vote(request, poll_id):
    step_hit_count_by_page(request.path)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
            'copy_year': datetime.now().year,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

    # logger.warning(f"Testing logger, should be in vote for polls...")
    # logger.info("Testing...")
