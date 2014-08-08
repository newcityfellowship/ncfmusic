from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.views.generic.list_detail import object_list
from django.conf import settings
from django import http
from django.template import Context, loader

from ncfmusic.apps.content.models import *
from ncfmusic.apps.content.forms import *
from ncfmusic.apps.content.utils import *
from ncfmusic.apps.heroshots.models import *

from ncfmusic.lib.tiny_paypal import PayPal

import datetime, re, csv

def home(request):
    songs = Listen.objects.order_by('-insert_date')[:3]
    watch = Watch.objects.order_by('-insert_date')[0]
    learn = Article.objects.order_by('-insert_date')[:2]
    entries = BlogEntry.objects.order_by('-insert_date')[:3]
    
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
        'heroshots': heroshots,
        'entries': entries,
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
    
    return render_to_response('about.html', context)
    
def listen(request):
    return HttpResponsePermanentRedirect('/resources/')
    
def podcast(request):
    listens = Listen.objects.order_by('-insert_date')
    
    context = RequestContext(request, {
        'listens': listens
    })    
    
    return render_to_response('podcast.xml', context)
    
def watch(request, slug=None):
    page = get_object_or_404(Page, slug__exact='watch')
    watch_list = Watch.objects.order_by('-insert_date')
    
    if slug:
        watch = get_object_or_404(Watch, slug__exact=slug)
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
    
def tutorials(request, slug=None, tag=None):
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
        'learns': tutorials,
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'expanded': 'tutorials',
        'article_list': article_list,
        'tags': Tag.objects.filter(learn__isnull=False).distinct().order_by('name'),
        'tag': tag,
    })
    
    return render_to_response('learns.html', context)
    
def tutorial(request, slug):
    tutorial = get_object_or_404(Tutorial, slug__exact=slug)
    source_list, tutorial_list, talk_list, article_list = learn_sidebar()
    
    context = RequestContext(request, {
        'tutorial': tutorial,
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'expanded': 'tutorials',
        'article_list': article_list
    })
    return render_to_response('tutorial.html', context)

def talk(request, slug):
    talk = get_object_or_404(Talk, slug__exact=slug)
    source_list, tutorial_list, talk_list, article_list = learn_sidebar()

    context = RequestContext(request, {
        'talk': talk,
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'expanded': 'talks',
        'article_list': article_list
    })
    return render_to_response('talk.html', context)
    
def talks(request, tag=None):
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

    if tag:
        article_list = article_list.filter(tags__slug=tag)
        try:
            tag = Tag.objects.get(slug__exact=tag)
        except Tag.DoesNotExist:
            tag = None
        
    source_list, tutorial_list, talk_list, article_list = learn_sidebar()
        
    context = RequestContext(request, {
        'page': page,
        'learns': talks,
        'expanded': 'talks',
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'article_list': article_list,
        'tags': Tag.objects.filter(learn__isnull=False).distinct().order_by('name'),
        'tag': tag,
    })
    
    return render_to_response('learns.html', context)

def learn(request, tag=None):
    article_list = Learn.objects.filter(blogentry__isnull=True).order_by('-date')

    if tag:
        article_list = article_list.filter(tags__slug=tag)
        try:
            tag = Tag.objects.get(slug__exact=tag)
        except Tag.DoesNotExist:
            tag = None
    
    paginator = Paginator(article_list, 5)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        learns = paginator.page(page)
    except (EmptyPage, InvalidPage):
        learns = paginator.page(paginator.num_pages)
        
    source_list, tutorial_list, talk_list, thearticle_list = learn_sidebar()
    context = RequestContext(request, {
        'page': page,
        'learns': learns,
        'expanded': 'articles',
        'article_list': article_list[:10], #   For the sidebar
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'tags': Tag.objects.filter(learn__isnull=False).distinct().order_by('name'),
        'tag': tag,
    })
    return render_to_response('learns.html', context)
    
def articles(request, tag=None):
    article_list = Article.objects.order_by('-date')
    
    paginator = Paginator(article_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        articles = paginator.page(page)
    except (EmptyPage, InvalidPage):
        articles = paginator.page(paginator.num_pages)

    if tag:
        article_list = article_list.filter(tags__slug=tag)
        try:
            tag = Tag.objects.get(slug__exact=tag)
        except Tag.DoesNotExist:
            tag = None
        
    source_list, tutorial_list, talk_list, thearticle_list = learn_sidebar()
    context = RequestContext(request, {
        'page': page,
        'learns': articles,
        'expanded': 'articles',
        'article_list': article_list[:10], #   For the sidebar
        'tutorial_list': tutorial_list, 
        'talk_list': talk_list,
        'tags': Tag.objects.filter(learn__isnull=False).distinct().order_by('name'),
        'tag': tag,
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
    return HttpResponsePermanentRedirect('/resources/')

@cache_page(60 * 15)
def resources(request, start_letter=None, resource_type=None, genre=None, tag=None):
    page = get_object_or_404(Page, slug__exact='resources')

    q = request.GET.get('q', '').strip()
    song_list = Song.objects.all()

    if q:
        song_list = song_list.filter(Q(album_title__icontains=q) | Q(songwriter__name__icontains=q) | Q(title__icontains=q))
        if ('type' in request.GET) and request.GET['type'].strip():
            song_list = {
                'sheet_music': song_list.filter(Q(sheet_music__isnull=False) | Q(sheet_music='')),
                'lyrics': song_list.filter(Q(lyrics__isnull=False) | Q(lyrics='')),
                'slides': song_list.filter(Q(slides__isnull=False) | Q(slides='')),
            }[request.GET['type']]

    else:
        if resource_type:
            if resource_type == 'watch':
                song_list = song_list.filter(related_videos__isnull=False).distinct()
            elif resource_type == 'listen':
                song_list = song_list.filter(related_talks__isnull=False).distinct()
            elif resource_type == 'read':
                song_list = song_list.filter(related_articles__isnull=False).distinct()

        if genre:
            song_list = song_list.filter(genre__slug=genre)
            try:
                genre = Genre.objects.get(slug__exact=genre)
            except Genre.DoesNotExist:
                genre = None

        if tag:
            song_list = song_list.filter(tags__slug=tag)
            try:
                tag = Tag.objects.get(slug__exact=tag)
            except Tag.DoesNotExist:
                tag = None
    
    #   I'm sure there's a better way to do this, but it's late and my brain's tired, so this will work
    from django.utils.datastructures import SortedDict
    sections = SortedDict()
    for letter in map(chr, range(65, 91)):
        sections[letter] = song_list.filter(title__startswith=letter)
    
    if start_letter:
        song_list = sections[start_letter]

    #   Sort the song_list by effective date
    song_list = sorted(song_list, key=lambda s: s.effective_date, reverse=True)
            
    # paginator = Paginator(song_list, 4)
    # print 'paginated: %s' % datetime.datetime.now()

    # try:
    #     page = int(request.GET.get('page', '1'))
    # except ValueError:
    #     page = 1
       
    # print 'here: %s' % datetime.datetime.now() 
    # try:
    #     songs = paginator.page(page)
    # except (EmptyPage, InvalidPage):
    #     songs = paginator.page(paginator.num_pages)

    context = RequestContext(request, {
        'page': page,
        #'songs': songs,
        'songs': song_list,
        'sections': sections,
        'start_letter': start_letter,
        'genres': Genre.objects.order_by('name'),
        'tags': Tag.objects.filter(song__isnull=False).distinct().order_by('name'),
        'genre': genre,
        'tag': tag,
    })
    
    return render_to_response('songs.html', context)
    
# def events(request, month=None, year=None):
#     import datetime
#     
#     # page = get_object_or_404(Page, slug__exact='events')
#     
#     events_list = Event.objects.order_by('start_date')
#     
#     #   I'm sure there's a better way to do this, but it's late and my brain's tired, so this will work
#     months = {}
#     try:
#         first = events_list.order_by('start_date')[0]
#         last = events_list.order_by('-start_date')[0]
#     except IndexError:
#         first = datetime.date(2011, 1, 1)
#         last = datetime.date.today()
#     
#     
#     
#     try:
#       thisdate = datetime.date(first.start_date.year, first.start_date.month, 1)
#       named_month = lambda month_num:datetime.date(1900,month_num,1).strftime('%B')
#       while thisdate <= last.start_date:
#           months[named_month(thisdate.month) + ' '+ str(thisdate.year)] = events_list.filter(start_date__month=thisdate.month, start_date__year=thisdate.year)
#           if thisdate.month == 12:
#               thisdate = datetime.date(thisdate.year+1, 1, 1)
#           else:
#               thisdate = datetime.date(thisdate.year, thisdate.month+1, 1)
#     except (AttributeError):
#       events = []
#     
#     if month and year:
#         events_list = months[datetime.date(year,month,1)]
#         
#     paginator = Paginator(events_list, 4)
#     
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#         
#     try:
#         events = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         events = paginator.page(paginator.num_pages)
# 
#     print('Months:')
#     print(months)
#     
#     context = RequestContext(request, {
#         'page': page,
#         'events': events,
#         'months': months,
#         'month': month,
#         'year': year,
#     })
#     
#     return render_to_response('events.html', context)
    
def resource(request, slug):
    song = get_object_or_404(Song, slug__exact=slug)
    page = get_object_or_404(Page, slug__exact='resources')

    context = RequestContext(request, {
        'song': song,
        'page': page,
    })

    return render_to_response('song.html', context)

def events(request, month=None, year=None):
    events_list = Event.objects.filter(end_date__gte=datetime.datetime.now()).order_by('start_date')
    if year:
        events_list = events_list.filter(start_date__year=year)
    if month:
        events_list = events_list.filter(start_date__month=month)
    # page = get_object_or_404(Page, slug__exact='events')
    #event = get_object_or_404(Event, slug__exact=slug)
    
    context = RequestContext(request, {
        'event': len(events_list) and events_list[0] or {},
        'events': events_list
    })
    
    return render_to_response('event.html', context)

def event(request, slug):
    events_list = Event.objects.order_by('start_date')
    # page = get_object_or_404(Page, slug__exact='events')
    event = get_object_or_404(Event, slug__exact=slug)

    context = RequestContext(request, {
        'event': event,
        'events': events_list
    })

    return render_to_response('event.html', context)
    
def churches(request):
    churches = Church.objects.order_by('name')
    contribs = Contributor.objects.order_by('name')
    context = RequestContext(request, {
        'churches': churches,
        'contribs': contribs,
        'expanded' : 'churches'
    })
    
    return render_to_response('churches.html', context)
    
    
def church(request, slug):
    page = get_object_or_404(Page, slug__exact='contributors')
    church = get_object_or_404(Church, slug__exact=slug)
    
    context = RequestContext(request, {
        'page': page,
        'expanded' : 'churches',
        'church': church,
    })
    
    return render_to_response('church.html', context)    
    
def musicians(request, slug=None):
    page = get_object_or_404(Page, slug__exact='contributors')
    
    #   If we have musician slug we'll put them at the top of the list
    if slug:
        import itertools
        musician = get_object_or_404(Contributor, slug__exact=slug)
        musician_list = itertools.chain(Contributor.objects.filter(slug__exact=slug), Contributor.objects.exclude(slug__exact=slug).filter(listed_contributor=True).order_by('name'))
    else:
        musician_list = Contributor.objects.filter(listed_contributor=True).order_by('name')
    
    churches = Church.objects.order_by('name')
    
    context = RequestContext(request, {
        'page': page,
        'musician_list': musician_list,
        'churches': churches,
        'contribs': Contributor.objects.filter(listed_contributor=True).order_by('name'),
        'expanded' : 'musicians'
    })
    
    return render_to_response('musicians.html', context)
    
def search(request):
    #page = get_object_or_404(Page, slug__exact='search')
    
    query_string = request.GET.get('q', '').strip()
    if query_string:
        listen_query = get_query(query_string, ['title', 'album_title',])
        listens = Listen.objects.filter(listen_query).order_by('-record_date')

        watch_query = get_query(query_string, ['title', 'description', 'church__name',])
        watches = Watch.objects.filter(watch_query).order_by('-date')
        
        tutorial_query = get_query(query_string, ['title', 'teaser', 'author__name', 'church__name',])
        tutorials = Tutorial.objects.filter(tutorial_query).order_by('-insert_date')
        
        talk_query = get_query(query_string, ['title', 'teaser', 'author__name', 'church__name',])
        talks = Talk.objects.filter(talk_query).order_by('-date')
        
        article_query = get_query(query_string, ['title', 'teaser', 'article_body', 'author__name', 'church__name',])
        articles = Article.objects.filter(article_query).order_by('-date')
        
        song_query = get_query(query_string, ['title', 'album_title', 'songwriter__name',])
        songs = Song.objects.filter(song_query).order_by('-release_date')
        
        church_query = get_query(query_string, ['name', 'address', 'city', 'state', 'postal_code',])
        churches = Church.objects.filter(church_query).order_by('name')
        
        contributor_query = get_query(query_string, ['name', 'title',])
        contributors = Contributor.objects.filter(contributor_query).order_by('name')
        
        event_query = get_query(query_string, ['title', 'teaser', 'article_body',])
        events = Event.objects.filter(event_query).filter(end_date__gte=datetime.datetime.now()).order_by('title')

        blog_query = get_query(query_string, ['title', 'author__name', 'church__name', 'text',])
        blog_entries = BlogEntry.objects.filter(blog_query).order_by('-insert_date')
        
        context = RequestContext(request, {
            #'page': page,
            'listens': listens,
            'watches': watches,
            'tutorials': tutorials,
            'talks': talks,
            'articles': articles,
            'songs': songs,
            'churches': churches,
            'contributors': contributors,
            'events': events,
            'blogs': blog_entries,
        })

        return render_to_response('search.html', context)
    else:
        #   No query params, head back to the home page
        return HttpResponseRedirect('/')

def blog_category_list(request, slug):
    qs = BlogEntry.objects.filter(categories__slug=slug)

    paginator = Paginator(qs, 5)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    page_obj = paginator.page(page)

    return object_list(request, queryset=qs, extra_context={
        'content_page': Page.objects.get(slug='blog'),
        'categories': BlogCategory.objects.order_by('name'),
        'page_obj': page_obj,
        'category_slug': slug,
    })
    

def conference(request):
    page = get_object_or_404(Page, slug__exact='conference')

    context = RequestContext(request, {
            'page': page,
    })

    return render_to_response('conference.html', context)

def conference_registration(request):
    page = get_object_or_404(Page, slug__exact='conference')

    is_early = (datetime.date.today() < settings.CONFERENCE_EARLY_DEADLINE)

    registrant_errors = False
    registrants = []
    if request.method == 'POST':
        form = ConferenceRegistrationForm(request.POST)
        registrant_fields = ['first_name', 'last_name', 'email', 'gender', 'student']

        registrant_count = len(request.POST.getlist('registrant-first_name[]'))
        
        for i in range(registrant_count):
            registrant = {}
            for field in registrant_fields:
                val = request.POST.getlist('registrant-%s[]' % field)[i]
                registrant[field] = val
                if not val:
                    registrant_errors = True

            registrants.append(registrant)
        
        if form.is_valid() and not registrant_errors:
            reg = form.save(commit=False)

            #per = len(registrants) and settings.CONFERENCE_COSTS['group'] or settings.CONFERENCE_COSTS['single']
            total_cost = per = reg.get_leader_cost()


            #total_cost = (reg.student == 'Yes') and settings.CONFERENCE_COSTS['student'] or per

            #print 'per: %s' % total_cost

            purchase_details = {
                'L_PAYMENTREQUEST_0_NAME0': '2013 New City Music Conference Registration',
                'L_PAYMENTREQUEST_0_DESC0': '%s %s Registration' % (reg.first_name, reg.last_name),
                'L_PAYMENTREQUEST_0_AMT0': total_cost,
                'L_PAYMENTREQUEST_0': 1,
            }
            i = 1
            for registrant in registrants:
                reg_per = (registrant['student'] == 'Yes') and settings.CONFERENCE_COSTS['student'] or per
                total_cost += reg_per

                #print 'reg_per: %s' % reg_per

                purchase_details.update({
                    'L_PAYMENTREQUEST_0_NAME%d' % i: '2013 New City Music Conference Registration',
                    'L_PAYMENTREQUEST_0_DESC%d' % i: '%s %s Registration' % (registrant['first_name'], registrant['last_name']),
                    'L_PAYMENTREQUEST_0_AMT%d' % i: reg_per,
                    'L_PAYMENTREQUEST_0_QTY%d' % i: 1,
                })
                i += 1


            purchase_details.update({
                'PAYMENTREQUEST_0_ITEMAMT': total_cost,
                'PAYMENTREQUEST_0_AMT': total_cost,
                'PAYMENTREQUEST_0_DESC': '2013 New City Music Conference Registration'
            })

            paypal = PayPal()
            pp_token = paypal.SetExpressCheckout(total_cost, **purchase_details)
            reg.cost = total_cost
            reg.pp_token = pp_token
            reg.save()

            for registrant in registrants:
                reg_per = (registrant['student'] == 'Yes') and settings.CONFERENCE_COSTS['student'] or per

                r = ConferenceRegistrant(registration=reg, first_name=registrant['first_name'], last_name=registrant['last_name'], email=registrant['email'], gender=registrant['gender'], student=registrant['student'])
                r.save()

            express_token = paypal.GetExpressCheckoutDetails(pp_token)
            url = paypal.PAYPAL_URL + express_token
            return HttpResponseRedirect(url)
    else:
        form = ConferenceRegistrationForm()

    context = RequestContext(request, {
        'page': page,
        'form': form,
        'early': is_early,
        'settings': settings,
        'registrant_errors': registrant_errors,
        'registrants': registrants,
    })

    return render_to_response('conference_registration.html', context)
    
def paypal_return(request):
    page = get_object_or_404(Page, slug__exact='conference')

    token = request.GET.get('token', '')
    pp = PayPal()

    payer_id = request.GET.get('PayerID')
    paypal_details = pp.GetExpressCheckoutDetails(token, return_all=True)

    if request.method == 'POST':
        token = request.POST.get('token')
        payer_id = request.POST.get('payer_id')
        reg = ConferenceRegistration.objects.get(pp_token=token)
        amount = float(reg.cost)
        payment_details = pp.DoExpressCheckoutPayment(token=token, payer_id=payer_id, amt=amount)

        if 'Success' in payment_details['ACK']:
            reg.has_paid = True
            reg.payer_id = payer_id
            reg.save()

            return HttpResponseRedirect('/conference/registration/thanks/')
        else:
            raise Http404
    else:
        if 'Success' in paypal_details['ACK']:
            
            reg = ConferenceRegistration.objects.get(pp_token=token)
            amount = reg.cost
            token = paypal_details['TOKEN'][0]

            context = RequestContext(request, {
                'page': page,
                'amount': amount,
                'token': token,
                'payer_id': payer_id,
                'registration': reg,
            })

            return render_to_response('paypal_return.html', context)
        else:
            context = RequestContext(request, {
                'page': page,
                'paypal_details': paypal_details,
            })

            return render_to_response('paypal_error.html', context)

def conference_registration_thanks(request):
    page = get_object_or_404(Page, slug__exact='conference')

    context = RequestContext(request, {
        'page': page,
    })

    return render_to_response('conference_registration_thanks.html', context)

def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context:
        MEDIA_URL
            Path of static media (e.g. "media.example.org")
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return http.HttpResponseServerError(t.render(Context({
        'MEDIA_URL': settings.MEDIA_URL
    })))    


def standalone_page(request, slug):
    page = get_object_or_404(Page, slug__exact=slug, standalone=True)

    context = RequestContext(request, {
        'page': page,
    })

    return render_to_response('standalone_page.html', context)










def export_registrations(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=registrations.csv'
    writer = csv.writer(response)

    writer.writerow(['Registartion Date', 'First Name', 'Last Name', 'Email', 'Address', 'City', 'State', 'Postal Code', 'Country', 'Phone', 'Gender', 'Church Name', 'How are you serving these days', 'What are your musical skills', 'What are you most wanting to learn', 'Need housing', 'Special Housing Needs', 'Food Allergies', 'Ride from Airport', 'Flight Information', 'Are you a student', 'Cost', 'Has Paid'])

    for registration in ConferenceRegistration.objects.order_by('-insert_date'):
        row = [registration.insert_date, registration.first_name.encode('utf-8').strip(), registration.last_name.encode('utf-8').strip(), registration.email.encode('utf-8').strip(), registration.address.encode('utf-8').strip(), registration.city.encode('utf-8').strip(), registration.state.encode('utf-8').strip(), registration.postal_code, registration.country and registration.country.encode('utf-8').strip(), registration.phone_number, registration.gender, registration.church_name.encode('utf-8').strip(), registration.how_serving and registration.how_serving.encode('utf-8').strip(), registration.skills and registration.skills.encode('utf-8').strip(), registration.wanting_to_learn and registration.wanting_to_learn.encode('utf-8').strip(), registration.housing, registration.special_housing_needs and registration.special_housing_needs.encode('utf-8').strip(), registration.food_allergies and registration.food_allergies.encode('utf-8').strip(), registration.ride_from_airport, registration.flight_information and registration.flight_information.encode('utf-8').strip(), registration.student, registration.cost, registration.has_paid]
        writer.writerow(row)
        for registrant in ConferenceRegistrant.objects.filter(registration=registration):
            row = ['', registrant.first_name.encode('utf-8').strip(), registrant.last_name.encode('utf-8').strip(), registrant.email.encode('utf-8').strip(), '', '', '', '', '', '', registrant.gender, '', '', '' '', '', '', '', '', '', '', registrant.student,]
            writer.writerow(row)


    return response


def facebook_auth_post(request):
    print request.POST
    print request.GET

    return HttpResponse('Test')
