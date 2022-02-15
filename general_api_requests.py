import config
import json


def new_header(eni):
    if eni.get("auth", False):
        header = {
            "Authorization": config.dev_token,
            "Content-Type": "application/json"
            }
    else:
        header = {
            "Content-Type": "application/json"
            }
    return header


def get_order_info(eni):
    headers = new_header(eni)
    url_request = f"{config.DHurl}{config.apiVersion}order/{eni['uid']}/view/"
    return {"header": headers, "url": url_request, "method": "GET"}


def delete_order(eni):
    headers = {
        "Authorization": config.dev_token,
        "Content-Type": "application/json"
    }
    request_body = {
        "order_uid": eni.get("order_uid", eni["uid"])
    }
    url_request = f"{config.DHurl}{config.apiVersion}order/"
    body_json = json.dumps(request_body, skipkeys=True, separators=None)
    return {"header": headers, "body": body_json, "url": url_request, "method": "DELETE"}

def check_cells_status(eni):
    headers = {
        "Authorization": config.dev_token,
        "Content-Type": "application/json"
    }
    url_request = f"{config.DHurl}{config.apiVersion}device/{config.device_uid}/cells/statuses/?"
    return {"header": headers, "url": url_request, "method": "GET"}


def set_order_status(eni):
    headers = {
        "Authorization": config.dev_token,
        "Content-Type": "application/json"
    }
    request_body = {
        "order_uid": eni["uid"],
        "status": 15
    }
    body_json = json.dumps(request_body, skipkeys=True, separators=None)
    url_request = f"{config.DHurl}{config.apiVersion}order/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "PATCH"}


def create_order(eni):
    headers = eni.get("header")
    request_body = {
    "device_id": eni.get("device_id"),
    "ref_order": "",
    "order_type": 5,
    "status": int(eni.get("status"), 0),
    "client_system_id": "John(AUTO)Doe",
    "barcode": f"bar-{eni.get('order_number')}",
    "guid": f"auto-guid{eni.get('order_number')}",
    "order_number": eni.get("order_number"),
    "request_number": eni.get("order_number"),
    "price": eni.get("price"),
    "recipient_phone": config.sender_phone,
    "recipient_sign": "AutoCheck",
    "cell_width": 10,
    "cell_height": 10,
    "cell_depth": 10,
    "route_sheet": "",
    "order_payment": 1,
    "storehouse_item_id": "12345678",
    "additional_barcodes": [
        f"Auto-{eni.get('order_number')}1"
    ],
    "packages": [
        {
            "number_place": f"auto{eni.get('order_number')}1",
            "barcode_place": f"[AUTO]{eni.get('order_number')}1",
            "cell_width": 30,
            "cell_height": 60,
            "cell_depth": 50
        }
        ]
    }
    body_json = json.dumps(request_body)
    url_request = f"{config.DHurl}{config.apiVersion}order/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "POST"}

def barcode_read(eni):
    headers = {
        "Authorization": config.dev_token,
        "Content-Type": "application/json"
    }
    barcode = ""
    if eni.get("order_number") is not None:
        barcode = eni.get("order_number")
    else:
        barcode = eni.get("order_guid")
    request_body = {
        "device_id": eni.get("device_id"),
        "order_number": eni.get("order_number"),
        "barcode": barcode
    }
    body_json = json.dumps(request_body)
    url_request = f"{config.DHurl}{config.apiVersion}order/barcode/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "POST"}


def place_order(eni):
    headers = {
        "Authorization": config.dev_courier_token,
        "Content-Type": "application/json"
    }
    request_body = {
        "device_id": config.device_id,
        "codes" : {
            "placement": eni.get('order_number'),
            "recipient": eni.get('recipient_number')
        }
    }
    body_json = json.dumps(request_body)
    url_request = f"{config.DHurl}{config.apiVersion}order/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "POST"}
