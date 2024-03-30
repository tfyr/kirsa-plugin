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

ooo_dionis_smelovsk = {
            'ClientRegId': '030000834218',
            'INN': '0201014099',
            'KPP': '745645003',
            'FullName': 'Общество с ограниченной ответственностью "Дионис"',
            'ShortName': 'ООО "Дионис"',
            'address': {
                'Country': '643',
                'RegionCode': '74',
                'description': 'Россия, Челябинская Область, Верхнеуральский Район, , Смеловский Поселок, Первомайский Переулок, 8А,, '
            },
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
    def __test_write_off_v3(self,):
        utm_url = 'http://tupak48:8080'
        fsrar_id = get_fsrar_id(utm_url)
        positions = [
            {'quantity': 2, 'F2RegId': 'FB-000003679121459', 'marks': ['177400451244141018001CRVEMPFAI6UUPWCTXHVETPWSEU3LGOUYBLN33RX7BKTEDMJZHKHJC5LP4A7LBD2VCHPXPTAVLHWREQEOTND4RSZJZMV6CMAY6WPMKF3KK5Y5HFY3L2FZAWY6GN7DKVRBA','177400451244171018001YEPLFSA5IXUV6CELI22FY5YMDIC5HBYAOTG3QNICZLASN7XNMYYW6FE4MZIFY5E4Z7BXPUPH4WIG6LVXOE2P235TPI2P2VGKXRMNIV363FIXBHTYPONZG3Q3DSOCACIYA']},
            {'quantity': 4, 'F2RegId': 'FB-000003679121458', 'marks': [
                '177400451594241018001S7TWAZ5FABVN3IHY3F5K5E5G6APBSK3HPFWWIEPZDWK5ZOWG7I5VKBKE7TQQE3FVCSZSA2A6HKPVRPWZJTIRX67GX4DGHPGTX6PB7ZTREPBDEMVFRVWSYKMJWLJUIGPEQ',
                '177400451594191018001XNQMCKAQGWFIRPBD24IGPYGWIYJJD7GLLFPQF4TZ4CHDT6OZVUMEAKEWCO2V4NHRTEPVYSGXAPIO23PL2NRWZJVHK4HT3SRQNZU7XC7QTIBAXHB6VPL67PA5QEMFAIQMQ',
                '177400451594221018001FD45RP23IJAP7YWZSBDHCMO54YQJHHW3BXWZMUOM3L3CA42EIW7SBJEFGKUNCFSDVCPM4KMMUY7HAGBKTKEOHHXTV7GL4MUCVWHYTIPYUF5Q2DRE7LDLF26N75TIY3IWI',
                '177400451594401018001CWJST3Y636HNDEQJEHC5Y6OZVQA742QUF6VOU34SJB7LUKUJJ4BIY5JED675UAJAE4OEMJRKTPQ4TNIXMJ3YDUOFVR3FOUP2YZTYE46Y4A6W24OZNFU6WOZFAR35BMOFQ']},
            # {'quantity': 1, 'F2RegId': '', 'marks': ['']},
        ]
        write_off_v3(utm_url, fsrar_id, positions, "5")


class TestWaybill4(unittest.TestCase):
    def test_waybill_v4(self,):
        positions = [
            {
                'quantity': 2,
                'price': 790.00,
                'FARegId': 'FA-000000043893816',
                'F2RegId': 'FB-000003552832754',
                'AlcCode': '0116116000002544848',
                'Capacity': '0.5000',
                'AlcVolume': '40.000',
                'ProductVCode': '237',
                #'Producer': ''
                # <pref:Producer><oref:UL xmlns:pref="http://fsrar.ru/WEGAIS/ProductRef_v2" xmlns:oref="http://fsrar.ru/WEGAIS/ClientRef_v2" xmlns:rst="http://fsrar.ru/WEGAIS/ReplyRests_v2" xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><oref:ClientRegId>010000000539</oref:ClientRegId><oref:INN>1681000049</oref:INN><oref:KPP>165902005</oref:KPP><oref:FullName>Акционерное общество "Татспиртпром"</oref:FullName><oref:ShortName>АО филиал АО "Татспиртпром" "Vigrosso"</oref:ShortName><oref:address><oref:Country>643</oref:Country><oref:RegionCode>16</oref:RegionCode><oref:description>РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Учительская ул,5,,</oref:description></oref:address></oref:UL></pref:Producer>
            },
        ]
        shipper = ooo_dionis
        consignee = ooo_dionis_smelovsk

        transport = {
            'TRAN_TYPE': 'Автомобиль',
            'TRANSPORT_TYPE': 'car',
            'TRAN_COMPANY': 'ООО "Дионис", ИНН/КПП: 0201014099/745645002',
            'TRANSPORT_REGNUMBER': 'Лада Ларгус, е885ху174',
            'TRAN_CUSTOMER': 'ООО "Дионис"',
            'TRAN_DRIVER': 'Палагутин И.В.',
            'TRAN_LOADPOINT': 'Башкортостан Республика, Абзелиловский Район, , Ташбулатово Село, Центральная Улица, 17,',
            'TRAN_UNLOADPOINT': 'Россия, Челябинская Область, Верхнеуральский Район, , Смеловский Поселок, Первомайский Переулок, ,, ',
            'TRAN_FORWARDER': 'Палагутин И.В.',
        }

        utm_url = 'http://localhost:8080'
        fsrar_id = get_fsrar_id(utm_url)
        waybill_v4(utm_url, fsrar_id, shipper, consignee, transport, positions, "19", 'Перемещение')


class TestEgaisAction(unittest.TestCase):
    def __test_send_rest_bcode(self, ):
        get_actions(fsrar_id='030000543922', url="http://localhost:8015/file/", utm_url='http://localhost:8082')

    def __test_x(self):
        params = {'fsrar_id': '030000543922', 'action': 'store_sign', 'id': 1, 'transport_id': '90813081-144c-4512-aa28-972f61f8a90d', 'sign': '4DC19C9C13A67E277BB81EBA3577629244522657CC89A171EB2AC85F2B84753B05C7BA2BF0E84C40EA3B7FD145F2B9B2612BEFC3249C70CEB70993D6C97293C2'}
        q = requests.post("http://localhost:8015/file/", params=params)

class TestAct4(unittest.TestCase):
    def __test_act4(self,):
        utm_url = 'http://localhost:8080'
        fsrar_id = get_fsrar_id(utm_url)
        act4(utm_url, fsrar_id, 'TTN-0708990547', False)

# params = {'fsrar_id': fsrar_id, 'action': 'get_actions'}
# q = requests.post("https://kirsa.9733.ru/file/", params=params)
# assert q.status_code == 200

if __name__ == "__main__":
    unittest.main()