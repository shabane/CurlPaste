from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from curlpaste.settings import MEDIA_ROOT
from hashlib import md5
import os.path
from .utils import interpret

@csrf_exempt
def root(request):
    if request.method == 'POST':
        print()
        interpret(request)
        return HttpResponse('file saved')
    elif request.method == 'GET':
        return HttpResponse('by')
