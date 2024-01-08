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
    """Retrieves the number of each objects by type."""
    stats_dict = {"Amenity": "amenities", "City": "cities",
                  "Place": "places", "Review": "reviews",
                  "State": "states", "User": "users"
                  }
    all_stats = {stats_dict[key]: storage.count(key) for key in stats_dict}
    return jsonify(all_stats)
