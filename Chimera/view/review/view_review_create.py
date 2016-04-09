from Chimera.utils import model_to_dict
from django.http import HttpResponse
from Chimera.results import Result
from Chimera.models import Review
from json import dumps, loads


def review_create(request, **kwargs):
    if (request and request.method == 'POST') or kwargs:
        if request and request.method == 'POST':
            body = loads(request.body)
        elif kwargs:
            body = kwargs
        else:
            response = Result.get_result_dump(Result.POST_ONLY)
            return HttpResponse(response, content_type='application/json')

        post_id = body.get('post_id')
        consumer_id = body.get('consumer_id')
        rating = body.get('rating')
        title = body.get('title')
        description = body.get('description')

        if not (post_id and consumer_id and rating):
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')

        if type(rating) is not int or rating < 0 or rating > 10:
            response = Result.get_result_dump(Result.RATING_INVALID)
            return HttpResponse(response, content_type='application/json')

        review_create_kwargs = {
            'post_id': post_id,
            'consumer_id': consumer_id,
            'rating': rating,
        }

        if title:
            review_create_kwargs['title'] = title
        if description:
            review_create_kwargs['description'] = description

        try:
            review = Review(**review_create_kwargs)
        except StandardError:
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE_REVIEW)
            return HttpResponse(response, content_type='application/json')

        response = {'review': model_to_dict(review)}
        Result.append_result(response, Result.SUCCESS)
        response = dumps(response)
        return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')
