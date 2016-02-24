from Chimera.utils import model_to_dict
from django.http import HttpResponse
from Chimera.results import Result
from Chimera.models import Album
from datetime import datetime
from json import loads, dumps


def album_create(request, **kwargs):
    if (request and request.method == 'POST') or kwargs:
        if request and request.method == 'POST':
            body = loads(request.body)
        elif kwargs:
            body = kwargs
        else:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')

        album = Album(time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f"))

        if kwargs:
            return album

        response = {'album': model_to_dict(album)}
        Result.append_result(response, Result.SUCCESS)
        response = dumps(response)
        return HttpResponse(response, content_type='application/json')
