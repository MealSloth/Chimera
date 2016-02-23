def user_create(request):  # /user/create
    if request.method == 'POST':
        if not request.body:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')

        json_request = loads(request.body)

        if not json_request.get('email') and json_request.get('password'):
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')

        current_user = User(
            email=json_request.get('email'),
            join_date=datetime.utcnow(),
        )

        if User.objects.filter(email=current_user.email):
            response = Result.get_result_dump(Result.EMAIL_IN_USE)
            return HttpResponse(response, content_type='application/json')
        else:
            current_user.save()

        current_user_login = UserLogin(
            id=current_user.user_login_id,
            user_id=current_user.id,
            username=current_user.email,
            password=json_request.get('password'),
        )

        current_user_login.save()

        if not UserLogin.objects.filter(id=current_user_login.id):
            current_user.delete()
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        location = Location(
            id=current_user.location_id,
            user_id=current_user.id,
        )

        location.save()

        if not Location.objects.filter(id=location.id):
            current_user.delete()
            current_user_login.delete()
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        consumer = Consumer(
            id=current_user.consumer_id,
            user_id=current_user.id,
            location_id=location.id,
        )

        consumer.save()

        if not Consumer.objects.filter(id=consumer.id):
            current_user.delete()
            current_user_login.delete()
            location.delete()
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        chef = Chef(
            id=current_user.chef_id,
            user_id=current_user.id,
            location_id=location.id,
        )

        chef.save()

        if not Chef.objects.filter(id=chef.id):
            current_user.delete()
            current_user_login.delete()
            location.delete()
            consumer.delete()
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        billing = Billing(
            id=current_user.billing_id,
            user_id=current_user.id,
            consumer_id=consumer.id,
            chef_id=chef.id,
            location_id=location.id,
        )

        billing.save()

        if not Billing.objects.filter(id=billing.id):
            current_user.delete()
            current_user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        album = Album(time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f"))

        album.save()

        if not Album.objects.filter(id=album.id):
            current_user.delete()
            current_user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            billing.delete()
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        profile_photo = ProfilePhoto(
            id=current_user.profile_photo_id,
            album_id=album.id,
            user_id=current_user.id,
        )

        profile_photo.save()

        if not ProfilePhoto.objects.filter(id=profile_photo.id):
            current_user.delete()
            current_user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            billing.delete()
            album.delete()
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        current_user = User.objects.get(pk=current_user.id)
        current_user_login = UserLogin.objects.get(pk=current_user_login.id)

        if not current_user and current_user_login:
            response = Result.get_result_dump(Result.DATABASE_CANNOT_SAVE)
            return HttpResponse(response, content_type='application/json')

        current_user = User.objects.filter(id=current_user.id).values()[0]
        current_user_login = UserLogin.objects.filter(id=current_user_login.id).values()[0]

        response = {'user': current_user, 'user_login': current_user_login}
        Result.append_result(response, Result.SUCCESS)
        response = dumps(response)
        return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')