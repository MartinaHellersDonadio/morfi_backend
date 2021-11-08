class Requests:
    def __init__(self, application_id, owner_name, email, restaurant_name, address, open_time, close_time, description):
        self.application_id = application_id
        self.owner_name = owner_name
        self.email = email
        self.restaurant_name = restaurant_name
        self.address = address
        self.open_time = open_time
        self.close_time = close_time
        self.description = description

    def to_json(self):
        return self.__dict__



class SubscribeRequests:
    def __init__(self, subscription_id, subscribe_email):
        self.subscription_id = subscription_id
        self.subscribe_email = subscribe_email

    def to_json(self):
        return self.__dict__


class Reservations:
    def __init__(self, reservation_id, day, time, restaurant, full_name, phone_number, quantity):
        self.reservation_id = reservation_id
        self.day = day
        self.time = time
        self.restaurant = restaurant
        self.full_name = full_name
        self.phone_number = phone_number
        self.quantity = quantity

    def to_json(self):
        return self.__dict__