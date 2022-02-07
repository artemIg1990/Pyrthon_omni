import logging

import requests
import common_functions
import config
from VDNG_env import envi
import random
import string
import json


envio = {"token": config.VDNG_token, "device_id":config.device_id, "phone":config.recipient_phone, "status":config.order_status_reserved, "price": 0}


def create_order(eni):
    headers = {
        "Authorization": config.VDNG_token,
        "Content-Type": "application/json"
    }
    request_body = {
        "device_id": eni['device_id'],
        "order_type": 5,
        "status": eni["status"],
        "recipient_phone": eni["phone"],
        "recipient_sign": "John Doe",
        "cell_width": 10,
        "cell_height": 10,
        "cell_depth": 10,
        "price": eni["price"],
        "currency": 10
    }
    url_request = f"{config.DHurl}{config.apiVersion}order/storage/"
    logging.debug("header: ", headers)
    logging.debug("body:", request_body)
    body_json = json.dumps(request_body, skipkeys=True, separators=None)
    return {"header": headers, "body": body_json, "url": url_request, "method": "POST"}

def place_order(eni):
    headers = {
        "Authorization": config.dev_token,
        "Content-Type": "application/json"
    }
    request_body = {
        "device_id": eni['device_id'],
        "codes": {
            "placement": eni["placement"],
            "recipient": common_functions.barcode_generator_four()
        }
    }
    body_json = json.dumps(request_body)
    url_request = f"{config.DHurl}{config.apiVersion}order/placing/storage/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "POST",
            "recipient_code": (request_body["codes"])["recipient"]}


def receipt_order(eni):
    headers = {
        "Authorization": config.VDNG_token,
        "Content-Type": "application/json"
    }
    request_body = {
        "device_id": eni["device_id"],
        "recipient_phone": eni["phone"],
        "recipient_code": eni["recipient"]
    }
    body_json = json.dumps(request_body)
    url_request = f"{config.DHurl}{config.apiVersion}order/receipt/storage/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "POST"}


def check_order(eni):
    headers = {
        "Authorization": config.VDNG_token
    }
    request_body = {
        "device_id": eni["device_id"],
        "recipient_phone": eni["phone"],
        "recipient_code": eni["recipient"]
    }
    body_json = json.dumps(request_body)
    url_request = f"{config.DHurl}{config.apiVersion}order/receipt/storage/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "PATCH"}

def temp_open_cell(eni):
    headers = {
        "Authorization": config.VDNG_token,
        "Content-Type": "application/json"
    }
    check_order_json = common_functions.run_request(check_order(eni), True).json
    order_uid = check_order_json.get("order_uid")
    request_body = {
        "oreder_uid": order_uid
    }
    url_request = f""





