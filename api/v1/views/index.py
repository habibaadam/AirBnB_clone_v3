#!/usr/bin/python3
"""Defines a Flask route"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    Returns a JSON response with the status OK
    """
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each object by type"""
    model_counts = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }

    return jsonify(model_counts)
