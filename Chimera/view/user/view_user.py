from django.http import HttpResponse
from Chimera.results import Result
from Chimera.models import User
from json import dumps, loads


def user(request):  # /user
    if request.method == 'POST':
        body = loads(request.body)
        email = body.get('email')
        user_id = body.get('user_id')
        if email:
            user = User.objects.filter(email=email).values()
            if user.count() > 0:
                response = {'user': user[0]}
                Result.append_result(response, Result.SUCCESS)
                response = dumps(response)
                return HttpResponse(response, content_type='application/json')
            else:
                response = Result.get_result_dump(Result.INVALID_PARAMETER)
                return HttpResponse(response, content_type='application/json')
        elif user_id:
            user = User.objects.filter(pk=user_id)
            if user.count() > 0:
                response = {'user': user[0]}
                Result.append_result(response, Result.SUCCESS)
                response = dumps(response)
                return HttpResponse(response, content_type='application/json')
        else:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')