import unittest
import smoke_test_assist



def test_create_order_no_pay():       ## Придумать как запихнуть параметры в тест-фикстуру (верю, что так можно)
    params = {"price": 0, "status": 0, "client_order": False, "auth": True}
    result = smoke_test_assist.create_order(params)
    assert result.get("status_code") == 201
    assert result["data"].get("price") == 0
"""
    def test_create_order_pay(self):
        params = {"price": 11, "status": 0, "client_order": False}
        result = smoke_test_assist.create_order(params)
        assert result.get("status_code") == 201
        assert result["data"].get("price") > 0

    def test_create_order_no_pay_book(self):
        params = {"price": 0, "status": 1, "client_order": False}
        result = smoke_test_assist.create_order(params)
        assert result.get("status_code") == 201
        assert result["data"].get("price") == 0

    def test_create_order_pay_book(self):
        params = {"price": 11, "status": 1, "client_order": False}
        result = smoke_test_assist.create_order(params)
        assert result.get("status_code") == 201
        assert result["data"].get("price") > 0

    def test_create_client_order_no_pay(self):
        params = {"price": 0, "status": 0, "client_order": True}
        result = smoke_test_assist.create_order(params)
        assert result.get("status_code") == 201
        assert result["data"].get("price") == 0

    def test_create_client_order_pay(self):
        params = {"price": 11, "status": 0, "client_order": True}
        result = smoke_test_assist.create_order(params)
        assert result.get("status_code") == 201
        assert result["data"].get("price") > 0

    def test_create_client_order_no_pay_book(self):
        params = {"price": 0, "status": 1, "client_order": True}
        result = smoke_test_assist.create_order(params)
        assert result.get("status_code") == 201
        assert result["data"].get("price") == 0


    def test_create_client_order_pay_book(self):
        params = {"price": 11, "status": 1, "client_order": True}
        result = smoke_test_assist.create_order(params)
        assert result.get("status_code") == 201
        assert result["data"].get("price") == 11.0
"""
if __name__ == '__main__':
    unittest.main()
