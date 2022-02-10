import logging

DHurl = "http://dev.hub.omnic.solutions/"
BHurl = "https://brandshub-test.omnic.solutions/"
VB_url = "http://incsoft.space:3000/#/"
apiVersion = "api/2.0.0/"
atolToken = "Token 8ee5cf663f99b61f69082f5aaf8fac4194e020a7"
omniToken = "Token 803b28a3406911b36684d8a6c266fa54dbf00798"
BHToken = "Token 7e3b37f1e08b250ba72510052c13ca3402cd4e1f"
VDNG_token = "803b28a3406911b36684d8a6c266fa54dbf00798"
dev_token = "Token 803b28a3406911b36684d8a6c266fa54dbf00798"
dev_courier_token = "Token 0454999b6b674ede42adf777c3de01032130b620"
order_status_hew = "0"
order_status_reserved = "1"
order_status_placed = 3
logging_level = logging.DEBUG
login_bh_cc = "ignatenko.a"
password_bh_cc = "123456"
window_size = "1280,1024"


#Локальные переменные. Можно менять для конкретного тест-рана
device_id = "0011"
device_uid = "5e0fb27c-b431-411d-8c82-87dc89ed76d9"
order_status = order_status_hew
sender_phone = "79111236525"
sender_phone_u = "380501236547"
recipient_phone = "380631234566"

"""
def sort_devices(device_list = ["0", "1"], search_from = "0", search_to = "1"):
    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k
    di = {}
    for i in range(len(device_list)):
        di.update({int(device_list[i]): device_list[i]})
    keys_list = di.keys()
    lis = []
    for i in keys_list: lis.append(i)
    lis.sort()
    new_di = {}
    for device_number in range(len(lis)):
        sub_di = {lis[device_number]: di.get(lis[device_number])}
        new_di.update({device_number: sub_di})
    from_key = {int(search_from): search_from}
    to_key = {int(search_to): search_to}
    search_from_number = get_key(new_di, from_key)
    search_to_number = get_key(new_di, to_key)
    if search_to_number-search_from_number < 100:
        final_list = []
        for device in range(search_from_number, search_to_number+1):
            d_data = new_di.get(device)
            added_device = d_data.values()
            for ld in added_device: final_list.append(ld)
        return final_list
    else:
        return f"ERROR. Too many items selected. Selected {len(lis)} items. Max 100 items"

def sort_devices(device_list, search_from: str, search_to: str):
    indexes = sorted({int(i): i for i in device_list if i.isdigit()}.items())
    search_from_index = int(search_from)
    search_to_index = int(search_to)
    return [dev for i, dev in indexes if search_from_index <= i <= search_to_index]


print(sort_devices(device_list=['1001', '0011', '000254', '10025', '0100'], search_from = "0011", search_to = "1001"))
"""
