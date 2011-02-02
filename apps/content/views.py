from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect

from ncfmusic.apps.content.models import *
from ncfmusic.apps.content.forms import *
from ncfmusic.apps.content.utils import *
from ncfmusic.apps.heroshots.models import *

def home(request):
    songs = Listen.objects.order_by('-insert_date')[:3]
    watch = Watch.objects.order_by('-insert_date')[0]
    learn = Learn.objects.order_by('-insert_date')[:2]
    
    heroshots = Category.objects.filter(slug='homepage')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
            
    else:
        form = ContactForm()
    
    context = RequestContext(request, {
        'songs': songs,
        'watch': watch,
        'learn': learn,
        'form': form,
        'heroshots': heroshots
    })
    
    return render_to_response('homepage.html', context)
    
def about(request):
    page = get_object_or_404(Page, slug__exact='about')
    #church = get_object_or_404(Church, name='New City Fellowship Glenwood')
    #   Maybe it would be easier to hard code this into the template? 
    # I agree. Pulled it out.
    #contact = get_object_or_404(Contact, church=church, first_name='James', last_name='Ward')
    
    context = RequestContext(request, {
        'page': page
    })
    
    return render_to_response('about.html', context);
    
def listen(request):
    contentpage = get_object_or_404(Page, slug__exact='listen')
    listen_list = Listen.objects.order_by('-insert_date')
    
    paginator = Paginator(listen_list, 5)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        listens = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listens = paginator.page(paginator.num_pages)
        
    context = RequestContext(request, {
        'contentpage': contentpage,
        'page': page,
        'listens': listens
    })
    
    return render_to_response('listen.html', context)
    
def watch(request, slug=None):
    page = get_object_or_404(Page, slug__exact='watch')
    watch_list = Watch.objects.order_by('-insert_date')
    
    if slug:
        watch = get_object_or_404(Watch, slug__exect=slug)
    else:
        watch = watch_list[0];
    
    paginator = Paginator(watch_list, 5)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        watches = paginator.page(page)
    except (EmptyPage, InvalidPage):
        watches = paginator.page(paginator.num_pages)
        
    context = RequestContext(request, {
        'page': page,
        'watches': watches,
        'watch': watch
    })
    
    return render_to_response('watch.html', context)
    
def learn_sidebar():
    source_list = Church.objects.order_by('name')
    tutorial_list = Tutorial.objects.order_by('-date')[:5]
    talk_list = Talk.objects.order_by('-date')[:5]
    article_list = Article.objects.order_by('-date')[:5]
    
    return source_list, tutorial_list, talk_list, article_list
        
def sources(request, slug=None):
    page = get_object_or_404(Page, slug__exact='learn')
    
    learn_list = Learn.objects.order_by('-date')
    
    if (slug):
        learn_list = learn_list.filter(church__slug__exact=slug)

    paginator = Paginator(learn_list, 3)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        learns = paginator.page(page)
    except (EmptyPage, InvalidPage):
        learns = paginator.page(paginator.num_pages)

    source_list, tutorial_list, talk_list, article_list = learn_sidebar()

    context = RequestContext(request, {
        'page': page,
        'learns': learns,
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'article_list': article_list,
    })
    
    return render_to_response('learns.html', context)
    
def tutorials(request, slug=None):
    page = get_object_or_404(Page, slug__exact='learn')
    
    if slug:
        tutorial_list = Tutorial.objects.filter(church__slug=slug).order_by('-date')
    else:
        tutorial_list = Tutorial.objects.order_by('-date')
    
    paginator = Paginator(tutorial_list, 3)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        tutorials = paginator.page(page)
    except (EmptyPage, InvalidPage):
        tutorials = paginator.page(paginator.num_pages)
        
    source_list, tutorial_list, talk_list, article_list = learn_sidebar()
        
    context = RequestContext(request, {
        'page': page,
        'tutorials': tutorials,
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'expanded': 'tutorials',
        'article_list': article_list,
    })
    
    return render_to_response('tutorials.html', context)
    
def tutorial(request, slug):
    tutorial = get_object_or_404(Tutorial, slug__exact=slug)
    context = RequestContext(request, {
        'tutorial': tutorial,
    })
    return render_to_response('tutorial.html', context)
    
def talks(request):
    talk_list = Talk.objects.order_by('-insert_date')
    paginator = Paginator(talk_list, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        talks = paginator.page(page)
    except (EmptyPage, InvalidPage):
        talks = paginator.page(paginator.num_pages)
        
    source_list, tutorial_list, talk_list, article_list = learn_sidebar()
        
    context = RequestContext(request, {
        'page': page,
        'talks': talks,
        'expanded': 'talks',
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'article_list': article_list,
    })
    
    return render_to_response('talks.html', context)
    
def articles(request):
    article_list = Article.objects.order_by('-insert_date')
    
    paginator = Paginator(article_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        articles = paginator.page(page)
    except (EmptyPage, InvalidPage):
        articles = paginator.page(paginator.num_pages)
        
    source_list, tutorial_list, talk_list, thearticle_list = learn_sidebar()
    context = RequestContext(request, {
        'page': page,
        'learns': articles,
        'expanded': 'articles',
        'article_list': article_list[:5], #   For the sidebar
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list
    })
    return render_to_response('learns.html', context)
    
def article(request, slug):
    article = get_object_or_404(Article, slug__exact=slug)
    article_list = Article.objects.order_by('-insert_date')
    context = RequestContext(request, {
        'article': article,
        'expanded': 'articles',
        'article_list': article_list[:5], #   For the sidebar
    })
    return render_to_response('article.html', context)
    
def songs(request, start_letter=None):
    page = get_object_or_404(Page, slug__exact='songs')
    
    song_list = Song.objects.order_by('title')
    
    if ('q' in request.GET) and request.GET['q'].strip():
        if ('type' in request.GET) and request.GET['type'].strip():
            song_list = {
                'sheet_music': song_list.filter(sheet_music__isnull=False),
                'lyrics': song_list.filter(lyrics__isnull=False),
                'slides': song_list.filter(slides__isnull=False),
            }[request.GET['type']]

    
    #   I'm sure there's a better way to do this, but it's late and my brain's tired, so this will work
    sections = {}
    for letter in map(chr, range(65, 91)):
        sections[letter] = song_list.filter(title__startswith=letter)
    
    if start_letter:
        song_list = sections[start_letter]
        
    
        
        
    paginator = Paginator(song_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        songs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        songs = paginator.page(paginator.num_pages)

    context = RequestContext(request, {
        'page': page,
        'songs': songs,
        'sections': sections,
        'start_letter': start_letter
    })
    
    return render_to_response('songs.html', context)
    
def events(request, month=None, year=None):
    import datetime
    
    page = get_object_or_404(Page, slug__exact='events')
    
    events_list = Event.objects.order_by('start_date')
    
    #   I'm sure there's a better way to do this, but it's late and my brain's tired, so this will work
    months = {}
    first = events_list.order_by('start_date')[0]
    last = events_list.order_by('-start_date')[0]
    
    thisdate = datetime.date(first.year, first.month, 1)
    while thisdate <= last:
        months[thisdate] = events_list.filter(start_date__month=thisdate.month, start_date__year=thisdate.year)
        if thisdate.month == 12:
            thisdate = datetime.date(thisdate.year+1, 1, 1)
        else:
            thisdate = datetime.date(thisdate.year, thisdate.month+1, 1)
    
    if month and year:
        events_list = months[datetime.date(year,month,1)]
        
    paginator = Paginator(events_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        events = paginator.page(page)
    except (EmptyPage, InvalidPage):
        events = paginator.page(paginator.num_pages)

    context = RequestContext(request, {
        'page': page,
        'events': events,
        'months': months,
        'month': month,
        'year': year,
    })
    
    return render_to_response('events.html', context)
    
def event(request, slug):
    page = get_object_or_404(Page, slug__exact='events')
    event = get_object_or_404(Event, slug__exact=slug)
    
    context = RequestContext(request, {
        'page': page,
        'event': event,
    })
    
    return render_to_response('event.html', context)
    
def churches(request):
    page = get_object_or_404(Page, slug__exact='contributors')
    
    church_list = Church.objects.order_by('name')
    
    context = RequestContext(request, {
        'page': page,
        'church_list': church_list,
    })
    
    return render_to_response('churches.html', context)
    
    
def church(request, slug):
    page = get_object_or_404(Page, slug__exact='contributors')
    church = get_object_or_404(Church, slug__exact=slug)
    
    context = RequestContext(request, {
        'page': page,
        'church': church,
    })
    
    return render_to_response('church.html', context)    
    
def musicians(request, slug=None):
    page = get_object_or_404(Page, slug__exact='contributors')
    
    #   If we have musician slug we'll put them at the top of the list
    if slug:
        musician_list = get_object_or_404(Contributor, slug__exact=slug)
        musician_list = musician_list | Contributors.objects.exclude(slug__exact=slug).order_by('name')
    else:
        musician_list = Contributors.objects.order_by('name')
    
    context = RequestContext(request, {
        'page': page,
        'musician_list': musician_list,
    })
    
    return render_to_response('musicians.html', context)
    
def search(request):
    page = get_object_or_404(Page, slug__exact='search')
    
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        listen_query = get_query(query_string, ['title', 'album_title',])
        listen = Listen.objects.filter(listen_query).order_by('-release_date')

        watch_query = get_query(query_string, ['title', 'description', 'church',])
        watch = Watch.objects.filter(watch_query).order_by('-date')
        
        tutorial_query = get_query(query_string, ['title', 'teaser',])
        tutorial = Tutorial.objects.filter(tutorial_query).order_by('-insert_date')
        
        talk_query = get_query(query_string, ['title', 'teaser',])
        talk = Talk.objects.filter(talk_query).order_by('-date')
        
        article_query = get_query(query_string, ['title', 'teaser', 'article_body',])
        article = Article.objects.filter(article_query).order_by('-date')
        
        song_query = get_query(query_string, ['title',])
        song = Song.objects.filter(song_query).order_by('-release_date')
        
        church_query = get_query(query_string, ['name', 'address', 'city', 'state', 'postal_code',])
        church = Church.objects.filter(church_query).order_by('name')
        
        contributor_query = get_query(query_string, ['name', 'title',])
        contributor = Contributor.objects.filter(contributor_query).order_by('name')
        
        event_query = get_query(query_string, ['title', 'teaser', 'article_body',])
        event = Event.objects.filter(event_query).order_by('title')
        
        context = RequestContext(request, {
            'page': page,
            'listen': listen,
            'watch': watch,
            'tutorial': tutorial,
            'talk': talk,
            'article': article,
            'song': song,
            'church': church,
            'contributor': contributor,
            'event': event,
        })

        return render_to_response('search.html', context)
    else:
        #   No query params, head back to the home page
        return HttpResponseRedirect('/')
    