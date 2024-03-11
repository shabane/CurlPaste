from .models import File, Limit, Username
from hashlib import md5
from curlpaste import settings
import random


def name_it(file) -> str:
    if settings.nemer == 'rand':
        chars = list("abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        name = ''
        for _ in range(settings.name_len):
            name += random.choice(chars)
        return name

    file_data = file.file.read()
    file_type = file.name.split('.')[-1]
    return md5(file_data).hexdigest() + f'.{file_type}'

def save(file, name: str, password: str, username: str = None, t_limit: int = settings.hours, v_limit: int = 0) -> str:
    print(t_limit)
    new_file = File(name=name, file=file, password=password if password else None)
    new_file.save()
    Limit(file=new_file, time=t_limit, view=v_limit).save()
    if username:
        Username(file=new_file, name=username).save()
    return new_file


def interpret(request):
    if request.FILES.dict().get('file'):
        file = request.FILES.get('file')
        name = name_it(file)
        request.FILES.get('file').name = name
        password = request.GET.get('password')
        return f"{request.get_host()}/file/{save(file, name, password)}/{f'?password={password}' if password else ''}"
    elif request.FILES.dict().get('once'):
        file = request.FILES.get('once')
        name = name_it(file)
        request.FILES.get('once').name = name
        password = request.GET.get('password')
        return f"{request.get_host()}/file/{save(file, name, password, v_limit=1)}/{f'?password={password}' if password else ''}"
    else:
        #TODO: split username and other interprets
        username = list(request.FILES.keys())[0]
        file = request.FILES.get(username)
        name = name_it(file)
        request.FILES.get(username).name = name
        save(file, name, request.GET.get('password'), username=username)
        return f"{request.get_host()}/{username}"
