from Chimera.utils import model_to_dict
from django.http import HttpResponse
from Chimera.models import Consumer
from Chimera.results import Result
from json import dumps, loads


def consumer(request, **kwargs):  # /consumer
    if (request and request.method == 'POST') or kwargs:
        if request.method == 'POST':
            body = loads(request.body)
        elif kwargs:
            body = kwargs
        else:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')

        consumer = body.get('consumer_id')
        if not consumer:
            response = Result.get_result_dump(Result.get_result_dump(Result.INVALID_PARAMETER))
            return HttpResponse(response, content_type='application/json')

        try:
            current_consumer = Consumer.objects.get(pk=consumer)
        except Consumer.DoesNotExist:
            response = Result.get_result_dump(Result.DATABASE_ENTRY_NOT_FOUND)
            return HttpResponse(response, content_type='application/json')
        except Consumer.MultipleObjectsReturned:
            response = Result.get_result_dump(Result.DATABASE_MULTIPLE_ENTRIES)
            return HttpResponse(response, content_type='application/json')

        response = {'consumer': model_to_dict(current_consumer)}
        Result.append_result(response, Result.SUCCESS)
        response = dumps(response)
        return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')
