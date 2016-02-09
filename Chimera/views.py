from lib.appengine_gcs_client_master.python.src.cloudstorage import cloudstorage_api
from django.http import HttpResponse
from models import User, Post, UserLogin
from json import dumps, loads
from datetime import datetime


def user_model_from_id(request, user_id):
    if request.method == 'GET':
        if User.objects.filter(id=user_id).values().count() > 0:
            user = User.objects.filter(id=user_id).values()[0]
            return HttpResponse(dumps(user), content_type='application/json')
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(dumps(response), content_type='application/json')
    else:
        return HttpResponse(dumps({'result': 9002, 'message': 'This method is accessible only by GET'}))


def user_model_from_email(request, email):
    if request.method == 'GET':
        if User.objects.filter(email=email).values().count() > 0:
            user = User.objects.filter(email=email).values()[0]
            return HttpResponse(dumps(user), content_type='application/json')
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(dumps(response), content_type='application/json')
    else:
        return HttpResponse(dumps({'result': 9002, 'message': 'This method is accessible only by GET'}))


def post_model_from_id(request, post_id):
    if request.method == 'GET':
        if Post.objects.filter(id=post_id).values().count() > 0:
            post = Post.objects.filter(id=post_id).values()[0]
            return HttpResponse(dumps(post), content_type='application/json')
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(dumps(response), content_type='application/json')
    else:
        response = {'result': 9002, 'message': 'This method is accessible only by GET'}
        return HttpResponse(dumps(response), content_type='application/json')


def user_login_model_from_id(request, user_login_id):
    if request.method == 'GET':
        if UserLogin.objects.filter(id=user_login_id).values().count() > 0:
            user_login = UserLogin.objects.filter(id=user_login_id).values()[0]
            return HttpResponse(dumps(user_login), content_type='application/json')
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(dumps(response), content_type='application/json')
    else:
        response = {'result': 9002, 'message': 'This method is accessible only by GET'}
        return HttpResponse(dumps(response), content_type='application/json')


def user_login_model_from_user_id(request, user_id):
    if request.method == 'GET':
        if User.objects.filter(id=user_id).values().count() > 0:
            if UserLogin.objects.filter(user_id=user_id):
                user_login = UserLogin.objects.filter(user_id=user_id).values()[0]
                return HttpResponse(dumps(user_login), content_type='application/json')
            else:
                response = {'result': 2011, 'message': 'No user_login for this user_id'}
                return HttpResponse(dumps(response), content_type='application/json')
        else:
            response = {'result': 9000, 'message': 'Invalid parameter'}
            return HttpResponse(dumps(response), content_type='application/json')
    else:
        response = {'result': 9002, 'message': 'This method is accessible only by GET'}
        return HttpResponse(dumps(response), content_type='application/json')


def create_user_from_model(request):
    if request.method == 'POST':
        json_request = loads(request.body)
        temp_user = User(
            email=json_request.get('email'),
            join_date=datetime.utcnow(),
        )

        if User.objects.filter(email=json_request.get('email')).values().count() > 0:
            response = {'result': 2001, 'message': 'Email address already in use'}
            return HttpResponse(dumps(response), content_type='application/json')
        else:
            temp_user.save()

        user = User.objects.filter(email=json_request.get('email')).values()[0]

        temp_user_login = UserLogin(
            user_id=user.get('id'),
            username=user.get('email'),
            password=json_request.get('password'),
        )

        temp_user_login.save()

        user_login = UserLogin.objects.filter(user_id=user.get('id')).values()[0]

        response = {'user': user, 'user_login': user_login, 'result': 1000}
        return HttpResponse(dumps(response), content_type='application/json')
    else:
        response = {'result': 9001, 'message': 'This method is accessible only by POST'}
        return HttpResponse(dumps(response), content_type='application/json')
