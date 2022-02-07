import common_functions
import config
import json
import logging
logging.basicConfig(filename="VDNG_tst.log", level=config.logging_level)

body_list = [
    {"guid": "c7229e81-30f9-4771-b049-e22315afa91a", "price": 0.0, "barcode": "[CDK]1301443381", "packages": [{"cell_depth": 250, "cell_width": 200, "cell_height": 100, "number_place": "1", "barcode_place": "[ITM]000140540819"}], "cell_type": "5", "payer_num": "ИМ-РФ-1ЭП-39", "device_uid": "5e0fb27c-b431-411d-8c82-87dc89ed76d9", "order_type": 5, "seller_name": "ИП Силин А.В.", "sender_name": "\"Силин Александр Васильевич\"", "client_order": False, "order_number": 1301443381, "recipient_sign": "Матвеева Оксана Андреевна", "request_number": "2620", "recipient_phone": "+79194113621", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000140540819", "1"]},
    {"guid": "9d4cf7c7-02dc-4cb1-85f6-4756e4d19d4c", "price": 2550.0, "barcode": "[CDK]1300656588", "currency": 30, "packages": [{"cell_depth": 270, "cell_width": 250, "cell_height": 20, "number_place": "1", "barcode_place": "[ITM]000139708633"}], "cell_type": "5", "payer_num": "ИМ-РФ-ЧЛТ-456", "device_uid": "cdb03de1-fe1f-47ee-ac01-156210ad2462", "order_type": 5, "seller_name": "Ямкулин Гайрат Флюсович'", "sender_name": "Ямкулин Гайрат Флюсович'", "client_order": False, "order_number": 1300656588, "recipient_sign": "Вакуев Алексей Александрович", "request_number": "17.12", "recipient_phone": "+79689030666", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000139708633", "1"]},
    ]

def create_order(eni):
    headers = {
        "Authorization": config.dev_token,
        "Content-Type": "application/json"
    }
    request_body = eni
    body_json = json.dumps(request_body)
    url_request = f"{config.DHurl}{config.apiVersion}order/"
    return {"header": headers, "body": body_json, "url": url_request, "method": "POST"}


for line in body_list:
    try:
        order = common_functions.run_request(create_order(line), True)
        logging.info(f"result: {order['code']}, order: {order['body'].get('data').get('order_number')}")
    except:
        logging.warning(f"error. Code: {order['code']} message: {order['body']}")
