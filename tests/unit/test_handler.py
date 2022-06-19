from __future__ import annotations

import json
from typing import Any

from aws_lambda_powertools.event_handler import content_types
from aws_lambda_powertools.utilities.typing import LambdaContext

from html_input_form import app


class Response:
    def __init__(self, response: dict[str, Any]) -> None:
        self.statusCode: int = response.get("statusCode", 0)
        self.headers: str = response.get("headers", {"", ""})
        self.Content_type: str = self.headers.get("Content-Type", "")
        self.isBase64Encoded: bool = response.get("isBase64Encoded", False)
        self.multiValueHeaders: dict[str, Any] = response.get(
            "multiValueHeaders", {"", ""}
        )
        self.body: str | bytes = response.get("body", "")


def apigw_event(path: str, body: dict[str, Any] | str, method: str) -> dict[str, Any]:
    """Generates API GW Event"""

    if isinstance(body, dict):
        body = json.dumps(body)

    return {
        "body": body,
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": method,
        "stageVariables": {"baz": "qux"},
        "path": path,
    }


def test_get_hello() -> None:

    body: dict[str, Any] = {}
    path: str = "/hello"
    method: str = "GET"
    event = apigw_event(path, body, method)
    context = LambdaContext()

    ret: Response = app.lambda_handler(event, context)
    res: str | bytes = ret.get("body", "")
    data: str = json.loads(res).get("message", "")

    assert data == "hello universe"


def test_post_form() -> None:

    path: str = "/form"
    body: str = "input3=sample&number=8"
    method: str = "POST"
    event = apigw_event(path, body, method)
    context = LambdaContext()
    ret = Response(app.lambda_handler(event, context))

    assert ret.statusCode == 200
    assert ret.Content_type == content_types.TEXT_PLAIN + "; charset=utf-8"
    assert json.loads(ret.body).get("input3", "") == "sample"
