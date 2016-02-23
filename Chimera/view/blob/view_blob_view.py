from django.http import HttpResponse
from Chimera.results import Result
from Chimera.models import Blob
from json import dumps


def blob_view(request):  # /blob/view
    if request.method == 'POST':
        if not request.POST['blob_id']:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
        blob_id = request.POST['blob_id']
        blob = Blob.objects.get(pk=blob_id)
        if not blob:
            response = Result.get_result_dump(Result.DATABASE_ENTRY_NOT_FOUND)
            return HttpResponse(response)
        response = {'url': ''}  # TODO: Include a real URL
        Result.append_result(response, Result.SUCCESS)
        response = dumps(response)
        return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')
