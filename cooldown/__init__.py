import logging
import os

import azure.functions as func

import requests
from requests.auth import HTTPDigestAuth
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger "cooldown" function was called.')

    path = req.params.get('path')
    if not path:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            path = req_body.get('path')

    if path:
        fullpath = set_access_tier(path)

        return func.HttpResponse(f"Path={fullpath} was used to change access tier to 'Cold'.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a blob path in the query string or in the request body to change the access tier to 'Cold'.",
             status_code=200
        )


def set_access_tier(path) -> str:
    logging.info(f'Setting {path} to Cold access tier')


    # Get the setting named 'myAppSetting'
    try:
        storage_url = os.environ["storage.url"]
        logging.info(f'My "storage.url" setting value: {storage_url}')
    except KeyError:
        pass
    else:
        storage_url = 'https://coredevstg.blob.core.windows.net'


    return storage_url + path