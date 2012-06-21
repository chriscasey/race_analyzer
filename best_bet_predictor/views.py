#IMPORTS
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import simplejson
from collections import defaultdict
from best_bet_predictor.models import *
from django.http import HttpResponse, QueryDict

def home(request):
    
    greeting = "hello world!"
    sub_greeting = "we're making $$$"
    
    return render_to_response('home.html',
                              {'greeting': greeting,
                              'sub_greeting': sub_greeting,
                              },
                              context_instance=RequestContext(request))