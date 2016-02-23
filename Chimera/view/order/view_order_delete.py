from django.http import HttpResponse
from Chimera.results import Result
from Chimera.models import Order
from json import loads


def order_delete(request, **kwargs):
    if (request and request.method == 'POST') or kwargs:
        if request and request.method == 'POST':
            body = loads(request.body)
        elif kwargs:
            body = kwargs
        else:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')
        order_id = body.get('order_id')

        if not order_id:
            response = Result.get_result_dump(Result.INVALID_PARAMETER)
            return HttpResponse(response, content_type='application/json')

        order = Order.objects.filter(pk=order_id)
        if order.count() > 0:
            order = order[0]
        else:
            response = Result.get_result_dump(Result.DATABASE_ENTRY_NOT_FOUND)
            return  HttpResponse(response, content_type='application/json')

        try:
            order.delete()
        except StandardError:
            response = Result.get_result_dump(Result.DATABASE_CANNOT_DELETE_ORDER)
            return HttpResponse(response, content_type='application/json')

        response = Result.get_result_dump(Result.SUCCESS)
        return HttpResponse(response, content_type='application/json')
    else:
        response = Result.get_result_dump(Result.POST_ONLY)
        return HttpResponse(response, content_type='application/json')