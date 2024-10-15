import json
import unittest
from time import sleep

import requests

from egais import get_actions, act4, write_off_shop_v2, write_off_v3, waybill_v4, get_fsrar_id, query_bcode

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

ooo_dionis_tashb = {
            'ClientRegId': '030000543922',
            'INN': '0201014099',
            'KPP': '020145006',
            'FullName': 'Общество с ограниченной ответственностью "Дионис"',
            'ShortName': 'ООО "Дионис"',
            'address': {
                'Country': '643',
                'RegionCode': '02',
                'description': 'Башкортостан Республика, Абзелиловский Район, , Ташбулатово Село, Центральная Улица, 17,,'
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
        utm_url = 'http://localhost:8088'
        fsrar_id = get_fsrar_id(utm_url)
        positions = [
            {'quantity': 51,
             'F2RegId': 'FB-000006638627341',
             'marks': [
                    '',
                ]
             },
            # {'quantity': 1, 'F2RegId': '', 'marks': ['']},
        ]
        write_off_v3(utm_url, fsrar_id, positions, "12")


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
                'FullName': 'Купажированный виски "GLEN RIVERS"',
                'ShortName': 'Купажированный виски "GLEN RIVERS"',
                'marks': [
                    '103400566296331018001LSHQAPAIIJ7JTBRDJBHNCTPLQI3GBWDBKOXO6YRSZMTSKCTWH4QVGJS5XQ6V3I7VEK73L3WXPCJT5RVDFAERVPPV63665E5QAK5BTT7Q6E4F3DUTCIC7GMKGUDBYZ6H6I',
                    '103400566296481018001NE7FFWLD7MML7QCVOYBG5KAQPI5M6ADV6TVK7SZ2WLX7RFFJH3LVH5VDN4XSYF5MD5BYFRBAHJ2OVL7SZUKEFGH3RZCDGYUUYHXEO7EVH53KR3N4KA5XP7MWCD3QGTY3A',
                ],
                'Producer': {
                    'UL': {
                        'ClientRegId': '010000000539',
                        'INN': '1681000049',
                        'KPP': '165902005',
                        'FullName': 'Акционерное общество "Татспиртпром"',
                        'ShortName': 'АО филиал АО "Татспиртпром" "Vigrosso"',
                        'address': {
                            'Country': '643',
                            'RegionCode': '16',
                            'description': 'РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Учительская ул,5,,',
                        },
                    }
                }
            },
        ]
        shipper = ooo_dionis_tashb
        consignee = ooo_dionis_smelovsk

        transport = {
            'TRAN_TYPE': 'Автомобиль',
            'TRANSPORT_TYPE': 'car',
            'TRAN_COMPANY': 'ООО "Дионис", ИНН/КПП: 0201014099/745645002',
            'TRANSPORT_REGNUMBER': 'Лада Ларгус, е885ху174',
            'TRAN_CUSTOMER': 'ООО "Дионис"',
            'TRAN_DRIVER': 'Палагутин И.В.',
            'TRAN_LOADPOINT': 'Башкортостан Республика, Абзелиловский Район, , Ташбулатово Село, Центральная Улица, 17,,',
            'TRAN_UNLOADPOINT': 'Россия, Челябинская Область, Верхнеуральский Район, , Смеловский Поселок, Первомайский Переулок, ,, ',
            'TRAN_FORWARDER': 'Палагутин И.В.',
        }

        waybill_v4('http://localhost:8088', '030000687073', shipper, consignee, transport, positions, "19", 'Договор №102 от 16.07.2024')


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
        act4(utm_url, fsrar_id, 'TTN-0725910955', False)

# params = {'fsrar_id': fsrar_id, 'action': 'get_actions'}
# q = requests.post("https://kirsa.9733.ru/file/", params=params)
# assert q.status_code == 200

class TestQueryBCode(unittest.TestCase):
    def __test_query_bcode(self,):
        utm_url = 'http://oct2:8080'
        query_bcode(utm_url, fsrar_id=get_fsrar_id(utm_url), fb='FB-000005196978883')

if __name__ == "__main__":
    unittest.main()

    done= [
'FB-000005097843687',
'FB-000005097843683',
'FB-000005097843686',
'FB-000005097843684',
'FB-000005097843685',
'FB-000005725925993',
'FB-000005725925994',
'FB-000005195995165',
'FB-000005195995166',
'FB-000005195995167',
'FB-000005195995168',
'FB-000006326145806',
'FB-000006326326128',
]

    s2 = [
        'FB-000006326145806',
        'FB-000006448947766',
        'FB-000006581796434',
        'FB-000006581796442',
        'FB-000006581796447',
        'FB-000006581796454',
        'FB-000006742011793',
        'FB-000006741950939',
        'FB-000006741946704',
        'FB-000006741946705',
        'FB-000006774122354',
        'FB-000006774122355',
        'FB-000006774122356',
        'FB-000006774122367',
        'FB-000006902910251',
        'FB-000006902910255',
        'FB-000006902910268',
        'FB-000006902910270',
        'FB-000006902985135',
        'FB-000006902985149',
        'FB-000006905493712',
        'FB-000004529205520',
        'FB-000004675943570',
        'FB-000006448947575',
        'FB-000006448947786',
        'FB-000006448947793',
        'FB-000006449431037',
        'FB-000006581719750',
        'FB-000006581796436',
        'FB-000006581796446',
        'FB-000006581796448',
        'FB-000006638627336',
        'FB-000006741950945',
        'FB-000006741946703',
        'FB-000006741946731',
        'FB-000006741785332',
        'FB-000006774122357',
        'FB-000006774122368',
        'FB-000006902910263',
        'FB-000006902910267',
        'FB-000006902910276',
        'FB-000006902985139',
        'FB-000006638627324',
        'FB-000004519295886',
        'FB-000004519295916',
        'FB-000004521474958',
        'FB-000004521474966',
        'FB-000004630593269',
        'FB-000004661131795',
        'FB-000004678493953',
        'FB-000004683394023',
        'FB-000004683394029',
        'FB-000004683394032',
        'FB-000004708614069',
        'FB-000004708614070',
        'FB-000004708614076',
        'FB-000004743706592',
        'FB-000004775642733',
        'FB-000004778419925',
        'FB-000004778419930',
        'FB-000004832365062',
        'FB-000004860380914',
        'FB-000004860380917',
        'FB-000004863781851',
        'FB-000005164416267',
        'FB-000005169197290',
        'FB-000005186655581',
        'FB-000005186655582',
        'FB-000005186655587',
        'FB-000005186468008',
        'FB-000005275731142',
        'FB-000005545553060',
        'FB-000005726155959',
        'FB-000005864453490',
        'FB-000005921900087',
        'FB-000006160499102',
        'FB-000006160557193',
        'FB-000006165418426',
        'FB-000006325973306',
        'FB-000006326145800',
        'FB-000006326145822',
        'FB-000006326152505',
        'FB-000006448947568',
        'FB-000006448947774',
        'FB-000006448947788',
        'FB-000006449431098',
        'FB-000006458732363',
        'FB-000006581719751',
        'FB-000006581719762',
        'FB-000006581719770',
        'FB-000006582005556',
        'FB-000006581922757',
        'FB-000006581796438',
        'FB-000006581796445',
        'FB-000006742011792',
        'FB-000006741950892',
        'FB-000006741950903',
        'FB-000006741950938',
        'FB-000006741950942',
        'FB-000006741950948',
        'FB-000006741946688',
        'FB-000006741946719',
        'FB-000006741946724',
        'FB-000006741946730',
        'FB-000006741946732',
        'FB-000006774122351',
        'FB-000006774122358',
        'FB-000006774122359',
        'FB-000006774122365',
        'FB-000006902910252',
        'FB-000006902910253',
        'FB-000006902910256',
        'FB-000006902910277',
        'FB-000006902985136',
    ]
    utm_url = 'http://localhost:8088'
    fsrar_id = get_fsrar_id(utm_url)
#    for s in s2:
#        print(s)
#        query_bcode(utm_url, fsrar_id=fsrar_id, fb=s)
#        sleep(60*35)

