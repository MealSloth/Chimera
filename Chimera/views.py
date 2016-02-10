from models import User, Post, UserLogin, Consumer, Chef, Location, Billing, Album, ProfilePhoto
from lib.appengine_gcs_client_master.python.src.cloudstorage import cloudstorage_api
from django.http import HttpResponse
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
        user = User(
            email=json_request.get('email'),
            join_date=datetime.utcnow(),
        )

        if User.objects.filter(email=user.email):
            response = {'result': 2001, 'message': 'Email address already in use'}
            return HttpResponse(dumps(response), content_type='application/json')
        else:
            user.save()

        user_login = UserLogin(
            id=user.user_login_id,
            user_id=user.id,
            username=user.email,
            password=json_request.get('password'),
        )

        user_login.save()

        if not UserLogin.objects.filter(user_login.id):
            user.delete()
            response = {'result': 9010, 'message': 'Could not save to database'}
            return HttpResponse(dumps(response), content_type='application/json')

        location = Location(
            id=user.location_id,
            user_id=user.id,
        )

        location.save()

        if not Location.objects.filter(id=location.id):
            user.delete()
            user_login.delete()
            response = {'result': 9010, 'message': 'Could not save to database'}
            return HttpResponse(dumps(response), content_type='application/json')

        consumer = Consumer(
            id=user.consumer_id,
            user_id=user.id,
            location_id=location.id,
        )

        consumer.save()

        if not Consumer.objects.filter(id=consumer.id):
            user.delete()
            user_login.delete()
            location.delete()
            response = {'result': 9010, 'message': 'Could not save to database'}
            return HttpResponse(dumps(response), content_type='application/json')

        chef = Chef(
            id=user.chef_id,
            user_id=user.id,
            location_id=location.id,
        )

        chef.save()

        if not Chef.objects.filter(id=chef.id):
            user.delete()
            user_login.delete()
            location.delete()
            consumer.delete()
            response = {'result': 9010, 'message': 'Could not save to database'}
            return HttpResponse(dumps(response), content_type='application/json')

        billing = Billing(
            id=user.billing_id,
            user_id=user.id,
            consumer_id=consumer.id,
            chef_id=chef.id,
            location_id=location.id,
        )

        billing.save()

        if not Billing.objects.filter(id=billing.id):
            user.delete()
            user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            response = {'result': 9010, 'message': 'Could not save to database'}
            return HttpResponse(dumps(response), content_type='application/json')

        album = Album()

        album.save()

        if not Album.objects.filter(id=album.id):
            user.delete()
            user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            billing.delete()
            response = {'result': 9010, 'message': 'Could not save to database'}
            return HttpResponse(dumps(response), content_type='application/json')

        profile_photo = ProfilePhoto(
            album_id=album.id,
            user_id=user.id,
        )

        profile_photo.save()

        if not ProfilePhoto.objects.filter(id=profile_photo.id):
            user.delete()
            user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            billing.delete()
            album.delete()
            response = {'result': 9010, 'message': 'Could not save to database'}
            return HttpResponse(dumps(response), content_type='application/json')

        response = {'user': user, 'user_login': user_login, 'result': 1000}
        return HttpResponse(dumps(response), content_type='application/json')
    else:
        response = {'result': 9001, 'message': 'This method is accessible only by POST'}
        return HttpResponse(dumps(response), content_type='application/json')
