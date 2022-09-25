import pytest


def success_response(client, path):
    rr = client.get(path)
