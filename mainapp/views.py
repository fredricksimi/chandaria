from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .forms import CreatePreapprovedChallengeForm
# from taggit.models import Tag
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from .models import Challenges, ChallengeTag
from django.views.generic import ListView


"""This is a filter for Challenges with tags e.g Education, Science, Energy e.t.c"""
def tagged(request, id):
    tag = get_object_or_404(ChallengeTag, id=id)
    challenges = Challenges.objects.filter(tags=tag).order_by('-date_posted')
    context = {
        'tag':tag,
        'challenges':challenges
    }
    return render(request, 'mainapp/tagged-detail.html', context)



"""This displays *some* of the challenges in the system"""
def home(request):
    latest_challenges = Challenges.objects.all().filter(Q(status='Open') | Q(status='Rolling')).order_by('-date_posted').reverse()[:6]
    the_tags = ChallengeTag.objects.all()
    context = {
    'latest_challenges':latest_challenges,
    'the_tags':the_tags,
    "home_page": "active",

    'obcolor':'#51bb35',
    'ocolor':'#fff',

    'rbcolor':'#eb0678',
    'rcolor':'#fff'

    }
    return render(request, 'mainapp/index.html', context)

"""This displays all the latest challenges in the system"""
def challenges(request):
    the_posts = Challenges.objects.all()
    # common_tags = Challenges.tags.most_common()[:4]
    context = {
    'the_posts':the_posts,
    "challenge_page": "active",

    'obcolor':'#51bb35',
    'ocolor':'#fff',

    'abcolor':'#d61111',
    'acolor':'#fff',

    'pbcolor':'#f5cc04',
    'pcolor':'#000',

    'rbcolor':'#eb0678',
    'rcolor':'#fff'

    }
    return render(request, 'mainapp/challenges.html', context)

def open_challenges(request):
    challenges = Challenges.objects.all().filter(status='Open')
    context = {
        'challenges':challenges,
        'bcolor':'#51bb35',
        'color':'#fff'
        }
    return render(request, 'mainapp/open-challenges.html', context)

def in_progress_challenges(request):
    challenges = Challenges.objects.all().filter(status='In Progress')
    context = {
        'challenges':challenges,
        'bcolor':'#f5cc04',
        'color':'#000'
    }
    return render(request, 'mainapp/in-progress-challenges.html', context)

def archived_challenges(request):
    challenges = Challenges.objects.all().filter(status='Archived')
    context = {
        'challenges':challenges,
        'bcolor':'#d61111',
        'color':'#fff'
        }
    return render(request, 'mainapp/archived-challenges.html', context)

def rolling_challenges(request):
    challenges = Challenges.objects.all().filter(status='Rolling')
    context = {
        'challenges':challenges,
        'bbcolor':'#eb0678',
        'ccolor':'#fff'
    }
    return render(request, 'mainapp/rolling-challenges.html', context)


def about(request):
    return render(request, 'mainapp/about.html')


"""This displays the details of a selected Challenge"""
@login_required
def challenge_detail(request, id, slug):
    the_tags = ChallengeTag.objects.all()
    the_post = get_object_or_404(Challenges, id=id, slug=slug)
    context = {'the_post':the_post}
    return render(request, 'mainapp/detail.html', context)


class SearchResultsView(ListView):
    model = Challenges
    template_name = 'mainapp/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Challenges.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query) |
        Q(challenge_summary__icontains=query) | Q(offered_by__icontains=query) |
        Q(status__icontains=query) | Q(targeted_audience__name__icontains=query)
        )
        return object_list


@login_required
def submit_a_challenge(request):
    if request.method == 'POST':
        form = CreatePreapprovedChallengeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mainapp:homepage')
    else:
        form = CreatePreapprovedChallengeForm()
    context = {'form':form}
    return render(request, 'mainapp/submit-a-challenge.html', context)
