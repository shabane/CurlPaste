from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from curlpaste.settings import MEDIA_ROOT
from hashlib import md5
import os.path


@csrf_exempt
def root(request):
    if request.method == 'POST':
        file_data = request.FILES.get('file').file.read()
        file_type = request.FILES.get('file').name.split('.')[-1]
        file_name = os.path.join(md5(file_data).hexdigest()+f'.{file_type}')
        with open(os.path.join(MEDIA_ROOT, file_name), 'wb') as fli:
            fli.write(file_data)
        return HttpResponse('file saved')
    elif request.method == 'GET':
        return HttpResponse('by')
