import logging
import random
import string
import requests
import config
import general_api_requests


def barcode_generator_six():
    i = 0
    barcode = ""
    while i < 6:
        i += 1
        barcode += str(random.randint(0, 9))
    return barcode


def barcode_generator_four():
    i = 0
    barcode = ""
    while i < 4:
        i += 1
        barcode += str(random.randint(0, 9))
    return barcode


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def guid_generator():
    guid = f"{generate_alphanum_random_string(6)}-{generate_alphanum_random_string(6)}-" \
           f"{generate_alphanum_random_string(4)}-{generate_alphanum_random_string(5)}"
    return guid


def run_request(request_data, auth):
    method = request_data.get("method")
    url = request_data.get("url")
    header = request_data.get("header")
    if not auth:
        header.update({"Authorization": "null"})
    if method == "GET":
        req = requests.get(url, headers=header)
    elif method == "POST":
        req = requests.post(url, headers=header, data=request_data.get("body"))
    elif method == "PUT":
        req = requests.put(url, headers=header, data=request_data.get("body"))
    elif method == "PATCH":
        req = requests.patch(url, headers=header, data=request_data.get("body"))
    elif method == "DELETE":
        req = requests.delete(url, headers=header, data=request_data.get("body"))
    # logging.info(f"method: {method} \nresponse_code: {req.status_code} \nurl: {url}")
    # logging.debug(f"request: {url} \n body: {request_data.get('body')} \n header: {header}")
    return {"code": req.status_code, "body": req.json()}


def check_order_exist(envi: dict):
    order_number_exist = run_request(general_api_requests.barcode_read(envi), True)
    order_guid_exist = run_request(general_api_requests.barcode_read(envi), True)
    if order_number_exist.get("code") == 200 or order_guid_exist.get("code") == 200:
        # Order exist
        return True
    else:
        return False


def prepare_envi(params: dict):
    envi = {
            "token": config.VDNG_token, "device_id": config.device_id, "phone": config.recipient_phone,
            "status": config.order_status_reserved
        }
    envi.update({"order_guid": guid_generator()})
    envi.update({"order_number": barcode_generator_six()})
    while check_order_exist(envi):    # подумать как заменить рекурсию циклом если в этом есть смысл
        prepare_envi(params)
    envi.update({"price": params.get("price", 0)})
    envi.update({"status": params.get("status", 0)})
    envi.update({"status": params.get("client_order", False)})

    return envi
