from Chimera.settings import PROTOCOL, GCS_URL
from django.http import HttpResponse
from Chimera.results import Result
from Chimera.models import Blob
from json import dumps, loads


def blob(request):  # /blob/view
    if request.method == 'POST':
        body = loads(request.body)

        blob_id = body.get('blob_id')
        album_id = body.get('album_id')

        if not (blob_id or album_id):
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')

        if blob_id:
            try:
                current_blob = Blob.objects.get(pk=blob_id)
            except Blob.DoesNotExist:
                response = Result.get_result_dump(Result.DATABASE_ENTRY_NOT_FOUND)
                return HttpResponse(response, content_type='application/json')
            except Blob.MultipleObjectsReturned:
                response = Result.get_result_dump(Result.DATABASE_MULTIPLE_ENTRIES)
                return HttpResponse(response, content_type='application/json')
            response = {'url': PROTOCOL + GCS_URL + current_blob.gcs_id}
        else:
            try:
                current_blob = Blob.objects.filter(album_id=album_id).values()
            except Blob.DoesNotExist:
                response = Result.get_result_dump(Result.DATABASE_ENTRY_NOT_FOUND)
                return HttpResponse(response, content_type='application/json')
            if current_blob.count() < 1:
                response = Result.get_result_dump(Result.DATABASE_ENTRY_NOT_FOUND)
                return HttpResponse(response, content_type='application/json')
            blob_list = []
            for blob_entry in current_blob:
                blob_list.append(PROTOCOL + GCS_URL + blob_entry.get('gcs_id'))
            response = {'blobs': blob_list}

        Result.append_result(response, Result.SUCCESS)
        response = dumps(response)
        return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')
