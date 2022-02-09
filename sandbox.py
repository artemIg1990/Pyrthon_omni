import random
import string
import common_functions
import config
import json
import logging
from time import sleep

logging.basicConfig(filename="VDNG_tst.log", level=config.logging_level)

body_list = [
{"request_data":	{"guid": "c8d80294-5ed2-4bcf-9e63-56f8a42b24a2", "price": 0.0, "barcode": "[CDK]1303536695", "packages": [{"cell_depth": 10, "cell_width": 10, "cell_height": 10, "number_place": "AECD0000668411RU", "barcode_place": "[ITM]000142780477"}], "cell_type": "5", "payer_num": "ИМ-РФ-ГЛ-23675", "order_type": 5, "seller_name": "KEYYOU KeyCase Store", "sender_name": "ЦАЙНЯО САПЛАЙН ЧЕЙН МЕНЕДЖМЕНТ (РУ)", "client_order": False, "order_number": 1303536695, "recipient_sign": "Antipin Alexandr Sergeevich", "request_number": "AECD0000668411RU", "recipient_phone": "+79199491199", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000142780477", "AECD0000668411RU"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "86f7bff9-22c8-421b-bb05-9e6f3aaae214", "price": 0.0, "barcode": "[CDK]1304702674", "packages": [{"cell_depth": 380, "cell_width": 130, "cell_height": 80, "number_place": "1", "barcode_place": "[ITM]000144021121"}], "cell_type": "5", "payer_num": "ИМ-РФ-АГВ-64", "order_type": 5, "seller_name": " ", "sender_name": "ИП Платон Василий Васильевич", "client_order": False, "order_number": 1304702674, "recipient_sign": "ПАНОВ АНАТОЛИЙ МИХАЙЛОВИЧ", "request_number": "3006", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144021121", "1"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "946e09c5-c9e0-448c-8f3d-2860f7409082", "price": 0.0, "barcode": "[CDK]1304956829", "packages": [{"cell_depth": 430, "cell_width": 410, "cell_height": 150, "number_place": "1", "barcode_place": "[ITM]000144283954"}], "cell_type": "5", "payer_num": "IM-KNR-F54-2", "device_uid": "f5c58726-efba-4e11-ad76-bc8327e26091", "order_type": 5, "seller_name": "SHEIN", "sender_name": "ZOETOP BUSINESS CO., LIMITED", "client_order": False, "order_number": 1304956829, "recipient_sign": "Прилипа Алина Евгеньевна", "request_number": "BG2201040928388", "recipient_phone": "79163953222", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144283954", "1", "[ITM]000144283954"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 727", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "6531d635-94ca-4f53-a8d1-a1404588de50", "price": 0.0, "barcode": "[CDK]1304958018", "packages": [{"cell_depth": 470, "cell_width": 430, "cell_height": 190, "number_place": "1", "barcode_place": "[ITM]000144285203"}], "cell_type": "5", "payer_num": "IM-KNR-F54-2", "device_uid": "815ff4cb-af2c-4db4-9a69-a6abdf994561", "order_type": 5, "seller_name": "SHEIN", "sender_name": "ZOETOP BUSINESS CO., LIMITED", "client_order": False, "order_number": 1304958018, "recipient_sign": "Федонина Алиса Сергеевна", "request_number": "BG2201040937567", "recipient_phone": "79301864797", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144285203", "1", "[ITM]000144285203"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 412", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "1b3ed601-71f8-47c4-a0b6-f755bdf20043", "price": 840.0, "barcode": "[CDK]1305104393", "currency": 30, "packages": [{"cell_depth": 640, "cell_width": 440, "cell_height": 40, "number_place": "796", "barcode_place": "[ITM]000144438608"}], "cell_type": "5", "payer_num": "ИМ1213401", "device_uid": "6a09b76d-7128-4191-89ef-b15ff898e03b", "order_type": 5, "seller_name": " ", "sender_name": "МЕДНИКОВ КОНСТАНТИН КОНСТАНТИНОВИЧ", "client_order": False, "order_number": 1305104393, "recipient_sign": "Цветкова Гульназ Робертовна", "request_number": "0022-000049", "recipient_phone": "79112543140", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144438608", "796", "[ITM]000144438608"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 78", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "49bed732-d4a2-46d9-8662-c3aec36f0153", "price": 0.0, "barcode": "[CDK]1305165033", "packages": [{"cell_depth": 490, "cell_width": 490, "cell_height": 140, "number_place": "1", "barcode_place": "[ITM]000144500629"}], "cell_type": "5", "payer_num": "IM-KNR-F54-2", "device_uid": "77768364-c392-4252-93dd-a57f27ffd8b0", "order_type": 5, "seller_name": "SHEIN", "sender_name": "ZOETOP BUSINESS CO., LIMITED", "client_order": False, "order_number": 1305165033, "recipient_sign": "Кашанова Алина Евгеньевна", "request_number": "BG2201050838109", "recipient_phone": "79209034984", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144500629", "1", "[ITM]000144500629"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 407", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "3f949b8f-fd57-40e0-84bc-b6aede9d63c1", "price": 0.0, "barcode": "[CDK]1305204118", "packages": [{"cell_depth": 520, "cell_width": 200, "cell_height": 50, "number_place": "8860027209", "barcode_place": "[ITM]000144541180"}], "cell_type": "5", "payer_num": "ИМ-РФ-ГЛ-3636", "order_type": 5, "seller_name": "Прозоров Сергей Андреевич", "sender_name": "Прозоров Сергей Андреевич", "client_order": False, "order_number": 1305204118, "recipient_sign": "Пирозерский Николай Юрьевич", "request_number": "1", "recipient_phone": "+79533477768", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144541180", "8860027209"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "3d17b6ee-6531-4300-858d-f22eb1f261bc", "price": 350.0, "barcode": "[CDK]1305257090", "currency": 30, "packages": [{"cell_depth": 670, "cell_width": 320, "cell_height": 60, "number_place": "1", "barcode_place": "[ITM]000144597097"}], "cell_type": "5", "payer_num": "ИМ-РФ-ПОЛ-45", "device_uid": "77768364-c392-4252-93dd-a57f27ffd8b0", "order_type": 5, "seller_name": "*", "sender_name": "Орлина Татьяна Сергеевна", "client_order": False, "order_number": 1305257090, "recipient_sign": "Башкиров Сергей Михайлович", "request_number": "1013", "recipient_phone": "79175509355", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144597097", "1", "[ITM]000144597097"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 407", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "891cebcf-0afe-4d50-8569-264bd286747a", "price": 0.0, "barcode": "[CDK]1305366218", "packages": [{"cell_depth": 500, "cell_width": 480, "cell_height": 180, "number_place": "1", "barcode_place": "[ITM]000144711028"}], "cell_type": "5", "payer_num": "IM-KNR-F54-2", "device_uid": "d200306d-ed84-4735-a924-b3a091463480", "order_type": 5, "seller_name": "SHEIN", "sender_name": "ZOETOP BUSINESS CO., LIMITED", "client_order": False, "order_number": 1305366218, "recipient_sign": "ВОЛКОВА ТАТЬЯНА МИХАЙЛОВНА", "request_number": "BG2201070008391", "recipient_phone": "79119661732", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144711028", "1", "[ITM]000144711028"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 31", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "897f9270-02ae-4782-bb0f-5568fc4b877e", "price": 0.0, "barcode": "[CDK]1305496530", "packages": [{"cell_depth": 600, "cell_width": 400, "cell_height": 170, "number_place": "2048926#1270114147", "barcode_place": "[ITM]000144843830"}], "cell_type": "5", "payer_num": "ИМ37758", "device_uid": "4857dbec-6647-4f73-be29-110eed8e801b", "order_type": 5, "seller_name": "Пузырьков Максим Олегович, Индивидуальный предприниматель", "sender_name": "Пузырьков Максим Олегович", "client_order": False, "order_number": 1305496530, "recipient_sign": "Екатерина Бочарова", "request_number": "1270114147", "recipient_phone": "79253806057", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144843830", "2048926#1270114147", "[ITM]000144843830"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 599", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "b4185f19-3bb0-4ece-a916-0b2dc66d1038", "price": 0.0, "barcode": "[CDK]1305543146", "packages": [{"cell_depth": 590, "cell_width": 310, "cell_height": 110, "number_place": "4653525#1687640012", "barcode_place": "[ITM]000144893183"}], "cell_type": "5", "payer_num": "ИМ-РФ-СБЛ-269", "device_uid": "222551a3-0852-4bc2-98cf-1f7e8abf4e02", "order_type": 5, "seller_name": "Харитонова Кристина", "sender_name": "Харитонова Кристина", "client_order": False, "order_number": 1305543146, "recipient_sign": "Корнишина Екатерина Алексеевна", "request_number": "1687640012", "recipient_phone": "79856830724", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144893183", "4653525#1687640012", "[ITM]000144893183"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 430", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "41886202-fe16-4504-b413-ce9d23921540", "price": 2190.0, "barcode": "[CDK]1305559641", "currency": 30, "packages": [{"cell_depth": 560, "cell_width": 160, "cell_height": 50, "number_place": "1", "barcode_place": "[ITM]000144910999"}], "cell_type": "5", "payer_num": "СЗ-РФ-ЭНЛ-23", "device_uid": "212d14ca-9b60-4092-a19b-062d81d71567", "order_type": 5, "seller_name": "Шульга Никита Леонидович", "sender_name": "Шульга Никита Леонидович\"", "client_order": False, "order_number": 1305559641, "recipient_sign": "Фёдоров Эрик Игоревич", "request_number": "1", "recipient_phone": "79219889775", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144910999", "1", "[ITM]000144910999"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 39", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "4c2e963b-9f95-4577-aedc-e9a25cc0f153", "price": 0.0, "barcode": "[CDK]1305596444", "packages": [{"cell_depth": 540, "cell_width": 450, "cell_height": 70, "number_place": "2640426#1024293367", "barcode_place": "[ITM]000144948818"}], "cell_type": "5", "payer_num": "ИМ-РФ-Б5Т-29", "device_uid": "e519e3fd-b041-4920-ac39-df4afeae001a", "order_type": 5, "seller_name": "Логинов Вадим Юрьевич, Индивидуальный предприниматель", "sender_name": "Логинов Вадим Юрьевич", "client_order": False, "order_number": 1305596444, "recipient_sign": "Солодова Анна Игоревна", "request_number": "1024293367", "recipient_phone": "79091684642", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144948818", "2640426#1024293367", "[ITM]000144948818"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 615", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "d27959b4-caa8-47e3-968d-6c90e90bd98e", "price": 0.0, "barcode": "[CDK]1305606029", "packages": [{"cell_depth": 510, "cell_width": 100, "cell_height": 120, "number_place": "24004058759", "barcode_place": "[ITM]000144958364"}], "cell_type": "5", "payer_num": "ИМ-РФ-ТПЗ-86", "device_uid": "c1083ab8-433a-468b-81fc-16914e46a446", "order_type": 5, "seller_name": "La Roche Posay", "sender_name": "Laroche Posay", "client_order": False, "order_number": 1305606029, "recipient_sign": "Greta Martinkute", "request_number": "0087360003", "recipient_phone": "79643236004", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000144958364", "24004058759", "[ITM]000144958364"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 25", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "89704fb2-785b-41fb-bf35-0dec3a9faeff", "price": 0.0, "barcode": "[CDK]1305649595", "packages": [{"cell_depth": 710, "cell_width": 100, "cell_height": 160, "number_place": "24004059437", "barcode_place": "[ITM]000145002950"}], "cell_type": "5", "payer_num": "ИМ-РФ-ТПЗ-86", "device_uid": "e419e2c9-ee12-4f88-9ca3-d9c20fe02048", "order_type": 5, "seller_name": "La Roche Posay", "sender_name": "Laroche Posay", "client_order": False, "order_number": 1305649595, "recipient_sign": "Ольга Барахоева", "request_number": "0087360279", "recipient_phone": "79112102121", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145002950", "24004059437", "[ITM]000145002950"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 110", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "23210f48-586c-4402-a4cc-86741bfb5c23", "price": 0.0, "barcode": "[CDK]1305689234", "packages": [{"cell_depth": 550, "cell_width": 370, "cell_height": 180, "number_place": "8900978929", "barcode_place": "[ITM]000145044620"}], "cell_type": "5", "device_uid": "e519e3fd-b041-4920-ac39-df4afeae001a", "order_type": 5, "sender_name": "Столярова Юлия Александровна", "client_order": False, "order_number": 1305689234, "recipient_sign": "Дворянкин Иван Игоревич", "request_number": "1305689234", "recipient_phone": "79858906611", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145044620", "8900978929", "[ITM]000145044620"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 615", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "f6edce5f-d1cc-45ad-b0f8-eeeee6651f26", "price": 0.0, "barcode": "[CDK]1305695429", "packages": [{"cell_depth": 350, "cell_width": 350, "cell_height": 150, "number_place": "1", "barcode_place": "[ITM]000145051153"}], "cell_type": "5", "payer_num": "ИМ1231272486", "order_type": 5, "seller_name": "\"ТОП ТОП\"-, ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ", "sender_name": "Топ Топ ООО", "client_order": False, "order_number": 1305695429, "recipient_sign": "Дикарева  Ольга", "request_number": "31191470/1", "recipient_phone": "+79217906463", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145051153", "1"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "caaf6f04-7ffa-4aa2-9dbf-4a88e667b6cb", "price": 0.0, "barcode": "[CDK]1305722286", "packages": [{"cell_depth": 450, "cell_width": 450, "cell_height": 120, "number_place": "1", "barcode_place": "[ITM]000145078673"}], "cell_type": "5", "payer_num": "ИМ-РФ-ТСВ-20", "device_uid": "6f03d9fc-495c-4d44-8476-39b589fb399b", "order_type": 5, "seller_name": "Пригодич Антон Дмитриевич", "sender_name": "Пригодич Антон Дмитриевич", "client_order": False, "order_number": 1305722286, "recipient_sign": "Загребельная Мария Сергеевна", "request_number": "4090", "recipient_phone": "79112980160", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145078673", "1", "[ITM]000145078673"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 44", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "5159b7b8-f8fb-47a9-90a6-8919ee98b777", "price": 0.0, "barcode": "[CDK]1305743201", "packages": [{"cell_depth": 570, "cell_width": 100, "cell_height": 140, "number_place": "24004061105", "barcode_place": "[ITM]000145099722"}], "cell_type": "5", "payer_num": "ИМ-РФ-ТПЗ-86", "device_uid": "de7de8a3-b218-404c-8f6d-6329adf700b6", "order_type": 5, "seller_name": "La Roche Posay", "sender_name": "Laroche Posay", "client_order": False, "order_number": 1305743201, "recipient_sign": "Анастасия Силкина", "request_number": "0087361128", "recipient_phone": "79032649888", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145099722", "24004061105", "[ITM]000145099722"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 839", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "92c9c7c5-686b-4660-8d77-39611ca01198", "price": 0.0, "barcode": "[CDK]1305777837", "packages": [{"cell_depth": 250, "cell_width": 100, "cell_height": 300, "number_place": "1", "barcode_place": "[ITM]000145135625"}], "cell_type": "5", "payer_num": "Н2К885", "order_type": 5, "sender_name": "СИБЕВРОВЭН", "client_order": False, "order_number": 1305777837, "recipient_sign": "Галкин Роман", "request_number": "1305777837", "recipient_phone": "+79138337590", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145135625", "1"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "a142f111-6f2d-4052-940e-9d90aaf2e1d6", "price": 940.0, "barcode": "[CDK]1305834071", "currency": 30, "packages": [{"cell_depth": 520, "cell_width": 350, "cell_height": 130, "number_place": "1", "barcode_place": "[ITM]000145195390"}], "cell_type": "5", "payer_num": "ИМ-РФ-ТЛТ-465", "device_uid": "fb5e48c7-d7dd-46e0-9a15-ea89a025271a", "order_type": 5, "seller_name": "\" НОВЫЕ РЕШЕНИЯ \"", "sender_name": "\" НОВЫЕ РЕШЕНИЯ \"", "client_order": False, "order_number": 1305834071, "recipient_sign": "Соколов Артём Александрович", "request_number": "#100165548", "recipient_phone": "79207440888", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145195390", "1", "[ITM]000145195390"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 429", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "d648cbae-2768-4cb2-b883-b9961b0ec178", "price": 0.0, "barcode": "[CDK]1305840310", "packages": [{"cell_depth": 560, "cell_width": 400, "cell_height": 20, "number_place": "2446555#1344408791", "barcode_place": "[ITM]000145202068"}], "cell_type": "5", "payer_num": "ИМ-РФ-БНГ-428", "device_uid": "d748543e-1608-400f-85a2-04e57656ec8a", "order_type": 5, "seller_name": "\"ХРАМЦОВА ЕЛЕНА\", ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ", "sender_name": "\"ХРАМЦОВА ЕЛЕНА\"", "client_order": False, "order_number": 1305840310, "recipient_sign": "Ксенофонтова Дарина Ильинична", "request_number": "1344408791", "recipient_phone": "79218834166", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145202068", "2446555#1344408791", "[ITM]000145202068"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 51", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "99d11f17-f045-48db-9ab9-763b778a251f", "price": 0.0, "barcode": "[CDK]1305845456", "packages": [{"cell_depth": 550, "cell_width": 400, "cell_height": 150, "number_place": "1", "barcode_place": "[ITM]000145207564"}], "cell_type": "5", "payer_num": "ИМ-РФ-МББ-33", "device_uid": "1236ef58-d5c6-4de1-90f2-f2a0b9c6ae01", "order_type": 5, "seller_name": "\"ГЕНЗА\"", "sender_name": "\"ГЕНЗА\"", "client_order": False, "order_number": 1305845456, "recipient_sign": "ПАВЛОВ ВЛАДИМИР ЮРЬЕВИЧ", "request_number": "995", "recipient_phone": "79119251188", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145207564", "1", "[ITM]000145207564"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 37", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "43dd9369-7632-4969-81cf-aeff207646b1", "price": 0.0, "barcode": "[CDK]1305854603", "packages": [{"cell_depth": 710, "cell_width": 170, "cell_height": 130, "number_place": "13030873791", "barcode_place": "[ITM]000145217166"}], "cell_type": "5", "payer_num": "ИМ-РФ-ТПЗ-86", "order_type": 5, "seller_name": "Vichy", "sender_name": "Vichy", "client_order": False, "order_number": 1305854603, "recipient_sign": "АНДРЕЙ АНДРЕЙ", "request_number": "0087361397", "recipient_phone": "+79263232596", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145217166", "13030873791"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "a8838893-3c37-4ada-b849-39a67fe5f9ec", "price": 0.0, "barcode": "[CDK]1305858149", "packages": [{"cell_depth": 600, "cell_width": 70, "cell_height": 70, "number_place": "1", "barcode_place": "[ITM]000145220913"}], "cell_type": "5", "payer_num": "ИМ-РФ-ИОН-123", "order_type": 5, "seller_name": "Шмаюк Л.Н.", "sender_name": "Шмаюк Людмила Николаевна", "client_order": False, "order_number": 1305858149, "recipient_sign": "Антонова Екатерина Евгеньевна", "request_number": "0", "recipient_phone": "+79771179395", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145220913", "1"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "c647158b-0c12-4378-ab4f-98fa7cb5c98c", "price": 0.0, "barcode": "[CDK]1305871213", "packages": [{"cell_depth": 410, "cell_width": 520, "cell_height": 40, "number_place": "_", "barcode_place": "[ITM]000145234993"}], "cell_type": "5", "payer_num": "ИМ-РФ-ЧЛН-533", "device_uid": "12086ef5-1991-43a6-98d6-038d4b0005f6", "order_type": 5, "seller_name": "ООО ШвейСклад", "sender_name": "ШвейСклад", "client_order": False, "order_number": 1305871213, "recipient_sign": "Яуфман Александр Лаврентьевич", "request_number": "1000", "recipient_phone": "79037665606", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145234993", "_", "[ITM]000145234993"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 800", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "d837944f-1a80-4807-a8e9-656253aedb31", "price": 0.0, "barcode": "[CDK]1305933056", "packages": [{"cell_depth": 700, "cell_width": 200, "cell_height": 50, "number_place": "1", "barcode_place": "[ITM]000145301555"}], "cell_type": "5", "payer_num": "ИМ4294973139", "device_uid": "de8b4ac3-c445-4de4-b28d-5019f9b9d836", "order_type": 5, "seller_name": "НемоПро", "sender_name": "Десятниченко Александр Сергеевич", "client_order": False, "order_number": 1305933056, "recipient_sign": "Малышев Олег Александрович", "request_number": "2201/37 (2)", "recipient_phone": "79214086858", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145301555", "1", "[ITM]000145301555"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 72", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "f2fa89d4-58f3-4e0d-8030-b72e41a746e3", "price": 0.0, "barcode": "[CDK]1305958239", "packages": [{"cell_depth": 330, "cell_width": 110, "cell_height": 350, "number_place": "1", "barcode_place": "[ITM]000145328564"}], "cell_type": "5", "payer_num": "ИМ-РФ-БСА-307", "order_type": 5, "seller_name": "\"\"Максимова Ирина Владимировна\"\", Индивидуальный предприниматель", "sender_name": "\"\"Максимова Ирина Владимировна\"\"", "client_order": False, "order_number": 1305958239, "recipient_sign": "Анна Сергушкина", "request_number": "№316528", "recipient_phone": "+79296594763", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145328564", "1"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "13c21298-a5a0-4d0e-93f2-d582deb8a2c0", "price": 2996.0, "barcode": "[CDK]1305965632", "currency": 30, "packages": [{"cell_depth": 510, "cell_width": 310, "cell_height": 80, "number_place": "240061082060", "barcode_place": "[ITM]000145336537"}], "cell_type": "5", "payer_num": "ИМ-РФ-ГЛ-18838", "device_uid": "b0212402-9e6e-4893-9ee1-c63a7a01db96", "order_type": 5, "seller_name": "Faktor", "sender_name": "\"Бета Про\"", "client_order": False, "order_number": 1305965632, "recipient_sign": "наталья данилина", "request_number": "240061082060", "recipient_phone": "79031343427", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145336537", "240061082060", "[ITM]000145336537"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 446", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "ed09e288-4e14-40b8-8176-515baf618f7a", "price": 0.0, "barcode": "[CDK]1306050402", "packages": [{"cell_depth": 300, "cell_width": 240, "cell_height": 170, "number_place": "1", "barcode_place": "[ITM]000145427819"}], "cell_type": "5", "payer_num": "ИМ-РФ-НКИ-115", "order_type": 5, "seller_name": "интернет-магазин", "sender_name": "\"Ладный Сад\"", "client_order": False, "order_number": 1306050402, "recipient_sign": "Романов Арсений Дмитриевич", "request_number": "3007", "recipient_phone": "+79963249781", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145427819", "1"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "e150e0a9-8af5-4542-b37f-4c27f52f9444", "price": 0.0, "barcode": "[CDK]1306205008", "packages": [{"cell_depth": 560, "cell_width": 50, "cell_height": 50, "number_place": "1", "barcode_place": "[ITM]000145591574"}], "cell_type": "5", "payer_num": "ИМ-РФ-ГЛ-15132", "device_uid": "5c7c50f1-3cac-49a0-a463-2f28f4ae3b22", "order_type": 5, "seller_name": "ООО  \"АС-Энергосервис\"", "sender_name": "«АС-Энергосервис»", "client_order": False, "order_number": 1306205008, "recipient_sign": "Воронина Юлия Владимировна", "request_number": "119, упд 4", "recipient_phone": "79166952006", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145591574", "1", "[ITM]000145591574"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 601", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "33127797-759a-4d3e-8c47-4420f7ecba42", "price": 0.0, "barcode": "[CDK]1306205790", "packages": [{"cell_depth": 510, "cell_width": 330, "cell_height": 130, "number_place": "1", "barcode_place": "[ITM]000145592392"}], "cell_type": "5", "payer_num": "КУ-РФ-БСЧ-32", "order_type": 5, "sender_name": "Кондрашева Ольга Олеговна-", "client_order": False, "order_number": 1306205790, "recipient_sign": "Филиппова Елена Вячеславовна", "request_number": "1306205790", "recipient_phone": "+79219478296", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145592392", "1"]}	,"response_data":	{"ids": "required_one_field", "data": 'null', "extra": {}, "message": "One of this fields '('device_id', 'device_uid', 'point_code')' is required", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "bf8fafba-db7d-4ffe-baf8-3e599f7eb9e6", "price": 9180.0, "barcode": "[CDK]1306263757", "currency": 30, "packages": [{"cell_depth": 530, "cell_width": 320, "cell_height": 100, "number_place": "1", "barcode_place": "[ITM]000145655266"}], "cell_type": "5", "payer_num": "ИМ120082", "device_uid": "4cdd8dff-923e-47dc-a2a1-c5eb63e2d391", "order_type": 5, "seller_name": "СЛАВЯНКА", "sender_name": "СЛАВЯНКА", "client_order": False, "order_number": 1306263757, "recipient_sign": "Щербаков Евгений Фёдорович", "request_number": "2914", "recipient_phone": "79052120337", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145655266", "1", "[ITM]000145655266"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 19", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "71193411-3eb2-4bea-88fd-8d09a389f957", "price": 2539.0, "barcode": "[CDK]1306282655", "currency": 30, "packages": [{"cell_depth": 520, "cell_width": 280, "cell_height": 140, "number_place": "1", "barcode_place": "[ITM]000145676024"}], "cell_type": "5", "payer_num": "ИМ4294973471", "device_uid": "678f45aa-3cd2-45cf-a117-b4093aeca051", "order_type": 5, "seller_name": "Деан СБ", "sender_name": "\"\"ДЕАН СБ\"\"", "client_order": False, "order_number": 1306282655, "recipient_sign": "Джафарджон +7903284-66-50", "request_number": "СВ00-000051", "recipient_phone": "79032846650", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145676024", "1", "[ITM]000145676024"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 538", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "cda96969-c637-419c-a798-a4513873b3ec", "price": 530.0, "barcode": "[CDK]1306341185", "currency": 30, "packages": [{"cell_depth": 600, "cell_width": 450, "cell_height": 50, "number_place": "1", "barcode_place": "[ITM]000145739887"}], "cell_type": "5", "payer_num": "ИМ-РФ-МОР-22", "device_uid": "0d5b2c82-6d1d-45f5-922c-0db9b6b8e57c", "order_type": 5, "seller_name": "Загидуллин Вадим Хамитович", "sender_name": "Загидуллин Вадим Хамитович", "client_order": False, "order_number": 1306341185, "recipient_sign": "Шумский Павел", "request_number": "1220", "recipient_phone": "79160702097", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145739887", "1", "[ITM]000145739887"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 544", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "d898507f-4e3d-449f-ab22-58db791b1fbf", "price": 0.0, "barcode": "[CDK]1306360950", "packages": [{"cell_depth": 530, "cell_width": 100, "cell_height": 130, "number_place": "24004062575", "barcode_place": "[ITM]000145761318"}], "cell_type": "5", "payer_num": "ИМ-РФ-ТПЗ-86", "device_uid": "96c71922-135d-4db0-baa1-c2b2328a5aa7", "order_type": 5, "seller_name": "La Roche Posay", "sender_name": "Laroche Posay", "client_order": False, "order_number": 1306360950, "recipient_sign": "Дарья Ермилова", "request_number": "0087363704", "recipient_phone": "79111976349", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145761318", "24004062575", "[ITM]000145761318"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 99", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "2e95693f-8ba8-48a5-aa2d-dcc91abc1de0", "price": 2459.0, "barcode": "[CDK]1306471624", "currency": 30, "packages": [{"cell_depth": 160, "cell_width": 540, "cell_height": 90, "number_place": "3424843-1090618-1", "barcode_place": "[ITM]000145877772"}], "cell_type": "5", "payer_num": "ИМ-РФ-ГЛ-13060", "device_uid": "d7d2531b-884d-4154-b7c7-869b5589d0c8", "order_type": 5, "seller_name": "meleon.ru", "sender_name": "\"Васт\"", "client_order": False, "order_number": 1306471624, "recipient_sign": "БЕЛЯНИНА НАТАЛЬЯ", "request_number": "3424843-1090618", "recipient_phone": "79161771539", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145877772", "3424843-1090618-1", "[ITM]000145877772"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 827", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "eb87a23d-acb2-4058-a58b-16150ff2a850", "price": 2818.54, "barcode": "[CDK]1306556462", "currency": 30, "packages": [{"cell_depth": 460, "cell_width": 460, "cell_height": 50, "number_place": "240061132514", "barcode_place": "[ITM]000145970339"}], "cell_type": "5", "payer_num": "ИМ12358616", "device_uid": "1b475a69-1135-432c-bdb7-74219d869edc", "order_type": 5, "seller_name": "HSR", "sender_name": "ХОМ ШОППИНГ РАША", "client_order": False, "order_number": 1306556462, "recipient_sign": "ГРИГОРЯН АРТАШЕС ГЕНРИКОВИЧ", "request_number": "240061132514", "recipient_phone": "79684441226", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145970339", "240061132514", "[ITM]000145970339"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 870", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "e918f7ff-56a7-4514-9fab-bf867b9d902c", "price": 0.0, "barcode": "[CDK]1306574652", "packages": [{"cell_depth": 600, "cell_width": 120, "cell_height": 260, "number_place": "1", "barcode_place": "[ITM]000145990339"}], "cell_type": "5", "device_uid": "c08102cf-4450-4294-8a02-791f4a3c24d8", "order_type": 5, "sender_name": "Коледова - Наталья Сергеевна", "client_order": False, "order_number": 1306574652, "recipient_sign": "Потапов Николай Владимирович", "request_number": "1306574652", "recipient_phone": "79653644952", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000145990339", "1", "[ITM]000145990339"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 584", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "9ec92421-99f4-4ee7-b04f-c994c25c0ecc", "price": 0.0, "barcode": "[CDK]1306635581", "packages": [{"cell_depth": 640, "cell_width": 80, "cell_height": 80, "number_place": "2588488#1003817838", "barcode_place": "[ITM]000146056631"}], "cell_type": "5", "payer_num": "ИМ-РФ-СНЯ-421", "device_uid": "c1083ab8-433a-468b-81fc-16914e46a446", "order_type": 5, "seller_name": "Геосемантика, ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ", "sender_name": "Геосемантика", "client_order": False, "order_number": 1306635581, "recipient_sign": "Akhror Asilkhodjaev", "request_number": "1003817838", "recipient_phone": "79817915133", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000146056631", "2588488#1003817838", "[ITM]000146056631"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 25", "success": False, "status_code": 400}	},
{"request_data":	{"guid": "be17c397-fedb-46df-bcac-f6ac496044e9", "price": 0.0, "barcode": "[CDK]1306691054", "packages": [{"cell_depth": 600, "cell_width": 160, "cell_height": 100, "number_place": "1", "barcode_place": "[ITM]000146114738"}], "cell_type": "5", "payer_num": "ИМ1215311", "device_uid": "3b30cc33-75e5-4566-b643-2c1ede8f02e3", "order_type": 5, "seller_name": "ИП Цветкова Л.Ю.", "sender_name": "ЦВЕТКОВА ЛАРИСА ЮРЬЕВНА", "client_order": False, "order_number": 1306691054, "recipient_sign": "Юлия Артамонова", "request_number": "10013358", "recipient_phone": "79035809303", "client_system_id": "CDEK", "additional_barcodes": ["[ITM]000146114738", "1", "[ITM]000146114738"]}	,"response_data":	{"ids": "no_active_cells", "data": 'null', "extra": {}, "message": "There are no active cells of suitable size in the device 572", "success": False, "status_code": 400}	},

]


