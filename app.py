import flask
from flask import Flask
from flask_cors import CORS

from models import Requests, SubscribeRequests, Reservations

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "<h1>MORFI - Mock Server</h1>" \
            "<p>Go to these URI's to use the mock server:</p>" \
            "<em>http://127.0.0.1:5000/api/v1/requestjoin</em>" \
            "<p><em>http://127.0.0.1:5000/api/v1/subscriberequest</em></p>" \
            "<p><em>http://localhost:5000/api/v1/reservations</em></p>" \
           "<h3>These HTTP methods are allowed: " \
            "<blockquote><code>GET</code></blockquote>" \
            "<blockquote><code>POST</code></blockquote>" \
            "<blockquote><code>PUT</code></blockquote>" \
            "<blockquote><code>DELETE</code></blockquote></h3>"


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
    is_get = flask.request.method == 'GET'

    if is_create:
        body = flask.request.json
        reservation_id_gen = generate_reservation_id()
        new_reservation = Reservations(
            reservation_id_gen,
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
                "day selected": body["day"],
                "time selected": body["time"],
                "restaurant selected": body["restaurant"],
                "full_name": body["full_name"],
                "phone_number": body["phone_number"],
                "quantity": body["quantity"]
            }
        )

    if is_get:
        return flask.jsonify(memory_reservation)


def generate_reservation_id():
    reservation_id.__add__(1)
    return str((len(memory_reservation) + 1)).rjust(8, "0")



if __name__ == '__main__':
    app.run(debug=True)
