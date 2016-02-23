from Chimera.settings import PROTOCOL
from django.http import HttpResponse
from Chimera.results import Result
from json import dumps, loads
import urllib2


def blob_upload(request):  # /blob/upload
    if request.method == 'POST':
        body = loads(request.body)
        image_file = body.get('file')
        dictionary = {'file': image_file}
        if body.get('album_id'):
            dictionary['album_id'] = body.get('album_id')
        if body.get('url_suffix'):
            dictionary['url_suffix'] = body.get('url_suffix')
        data = dumps(dictionary)
        re = urllib2.urlopen(PROTOCOL + 'blob.mealsloth.com/blob/upload/', data)
        return HttpResponse(re)
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')
