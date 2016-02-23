def post(request):  # /post
    if request.method == 'POST':
        body = loads(request.body)
        try:
            post_id = body['post_id']
        except KeyError:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
        if Post.objects.filter(id=post_id).values().count() > 0:
            post = Post.objects.filter(id=post_id).values()[0]
            response = post
            Result.append_result(response, Result.SUCCESS)
            response = dumps(response)
            return HttpResponse(response, content_type='application/json')
        else:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')