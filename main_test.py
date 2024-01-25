import unittest

import requests

from egais import get_actions, act4, write_off_shop_v2, write_off_v3, waybill_v4


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
    def __test_write_off_v3(self,):
        positions = [
            {
                'quantity': 2,
                'F2RegId': 'FB-000006385720362',
                'marks': ['187417658630031222001ZTVYMWSS7LG3TFN3AQ5YW7VMHMETWDBL7GSWLLEOIJ47RFT7ZGCWUSOMGYFEMDCKWNOIOF52LIBFEIEUPQ23XVTRIGO5NJP4ZELZJK3EUHSJXMUAFS2CQNUXGV6O4PO3Q',
                          '187417658627461222001S2OCX35T2T2L4VBJGLQOJEBT7IE56AOYNKWCLWBTBA2NMRDAOSVN7C54DNHSRGC23FAWXWXB3H75HYHGZ2GKY3BD37HA23LGOZPOOFSQKOP4HQHLKCZQIMOSJ6DMMHT7A']
            }
        ]
        write_off_v3('http://tasht:8080', '030000555605', positions, "18")


class TestWaybill4(unittest.TestCase):
    def test_waybill_v4(self,):
        positions = [
            {
                'quantity': 2,
                'F2RegId': 'FB-000006385720362',
            }
        ]
        waybill_v4('http://tasht:8080', '030000555605', positions, "18")


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