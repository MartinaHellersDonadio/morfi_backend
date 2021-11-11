import flask
from flask import Flask
from flask_cors import CORS

from models import Requests, SubscribeRequests, Reservations, Review

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "<h1>MORFI - Mock Server</h1>" \
            "<p>Go to these URI's to use the mock server:</p>" \
            "<em>http://127.0.0.1:5000/api/v1/requestjoin</em>" \
            "<p><em>http://127.0.0.1:5000/api/v1/subscriberequest</em></p>" \
            "<p><em>http://127.0.0.1:5000/api/v1/reservations</em></p>" \
           "<p><em>http://127.0.0.1:5000/api/v1/reviews</em></p>" \
           "<h3>These HTTP methods are allowed: " \
            "<blockquote><code>GET</code></blockquote>" \
            "<blockquote><code>POST</code></blockquote>"



memory_application = []
application_id = 0

@app.route('/api/v1/requestjoin', methods=["GET", "POST"])
def applications():
    is_create = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'

    if is_create:
        body = flask.request.json
        application_id_gen = generate_application_id()
        new_application = Requests(
            application_id_gen,
            body["owner_name"],
            body["email"],
            body["restaurant_name"],
            body["address"],
            body["open_time"],
            body["close_time"],
            body["description"],


        )
        memory_application.append(new_application.to_json())
        return flask.jsonify(
            {
                "owner_name": body["owner_name"],
                "email": body["email"],
                "restaurant_name": body["restaurant_name"],
                "address": body["address"],
                "open_time": body["open_time"],
                "close_time": body["close_time"],
                "description": body["description"],
                "application_id": application_id_gen
            }
        )

    if is_get:
        return flask.jsonify(memory_application)


def generate_application_id():
    application_id.__add__(1)
    return str((len(memory_application) + 1)).rjust(8, "0")



memory_subscription = []
subscription_id = 0

@app.route('/api/v1/subscriberequest', methods=["GET", "POST"])

def subscription():
    is_create = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'

    if is_create:
        body = flask.request.json
        subscription_id_gen = generate_subscription_id()
        new_subscription = SubscribeRequests(
            subscription_id_gen,
            body["subscribe_email"],

        )
        memory_subscription.append(new_subscription.to_json())
        return flask.jsonify(
            {
                "subscription_id": subscription_id_gen,
                "subscribe_email": body["subscribe_email"],

            }
        )

    if is_get:
        return flask.jsonify(memory_subscription)


def generate_subscription_id():
    subscription_id.__add__(1)
    return str((len(memory_subscription) + 1)).rjust(8, "0")


memory_reservation = []
reservation_id = 0

@app.route('/api/v1/reservations', methods=["GET", "POST"])

def reservation():
    is_create = flask.request.method == 'POST'
    is_fetch_all = flask.request.method == 'GET'

    if is_create:
        body = flask.request.json
        reservation_id_gen = generate_reservation_id()
        new_reservation = Reservations(
            reservation_id_gen,
            body["user_name"],
            body["day"],
            body["time"],
            body["restaurant"],
            body["full_name"],
            body["phone_number"],
            body["quantity"]

        )
        memory_reservation.append(new_reservation.to_json())
        return flask.jsonify(
            {
                "reservation_id": reservation_id_gen,
                "user_name": body["user_name"],
                "day selected": body["day"],
                "time selected": body["time"],
                "restaurant selected": body["restaurant"],
                "full_name": body["full_name"],
                "phone_number": body["phone_number"],
                "quantity": body["quantity"]
            }
        )

    if is_fetch_all:
        return flask.jsonify(memory_reservation)


def generate_reservation_id():
    reservation_id.__add__(1)
    return str((len(memory_reservation) + 1)).rjust(8, "0")

@app.route('/api/v1/reservations/<reservation_id>', methods=["GET", "PUT"])
def edit_reservation_id(reservation_id):
    is_edit = flask.request.method == "PUT"
    is_fetch = flask.request.method == "GET"

    if is_edit:
        body = flask.request.json
        for i in range(len(memory_reservation)):
            if memory_reservation[i]["reservation_id"] == reserv_id:
                update_reserv = memory_reservation[i]
                update_reserv["full_name"] = body["full_name"]
                update_reserv["day_selected"] = body["day_selected"]
                update_reserv["time_selected"] = body["time_selected"]
                update_reserv["restaurant_selected"] = body["restaurant_selected"]
                update_reserv["phone_number"] = body["phone_number"]
                update_reserv["quantity"] = body["quantity"]
                memory_reservation[i] = update_reserv
                return memory_reservation[i]

    if is_fetch:
        for reserv in memory_reservation:
            if reserv["reservation_id"] == reservation_id:
                return reserv


memory_reviews = []
review_id = 0
@app.route('/api/v1/reviews', methods=["POST"])

def review_manage ():
    is_create = flask.request.method == 'POST'

    if is_create:
        body = flask.request.json
        review_id_gen = generate_review_id()
        new_review = Review(
            review_id_gen,
            body["user_name"],
            body["date"],
            body["comment"],
            body["stars"],
            body["shop_id"],

        )
        memory_reviews.append(new_review.to_json())
        return flask.jsonify(
            {
                "review_id": review_id_gen,
                "user_name": body["user_name"],
                "date": body["date"],
                "comment": body["comment"],
                "stars": body["stars"],
            }
        )

def generate_review_id():
    review_id.__add__(1)
    return str((len(memory_reviews) + 1)).rjust(8, "0")


@app.route('/api/v1/reviews/<shop_id>', methods=["GET"])
def get_review(shop_id):
    is_fetch = flask.request.method == "GET"
    reviews_by_shop_id = []

    if is_fetch:
        for review in memory_reviews:
            if review["shop_id"] == shop_id:
                reviews_by_shop_id.append(review)
    return flask.jsonify(reviews_by_shop_id)




if __name__ == '__main__':
    app.run(debug=True)





