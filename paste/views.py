from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseRedirect, FileResponse
from django.views.decorators.csrf import csrf_exempt
from curlpaste.settings import MEDIA_ROOT
from hashlib import md5
import os.path
from .utils import interpret
from .models import File, Limit, Username


@csrf_exempt
def root(request, idf=None):
    if request.method == 'POST':
        print()
        interpret(request)
        return HttpResponse('file saved')
    elif request.method == 'GET':
        if idf:
            try:
                fli = File.objects.get(pk=idf).file.path
                if fli:
                    fli = open(fli, 'rb')
                    return FileResponse(fli)
            except:
                return HttpResponseNotFound('404') #TODO: replace this with html
        return HttpResponse('wellcome') #TODO: replace this with html and render
