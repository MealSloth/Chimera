from Chimera.settings import PROTOCOL, GCS_URL
from django.http import HttpResponse
from Chimera.results import Result
from Chimera.models import Blob
from json import dumps, loads


def blob(request):  # /blob/view
    if request.method == 'POST':
        body = loads(request.body)
        if not body.get('blob_id'):
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
        blob_id = body.get('blob_id')
        blob = Blob.objects.get(pk=blob_id)
        if not blob:
            response = Result.get_result_dump(Result.DATABASE_ENTRY_NOT_FOUND)
            return HttpResponse(response)
        response = {'url': PROTOCOL + GCS_URL + blob.gcs_id}
        Result.append_result(response, Result.SUCCESS)
        response = dumps(response)
        return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')
