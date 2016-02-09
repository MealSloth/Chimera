from lib.appengine_gcs_client_master.python.src.cloudstorage import cloudstorage_api
from django.http import HttpResponse
from models import User, Post, UserLogin
from json import dumps, loads
from datetime import datetime


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


def create_user_from_model(request):
    if request.method == 'POST':
        json_request = loads(request.body)
        json_user = json_request.get('user')
        temp_user = User(
            email=json_user.get('email'),
            join_date=datetime.utcnow(),
        )

        if User.objects.filter(email=json_user.get('email')).values().count() > 0:
            return {'result': 9000}
        else:
            temp_user.save()

        user = User.objects.filter(email=json_user.get('email')).values()[0]

        temp_user_login = UserLogin(
            user_id=user.get('id'),
            username=user.get('email'),
            password=json_user.get('password'),
        )

        temp_user_login.save()

        user_login = UserLogin.objects.filter(user_id=user.get('id')).values()[0]

        return HttpResponse(dumps({'user': user, 'user_login': user_login, 'response': 1000}), content_type="application/json")
