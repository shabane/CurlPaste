from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def root(request):
    if request.method == 'POST':
        return HttpResponse('hi')
    elif request.method == 'GET':
        return HttpResponse('by')
