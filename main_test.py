import unittest

import requests

from egais import get_actions, act4, write_off_shop_v2, write_off_v3, waybill_v4, get_fsrar_id

ooo_dionis = {
            'ClientRegId': '030000687073',
            'INN': '0201014099',
            'KPP': '745645002',
            'FullName': 'Общество с ограниченной ответственностью "Дионис"',
            'ShortName': 'ООО "Дионис"',
            'address': {
                'Country': '643',
                'RegionCode': '74',
                'description': 'Россия, 455000, Челябинская обл, г. Магнитогорск, ул. Автомобилистов, д. 8г'
            }
        }

class TestSum(unittest.TestCase):
    def __test_send_waybill(self, ):
        files = dict()
        #f = open('data/TTN-0557370828.xml', 'r')
        #files["Waybill_v4"] = f.read()
        #f.close()

        #f = open('data/TTN-0557370828-history.xml', 'r')
        #files["History_v4"] = f.read()
        #f.close()

        f = open('data/FORM2REGINFO.xml', 'r')
        files["FORM2REGINFO"] = f.read()
        f.close()

        params = {'fsrar_id': 'test'}
        q = requests.post("http://localhost:8015/file/",
                          files=files,
                          params=params)
        assert q.status_code == 200

    def __test_send_rest_bcode(self, ):
        files = dict()
        f = open('data/bc/560-ReplyRestBCode-aaab822b-18d9-40f1-aa4a-ef5f720c9f6a', 'r')
        files["FORM2REGINFO"] = f.read()
        f.close()
        params = {'fsrar_id': 'test'}
        q = requests.post("http://localhost:8015/file/",
                          files=files,
                          params=params)
        assert q.status_code == 200


class TestWriteOffShop2(unittest.TestCase):
    def __test_write_off_shop_v2(self,):
        positions=[
            {
                'quantity': 1,
                'FullName': 'Игристое вино полусладкое розовое «Российское золотое» 0.75',
                'AlcCode': "0000000000041745989",
                'AlcVolume': "11.5",
                'Capacity': "0.75",
                'ProductVCode': "440",
                'marks': ['193401585069831021001N7XTLMMGOBBVBK4MB3XDOKJ5YESYMDUL2CNIJGR7CRAW6PT3MBPH6XCCMD6JZ4IIALFMAKSJ7ZVJSAPZ6LUJMOO3V5SH5VNJ2MPIQKLSBSXKAZLA6LPODQXEYTR5K5DOY',]
            }
        ]
        write_off_shop_v2('http://izvekova:8080', '030000776423', positions)


class TestWriteOff3(unittest.TestCase):
    def test_write_off_v3(self,):
        utm_url = 'http://oct2:8080'
        fsrar_id = get_fsrar_id(utm_url)
        positions = [
            {'quantity': 1, 'F2RegId': 'FB-000004727570128', 'marks': ['195300812040111120001KVU3U2TFREGVNZHXQPTXWON63UIYJFIZUOYXH45HDQ7DWB7KBTF5BGKUE3D4DZQ6SFBYYJ6EL5LBBND3RJD3KGQTA52FP2AJD63CIKNJ3TE5E6XYSA3NPXHFUDJQ24QUA']},
            {'quantity': 1, 'F2RegId': 'FB-000006591634712', 'marks': ['197405643938091222001JL6TGLUSEK7HUUNIROF7M4G2EY3IFRBI2HBU524T4AHJFQH2XGTFI4FZYVKAMDULCYCQA2G4GN4PGYKH7OV4OL3BDBV33X5RDE2ESDVQAZIX6HX2N7TMYPNBQTHNKGQSY']},
            {'quantity': 1, 'F2RegId': 'FB-000006591634722', 'marks': ['187319692723690623001GSMPCEPHFZV3DJSYJW3LYKLCAU6Z5J23HNXCEEVOX7UNENIYWPAYA4ZUJGMNL7SLG33PKTB22T4PY2L2NBEG6HVV255NJ3LF6AFPYFNJK3JHZIB3XXFUE43A42HFAMYPA']},
            # {'quantity': 1, 'F2RegId': '', 'marks': ['']},
        ]
        write_off_v3(utm_url, fsrar_id, positions, "2")


class TestWaybill4(unittest.TestCase):
    def __test_waybill_v4(self,):
        positions = [
            {
                'quantity': 240,
                'price': 53.50,
                'FARegId': 'FA-000000049132760',
                'F2RegId': 'FB-000005018983051',
            },
            {
                'quantity': 120,
                'price': 53.00,
                'FARegId': 'FA-000000052088878',
                'F2RegId': 'FB-000006359834334',
            },
            {
                'quantity': 120,
                'price': 53.50,
                'FARegId': 'FA-000000052220381',
                'F2RegId': 'FB-000006493875295',
            },
        ]
        shipper = ooo_dionis
        consignee = {
            'ClientRegId': '030000729849',
            'INN': '742801598687',
            'KPP': '',
            'FullName': 'ИП Аюпова Ирина Николаевна',
            'ShortName': 'ИП Аюпова Ирина Николаевна',
            'address': {
                'Country': '643',
                'RegionCode': '74',
                'description': 'Россия, 455000, Челябинская обл, г. Магнитогорск, ул. Ворошилова, д. 9а'
            },
        }

        transport = {
            'TRAN_TYPE': 'Автомобиль',
            'TRANSPORT_TYPE': 'car',
            'TRAN_COMPANY': 'ООО "Дионис", ИНН/КПП: 0201014099/745645002',
            'TRANSPORT_REGNUMBER': 'Лада Ларгус, е885ху174',
            'TRAN_CUSTOMER': 'ООО "Дионис"',
            'TRAN_DRIVER': 'Палагутин И.В.',
            'TRAN_LOADPOINT': '643,455000,74,,МАГНИТОГОРСК Г,,АВТОМОБИЛИСТОВ УЛ,8Г,,',
            'TRAN_UNLOADPOINT': 'Россия, 455000, Магнитогорск, ул. Ворошилова 9а',
            'TRAN_FORWARDER': 'Палагутин И.В.',
        }

        waybill_v4('http://localhost:8080', '030000687073', shipper, consignee, transport, positions, "18", 'Договор №101 от 05.01.2024')


class TestEgaisAction(unittest.TestCase):
    def __test_send_rest_bcode(self, ):
        get_actions(fsrar_id='030000543922', url="http://localhost:8015/file/", utm_url='http://localhost:8082')

    def __test_x(self):
        params = {'fsrar_id': '030000543922', 'action': 'store_sign', 'id': 1, 'transport_id': '90813081-144c-4512-aa28-972f61f8a90d', 'sign': '4DC19C9C13A67E277BB81EBA3577629244522657CC89A171EB2AC85F2B84753B05C7BA2BF0E84C40EA3B7FD145F2B9B2612BEFC3249C70CEB70993D6C97293C2'}
        q = requests.post("http://localhost:8015/file/", params=params)

class TestAct4(unittest.TestCase):
    def __test_act4(self,):
        act4('http://oct2:8080', '030000502187', 'TTN-0698489259', True)

# params = {'fsrar_id': fsrar_id, 'action': 'get_actions'}
# q = requests.post("https://kirsa.9733.ru/file/", params=params)
# assert q.status_code == 200

if __name__ == "__main__":
    unittest.main()