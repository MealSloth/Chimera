def blob_delete(request):
    if request.method == 'POST':
        body = loads(request.body)
        blob_id = body.get('blob_id')
        if not blob_id:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
        else:
            data = {'blob_id': blob_id}
            data = dumps(data)
            return HttpResponse(
                urllib2.urlopen(PROTOCOL + 'blob.mealsloth.com/blob/delete/', data),
                content_type='application/json'
            )
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')