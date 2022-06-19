from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any
from urllib.parse import unquote

from aws_lambda_powertools.event_handler import content_types
from aws_lambda_powertools.event_handler.api_gateway import (
    APIGatewayRestResolver,
    Response,
)
from aws_lambda_powertools.utilities.typing import LambdaContext

app = APIGatewayRestResolver()


def lambda_handler(event: dict[str, Any], context: LambdaContext) -> Any:
    """lambda_handler

    aws-lambda-powertoolsのルーティング機能を使用しています。
    https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/#api-gateway-rest-api
    """
    return app.resolve(event, context)


@app.get("/form")
def get_form() -> Response:
    """htmlを読み込み返却します。

    /index.htmlを読み込み返却しています。
    index.htmlには、入力フォームのサンプルが記述してあります。
    """

    html_path = Path("index.html")
    with open(html_path, "r") as f:
        file = f.read()

    return Response(status_code=200, content_type=content_types.TEXT_HTML, body=file)


@app.post("/form")
def post_form() -> Response:
    """htmlフォームからのデータを受信します。

    受信されたデータは解析したのち、webページに表示しています。
    """

    body_data: dict[str, Any] = html_form_split(app.current_event.body)

    # テキストが日本語の場合はURLデコードを行う
    body_data["input3"] = unquote(body_data.get("input3", ""))

    # dictをstrに変換する。日本語を含む想定のため、文字コードに注意する。
    res: str = json.dumps(body_data, ensure_ascii=False)

    # 日本語に対応するためcharsetを設定
    return Response(
        status_code=200,
        content_type=content_types.TEXT_PLAIN + "; charset=utf-8",
        body=res,
    )


def html_form_split(body: str) -> dict[str, Any]:
    """formから送信されたbodyをパースし、辞書型で返却します。

    Args:
        body (str): _description_

    Returns:
        dict[str, Any]: _description_
    """

    keys = []
    values = []

    for data in body.split("&"):
        pair = data.split("=")
        keys.append(pair[0])
        values.append(pair[1])

    return dict(zip(keys, values))


@app.get("/favicon.ico")
def get_favicon() -> Response:
    """faviconを返却する

    githubのプロフィールに設定されているアイコンを返却します。
    URlは環境変数に保存されています。-> /template.yaml
    """
    headers = {"Location": os.environ.get("FAVICON_URL")}
    return Response(
        status_code=301, headers=headers, body="", content_type=content_types.TEXT_PLAIN
    )


@app.get("/hello")
def get_hello() -> Response:
    """helo universeを返却します。

    integrationテストにて、Lambdaが動いているかの確認に使用されています。
    """
    return Response(
        status_code=200,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps({"message": "hello universe"}),
    )
