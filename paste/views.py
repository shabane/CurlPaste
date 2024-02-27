from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseRedirect, FileResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from curlpaste.settings import MEDIA_ROOT
from hashlib import md5
import os.path
from .utils import interpret
from .models import File, Limit, Username


@csrf_exempt
def root(request, idf=None, username=None):
    if request.method == 'POST':
        print()
        interpret(request)
        return HttpResponse('file saved')
    elif request.method == 'GET':
        if idf:
            try: # To find the file or username
                idf = int(idf)
                fli = File.objects.get(pk=idf).file.path
                if fli:
                    fli = open(fli, 'rb')
                    return FileResponse(fli)
            except:
                return HttpResponseNotFound('404') #TODO: replace this with html
        elif username:
            files = []
            for user in Username.objects.filter(name=username):
                files.append(f'{request.get_host()}/{user.file.id}\r\n')
            return HttpResponse(files)
        return HttpResponse('wellcome') #TODO: replace this with html and render
