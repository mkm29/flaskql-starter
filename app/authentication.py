import jwt
import os
from functools import wraps
from flask import request, abort
from app.exceptions import (
    InvalidHttpHeaderException,
    InvalidTokenException,
    EnvironmentVariableNotFoundException,
)
import requests


def skip_auth():
    return os.getenv("SKIP_AUTH", "False").upper() == "TRUE"


def get_encoded_token_from_header():

    auth_header = request.environ.get("HTTP_AUTHORIZATION")

    if not auth_header:
        raise InvalidHttpHeaderException("Authorization header missing from request.")

    # split the value ( first should be Bearer and second should be the token )
    values = auth_header.split()

    if len(values) != 2:
        raise InvalidHttpHeaderException(
            'Authorization header should be in format "Bearer <token>"'
        )

    return values[1]


def get_public_key_from_env():

    # public key
    value = os.getenv("SSO_PUBLIC_KEY")

    if not value:
        raise EnvironmentVariableNotFoundException(
            "No environment variable found for SSO_PUBLIC_KEY"
        )

    return value


def validate_encoded_token(encoded_token):

    public_key = get_public_key_from_env()
    try:
        decoded_token = jwt.decode(
            encoded_token, public_key, algorithms="RS256", audience="account"
        )
    except Exception as e:
        raise InvalidTokenException("token provided is invalid: " + str(e))

    return decoded_token


def verify_jwt_in_request(endpoint=None):

    # check if auth should be checked
    if skip_auth():
        log_request(endpoint=endpoint)
        return None
    # get token from request header
    encoded_token = get_encoded_token_from_header()

    # validate token
    decoded_token = validate_encoded_token(encoded_token)

    # todo: Need to check the expiration on the token

    # log request
    log_request(decoded_token, endpoint=endpoint)

    return decoded_token


def authenticate(endpoint):
    def decorator(function):
        def wrapper(*args, **kwargs):
            verify_jwt_in_request(endpoint)
            return function(*args, **kwargs)

        return wrapper

    return decorator
