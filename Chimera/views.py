from django.http import HttpResponse
from models import User, Post
from json import dumps


def user_model_from_id(request, user_id):
    if request.method == 'GET':
        if User.objects.filter(id=user_id).values().count() > 0:
            user = User.objects.filter(id=user_id).values()[0]
            return HttpResponse(dumps(user), content_type="application/json")
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(response)


def user_model_from_email(request, email):
    if request.method == 'GET':
        if User.objects.filter(email=email).values().count() > 0:
            user = User.objects.filter(email=email).values()[0]
            return HttpResponse(dumps(user), content_type="application/json")
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(response)


def post_model_from_id(request, post_id):
    if request.method == 'GET':
        if Post.objects.filter(id=post_id).values().count() > 0:
            post = Post.objects.filter(id=post_id).values()[0]
            return HttpResponse(dumps(post), content_type="application/json")
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(response)
