# test_users_endpoint.py
"""Offline integration‑style tests for /users/ using **pytest‑mock**.

The tests patch ``requests.get`` so no running server is necessary.

Credential matrix we simulate:
  • (admin, admin)   → HTTP 401 + empty body
  • (admin, qwerty) → HTTP 200 + empty body

Dependencies:
    pip install pytest requests pytest-mock
"""

import requests
from requests.models import Response

BASE_URL = "http://127.0.0.1:8000/users/"


def _make_response(status_code: int, text: str = "") -> Response:
    """Utility to craft a ``requests.Response`` with minimal fields set."""
    resp = Response()
    resp.status_code = status_code
    resp._content = text.encode()  # ``Response.text`` derives from this
    return resp


def test_authentication_failed(mocker):
    """Expect 401 and empty body when password is *admin*."""
    params = {"username": "admin", "password": "admin"}

    # Patch ``requests.get`` for this test only
    mocker.patch("requests.get", return_value=_make_response(401))

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401, (
        f"Expected 401, got {response.status_code}"
    )
    assert response.text.strip() == "", "Expected empty response body"


def test_authentication_success(mocker):
    """Expect 200 and empty body when password is *qwerty*."""
    params = {"username": "admin", "password": "qwerty"}

    mocker.patch("requests.get", return_value=_make_response(200))

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200, (
        f"Expected 200, got {response.status_code}"
    )
    assert response.text.strip() == "", "Expected empty response body"
