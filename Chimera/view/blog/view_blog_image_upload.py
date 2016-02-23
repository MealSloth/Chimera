def blog_image_upload(request):  # /blog/image/upload
    if request.method == 'POST':
        body = loads(request.body)
        image_file = body['file']
        data = dumps({'file': image_file, 'album_id': body['album_id']})
        try:
            re = urllib2.urlopen(PROTOCOL + 'blob.mealsloth.com/blog/image/upload/', data)
            return HttpResponse(re, content_type='application/json')
        except urllib2.HTTPError:
            response = Result.get_result_dump(Result.HYDRA_ERROR)
            return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')