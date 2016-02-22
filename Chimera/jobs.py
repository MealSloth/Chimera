from enums import PostStatus, OrderStatus
from datetime import timedelta, datetime
from models import Post, Order


def job_post_status():
    post_list = Post.objects.all()
    for post in post_list:
        if datetime.utcnow() > datetime.strptime(post.expire_time, format="%Y-%m-%dT%H:%M:%S"):
            post.post_status = PostStatus.INACTIVE
            try:
                post.save()
            except StandardError, error:
                print(error)


def job_order_status():
    order_list = Order.objects.all()
    for order in order_list:
        order_time = datetime.strptime(order.order_time, format="%Y-%m-%dT%H:%M:%S.000000")
        if datetime.utcnow() - order_time > timedelta(days=1):
            order.order_status = OrderStatus.DELIVERED
            try:
                order.save()
            except StandardError, error:
                print(error)
