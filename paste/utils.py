from .models import File, Limit, Username
from hashlib import md5


def name_it(file) -> str:
    file_data = file.file.read()
    file_type = file.name.split('.')[-1]
    return md5(file_data).hexdigest() + f'.{file_type}'

#TODO: make 24 dynamic
def save(file, name: str, password: str, username: str = None, t_limit: int = 24, v_limit: int = 0) -> str:
    if password:
        new_file = File(name=name, file=file, password=password)
        new_file.save()
        Limit(file=new_file, time=t_limit, view=v_limit).save()
        if username:
            Username(file=new_file, name=username).save()
        return new_file
    else:
        new_file = File(name=name, file=file)
        new_file.save()
        Limit(file=new_file, time=t_limit, view=v_limit).save()
        if username:
            Username(file=new_file, name=username).save()
        return new_file


def interpret(request):
    if request.FILES.dict().get('file'):
        file = request.FILES.get('file')
        name = name_it(file)
        return save(file, name, request.GET.get('password'))
    elif request.FILES.dict().get('once'):
        file = request.FILES.get('once')
        name = name_it(file)
        return save(file, name, request.GET.get('password'), v_limit=1)
    else:
        #TODO: split username and other interprets
        username = list(request.FILES.keys())[0]
        file = request.FILES.get(username)
        name = name_it(file)
        save(file, name, request.GET.get('password'), username=username)
        return username