class Months:
    def __init__(self):
        pass

    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    Months = (
        (JANUARY, 'January'),
        (FEBRUARY, 'February'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December'),
    )


class Gender:
    def __init__(self):
        pass

    MALE = 0
    FEMALE = 1
    OTHER = 2

    Gender = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )


class PostStatus:
    def __init__(self):
        pass

    ACTIVE = 0
    SATURATED = 1
    INACTIVE = 2

    PostStatus = (
        (ACTIVE, 'Active'),
        (SATURATED, 'Saturated'),
        (INACTIVE, 'Inactive'),
    )


class OrderStatus:
    def __init__(self):
        pass

    PENDING = 0
    RECEIVED = 1
    PROGRESS = 2
    COMPLETED = 3
    SHIPPED = 4
    DELIVERED = 5
    DISPUTED = 6
    CANCELLED = 7

    OrderStatus = (
        (PENDING, 'Pending'),
        (RECEIVED, 'Received'),
        (PROGRESS, 'Progress'),
        (COMPLETED, 'Completed'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (DISPUTED, 'Disputed'),
        (CANCELLED, 'Cancelled'),
    )


class OrderType:
    def __init__(self):
        pass

    PICKUP = 0
    DELIVERY = 1
    DINEIN = 2

    OrderType = (
        (PICKUP, 'Pickup'),
        (DELIVERY, 'Delivery'),
        (DINEIN, 'DineIn'),
    )


class LocationPurpose:
    def __init__(self):
        pass

    BILLING = 0
    POST = 1
    DISPLAY = 2

    LocationPurpose = (
        (BILLING, 'Billing'),
        (POST, 'Post'),
        (DISPLAY, 'Display'),
    )


class LocationType:
    def __init__(self):
        pass

    RESIDENTIAL = 0
    COMMERCIAL = 1

    LocationType = (
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
    )
