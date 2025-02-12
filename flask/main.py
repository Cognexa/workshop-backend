#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get", methods=["GET"])
def get_example():
    return jsonify(message="This is a GET response!")


@app.route("/post", methods=["POST"])
def post_example():
    data = request.json  # Get JSON data from the request
    return jsonify(message="POST data received", received_data=data)
