def album_delete(request):  # /album/delete
    if request.method == 'POST':
        body = loads(request.body)
        album_id = body.get('album_id')
        if not album_id:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
        else:
            data = {'album_id': album_id}
            data = dumps(data)
            return HttpResponse(
                urllib2.urlopen(PROTOCOL + 'blob.mealsloth.com/album/delete/', data),
                content_type='application/json'
            )
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')