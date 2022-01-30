from typing import Dict, List
import requests
import json

from models.model import Model, drop_duplicates


def crawl():
    url = ""

    payload: Dict[str, str] = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length": "0",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)


def parse_models(res_json: List[str]) -> List[Model]:
    models: List[Model] = []

    if res_json:
        for entry in res_json:
            model = Model(entry.title, entry.summary, entry.link)
            models.append(model)

    return models


def drop_duplicates(path: str) -> List[Model]:
    models: List[Model] = []

    with open(path, "r") as f:
        text = f.read()

        if text:
            json_models = json.loads(text)
            for model_json in json_models:
                models.append(
                    Model(
                        title=model_json["title"],
                        summary=model_json["summary"],
                        url=model_json["url"],
                    )
                )

    return models


def store_models(path: str, models: List[Model], as_json: bool = True):
    with open(path, "w") as f:
        if as_json:
            models = [model.as_dict() for model in models]

        f.write(json.dumps(models, default=str))
