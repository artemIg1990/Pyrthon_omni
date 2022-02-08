import config
import common_functions
import general_api_requests
import PyQt5

created_orders = {}
params = {"price": 0, "status": 0, "client_order": False}


def create_order(params: dict):
    envi = common_functions.prepare_envi(params)
    new_order = common_functions.run_request(general_api_requests.create_order(envi), True)
    if new_order["code"] == 201:
        created_orders.update(new_order.get("body"))
    else:
        result = new_order["body"].get("message")
        return {"status_code": new_order.get("code"), "message": f"ERROR: Code: {new_order['code']}, Message: {result}"}
    return new_order.get("body")


def place_order(params: dict):
    envi = {}

"""
def test_create_order_pay():
    envi = common_functions.prepare_envi()
    envi.update({"price": 11})
    envi.update({"status": config.order_status_hew})
    new_order = common_functions.run_request(general_api_requests.create_order(envi), True)
    if new_order["code"] == 201:
        order_data = new_order["body"].get("data")
        price = order_data["price"]
    try:
        assert new_order["code"] == 201 and price != 0
    except AssertionError as err:
        print(err)
    uid = new_order["body"].get("data").get("uid")
    envi.update({"uid": uid})
    delete_order = common_functions.run_request(general_api_requests.delete_order(envi), True)
    try:
        assert delete_order["code"] == 200
    except AssertionError as err:
        print(err)
    finally:
        print("done")
"""

