import azure.functions as func
from function_app import http_trigger


def test_http_trigger_with_query_param():
    req = func.HttpRequest(
        method="GET",
        url="/api/http_trigger",
        params={"name": "John"},
        body=None
    )

    resp = http_trigger(req)

    assert resp.status_code == 200
    assert b"Hello, John" in resp.get_body()


def test_http_trigger_with_body():
    req = func.HttpRequest(
        method="POST",
        url="/api/http_trigger",
        params={},
        body=b'{"name": "Alice"}',
        headers={"Content-Type": "application/json"}
    )

    resp = http_trigger(req)

    assert resp.status_code == 200
    assert b"Hello, Alice" in resp.get_body()


def test_http_trigger_without_name():
    req = func.HttpRequest(
        method="GET",
        url="/api/http_trigger",
        params={},
        body=None
    )

    resp = http_trigger(req)

    assert resp.status_code == 200
    assert b"Pass a name in the query string" in resp.get_body()
