from time import sleep
import VDNG_requests
import logging
import common_functions
import config
import general_api_requests


automated = True
logging.basicConfig(filename="VDNG_tst.log", level=config.logging_level)


def test_create_order_VDNG():
    if automated:
        envi = {
            "token": config.VDNG_token, "device_id": config.device_id, "phone": config.recipient_phone,
            "status": config.order_status_reserved, "price": 0
        }

        try:
            create_order = common_functions.run_request(VDNG_requests.create_order(envi), True)
            print(create_order["code"])
            assert create_order["code"] == 201
            logging.debug(f"tex: {create_order['body']}, \n type: {type(create_order['body'])}")
            order_data = create_order["body"].get("data")
            logging.debug(f"order_data: {type(order_data)} \n  text: {order_data}")
            order_uid = order_data.get("uid")
            envi.update({"order_uid": order_uid})

            delete_or = common_functions.run_request(general_api_requests.delete_order(envi), True)
            logging.debug(f"del: {delete_or['body']} \nrequest: {create_order['body']}")
            logging.info("Create order: SUCCESS")
        except AssertionError:
            logging.info(f"exception response: {create_order['code']} \n response_text: {create_order['body']}")
            logging.warning("Create order: FAILED")

def test_place_order_VGNG():
    envi = {
        "token": config.VDNG_token, "device_id": config.device_id, "phone": config.recipient_phone,
        "status": config.order_status_reserved, "price": 0
    }
    create_order = common_functions.run_request(VDNG_requests.create_order(envi), True)

    order_data = create_order["body"]
    logging.debug(f"order_data: {type(order_data)} \n  text: {order_data}")
    codes_data = order_data['data']
    codes = codes_data["codes"]

    envi.update({"placement": codes['placement']})
    order_type = order_data["data"]
    envi.update({"uid": order_type.get("uid")})

    sleep(1)
    place = VDNG_requests.place_order(envi)
    envi.update({"recipient": place["recipient_code"]})
    place_order = common_functions.run_request(place, True)
    i = 0
    status_order = common_functions.run_request(general_api_requests.get_order_info(envi), True)
    status_body = status_order["body"].get("data")
    status = status_body.get("status")
    sleep(1)
    while status != 3 and i < 120:
        i += 1
        status_order = common_functions.run_request(general_api_requests.get_order_info(envi), True).get("body")
        status = status_order["data"].get("status")
        sleep(2)
    assert status == 3
    sleep(2)
    logging.warning(f"Error: {create_order['code']} \ntext: {create_order['body']}")
    receipt_order = common_functions.run_request(VDNG_requests.receipt_order(envi), True)

    #order_to_new = common_functions.run_request(general_api_requests.set_order_status(envi), True)
    # delete_order = common_functions.run_request(general_api_requests.delete_order(envi), True)
    #assert delete_order["code"] == 200


test_create_order_VDNG()
sleep(1)
test_place_order_VGNG()
