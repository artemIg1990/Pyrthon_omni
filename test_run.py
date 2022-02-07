import unittest
import smoke_test_assist


class MyTestCase(unittest.TestCase):
    def smoke_test(self):
        created_orders = {}
        self.create_order_no_pay()


if __name__ == '__main__':
    unittest.main()
