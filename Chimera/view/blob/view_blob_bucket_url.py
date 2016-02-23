def blob_bucket_url(request):  # /blob/bucket/url
    if request.method == 'POST':
        return HttpResponse(
            urllib2.urlopen(PROTOCOL + 'blob.mealsloth.com/bucket/url/'),
            content_type='application/json'
        )
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')