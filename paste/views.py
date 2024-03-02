from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseRedirect, FileResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from curlpaste.settings import MEDIA_ROOT
from hashlib import md5
import os.path
from .utils import interpret
from .models import File, Limit, Username
from django.shortcuts import render


@csrf_exempt
def root(request, idf=None, username=None):
    if request.method == 'POST':
        return HttpResponse(f'{interpret(request)}')
    elif request.method == 'GET':
        if idf:
            try: # To find the file or username
                idf = int(idf)
                fli = File.objects.get(pk=idf).file.path
                if fli:
                    return HttpResponseRedirect(f'/file/{os.path.basename(fli)}')
                    # fli = open(fli, 'rb')
                    # return FileResponse(fli, filename=str(fli))
            except:
                return HttpResponseNotFound('404') #TODO: replace this with html
        elif username:
            files = []
            for user in Username.objects.filter(name=username):
                files.append(f'{request.get_host()}/file/{user.file}\r\n')
            return HttpResponse(files)
        return render(request, 'index.html') #TODO: replace this with html and render


def file_serv(request, path):
    if request.method == 'GET':
        fli = File.objects.get(file=path)
        fli.visited += 1
        fli.save()
        print(fli.visited)
        return FileResponse(fli.file)
