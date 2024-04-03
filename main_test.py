import json
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

        utm_url = 'http://10.252.1.5:8080'
        fsrar_id = get_fsrar_id(utm_url)

        s = ''' 
[
    {
        "price": "392.00",
        "FARegId": "FA-000000043973836",
        "F2RegId": "FB-000003054100656",
        "AlcCode": "3771014000001260255",
        "Capacity": "0.700",
        "AlcVolume": "12.000",
        "ProductVCode": "405",
        "FullName": "Вино защищенного наименования места происхождения региона Кахетия сухое белое \\\"Цинандали\\\" серии \\\"AKAURI\\\"",
        "ShortName": null,
        "marks": [
            "22N0000SNEWWBTKKQFZ8TQE90131017000829N5T3GJAHXI1TQX5N5772VWJCJDEEVF1"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "268",
                    "description": "1509 , Грузия , село Карденахи , Гурджаанский район"
                },
                "ClientRegId": "050000046727",
                "FullName": "ООО \\\"Шалвино\\\"",
                "ShortName": "ООО \\\"Шалвино\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "420.00",
        "FARegId": "FA-000000043677383",
        "F2RegId": "FB-000003454242101",
        "AlcCode": "3771014000001260264",
        "Capacity": "0.700",
        "AlcVolume": "13.000",
        "ProductVCode": "403",
        "FullName": "Вино столовое сухое красное \\\"САПЕРАВИ\\\" серии \\\"AKAURI\\\"",
        "ShortName": null,
        "marks": [
            "22N0000SNEWWBTKKQG88TQE90528006000697H1H9S2429IHA6MWWW0QGYS655L3VSGQ",
            "22N0000SNEWWBTKKQG88TQE905280060012632ZAZRPCBZMJ8RYLROXZIEYMMMC2KDCJ"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "268",
                    "description": "1509 , Грузия , село Карденахи , Гурджаанский район"
                },
                "ClientRegId": "050000046727",
                "FullName": "ООО \\\"Шалвино\\\"",
                "ShortName": "ООО \\\"Шалвино\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "286.00",
        "FARegId": "FA-000000039032759",
        "F2RegId": "FB-000003454242102",
        "AlcCode": "0377162000002933307",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "404",
        "FullName": "Вино защищенного географического указания полусладкое красное регион Кастилья, категория VdT \\\"Меса Де Мундо\\\"",
        "ShortName": null,
        "marks": [
            "22N00002V5ORQU7HEEZ830Q70726008010856SZDN9TPRXF3MX44777KQQCV45806B0F"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "724",
                    "description": "Пасео Кастелар, 70, 13730 Санта Крус Де Мудела (Сьюдад Реаль), Испания"
                },
                "ClientRegId": "050000006900",
                "FullName": "\\\" Бодегас Фернандо Кастро, С.Л.\\\"",
                "ShortName": "Бодегас Фернандо"
            }
        },
        "quantity": 1
    },
    {
        "price": "240.00",
        "FARegId": "FA-000000043389323",
        "F2RegId": "FB-000003480924185",
        "AlcCode": "0017418000004916807",
        "Capacity": "0.500",
        "AlcVolume": "20.000",
        "ProductVCode": "462",
        "FullName": "Напиток винный сладкий \\\"Коньячный со вкусом кофе и сливок\\\"",
        "ShortName": null,
        "marks": [
            "179400029874871018001WGHOTE6XSKW4LBSNJ2WMMCFVDIAPBM2KJUU4W2AZQH2Z6PYUOFK7PQ4L35WK3AZOMETGGGJIP25DO4JDOZV3ECAEWJUQB5EXXJHDNOT34ABKMXHFKFWBAAPSZFTSIYXMA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,454036,ЧЕЛЯБИНСКАЯ ОБЛ,,Челябинск г,,Радонежская ул,5,,",
                    "RegionCode": "74"
                },
                "INN": "7423012592",
                "KPP": "744801001",
                "ClientRegId": "010000000090",
                "FullName": "Общество с ограниченной ответственностью \\\"Центр пищевой индустрии-Ариант\\\"",
                "ShortName": "ООО \\\"ЦПИ-Ариант\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "390.00",
        "FARegId": "FA-000000045122726",
        "F2RegId": "FB-000003500521420",
        "AlcCode": "3771014000001260260",
        "Capacity": "0.700",
        "AlcVolume": "13.000",
        "ProductVCode": "403",
        "FullName": "Вино столовое полусладкое белое \\\"Алазанская долина\\\" серии \\\"AKAURI\\\"",
        "ShortName": null,
        "marks": [
            "236203755562571019001ZB4YKINGVDV72F5AWQGGH6WGXUOKAMJ7JYU7SMWRUKJH6MIPSNLDWQ2A4ANLSYXPQM4WTYPQZPK2JLKMSI7H33GIAW64KJEIA4ZXHVC2MIHXAYKM62BYQGNZHXAELEJEI"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "268",
                    "description": "1509 , Грузия , село Карденахи , Гурджаанский район"
                },
                "ClientRegId": "050000046727",
                "FullName": "ООО \\\"Шалвино\\\"",
                "ShortName": "ООО \\\"Шалвино\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "397.00",
        "FARegId": "FA-000000045122727",
        "F2RegId": "FB-000003500521421",
        "AlcCode": "3771014000001260262",
        "Capacity": "0.700",
        "AlcVolume": "13.000",
        "ProductVCode": "403",
        "FullName": "Вино столовое полусладкое красное \\\"Алазанская долина\\\" серии \\\"AKAURI\\\"",
        "ShortName": null,
        "marks": [
            "236203755587321019001HDAGLXXVACB2RJS3HW4TQNH6KY7CST6RHQNEG6G7KHL75DQNEUCZKYSU6WQSTBEDQ7I5KZJC3XDUX2HQS4L64QWCNZBWLPC3SQRXZUGQFEKV5SLB3EZTKEVKF7NLKQXWQ"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "268",
                    "description": "1509 , Грузия , село Карденахи , Гурджаанский район"
                },
                "ClientRegId": "050000046727",
                "FullName": "ООО \\\"Шалвино\\\"",
                "ShortName": "ООО \\\"Шалвино\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "733.00",
        "FARegId": "FA-000000042342029",
        "F2RegId": "FB-000003522262831",
        "AlcCode": "0177320000003146882",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "229",
        "FullName": "Армянский коньяк пятилетний \\\"Вершина Армении\\\"",
        "ShortName": null,
        "marks": [
            "22N00001CHYOZFR594Y3STK81213002006196EH7WB4N1YBL9R833BWQR2GXQAW0X2R5",
            "22N00001CHYOZFR594Y3STK8121300200620063JAIIZEE2OTWMQBHBSLM5ZCO8G5BXM"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "Республика Армения, 0607, марз Арарат, с. Арарат, Раффи 1/1"
                },
                "ClientRegId": "050000041292",
                "FullName": "Общество с ограниченной ответственностью \\\"Араратский винный завод\\\"",
                "ShortName": "Араратский винный завод"
            }
        },
        "quantity": 2
    },
    {
        "price": "723.00",
        "FARegId": "FA-000000042342028",
        "F2RegId": "FB-000003522262832",
        "AlcCode": "0177320000003146880",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "229",
        "FullName": "Армянский коньяк трехлетний \\\"Вершина Армении\\\"",
        "ShortName": null,
        "marks": [
            "22N00001CHYOZFR594W3STK81213001003284AI8V5AOVONFUDBREBRU9AJK9FSATICG",
            "22N00001CHYOZFR594W3STK812130010073351BUJOJ297URTUKMK28Z9KSI716XGT37"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "Республика Армения, 0607, марз Арарат, с. Арарат, Раффи 1/1"
                },
                "ClientRegId": "050000041292",
                "FullName": "Общество с ограниченной ответственностью \\\"Араратский винный завод\\\"",
                "ShortName": "Араратский винный завод"
            }
        },
        "quantity": 2
    },
    {
        "price": "1066.00",
        "FARegId": "FA-000000044120146",
        "F2RegId": "FB-000003569580630",
        "AlcCode": "0350397000001378839",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "229",
        "FullName": "Армянский коньяк пятилетний \\\"АрАрАт *****\\\"",
        "ShortName": null,
        "marks": [
            "203200734972641018001GB63KFSPGDAYMCYCD7GEI4TRBEXQYJNXS4MVLZGDWTMQX6UXIMOEQUNNYFESEZL4WM6G7B3BQ5MSUWMUHAZSFYJ3KVNMR6QFYDYW32ZFOQASXPOT7WVNUMOCRPH6Y2W5Q"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "Республика Армения, 0082, г. Ереван, проспект Адмирала Исакова, 2"
                },
                "ClientRegId": "050000030065",
                "FullName": "ЗАО \\\"Ереванский Коньячный Завод\\\"",
                "ShortName": "ЗАО \\\"Е.К.З\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "221.00",
        "FARegId": "FA-000000042493263",
        "F2RegId": "FB-000003603012431",
        "AlcCode": "0012315000002094346",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "461",
        "FullName": "Напиток винный замутненный газированный сладкий \\\"АВИНО РОЗЕ\\\"/\\\"AVINO ROSE\\\"",
        "ShortName": null,
        "marks": [
            "177400451816681018001LI4DBSGUQN5EEKJGZV7CUPFLVEQF4XRIDTRPRJBFSUBV2DWV3L6TDGPQ64DLDEV5EB27422BXWPF5J6SXIAUD5GDTRPT7X4WATSDMSP5SV3D5IHID4TSBUGYZ6LS3ZJAA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,353468,КРАСНОДАРСКИЙ КРАЙ,,Геленджик г,,Солнечная ул,2,,",
                    "RegionCode": "23"
                },
                "INN": "2304042422",
                "KPP": "230401001",
                "ClientRegId": "010000000170",
                "FullName": "Закрытое акционерное общество \\\"Алкогольно-производственная компания \\\"Геленджик\\\"",
                "ShortName": "ЗАО АПК \\\"Геленджик\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "216.00",
        "FARegId": "FA-000000045691044",
        "F2RegId": "FB-000003811103032",
        "AlcCode": "0000000000038059371",
        "Capacity": "0.750",
        "AlcVolume": "11.500",
        "ProductVCode": "440",
        "FullName": "Игристое вино брют белое \\\"Ариант\\\"",
        "ShortName": null,
        "marks": [
            "173400968103871018001OZ5PVN2XTIB4V5PU6V2CEPWL3QWNAVVRLNKWS3MI3XA6TLN47LP73BWY3QLVAGCTIVOVMMPUWVUTP3TC6V76H5DVXCQRNSGO6NJN5MEU4ABX4UVPSBRE2T3LF5MXU6WBA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,454036,ЧЕЛЯБИНСКАЯ ОБЛ,,Челябинск г,,Радонежская ул,5,,",
                    "RegionCode": "74"
                },
                "INN": "7423012592",
                "KPP": "744801001",
                "ClientRegId": "010000000090",
                "FullName": "Общество с ограниченной ответственностью \\\"Центр пищевой индустрии-Ариант\\\"",
                "ShortName": "ООО \\\"ЦПИ-Ариант\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "207.00",
        "FARegId": "FA-000000045137124",
        "F2RegId": "FB-000003830707688",
        "AlcCode": "0123130000004249750",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "403",
        "FullName": "Вино столовое сухое белое \\\"Лаветти\\\"",
        "ShortName": null,
        "marks": [
            "171201801785290219001SU7ZCT4B5XCDRPXQRLJOKCOHXMVAT3QXYMTIUDDDPVJ36QGHDE5PLBR2GWEZVY7NJWZFF4CHRPZQYSWNKRHQIVM4MSZNR6YDCIJI4WJOH66F44MJI5O73VZ6237YWAIOA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "360.00",
        "FARegId": "FA-000000045627928",
        "F2RegId": "FB-000003943141850",
        "AlcCode": "3771014000001273951",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "403",
        "FullName": "Вино столовое \\\"Клаве Индако\\\" полусухое, белое",
        "ShortName": null,
        "marks": [
            "236303032550170820001LL7LBC4C62UWPXDSJUCXIKN4VA6NWZ4LTTYQLMIYLXPNLQ6DG57L3OQOZY4GFTSH36LQ2MPRRR67JS3E7S5VVKDPP7N6H6DY3O5PKHYAZCUQRSYYXJVS6LNBWQASH2VUI"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "724",
                    "description": "Кайе Реал 82 - 84, 13300 (Сьюдад Реаль), Испания"
                },
                "ClientRegId": "050000056198",
                "FullName": "Винья Гинеса Резервас С.Л.",
                "ShortName": "Винья Гинеса Резер.С.Л."
            }
        },
        "quantity": 1
    },
    {
        "price": "360.00",
        "FARegId": "FA-000000045611157",
        "F2RegId": "FB-000003943141851",
        "AlcCode": "3771014000001273961",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "403",
        "FullName": "Вино столовое \\\"Клаве Индако\\\" сухое, белое",
        "ShortName": null,
        "marks": [
            "2363030328845208200014CGYTZ4PTHCIZP2GIP3VDVUL74UPQ372HXNCEON7GQRKZRA3HVEONGYXN64EJJV67CNZSVWBIHHOVBCNHY5XL5UELCENFUZGNEDI44M5SBOQSXO7GKRNZ3UAT5LBS56WI"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "724",
                    "description": "Кайе Реал 82 - 84, 13300 (Сьюдад Реаль), Испания"
                },
                "ClientRegId": "050000056198",
                "FullName": "Винья Гинеса Резервас С.Л.",
                "ShortName": "Винья Гинеса Резер.С.Л."
            }
        },
        "quantity": 1
    },
    {
        "price": "216.00",
        "FARegId": "FA-000000047857166",
        "F2RegId": "FB-000004522138989",
        "AlcCode": "0000000000038114816",
        "Capacity": "0.750",
        "AlcVolume": "11.500",
        "ProductVCode": "440",
        "FullName": "Игристое вино полусладкое розовое \\\"Ариант\\\"",
        "ShortName": null,
        "marks": [
            "193300962604901120001WSJK4YK46PHGHAFAGBPHC4G25USTJYN3CXV24KZUZ67RAUECGP55VTIH474VNMUBP5R3GWAYGF2SPLXXKVJS3J24OVDD6LHBFLNJXXCATVPJSKQPBGZ4JQOUOWCKWGE3A",
            "193300962604931120001S5W6EUJBFCDRHKNB577UR22FTA72MFERXJTD2ZACW2MFZBODQKDTRPC6CECVSVRQZ24PQV3KLJTDNBDF7KDB5RNFBRS5N5GHBEBWZTQS5MHD6M7672SRNIGBJNTD56FKA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,454036,ЧЕЛЯБИНСКАЯ ОБЛ,,Челябинск г,,Радонежская ул,5,,",
                    "RegionCode": "74"
                },
                "INN": "7423012592",
                "KPP": "744801001",
                "ClientRegId": "010000000090",
                "FullName": "Общество с ограниченной ответственностью \\\"Центр пищевой индустрии-Ариант\\\"",
                "ShortName": "ООО \\\"ЦПИ-Ариант\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "156.00",
        "FARegId": "FA-000000048070172",
        "F2RegId": "FB-000004542466681",
        "AlcCode": "0000000000041991478",
        "Capacity": "0.700",
        "AlcVolume": "12.000",
        "ProductVCode": "401",
        "FullName": "Вино полусладкое красное \\\"Изабелла\\\"",
        "ShortName": null,
        "marks": [
            "192302866019150321001WB45XHUFVWO7FCDF2NN3YZDDWENWEQOJDCN547YYMTH52QORAH25MSBOGI3AJDHRWVYYT4MRRSGBPZX3VZYV6IP5NKJTUEWNCSI5F2NMPXCCZXII7V3CM6OISGHQSMWHY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Анапский Район,,Юровка Село,Октябрьская Улица,,1",
                    "RegionCode": "23"
                },
                "INN": "2301076247",
                "KPP": "230145001",
                "ClientRegId": "010060699786",
                "FullName": "Общество с ограниченной ответственностью \\\"Винзавод Юровский\\\"",
                "ShortName": "ООО \\\"Винзавод Юровский\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "203.00",
        "FARegId": "FA-000000047952859",
        "F2RegId": "FB-000004542466724",
        "AlcCode": "0000000000037565888",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "440",
        "FullName": "Вино игристое полусладкое белое \\\"РОССИЙСКОЕ ИГРИСТОЕ ПРЕМИУМ\\\"",
        "ShortName": null,
        "marks": [
            "193301265211820121001NLXYVUS6I2VJ55GE67BVE57AUQZ7NYQJBB2XANZWAYWWE2JPLMUT6PKXKXR6MYIHNJCPN6U3AOGNQJKUH3DOI67UFVMFZWQVSUBSDZYAINP6UWMYUDZNW6LSSHJ4U7BTY",
            "193301265211860121001EV2AROZ7RBKLPFYTHKNAUZWNWYQRCWZZJZU6HVUOMK3CY2ROIWNWZMHXD6ITQQES626JT4J35HZFD4VHL74DQ5DMXEGZ4POCEFXXVZVKH26SQW5HYJS3NEBTX7NXXBA7Y",
            "193301265211900121001AXNCBFLBUCI5RNGTU4FSPWW3EURKRMLC23FOH2CJ5FB7PKCICOVTNFFZQ3Z6N6BPDGKDKFOWTIPROLW5WHPL36SKEZZX6LTC42HBR3TQSV4WBOIB7MWP665OOQGDCXMXI",
            "193301265211960121001XWWFSFJLZC6XX7I7UX6N2NVPLA4F2OHNF6QFVVGN6DQQJECHXSZB2MOXD7FQBHTQQZXKEY6AMWNYAMC2PRIQNTQK573PVEZ2JBTZI7S2XZE6Q325OXQP3YDSFOIE73DJI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ставропольский Край,,,,,,,Минераловодский городской округ, поселок Первомайский, ул. Производственная | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем,  литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563 | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем, литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563",
                    "RegionCode": "26"
                },
                "INN": "2630800592",
                "KPP": "263045002",
                "ClientRegId": "010060702025",
                "FullName": "Общество с ограниченной ответственностью \\\"Минераловодский винзавод\\\"",
                "ShortName": "ООО \\\"Минераловодский винзавод\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "185.00",
        "FARegId": "FA-000000047908897",
        "F2RegId": "FB-000004542466725",
        "AlcCode": "0000000000042081991",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "461",
        "FullName": "Плодовый алкогольный напиток газированный сладкий \\\"ЛАМБРУСКО АФФЕТТО РОЗОВЫЙ\\\"",
        "ShortName": null,
        "marks": [
            "190300094220391120001GGIBPKEKFNACTQYAPYWPBG6LNQ75OYKHKKZBTU7E22ARFU6WM3X7PJRNE4W3HYUSSVZH4MP46SBE7AHMMZUNQDFD5FTJ52YM37HAU2G3LGTAZSJ4ZVDP74DLC7LWGXKNY",
            "190300094220551120001QRX6HE37JSQUSLIMGTDVWHRLTES6BHYWUC5L43BN7UG4I2PJXHZOYLW5AJTNJOHEMQD23BCDB4WK2SRBXYD4O3E4UDIC6Z6DPECCZXIU22PILBPVQCPKI5T6LSJB3RT5A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ставропольский Край,,,,,,,Минераловодский городской округ, поселок Первомайский, ул. Производственная | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем,  литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563 | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем, литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563",
                    "RegionCode": "26"
                },
                "INN": "2630800592",
                "KPP": "263045002",
                "ClientRegId": "010060702025",
                "FullName": "Общество с ограниченной ответственностью \\\"Минераловодский винзавод\\\"",
                "ShortName": "ООО \\\"Минераловодский винзавод\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "227.00",
        "FARegId": "FA-000000047899246",
        "F2RegId": "FB-000004542466726",
        "AlcCode": "0000000000042081989",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "461",
        "FullName": "Плодовый алкогольный напиток газированный сладкий \\\"ЛАМБРУСКО АФФЕТТО\\\"",
        "ShortName": null,
        "marks": [
            "190300093564821120001D5RRNCOGZPZMQK26OLFOYKKAB4UMXGROCSENLJ6AOEJX6Q2EOGFOKFWOKDIJZ7JUMBCTJFCPR5E5LCCZG2R4NVDUDAPKKUZ7O4OVZZQZ7ITAXTYN5IMPHIE6LHKMN7HSA",
            "190300093564861120001OGBWEZZX4NMTQK42U6QLNUEPLIPJFXDW3IBWW7GT67CRQMAXIU275XENR5WBPNNVXZJOAKXUZHGOODAEHLRUKNCRKN3MMSM5YZGLIKCCMQTCHBQ5K2F2Z25W2EP43Y43Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ставропольский Край,,,,,,,Минераловодский городской округ, поселок Первомайский, ул. Производственная | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем,  литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563 | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем, литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563",
                    "RegionCode": "26"
                },
                "INN": "2630800592",
                "KPP": "263045002",
                "ClientRegId": "010060702025",
                "FullName": "Общество с ограниченной ответственностью \\\"Минераловодский винзавод\\\"",
                "ShortName": "ООО \\\"Минераловодский винзавод\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "329.00",
        "FARegId": "FA-000000047480146",
        "F2RegId": "FB-000004648351032",
        "AlcCode": "0001291000004511307",
        "Capacity": "0.500",
        "AlcVolume": "24.000",
        "ProductVCode": "211",
        "FullName": "Настойка полусладкая \\\"Архангельская Вишня Ручного Сбора\\\"",
        "ShortName": null,
        "marks": [
            "187402891701830421001DQRNPWHXURGTF45QD7462IXSDEJURFHVICKLAVEWHIWVQK5K7OQUXVZVGHNF4E6YGARO7TQEXMOS26OYR4S56GDLDYVN3EDQ2ZLA7X6P4GU74WNRDPEM2SZLSRLIOCT6Q",
            "187402891701840421001XVMODMVO2P6VC2SE7INZNCJ5OYFKDH4CNB3OKOLYLLMDD5N4EMI4GY26RMGP4RTZQSCQBUIUUV25HADBBUWYWZ3OOMMQDVPUEF73WTHBURU3V3SMHBEMF7PRONKO77QRY",
            "187402891701940421001TKBWY2A5MXVJXJEBY6CPSKZKOUFIAHUM4FFLODZCQE7FMEVDO2TPKM6GXTJGKLCIR33JMY3HD5W6TR4ZCZZ2LIFJ5ZERQA3TZHLOOEQBQDW22Y4IE6JDTX2SDEOVGO5FQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,АРХАНГЕЛЬСКАЯ ОБЛ,,Архангельск,,наб. Северной Двины,д. 120,, | ; пр-кт Троицкий, д. 133, корп. 1, пом. 5-Н, пом. 6-Н",
                    "RegionCode": "29"
                },
                "INN": "2900000293",
                "KPP": "290101001",
                "ClientRegId": "010000000270",
                "FullName": "Акционерное общество \\\"Архангельский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"АЛВИЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "250.00",
        "FARegId": "FA-000000048494400",
        "F2RegId": "FB-000004794665023",
        "AlcCode": "0100000002030000015",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "4011",
        "FullName": "Вино ординарное сухое красное \\\"Саперави Мосавали\\\"",
        "ShortName": null,
        "marks": [
            "192302883184510321001LMEYNK4J3YAW4XPU6EZET2R2EAUQO4IBAEJLTVN4BT5V2U2YHN774A6FNDO6IASWAFTVMYKYKHFV2ST2KBIHXPHYBPVJCILI2GADD4Q33SLL3H6EMQUX2PJOEM5UCIYUQ",
            "192302883184560321001KLTEWDL3LVBTH7VJ2VLR6NOGHQJVSMESEQHSSWUPUDLXEXSHDHJZOSS6TRNQOWQ3DB6XG5MOEVWWUBTOF6ZTDSVQXMTW7WTDPX2PPXY35ST4NZX6RFCUYWZ4EFHELXC6A",
            "192302883184590321001OICXEHOSNOT5VB2YLBQJTE2LFYCI44MHWMFYO2WQ3NACC4XP4BRDTWGG6HOFXASQ3S2BIFH7GPH22RHGNRG7RAFJ2YL6IMEPHU53JSCFFBENTXFQYAKAYTMH7MGTMG3FY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "268.50",
        "FARegId": "FA-000000048513421",
        "F2RegId": "FB-000004833603801",
        "AlcCode": "0300006431080000068",
        "Capacity": "0.500",
        "AlcVolume": "35.000",
        "ProductVCode": "2129",
        "FullName": "Настойка полусладкая СТУЖА ЛЮКС КЛЮКВЕННАЯ",
        "ShortName": null,
        "marks": [
            "187307942009341221001K6NDM2HEHAPCJJP5UAQJQI42KEW5GDWYTL3NQJWYEAPFIAOKMYRHHLL7GO6D34YICN6ZVF2Q4CXTRU3UXJJFQ7O4GIQ276ZLXDA2DVQAXFOLMQ3RHEZRTDVALFWYWMYWQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ульяновская Область,,Ульяновск Город,,,Карла Либкнехта Улица,,д. 15 |  | нежилое помещение (S=3008,9 кв.м): помещения подвала: №№ 1-6, 8-13, 15, 16, 19-25; 1 этаж: №№ 1, 3, 5-10, 13-24, 28-35, 49-53, 55-59; 2 этаж: №№ 2-5, 10-23, 29-33, 42-44, 47; здание склада готовой продукции и административного корпуса с пристроем (S=2336,2 кв.м); здание спиртохранилища (S=387,7 кв.м); здание таропосудного цеха (S=613 кв.м); нежилое помещение (S=217,2 кв.м), помещения: 1 этаж - 25, 26, 48, 54; 2 этаж - 34-41; нежилое помещение (S=233,8 кв.м); нежилое помещение (S=672,5 кв.м); здание гаража (S=124,5 кв.м); нежилое здание (S=348,9 кв.м); нежилое здание (S=754,3 кв.м); здание трансформаторной подстанции (S=44,4 кв.м); нежилое здание (S=327,4 кв.м)",
                    "RegionCode": "73"
                },
                "INN": "7327080600",
                "KPP": "732545001",
                "ClientRegId": "030000643108",
                "FullName": "Общество с ограниченной ответственностью \\\"АЛКОГОЛЬНАЯ ПРОИЗВОДСТВЕННАЯ КОМПАНИЯ\\\"",
                "ShortName": "ООО \\\"АПК\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "268.50",
        "FARegId": "FA-000000048481545",
        "F2RegId": "FB-000004897578744",
        "AlcCode": "0300006431080000076",
        "Capacity": "0.500",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"СТУЖА МЕДОВАЯ С ПЕРЦЕМ\\\"",
        "ShortName": null,
        "marks": [
            "187307548102961221001PX7JMFDSMZE5BFGJ7H5YNCXNXALSA7KXDKJVCKJ4UKQBKANW3AL3NXGCYC3V4YYVSPIQEFCFNJFIHUWUYX6NMOR6EKU7K6756EY24DQXDDSEYTTGMSLCVFRSXHST5S7AY",
            "187307548103081221001BN3TIXYBI5S6R2FO3WOMJ6CLNYH4KNG2ZLIE2T75WOZSIZEKLIXZYNGCF324RYIO3AWEFKGBPF2ZPUNGKSFXCK54HIFDCYSCTF4FB6E5XZOF3L6IR6VBABBJBJRLKT2VA",
            "187307548103141221001VCOBAZA4KJGAKVRMAMPE2VGAWABQY3CFUMVVUUEM76EKQDRV5WVQFDEVNK67Z4GP4CUQ6X5ACG36UQRUIQWDZCWTTUEMBXNIFEQEMFFSOIE24W76GWRXY3ETPU3GWLJBQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ульяновская Область,,Ульяновск Город,,,Карла Либкнехта Улица,,д. 15 |  | нежилое помещение (S=3008,9 кв.м): помещения подвала: №№ 1-6, 8-13, 15, 16, 19-25; 1 этаж: №№ 1, 3, 5-10, 13-24, 28-35, 49-53, 55-59; 2 этаж: №№ 2-5, 10-23, 29-33, 42-44, 47; здание склада готовой продукции и административного корпуса с пристроем (S=2336,2 кв.м); здание спиртохранилища (S=387,7 кв.м); здание таропосудного цеха (S=613 кв.м); нежилое помещение (S=217,2 кв.м), помещения: 1 этаж - 25, 26, 48, 54; 2 этаж - 34-41; нежилое помещение (S=233,8 кв.м); нежилое помещение (S=672,5 кв.м); здание гаража (S=124,5 кв.м); нежилое здание (S=348,9 кв.м); нежилое здание (S=754,3 кв.м); здание трансформаторной подстанции (S=44,4 кв.м); нежилое здание (S=327,4 кв.м)",
                    "RegionCode": "73"
                },
                "INN": "7327080600",
                "KPP": "732545001",
                "ClientRegId": "030000643108",
                "FullName": "Общество с ограниченной ответственностью \\\"АЛКОГОЛЬНАЯ ПРОИЗВОДСТВЕННАЯ КОМПАНИЯ\\\"",
                "ShortName": "ООО \\\"АПК\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "268.50",
        "FARegId": "FA-000000048513421",
        "F2RegId": "FB-000004897578745",
        "AlcCode": "0300006431080000068",
        "Capacity": "0.500",
        "AlcVolume": "35.000",
        "ProductVCode": "2129",
        "FullName": "Настойка полусладкая СТУЖА ЛЮКС КЛЮКВЕННАЯ",
        "ShortName": null,
        "marks": [
            "1873079420096412210012R4FOWB2LR7BXTZHGHJY3A74KI5X4XZUEIBJ3E2BC2DDLJFJDELJPLDZNMSRFFNTUIKNSZJXSXMN6KRYPWQREXOKCECHTRFOZUK4FZEE42LLPLN54UASWGPLKJMW56N6A",
            "187307942009721221001NLKHAAEF5QV74S7XTC4XXWK7KYYNFATI5AIVQP7WIMVD6JQ5NB6USNFNUCAXOVYD6QBMCR4BAIOXBEDMWAYFTAAV5I2VCUQBMQRRVOASEE6XBUANDS2SKFT3LLTFSGJ4Q",
            "187307942012551221001RK56NIL53YQM3FJNLGIVTVI7FQF22MCJMCMLFSD5V3PXGAHONFY5NBCCJVPPWMQLL256TRK5YMP4E5KT5MQJ5DWQZILTSBS6O4T6VJ2OASKAYQDZ73EK5SEU2HZZ6IYWI",
            "187307942012561221001QVZ5LZDZJUECRQXIO63NPRJFXU2WBDUHIVNMSIM7DBPZR3QIQHPLOUZGO7HOBWWGZ6GUWFMC6RQFA2ZOSYKC2DUTM2NVITGJ3L3LSWH63VOCE6GVSA4EWRMH6R4C76U3A",
            "187307942012851221001YBO2HM6XWORIYBB56YNQ5PWCBQJGPVNOZDXC2ZYTSTDPUSTU7MQTLWP3V7BSUQHOTM6JBWGWVOK7SNUN7VBC5ETFTFXNVQLOHLCQRGC37LWRIJGA3MCLCDGTICSIRFZBA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ульяновская Область,,Ульяновск Город,,,Карла Либкнехта Улица,,д. 15 |  | нежилое помещение (S=3008,9 кв.м): помещения подвала: №№ 1-6, 8-13, 15, 16, 19-25; 1 этаж: №№ 1, 3, 5-10, 13-24, 28-35, 49-53, 55-59; 2 этаж: №№ 2-5, 10-23, 29-33, 42-44, 47; здание склада готовой продукции и административного корпуса с пристроем (S=2336,2 кв.м); здание спиртохранилища (S=387,7 кв.м); здание таропосудного цеха (S=613 кв.м); нежилое помещение (S=217,2 кв.м), помещения: 1 этаж - 25, 26, 48, 54; 2 этаж - 34-41; нежилое помещение (S=233,8 кв.м); нежилое помещение (S=672,5 кв.м); здание гаража (S=124,5 кв.м); нежилое здание (S=348,9 кв.м); нежилое здание (S=754,3 кв.м); здание трансформаторной подстанции (S=44,4 кв.м); нежилое здание (S=327,4 кв.м)",
                    "RegionCode": "73"
                },
                "INN": "7327080600",
                "KPP": "732545001",
                "ClientRegId": "030000643108",
                "FullName": "Общество с ограниченной ответственностью \\\"АЛКОГОЛЬНАЯ ПРОИЗВОДСТВЕННАЯ КОМПАНИЯ\\\"",
                "ShortName": "ООО \\\"АПК\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "292.00",
        "FARegId": "FA-000000049120189",
        "F2RegId": "FB-000005031539391",
        "AlcCode": "0100000020360000003",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"МЕДОВУХА ГРЕЧИШНАЯ\\\" с ароматом мёда",
        "ShortName": null,
        "marks": [
            "1873091140463801220014HPVZMBSBVVAYGVCQBKMJVAV3QXZOCA34URSXE3PQ6OWJD2VWQZDNHF3LTTYYNCSV7TWM245ZGURQPQYUCRUECWYM74PFPAPLNKHLQYK3XEWE3EBO4S3IHTBEVRILIVTA",
            "187309114046410122001GYYYW3JIJWHRAPC6BPETZGBQIIVEPB3YCUVSTH4A7ZY2NDPLNR657N55GFPYM6WXCHI7XUVR3XUDNPUZU6X643ISNSMIZUFLYXEA2V3JSZQBAGUCOJ43ADBOBUEWEPNOI",
            "187309114046470122001XAX2U5ZGQFLGJZHENU67PZ5JKYEJQ5LXCLZHJ3IYS7YZT6MG4BYZ7HHAUD6SRVF3ZJFBFESFZVP2BIYSYAQHTDB6OEVUZUHQFHZZXD6BH5HJFYY2GCNFAYVYEIJON2XQY",
            "187309114046550122001TIJOQGVZUK4PVTR5XI7QTNCSZ4DE5DZNMWWV373E3IFZHPFCPPZYA3NVGGFIM6G36UE4E54RZVOS5V3GI37G5Y3YTI44RZDWMLIJMMHVN2M4PCGTZUFCKNBCYFBX6JVXI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,Вологда Город,,3 Интернационала Улица,39 Дом  , | - нежилое здание с мезонином: 1 этаж: литера А3 - пом. 5, 6, 9а, 10, 11, 15-20; литера А6 - пом. 3, 3а, 3б, 6а, 9б; литера А7 - пом. 35; литера А8 - пом. 36, 36г; литера А9 - пом. 37, 38; литера А11 - пом. 33, 33а; литера А12 - пом. 30; 2 этаж: литера А3 - пом. 37, 38, 42, 43, 47; литера А5 - пом. 52; литера А6 - пом. 3, 3а; 3 этаж: литера А3 - пом. 8-10, 12, 13; литера А6 - пом. 2; литера А7 - пом. 3; мезонин: литера А13 - пом. 1, 2, 3; - административное здание с проходной и складами: 1 этаж: литера В2 - пом. 2; литера В3 - пом. 3; литера В4 - пом. 5, 7; 2 этаж: литера В5 - пом. 16-18; - здание основного производства: 1 этаж: литера А - пом. 6; литера А1 - пом. 1, 3, 3а, 5, 11; 2 этаж: литера А - пом. 5; литера А1 - пом. 1-4; мансарда: литера А2 - пом. 2, 3; - здание посудного цеха: 1 этаж: литера Ж9 - пом. 1, 1б, 1в; литера Ж6 – пом. 1; - здание кондитерского цеха, 1 этаж: литера Б, пом. 21, 24, 25;",
                    "RegionCode": "35"
                },
                "INN": "4720027123",
                "KPP": "352501001",
                "ClientRegId": "010000002036",
                "FullName": "Общество с ограниченной ответственностью \\\"Русский Север\\\"",
                "ShortName": "ООО \\\"Русский Север\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "192.00",
        "FARegId": "FA-000000049152831",
        "F2RegId": "FB-000005129090488",
        "AlcCode": "0100000001740000180",
        "Capacity": "0.700",
        "AlcVolume": "10.000",
        "ProductVCode": "404",
        "FullName": "Российское вино с защищенным географическим указанием «Кубань» сухое белое «Шардоне»",
        "ShortName": null,
        "marks": [
            "192302716327110321001A4WATMJ4QE3JJAJ5WBAVWYQBWULJ4SD7XZPE7QVLJ4BCQCBCIO4FO2724D6TFE7IIUC5EXN6QTSEIVGZMOE6RHUG6PMJUDEDD34ACTEFVMH25ZMZU5DERJFKHUXNYFVAA",
            "1923027163272603210015TK6G3DPQNCGMCZFD5ZW5ZPJVYD5SS7RDTG4IYRMGYMHM32QAOLVIYYV444G2JG4WZ6EIZMZMODVM3RXTATRFX3IATUSEISKXNNTMN3RA2H5EP3BQGYDPQJKHJWFHBFPI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Темрюкский р-н,,Вышестеблиевская ст-ца,Береговая ул,45,,",
                    "RegionCode": "23"
                },
                "INN": "2352032696",
                "KPP": "235201001",
                "ClientRegId": "010000000174",
                "FullName": "Общество с ограниченной ответственность \\\"Долина\\\"",
                "ShortName": "ООО \\\"Долина\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "192.00",
        "FARegId": "FA-000000048888225",
        "F2RegId": "FB-000005129090489",
        "AlcCode": "0100000001740000122",
        "Capacity": "0.700",
        "AlcVolume": "10.000",
        "ProductVCode": "404",
        "FullName": "Российское вино с защищенным географическим указанием «Кубань» сухое красное «Каберне»",
        "ShortName": null,
        "marks": [
            "192302711581030321001RGK7OFC2PAALUMZS2IOSK6MXWIB4X7BE4GD5LPT6QDIUNG4DFSQOEE3IXLUSA5MLJUWJIDBTYN7SLMK5IGK42LYAFRG5QFMAKWFK4IWFD3VCNDD5CGWKPEBYCT2UCGOOI",
            "192302711582230321001ZUEVL7Z2KVDXEEPU7A77KJO7PY3FCPIBAZT5SVQUDPPLSYVYKBJSVZKOC4XCFMDQMSYMWOFX7SSW3WZK2BDF66DIKVEHILT5ZFD6LCVTYZ7VQFK5ULDGBL63RHZA4SI2I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Темрюкский р-н,,Вышестеблиевская ст-ца,Береговая ул,45,,",
                    "RegionCode": "23"
                },
                "INN": "2352032696",
                "KPP": "235201001",
                "ClientRegId": "010000000174",
                "FullName": "Общество с ограниченной ответственность \\\"Долина\\\"",
                "ShortName": "ООО \\\"Долина\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "399.00",
        "FARegId": "FA-000000047805146",
        "F2RegId": "FB-000005184384001",
        "AlcCode": "0000000000042029706",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "229",
        "FullName": "Коньяк ординарный пятилетний \\\"Дубовый бочонок\\\"",
        "ShortName": null,
        "marks": [
            "187303234737440421001RTJEEJ7IM4AR6HA75QX3DJNSO4SM5VPWNWIU3IA7OJESPWXD63YRFSEQJ5ZXVE3PLM3NHZJH7RWTM4UCMIIIRWFM2R7WZ6KDQJOIFFN4JHHUH5RQR6MYSDPXZBTXFVUII"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРЫМ РЕСПУБЛИКА,Симферопольский р-н,с. Первомайское,ул. Дьяченко,д. 5,,, | (за исключением: Литер В, кадастровый номер 90:12:120401:79) | за исключением здания с кадастровым № 90:12:120401:79 (Литер В)",
                    "RegionCode": "91"
                },
                "INN": "9109005701",
                "KPP": "910901001",
                "ClientRegId": "010037660103",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Первомайский\\\"",
                "ShortName": "ООО \\\"Завод Первомайский\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "99.00",
        "FARegId": "FA-000000048961337",
        "F2RegId": "FB-000005184384005",
        "AlcCode": "0000000000039678375",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски зерновой \\\"Carte Blanсhe (Карт Бланш)\\\"",
        "ShortName": null,
        "marks": [
            "197301758842230421001EC56PUO3KUXEDJCPEQFHDCIF2A3OSYCFTAKF46JGJVSARGU5TXTEIR4IYN2MAOO3RY6JJWCSZ3PHAANJQEQNJNPGORRGRYLDHLY2AAZOEBSSILEOT2UMOKD4TKWCGXF7A",
            "197301758842290421001FZZWROD2OVC6VX6L32XKBSHJXQQC4RRKKMFRCHPK4CQ7UMLWQ5KRPUMLUMUQHACIXZBJ4SXPQS6A2K22TIXO24RXJCJ5IUNB6B22IV2OYDXCYOKLI4R73OQRDIS3QKKDI",
            "197301758842320421001J7OA75UJOC5GTYO3LS3KRU2GBMOR3A5EVNDHMIQEXSDMS3I3LKQLDJNUBC65UOEDVLMX6IKRTTQ572K3VRNQWNRVQKCD2VA7T5PKG5TFHFKVAYJV6XH25DUCSTTTQ4CHY",
            "197301758842330421001MNUJ72MD4UU2FPYXQFRRYS7N74EKYGNB22QAEQRD4P277E5MWIWTBXXVCH4JMUWMID3GJ3JTZLNXV7M2QFO5LL5EDFYZNA3T76DIFZ5RQM2FMC7IJ7QFWZLXMTM5OUENI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,454036,ЧЕЛЯБИНСКАЯ ОБЛ,,Челябинск г,,Радонежская ул,5,,",
                    "RegionCode": "74"
                },
                "INN": "7423012592",
                "KPP": "744801001",
                "ClientRegId": "010000000090",
                "FullName": "Общество с ограниченной ответственностью \\\"Центр пищевой индустрии-Ариант\\\"",
                "ShortName": "ООО \\\"ЦПИ-Ариант\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "408.00",
        "FARegId": "FA-000000049393689",
        "F2RegId": "FB-000005184384007",
        "AlcCode": "0017418000005750160",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски зерновой \\\"Carte Blanсhe (Карт Бланш)\\\"",
        "ShortName": null,
        "marks": [
            "187310218556280122001TPVRT57VD4LHCTW6TLO5O2LQZUHN3PWT5FTOBZR37EKVMG5SGW6KDLJM73NPV64KHNIVMXYFRIKHKOTQ2B2MF22G4TSWWEMHSNW7T5Z3LFXD7TEBEWYVDJLH6UIXXTMHQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,454036,ЧЕЛЯБИНСКАЯ ОБЛ,,Челябинск г,,Радонежская ул,5,,",
                    "RegionCode": "74"
                },
                "INN": "7423012592",
                "KPP": "744801001",
                "ClientRegId": "010000000090",
                "FullName": "Общество с ограниченной ответственностью \\\"Центр пищевой индустрии-Ариант\\\"",
                "ShortName": "ООО \\\"ЦПИ-Ариант\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "334.50",
        "FARegId": "FA-000000049013041",
        "F2RegId": "FB-000005184540419",
        "AlcCode": "0100000005410000013",
        "Capacity": "0.500",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\\"БЕЛЕБЕЙ ЭЛИТНЫЙ\\\"",
        "ShortName": null,
        "marks": [
            "187308083936421221001QO3HBRL4LF7UU4X254QD2FD56U3A265MP4I2RZLERIU2N2RH4CDXMLLN7JW6AHDG6GQJLD2PRLVZRTPUPDXPQ2NP2Y7NKBDJ7FDREM4DAT7CEM4PUYD5CMQMXWWPLXRNY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "320.00",
        "FARegId": "FA-000000048556854",
        "F2RegId": "FB-000005184540422",
        "AlcCode": "0032136000001257262",
        "Capacity": "0.500",
        "AlcVolume": "45.000",
        "ProductVCode": "212",
        "FullName": "Бальзам \\\"Парне\\\"",
        "ShortName": null,
        "marks": [
            "187307595876551221001KVULSYRNN4HK3ZI4Y5O2ZD3C4Y2G6QPTHGR62RPTCZUCKUP7VYNVVKCGEBUDEFNOPZPZ7WTCFDNSK4PRQ4WA2GRJSSXQ3VCTTANAZQF2MBB3YDWIRPIDCYB7D3B7R6WCI",
            "187307595876621221001YMUVD5KJU547ARKMM3ZJRJBWTIJK2L45P73QK3FPOT53IMIN3VO2LUG2Y4HNPL2HZHETU4QS4S7SLHVS5UAT76UMXWVAVS5UP7B6RHL32JEZ2YEOSW2K5TWL5NST4YFKY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "192.00",
        "FARegId": "FA-000000049152831",
        "F2RegId": "FB-000005184540423",
        "AlcCode": "0100000001740000180",
        "Capacity": "0.700",
        "AlcVolume": "10.000",
        "ProductVCode": "404",
        "FullName": "Российское вино с защищенным географическим указанием «Кубань» сухое белое «Шардоне»",
        "ShortName": null,
        "marks": [
            "19230271632771032100135PJJBPUTQC5OIC7VJUK5RQTQ4CGZ6Z5SHRTZRKVEGVUSG74SXJEG7SCWNKD7K4CSJX22ZCNNZLPHA22TM3ECMUGLBNSRULO6PR7EC2Z6LLZLCVMNQ2FIAVL453XKZZWI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Темрюкский р-н,,Вышестеблиевская ст-ца,Береговая ул,45,,",
                    "RegionCode": "23"
                },
                "INN": "2352032696",
                "KPP": "235201001",
                "ClientRegId": "010000000174",
                "FullName": "Общество с ограниченной ответственность \\\"Долина\\\"",
                "ShortName": "ООО \\\"Долина\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "192.00",
        "FARegId": "FA-000000048888225",
        "F2RegId": "FB-000005184540424",
        "AlcCode": "0100000001740000122",
        "Capacity": "0.700",
        "AlcVolume": "10.000",
        "ProductVCode": "404",
        "FullName": "Российское вино с защищенным географическим указанием «Кубань» сухое красное «Каберне»",
        "ShortName": null,
        "marks": [
            "192302711583230321001QY66Y2D2AKSTQHYYF6WRN7ITRM5QOOX3L53PG6J7BQLP244UNVOGYFUP2N4ZPBSY3VZYZC2XL7PZA4WTSIUQ4TX562CEZBQTZEEUNTDWRWN422GP6GLQV7W64BHOINVFI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Темрюкский р-н,,Вышестеблиевская ст-ца,Береговая ул,45,,",
                    "RegionCode": "23"
                },
                "INN": "2352032696",
                "KPP": "235201001",
                "ClientRegId": "010000000174",
                "FullName": "Общество с ограниченной ответственность \\\"Долина\\\"",
                "ShortName": "ООО \\\"Долина\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "216.50",
        "FARegId": "FA-000000049046745",
        "F2RegId": "FB-000005184540426",
        "AlcCode": "0100376750480000029",
        "Capacity": "0.750",
        "AlcVolume": "10.500",
        "ProductVCode": "4011",
        "FullName": "Вино ординарное полусладкое красное «АДЖА»",
        "ShortName": null,
        "marks": [
            "192303363053690321001UCPUNNXCJ523PTAMF4Q3EW4DOQE5TNZJ4FWGMN3D6QTY4Z5DECJTCLVUMU3MU7UFUNOYZHCEMJYAQJX3UCLV2WWROJ2JEWKH3YOAC2BKNO7C45BH7HETUDABZV72GI36I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРЫМ РЕСПУБЛИКА,г. Феодосия,ул. Любы Самариной,19,,,, | лит. П, В, Х, И, АБ | литер АБ, Я, подвал литер \\\"З\\\"",
                    "RegionCode": "91"
                },
                "INN": "9108001581",
                "KPP": "910801001",
                "ClientRegId": "010037675048",
                "FullName": "Общество с ограниченной ответственностью \\\"Крымский Винный Дом\\\"",
                "ShortName": "ООО \\\"Крымский Винный Дом\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "216.50",
        "FARegId": "FA-000000049112486",
        "F2RegId": "FB-000005184540427",
        "AlcCode": "0100376750480000039",
        "Capacity": "0.750",
        "AlcVolume": "10.500",
        "ProductVCode": "4011",
        "FullName": "Вино ординарное сухое красное \\\"АРДЕШ\\\"",
        "ShortName": null,
        "marks": [
            "192304781647790421001YF7GJTQLHDDTVMCXKSMASD5TQU5SPNCLRDDGIB6XKJMFGBQFWJPVGRI6Z2UU3N5WERXZE5KDZUWSDGI5J4XQGZSVWGVU7UX4646AXLWJ33GSNFUETSV4GZKKXBPWUBK7Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРЫМ РЕСПУБЛИКА,г. Феодосия,ул. Любы Самариной,19,,,, | лит. П, В, Х, И, АБ | литер АБ, Я, подвал литер \\\"З\\\"",
                    "RegionCode": "91"
                },
                "INN": "9108001581",
                "KPP": "910801001",
                "ClientRegId": "010037675048",
                "FullName": "Общество с ограниченной ответственностью \\\"Крымский Винный Дом\\\"",
                "ShortName": "ООО \\\"Крымский Винный Дом\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "175.00",
        "FARegId": "FA-000000048452622",
        "F2RegId": "FB-000005184540432",
        "AlcCode": "0000000000041776391",
        "Capacity": "0.700",
        "AlcVolume": "11.500",
        "ProductVCode": "401",
        "FullName": "Вино ординарное сладкое красное \\\"Канонические Традиции\\\"",
        "ShortName": null,
        "marks": [
            "192303198010010321001PSNG6OCZBGUF6KNYO34LB2GXDIZYL7BGTJSAH76YWZEHLY3V4ID6N6F7VWIJ6GQGWD5ZBBQHAJ5UV4UH4CCIOLDLD6NA6JCIB434VF7TADOQFMG2TC274EQGFGXRKCHOQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "172.00",
        "FARegId": "FA-000000048532349",
        "F2RegId": "FB-000005184540433",
        "AlcCode": "0000000000041191846",
        "Capacity": "0.700",
        "AlcVolume": "11.000",
        "ProductVCode": "401",
        "FullName": "Вино ординарное сухое красное \\\"Каберне-Совиньон\\\"",
        "ShortName": null,
        "marks": [
            "1923034829470603210013AQQI7INWGE7XYDXXSPT3V5VXY2KMZBOLKXAGYHOYYQE44XJJ2LM5X62NSBIRMYENXKA6SPYRR5VKMNW5FUZ6N6XH4OUZC4AFKJN4D4SEJKD3WZDDFEFTD7Y42OSS343I",
            "1923034829471303210017UNMXMCDOFAGSUQEUK22QFOIUI3KMTPSJBZ6MSZJ3MGQHIGYYVT7LQBPP6HHGUYQ6FQBXG73YH7OHEBS3MDHYHQ7GYH2TVBCK76LX7FYEHFV64OY2SX5H6ZAVEJYKDBMI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "257.00",
        "FARegId": "FA-000000049061128",
        "F2RegId": "FB-000005184540457",
        "AlcCode": "0010249000002494599",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"БЕЛАЯ КРЕПОСТЬ\\\"",
        "ShortName": null,
        "marks": [
            "187408234670651221001GEODVT3ATMAATIEXDU7PVHNIS4YXCIFJTT5A5ZH3DXCWTKEPPFBLNGLODH5PDKLLEFSLHGXSMML35IRK3ZEGSWJHFPTWEV77RC2MYRQF5W6AMZ6KHEIKRL2XC4R7CKU6Q",
            "187408234670791221001L4S3W6AX7BT7P47RTSAY33NEXM7TBAXKH4AVEBL7DGOSYSG6E5DDAIHMUWQC3CRXO7TE5OCS4YGIAVABIHJRBXW3GQ24CSXLYKRY6VIL3CSH6IQEZ3JZE6J4QC5ANOBEY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "222.00",
        "FARegId": "FA-000000049515334",
        "F2RegId": "FB-000005299308129",
        "AlcCode": "0100000003150000038",
        "Capacity": "0.500",
        "AlcVolume": "21.000",
        "ProductVCode": "21210",
        "FullName": "Настойка сладкая \\\"СОРМОВСКАЯ КЛЮКВА НА КОНЬЯКЕ\\\"",
        "ShortName": null,
        "marks": [
            "187409720435920322001ZMSVEBN5CHZGEGWZGSYU4FYGEYGK7RSMGEJ6SBRMVDJ5X4ZCIB3EUYRIHVGZZHUZZWXPQUDEWVY7OHZGLFCWCYBRRCI2IGBAZAOKWB3OGK3H3P764TAMBUTGQPYB6H2PI",
            "187409720436010322001KVFXODO6RUUAMDFZEIB7IJD23IYHZPRVLYJCQKR5MH2RWN52OAPXAHIEVOY2ULO7IHHEV44OEGL7KXR2275DBFUXX2IWAY5FUYREEEMLA2LRARBA5KTNCJPLWIDRDDQEA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Нижегородская Область,,Нижний Новгород Город,,,,Сормовский район, ул. Федосеенко, д. 47 | отдельно стоящее нежилое здание (литер И, И1), литер И, этаж 1, помещения №№ 41-43, 45, 64, 65, 81-83, 88, 90-93, 100-105, 110, 115-118, 235, 237, 237б, 238, этаж антресоль, помещения №№ 141, 144, 152; спиртохранилище (литер Д), нежилое здание; отдельно стоящее нежилое здание (литер Ю), этаж 1, помещения №№ 1-3, этаж 2, помещения №№ 1-10; склад № 2, нежилое здание (литер Я), этаж 1, помещения №№ 1-4 | полуприцеп цистерна CARDI M310 01TC, ГРЗ ВВ 3767 52 RUS",
                    "RegionCode": "52"
                },
                "INN": "5263043395",
                "KPP": "526301001",
                "ClientRegId": "010000000315",
                "FullName": "Общество с ограниченной ответственностью \\\"СОРДИС\\\"",
                "ShortName": "ООО \\\"СОРДИС\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "222.00",
        "FARegId": "FA-000000049506794",
        "F2RegId": "FB-000005327339576",
        "AlcCode": "0100000010250000009",
        "Capacity": "0.500",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"ПЕРЦОВАЯ С МЕДОМ\\\"",
        "ShortName": null,
        "marks": [
            "187411085408860522001FUOJD5E7THDIRXZOLN4RHZUGSM3MGXFFRA3GDZ77L57T5ABHVVAG6OT7CD3DA43UIM7MVDGBNQ2QZU465XF4VVGBUP2SCCDWVA7YT4QCVXNCBBQT7H5EGVZJDM4VA4V4A",
            "1874110854088705220016UN2WBEJG3UIRN2IHFNBLX24VIFIAW2SMLO2TL5CQYSIAMW6XDHXYTGJ442QUFPKDA75KQXHQJFJZILCRIJQP4MZ3QJTHDLFZVBK7TVC5KOWJPM63S64COEYEFZFTGANA",
            "187411085408910522001MYIHV6LUL63Q772HAN5W2FNA5IPWZ3FYMRZ532HXXISVWS3LC5TF3VELUWTNMHTGRRRCUXIESRKLQTUDIXP2YLPV5Q5FQGWBBV4VOEGQ6KY6CNMSCEJXVSNZGRTAVPGVQ",
            "187411085408920522001TVIE24ZD4YIA7IGTYQXG276W4QXJNX4FNDQV3SMBZMAKR6CJUUXPJAZOY52W6BEZQ2CKE7CQFMCV2UMLOOV6JPTAG74JWXVH7AF7M5G6LKF2WBK7JB4JEJIOJSFOOULSA",
            "187411085408970522001PX5KVOHI4TNN6GXBQPYKC3YWNEI4KOAHDVWS2RPASWKHWNF4JB5XA6YOQHNLIQSMZVOS2QYFHCFZBDWUL3P3XH377YAEIGYD2JBYTQCP6MB5ZN3GZF2KS7BRMZHLAHQFY",
            "187411085408990522001XNDSMVVDFEIABWIRJLGRPOB5NQOYESSSZCTVE6ZMAZZTCJWJ6ZSDAQ5KAAIBLAYBH72BH4JJ5QXX6XUTAIKCCBRYLPTTF3DX3PHMWLOSLZLTK25MBQHJDQIY4QRKZBEBQ",
            "187411085409030522001SJQWZXYL3AEWM55IR7WP3XKLE44N4I7FU6PP6C5YSDQ4MDW4XADOAFLU5OU2E72NNNGQ6SNLYMDWBFSQQ6H5U3TZSSXNUCCRLFRCKYELQZ5ZZNR5XEEPU37JQDPSOJPAQ",
            "187411085409060522001FF5NWH5IDJQZ46A4IDWZVHZDV4BCIKX3YSR6I4WNEUK2ZBEEDVYRNQECXYFNYCQILLUBIMWMGOSQX4AXAXDBBIE4PO6FRTPYJG75PIU4PUI3YE3WHUXXBLV2JREE4G5OI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "276.50",
        "FARegId": "FA-000000050038704",
        "F2RegId": "FB-000005440554720",
        "AlcCode": "0100000005410000036",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"БЕЛЕБЕЕВСКАЯ КЛАССИЧЕСКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "1873124190990803220013QCWGEIFRS5XQUYZBBCFCDKIYQ64HX5LYLF6UQ4UYSXNDMWMWB4MQ3IVI6AOYOLCWIEXA67WTDQMZ46WOBS7WEDPPF6VDEWJLAMR4QABOJOIONP7WTXSANWU2ZXEP2XUI",
            "1873124190991003220012BYYE6UDVMEBI5N4V6EKLZ5UE4WJSLSLHRMUCFUHVKFI7J6HMKAOXVMCGG4TW7QUP6HX5GAKYIX3QBELZOI4TH7WUGMTQSSCPATUTRP66J7IVVCEUZGCXIOR7HJXHW3ZQ",
            "187312419099110322001OSOIAXYKZKGXIOKYKYGVYSVROYECSQ6QRKUI35L5EAVMLQ366DGHBWGKISDZCWZIAJC26FZLSANAFA6QH2SJHTF24UHW64O3PNOFWSXJAZSC67R2KXRK35GVAHVP5RPFA",
            "18731241909912032200147CNOLSRYJIXCAEV6446CQSRFMKSG3OOQN37WJCXW4FBZIZAR5B675QUZPFG6DFOECJDP7EL3PMB6YR7TKDYQBOETGAZNF7RT2HZ2NMQSA2OF7CTUP4HY3VPSLTQ7Z3XI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "499.00",
        "FARegId": "FA-000000049796009",
        "F2RegId": "FB-000005440554742",
        "AlcCode": "0100606880350000011",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\\"Армянский коньяк Виват Армения пятилетний\\\"",
        "ShortName": null,
        "marks": [
            "187409481961980222001JQQORSORSMRISNYTYPDNEFIP5UG5JGOAINGPAMY4NIDGWYI5RFHC3WIYOMMLWOOC7U5VMGJ3A3472OVKQFELK5AQYJHZB3IYQEZQH5HCMKXM3BPAJNZ3FTQZKFVEQMXPI"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\\"Гетапский вино коньячный завод\\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 1
    },
    {
        "price": "479.00",
        "FARegId": "FA-000000049397787",
        "F2RegId": "FB-000005440554743",
        "AlcCode": "0100606880350000021",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\\"Армянский коньяк Трехлетний\\\" (матовая бутылка)",
        "ShortName": null,
        "marks": [
            "187309043371030122001XZA5JJYKGKSJMVNCGQIC5SSH4QH4CLQQBDZI3P3QOA3HDZKK2JH3IVNREMG4YKCR5LENRTB7FJ4CTNKS23TQVLFJWRRVHU6EGHIKOIKC7K52F6EVB4XU23IZ5MJWQRNMY"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\\"Гетапский вино коньячный завод\\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 1
    },
    {
        "price": "235.00",
        "FARegId": "FA-000000050037303",
        "F2RegId": "FB-000005440554744",
        "AlcCode": "0100000001870000154",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "440",
        "FullName": "Игристое вино полусладкое белое \\\"Московское\\\"",
        "ShortName": null,
        "marks": [
            "193303594718820222001ODTNY45ZGPYS4SRM2Y72VWARGYNL7SF4K33CAAHC6FMWRUQS6RKUG362EG4J575UVFEQELK3GQYTNCBG4CVN5RVOHIZGZLIIC3BODHATPKDGUF6GN2I3OP6JX275CPH2I",
            "1933035947188302220014G5A6X32OBEUJCO7ATFKMTMG3QQSF3VHFLE2GP46HWHDMOTLARY3UZIAKM6ATH7P7IISGDHDAZRARAVG4PJD4ISYI3YRAHQSGW43TEXIJYL5BZIU7YW2Q5IQWIZALVDXA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Темрюкский р-н,,Старотитаровская ст-ца,Заводская ул,2,, | (за исключением помещения № 5, 1 этаж, литера Д)",
                    "RegionCode": "23"
                },
                "INN": "2352034598",
                "KPP": "235201001",
                "ClientRegId": "010000000187",
                "FullName": "Общество с ограниченной ответственностью \\\"Кубань-Вино\\\"",
                "ShortName": "ООО \\\"Кубань-Вино\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "190.00",
        "FARegId": "FA-000000049902606",
        "F2RegId": "FB-000005440554745",
        "AlcCode": "0100607020250000045",
        "Capacity": "0.750",
        "AlcVolume": "10.500",
        "ProductVCode": "440",
        "FullName": "Вино игристое полусладкое белое \\\"РОССИЙСКОЕ ИГРИСТОЕ ПРЕМИУМ\\\"",
        "ShortName": null,
        "marks": [
            "19330333237007022200157H273G6JQJ6ENB6VSHBZTRER4LMKCEWPSYM5UIA25ZXHNR57HLPKUTYSSRFYCBWWHUZUMHW6LOMVSXOOVS3EK4QTT3LJA5OBMULUTP2LN7P62XUOY3Q5DJHSCWLUXZMA",
            "193303332370760222001Q4WUITBOWYSHQ5ITTWN7T3BYT4XMBTP54AVFWERHKUMH3TRMYGLCCV4PD3TCXNOHZO64YZDMONQTLXI4MVKJOKMJFMPNXOFO7VCIPDVVH77Z4FTEWAMQPNA47VE2MVZ4Y",
            "193303332370800222001L5XZBT4DUXMZOWERCBYQW2W7AQ6WM5LNM3D5TI2IOO3FKE53ZGV6LRGSXCAZZ723Q4BEZ2AWSEXMPWXAPV3CVMT4POKD7QT66PILHKAQ5PEGLBU5THI5M4DM6NI3HTLZQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ставропольский Край,,,,,,,Минераловодский городской округ, поселок Первомайский, ул. Производственная | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем,  литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563 | строение 11/1, цех по производству натуральных вин, литер А, S=1154,9 кв.м, кадастровый номер 26:24:030101:253; строение 11/2, цех по производству шампанских, игристых и газированных вин с винохранилищем, литер К, S=1023,4 кв.м, кадастровый номер 26:24:030101:564; строение 11/3, спиртохранилище с приемно-отпускным отделением, литер Д, S=174,3 кв.м, 26:24:030101:566; строение 11/4, нежилое здание, S=201,9 кв.м, кадастровый номер 26:24:030101:665; строение 11/7, нежилое здание, S=13,0 кв.м, кадастровый номер 26:24:030101:563",
                    "RegionCode": "26"
                },
                "INN": "2630800592",
                "KPP": "263045002",
                "ClientRegId": "010060702025",
                "FullName": "Общество с ограниченной ответственностью \\\"Минераловодский винзавод\\\"",
                "ShortName": "ООО \\\"Минераловодский винзавод\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "195.00",
        "FARegId": "FA-000000049702063",
        "F2RegId": "FB-000005440554746",
        "AlcCode": "0100000002030000128",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "46111",
        "FullName": "Плодовый алкогольный напиток газированный полусладкий \\\"Лаветти Айс\\\"",
        "ShortName": null,
        "marks": [
            "190300678080921120001XKV6FULYONCBO6T3SJIUNUGFRUTSY5AFULF7C2GKWF53SVMIJIBF7WNRADEFFV7UAT4X35WKHMFE7I4QT7IAUZA5ZIF4ZCV5PEJGWYUIN3SF5FQXBCNLY6J7KQHRMTU4A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "257.00",
        "FARegId": "FA-000000049562948",
        "F2RegId": "FB-000005529374575",
        "AlcCode": "0010249000002494599",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"БЕЛАЯ КРЕПОСТЬ\\\"",
        "ShortName": null,
        "marks": [
            "187411503913140522001WPB7WYHYJFPM2UMZJDZIITZLWE4NYYUY7LPL7HNK6YQU2MFEITHUVLUZPYHHDEQAEGMZWC5NRMZBVRV6PAOUVFYNWAT4MOTYZGUZ2LUXIGPKE76D4WX5JXU5Z22U7SJ2Q",
            "1874115039133205220015HUE4T4SIHXEMX2PGL7TIHPLHIDZN66VJF7UL3N2JYHNW4BWN5HR4IGIVJY67ZIZCKWCPP7HVDCIHXBP2S5FCZDEQ5EVOB4Q5WYXM3QJ76AHYZXVLQ522PTBYMEDIRH6I",
            "187411503918000522001BJBO5JPAVWTK3IEXFETQLIN36Y5A4C5IV5ZGOOXIXKQL2JFTD62YCUGAZL5R45RXXCTDYL25A4MNFGBCCL5TS6W2J2YY6EAO73SM5X3SEBQKXBFDBQS3PARZHTXPPPNXI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "276.50",
        "FARegId": "FA-000000050032950",
        "F2RegId": "FB-000005529374576",
        "AlcCode": "0100000005410000036",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"БЕЛЕБЕЕВСКАЯ КЛАССИЧЕСКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "1873124189453903220013FZMBW3IJIU4DTKOD4KTKKTYG43U6X74OJ7THPIJKJSBINBKMXDXCA3NZQXMTO4GEFOUEPRXVHOGBM5LXQPOTVH2CKYOXGA7OXNWVSKBKMQQDHZPVXXG6SPY5B5HJ5TNI",
            "187312418945420322001SAYVE2OBHR5XMC43C3E4OFURIM42UTFUHYS7RXLTI5WV3E4MEKVA5EKZMZMTZS3TMKEOURH4EVJ6AP63YB5WGUP7VP3HNDQULE54SZIMZOVPWGXKMKZOU2KMWN5A744WI",
            "187312418945440322001N2CNYDZPVJRBNUDB7VJI5XJ4SAOTEKB5D3WWIABIE4ZBEZYYUH4I2WP55Z5MWJFMMIELYJYZ63NJAM7IKPJAQKJUFX2UL57AOKGLS4X4XIDQBONJ6HKNII5ZOYRHYJPVA",
            "187312418945450322001VZPKQDZGOUAXQ7DS3HT4R7DZUQWKW6C7TXPRSVNWVYLF3NY4AGCBJC2F4BR46HFXCUTLTGFQD7DNJA7LADT3KKJNFHWD75UHOY74W6JYTXCZVCLQSWNKE4FPJMQS7RVPY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "296.55",
        "FARegId": "FA-000000049591566",
        "F2RegId": "FB-000005579909429",
        "AlcCode": "0100000054580000107",
        "Capacity": "0.500",
        "AlcVolume": "35.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\\"СИБИРСКИЙ. ПЯТЬ ОЗЕР\\\"",
        "ShortName": null,
        "marks": [
            "1873098565373001220013C2OJNULSW7X3VNOOPQOUU7X7MH5GB7BJHT72UEYQLIVGTCVQQXYM4PB2ZOUJ332I5LTPTMROUUBQLFEGU5QUO36UMQBHAR52WTGFA4M6CL5LRJ3FP5VBTR3COSMPVRHA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "152.00",
        "FARegId": "FA-000000050697088",
        "F2RegId": "FB-000005734992006",
        "AlcCode": "0100606966550000003",
        "Capacity": "1.000",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\\"ГУСТАРЕ\\\"",
        "ShortName": null,
        "marks": [
            "192405808357061022001NMDQDQQERGVPLNGY46DMHMUGQESC62ZRHD5FEO22KOXPXSWNV5Q3EPHCTE7TJ3FGET65NLQ5CRPL65W2KOHWDCFF5AQBZ3KNBIMIU7RD2232AA6JSPNFJKDPPHZYRMMBY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ленинградская Область,,,,,,Волховский р-н, Волхов г,,Вокзальная ул, д. 11 | литер А пом. 2, 3, 21, 22, 45-47, кадастровый номер 47:12:0201004:118, Административно-бытовой корпус, общая площадь 93,4 кв.м; литер Б пом. 23, 30-35, 41, 47-51, кадастровый номер 47:12:0201004:233, Реконструкция главного корпуса под производство алкогольной продукции, назначение: нежилое, площадь помещений 2220,8 кв.м; литер Д пом. 1, 2, кадастровый номер 47:12:0201004:116, Автовесовая, площадь помещений 89,3 кв.м; литер П, кадастровый номер 47:12:0000000:2789, Склад готовой продукции вместимостью 50 тыс. дал, площадь помещений 989,4 кв.м; литер Р, кадастровый номер 47:12:0201004:226, Склад готовой продукции вместимостью 7,5 тыс. дал, площадь помещений 476,2 кв.м; литер С, кадастровый номер 47:12:0201004:225, Склад для хранения готовой продукции, площадь помещений 939,8 кв.м | литер А, литер Б, помещения №№ 21-25, 30-37, 40, 41, 45, 47-51,литер Д, помещения №№ 1, 2, литер П, литер Р, литер С | литер А, пом. 2, 3, 21, 22, 45-47, кадастровый номер 47:12:0201004:118, Административно-бытовой корпус, общая площадь 93,4 кв.м; литер Б, пом. 23, 30-33, 35, 37, 47-51, кадастровый номер 47:12:0201004:233, Реконструкция главного корпуса под производство алкогольной продукции, площадь помещений 2210,0 кв. м; литер Д, пом. 1, 2, кадастровый номер 47:12:0201004:116, Автовесовая, площадь помещений 89,3 кв. м; литер П, кадастровый номер 47:12:0000000:2789, Склад готовой продукции вместимостью 50 тыс. дал, площадь помещений 989,4 кв. м; литер Р, кадастровый номер 47:12:0201004:226, Склад готовой продукции вместимостью 7,5 тыс. дал, площадь помещений 476,2 кв. м; литер С, кадастровый номер 47:12:0201004:225, Склад для хранения готовой продукции, площадь помещений 939,8 кв. м)",
                    "RegionCode": "47"
                },
                "INN": "4702012163",
                "KPP": "470245002",
                "ClientRegId": "010060696655",
                "FullName": "Общество с ограниченной ответственностью \\\"ВИЛАШ-Комбинат шампанских вин\\\"",
                "ShortName": "ООО \\\"ВИЛАШ-КШВ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "152.00",
        "FARegId": "FA-000000050752869",
        "F2RegId": "FB-000005734992008",
        "AlcCode": "0100606966550000001",
        "Capacity": "1.000",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое белое \\\"ГУСТАРЕ\\\"",
        "ShortName": null,
        "marks": [
            "192405764502261022001ETGJYBYVAS54XYSH3MUN4ZOP545VHGVUP62ZFDO6Q3HE7ETDUG32YBQEKYSRQUVH5GVQCCLA5JKSDBFK3TTT3FPEURU4HY5SUWINJT6OV3J3Y2K2XK6YEWUHMZZBELOYI",
            "192405764502271022001VBTI2YVT357JHV6FFWBDEPZGZE3YEEG7XQDIYNJ4K2TKDVHROXFSTAN4DFYCZLZLZD4YJWT3E7ROBGDRG4M4GTA5EWJX3YZLMS6XAI6FKQLHG2VESA5UFVZQ2B6NUKMIA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ленинградская Область,,,,,,Волховский р-н, Волхов г,,Вокзальная ул, д. 11 | литер А пом. 2, 3, 21, 22, 45-47, кадастровый номер 47:12:0201004:118, Административно-бытовой корпус, общая площадь 93,4 кв.м; литер Б пом. 23, 30-35, 41, 47-51, кадастровый номер 47:12:0201004:233, Реконструкция главного корпуса под производство алкогольной продукции, назначение: нежилое, площадь помещений 2220,8 кв.м; литер Д пом. 1, 2, кадастровый номер 47:12:0201004:116, Автовесовая, площадь помещений 89,3 кв.м; литер П, кадастровый номер 47:12:0000000:2789, Склад готовой продукции вместимостью 50 тыс. дал, площадь помещений 989,4 кв.м; литер Р, кадастровый номер 47:12:0201004:226, Склад готовой продукции вместимостью 7,5 тыс. дал, площадь помещений 476,2 кв.м; литер С, кадастровый номер 47:12:0201004:225, Склад для хранения готовой продукции, площадь помещений 939,8 кв.м | литер А, литер Б, помещения №№ 21-25, 30-37, 40, 41, 45, 47-51,литер Д, помещения №№ 1, 2, литер П, литер Р, литер С | литер А, пом. 2, 3, 21, 22, 45-47, кадастровый номер 47:12:0201004:118, Административно-бытовой корпус, общая площадь 93,4 кв.м; литер Б, пом. 23, 30-33, 35, 37, 47-51, кадастровый номер 47:12:0201004:233, Реконструкция главного корпуса под производство алкогольной продукции, площадь помещений 2210,0 кв. м; литер Д, пом. 1, 2, кадастровый номер 47:12:0201004:116, Автовесовая, площадь помещений 89,3 кв. м; литер П, кадастровый номер 47:12:0000000:2789, Склад готовой продукции вместимостью 50 тыс. дал, площадь помещений 989,4 кв. м; литер Р, кадастровый номер 47:12:0201004:226, Склад готовой продукции вместимостью 7,5 тыс. дал, площадь помещений 476,2 кв. м; литер С, кадастровый номер 47:12:0201004:225, Склад для хранения готовой продукции, площадь помещений 939,8 кв. м)",
                    "RegionCode": "47"
                },
                "INN": "4702012163",
                "KPP": "470245002",
                "ClientRegId": "010060696655",
                "FullName": "Общество с ограниченной ответственностью \\\"ВИЛАШ-Комбинат шампанских вин\\\"",
                "ShortName": "ООО \\\"ВИЛАШ-КШВ\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "97.50",
        "FARegId": "FA-000000050646516",
        "F2RegId": "FB-000005858003300",
        "AlcCode": "0100000003130000011",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\\"Ардели\\\"",
        "ShortName": null,
        "marks": [
            "197403442640790322001SYV75F2ZCGIMZJKJ34EVEDQV6AZ3VJYHAWEEBGQJ3RLMSSF7ZIKMCEGGIH7EVLMKITIQKC3WF3MTEKZUEEJPE3BTIQKLE5PGWHT3ASZB4TXDLDTBLSW7NRL2W2RDJU4LI",
            "1974034426408903220013NVINIC2YYHOHLP6HFQ2UX7ISMWSB4AFROYWDGUDBA3L56VPDM7FKHWU2QQ6GYLDUHKRWVH3JJSHSIGFR3BRUA6ETBEINSO26R7U2IZ2A3UIZQN364LBCACB566L7M6VY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Пермский Край,,,,,,,г.о. Пермский, г. Пермь, ул. Героев Хасана, д. 104 | Литер Б; Литер Б2, этаж 2, помещения №№ 15 – 17, 31, 33; Литер Б3; Литер Г3; Литер Г5; Литер Д, этаж 1, помещения №№ 5 – 7; Литер Е; Литер И; к. Б",
                    "RegionCode": "59"
                },
                "INN": "5904101820",
                "KPP": "590401001",
                "ClientRegId": "010000000313",
                "FullName": "Акционерное общество \\\"Бастион осн. 1942 г.\\\"",
                "ShortName": "АО \\\"Бастион\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "281.50",
        "FARegId": "FA-000000050091796",
        "F2RegId": "FB-000005931113235",
        "AlcCode": "0100000005410000032",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ИЛЛЮЗИОН\\\"",
        "ShortName": null,
        "marks": [
            "187313293966190722001XF4GAJZO2ANVM7LH47XZTZJW4MZUEHIHGED5NX6IW36I4RAL7WTVY3TFFJ5HAUEH3MUCOGOJTDU4GRSZLLYGBUGQSKKYYXQBMDEGUUSXRWSFXQ2AS7OICOVD6AKDVLPWA",
            "187313293966200722001R6NIT4EUBD6ISH2S5TJTTR3YEMRH667CYRR7UO5EWMLWAVKIWCXME5S5VSXQ4MSAIXDWFG5HTNTARVTJVDNR6DSZQU7KUW3ZMDD2WVIDW6L5UXZXJTV5XGAYYLRQYOA5Y",
            "187313293966210722001W2VLHZCBBS25NNMUYAKYKPTFHUXXAP5G2AN227Z5ZPQ7IHO5QT6APDVI6NYTAANE2VRIIHABDI5LKALO4G6OYRPLVXODJ6NVYE5S4DRYIVAEV7XWOAQQ52ERJKUKYMPBA",
            "187313293966250722001HQZMMYZEJGE2PMBATVLJHCZFGYZAK32IMNGFMN2FGJEEY5BGXY4J55K454PPFBBX7Z4M23OKQMWCJBWEWAX4XXPHUOWH4XNKYA76OG2VJGMJCXT4HTYVRTJAKDPRDOXHY",
            "187313293966290722001QQ2PTVBZMLGZB5R7ZSTZ7LBWLAXD7JHAMARA6NEQWX46GY3KO55KGTS4CDPRPNGD4ULJQ7BBZVEZ4JIESTNBL3YJ4FSPWI3UM2U5E4R34LM22TEAEMVQWUYIGZUOWLGHQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "195.00",
        "FARegId": "FA-000000051004256",
        "F2RegId": "FB-000005931113239",
        "AlcCode": "0100000002030000128",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "46111",
        "FullName": "Плодовый алкогольный напиток газированный полусладкий \\\"Лаветти Айс\\\"",
        "ShortName": null,
        "marks": [
            "190301062308790121001VT5HUSS2WARMWJIGVWVU6ZOAXEUN4AEU4UBYTVPTXJFA2NSITOXHTGOXL6RGSM4COY3VHXDMOUDRZEHTHFT6P56VAHEGGWL7HUJFWU6AU3TDS6EM4GNLNLIDN45UWVSTI",
            "190301062308800121001A5WGDQWWGONHPWUKVCDM2TIA4IGG24L2IOICJ3ZFSFOBZNBSOP7EXQP3Z624G2J5JD63PYGIZPSKXGQP5EVGRZKDFVSW25O7EY2A5W3HZM6IUEOYHGZW7P7UWSJFAK4DY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "300.00",
        "FARegId": "FA-000000047950209",
        "F2RegId": "FB-000006014864413",
        "AlcCode": "0000000000040404984",
        "Capacity": "0.750",
        "AlcVolume": "12.000",
        "ProductVCode": "403",
        "FullName": "Вино столовое белое полусладкое \\\"Алазанская Долина\\\", серия \\\"Kavkasioni\\\" (Кавкасиони)",
        "ShortName": null,
        "marks": [
            "236300073674681018001KWQGI75SOZEER2OVTFQKBPASHQCOS6HQUX6D23SKGTCIVYPMFTGC4KKNTXHZOC7BUOGBKEZV3B4PDUV2M5D7U3TUSKYKLSLKSXI54WZSVUDJGMTKDO6RAATPVMNVRIELI",
            "236300073674721018001NK57D6EN5KJKUFRQZNTNPJ3M7UOWIE7WRKLEMC5UTY6YT3IYUHHQB74W7RNL5WXT46LUS5CHPL3FA3VB6TVLC52TJSNFSPXVXTGFDIHM72XXY6V734VZQJTGC6U5RNZPQ"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "268",
                    "description": "ул. Юмашева д. 27, 0198, г. Тбилиси, ГРУЗИЯ."
                },
                "ClientRegId": "050000061057",
                "FullName": "ООО \\\"ГЛАВСПИРТПРОМ\\\"",
                "ShortName": "ООО ГЛАВСПИРТПРОМ"
            }
        },
        "quantity": 2
    },
    {
        "price": "140.00",
        "FARegId": "FA-000000050062027",
        "F2RegId": "FB-000006014864414",
        "AlcCode": "0100000005470000141",
        "Capacity": "0.960",
        "AlcVolume": "10.500",
        "ProductVCode": "4213",
        "FullName": "ПЛОДОВАЯ АЛКОГОЛЬНАЯ ПРОДУКЦИЯ ПОЛУСЛАДКАЯ \\\"КРЫМСКАЯ АЭЛИТА БЕЛОЕ\\\"",
        "ShortName": null,
        "marks": [
            "1954005292307511200014QGQJ2QN2ODQWGG7OO2HNMB4G47UVQK6U6GWPJDUPEIJ2ZRNCETRPPHDWENUPM36ZNEROHFEXGR4F4QZ2SYTFAH7RIWD2KJTJVQEMLMCAR3AJ3QBTVEOHNJDOQFUAMS4I",
            "195400529231441120001EL6FEBVDCA2243NKVYFPX7NRFYWSUIM5O2TU4L2NZDA3YTI7QS5ZLUP62ZZP5TOKBWX77SMGBCF2L6W6AAX2SGYOCKFI7VDFBFQD4UFCGCI7OFRJTBDVQSEHFWVN5W7GI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Пензенская Область,,,,,,Нижний Ломов г, ул. Урицкого, 129",
                    "RegionCode": "58"
                },
                "INN": "5837025458",
                "KPP": "582702001",
                "ClientRegId": "010000000547",
                "FullName": "филиал общества с ограниченной ответственностью \\\"Объединенные пензенские водочные заводы\\\" Нижнеломовский ликеро-водочный завод (Нижнеломовский ЛВЗ)",
                "ShortName": "филиал ООО \\\"Объединенные пензенские ЛВЗ\\\" Нижнеломовский ликеро-в"
            }
        },
        "quantity": 2
    },
    {
        "price": "194.00",
        "FARegId": "FA-000000049745838",
        "F2RegId": "FB-000006014864416",
        "AlcCode": "0100606973030000125",
        "Capacity": "1.000",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое белое \\\"Шардоне Оригинальное \\\"",
        "ShortName": null,
        "marks": [
            "1923066238473305220014I3OA4O3VZSHVGWO52K7H4EUYQ3HIHORALLTCE7F4BZ7VOWA3C2VAPA3QWH3GTY3XY2UZHQLB3UXIWR6RZS3K5GD6NUMJM3A5WI223AXRIXN6UZIBU5LYRBS4WLZFZXFQ",
            "1923066238473405220017J6ZXLV7YYETWTX4RHRKEQBIIEJ7ERAJFFL3T52L4LOUI6C5NX2WTMXDBOFX44265Q6TNH5FN5DUDIVX3VFGRP3JCEULNCCNKK4O2SJFIBQRSAHCMRLCJIHM62HTR7K5I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,,,,,,,Темрюкский муниципальный район, Старотитаровское сельское поселение, станица Старотитаровская, улица Ростовская, 190А",
                    "RegionCode": "23"
                },
                "INN": "2352033467",
                "KPP": "235245002",
                "ClientRegId": "010060697303",
                "FullName": "Общество с ограниченной ответственностью \\\"Прохлада\\\"",
                "ShortName": "ООО \\\"Прохлада\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "336.38",
        "FARegId": "FA-000000050399551",
        "F2RegId": "FB-000006014864425",
        "AlcCode": "0100000003150000024",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"СОРМОВСКАЯ ЛЮКС СОЛОДОВАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187415329436491122001LARGQDJUJAU77UFN2N5RZ5DLWMMHJJCMJ7J2V7D7IEG7LSLGYWCNZOWJWS4UC5GNZSNEHCGI3T4XKDCNMXJUZKFODUEAPMBKPUAW6S6RBEU4HANYXFD5S7AJOIISLBGOQ",
            "187415329436531122001OK36AL33VRWXYAKFUSUGTERQX4MWKJC2FGDSMRJM4VMJIOYJWQ56NT3TV7XC6AE3DZ2MVHZ4RUFAKDBGMN35VLAXEQIKMGTB4EELECC4JF7HFUETMBU7KJLH6A7WIAITI",
            "187415329436601122001VGYDYZWS4XGPJDNTWH5ACI3VMQLR4KYIMU3MHVEQ5BJE5CKOUMHR2C277D3SP7GRGWZYYT4DL3MPP5DHYUD2LU5DMODZYQJFOYCOUH5E3WPOHZQS2MWOOHPMJFVLUGKQQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Нижегородская Область,,Нижний Новгород Город,,,,Сормовский район, ул. Федосеенко, д. 47 | отдельно стоящее нежилое здание (литер И, И1), литер И, этаж 1, помещения №№ 41-43, 45, 64, 65, 81-83, 88, 90-93, 100-105, 110, 115-118, 235, 237, 237б, 238, этаж антресоль, помещения №№ 141, 144, 152; спиртохранилище (литер Д), нежилое здание; отдельно стоящее нежилое здание (литер Ю), этаж 1, помещения №№ 1-3, этаж 2, помещения №№ 1-10; склад № 2, нежилое здание (литер Я), этаж 1, помещения №№ 1-4 | полуприцеп цистерна CARDI M310 01TC, ГРЗ ВВ 3767 52 RUS",
                    "RegionCode": "52"
                },
                "INN": "5263043395",
                "KPP": "526301001",
                "ClientRegId": "010000000315",
                "FullName": "Общество с ограниченной ответственностью \\\"СОРДИС\\\"",
                "ShortName": "ООО \\\"СОРДИС\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "155.00",
        "FARegId": "FA-000000051104604",
        "F2RegId": "FB-000006014864426",
        "AlcCode": "0100000010250000018",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТАЙГА\\\"",
        "ShortName": null,
        "marks": [
            "198409874510091222001DXBHL5SMYXAR27FRKACXGZXGYAE4XIVAWKVYM6RHW5BEPFAN7TL5XEVSLY2JTS33WZ25AUV74IRMMQ7MM4RWAH5GBDOCOVGQJZY4L3PI7LNNR7V7XC2Z62OIS3YGR7GCQ",
            "198409874510111222001FMSV6SZDTSBYS3PU2KD7LQGRH4G62WJF63OPJTNXAAQGC2XSQPZS54HQBFADXMYHJQOYIUZBAA3227Z6YN7VYILFVAWCUZS2TPKY6ZK537WPF6GFUNG7RSFVM5FOVX55Q",
            "1984098745102812220015OXN4QVZ2XW5M32YOI7NA44AJUMR2Z6BHTLG72BLKON5DOHJX557TC5FJGACUKJXKFZ6VSBL7BDJ5GQJQRYFKS5RDCBV25WAJSO7FROFIRGOGCDLPGPFZUEH2CQDPZTJA",
            "198409874777681222001X5NWNI3WYMHBATYTT6KGEJO2DQGMCGCOGBA3KVYCLJUTXP5GA36M3XQRJCXLWTQTMEVLUNGCJ4XAE5FJYLLYYCJYSKJYUJGIMVBSIQQ5UCBQBYKQJ2A2RZHE6YMCYIOCY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "299.00",
        "FARegId": "FA-000000050835999",
        "F2RegId": "FB-000006014864427",
        "AlcCode": "0100000010250000036",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТАЙГА\\\"",
        "ShortName": null,
        "marks": [
            "187416634930491222001VW3FQZMQDXAAZF3QSJMQGOHAYIWAWOBFCMNN4WYQQ7ZEGHEW73PSW3EAFUSMU74BWCITKF23IVZFOMMKXXVI3UJN7Q4R7VTWJYWNUOBMSWDMZVF7OKXWSH3KM52Y6OA7Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "157.76",
        "FARegId": "FA-000000051201435",
        "F2RegId": "FB-000006014864428",
        "AlcCode": "0100000004970000167",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Царь»",
        "ShortName": null,
        "marks": [
            "198409850431601222001YSB3XESQVQGF3DXQLXUSSQUD6ARCJABYX7G6C2Y5SZE54YPMDNVRB4HUYYRAEZAPXEU5LGUBJ7LKN2JH7L5KXOJMVUVSWX5TTYAQD2DIQLIXBQ6IVTCSWKY343Y7OL6BI",
            "198409850432751222001UBEPFAOKEPBCVCG4P3JN43WZ3M7N46IBHYPERYN2DHZHFK2ETXRXZOAX4VIEWAFFHDPFOIPQ5ZHIJOBRBO2HDLZSTADKHMYCJ6WLA6SDYVOLR5N6BL2IG3JBR5JQ3TLSA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Краснознаменск Город,,Строителей Улица,15 Дом  , | литера Б10;  корпус 1, литера Б3, этаж 1, помещения №№ 12-15, 20, 41, 43; корпус 2, строение 1, литера Б14; корпус 2, строение 2, литера Б9; корпус 2, строение 3, литера Б12; корп.2, стр. 5, корпус 3, литера Б5, этаж 1, помещение № 1; корпус 5, литеры Б, Б2, Б6, Б8, Б13, литера Б7, этаж 1, помещение № 35; корпус 6, литера Б10; корпус 8, литера Б1",
                    "RegionCode": "50"
                },
                "INN": "5006008213",
                "KPP": "500601001",
                "ClientRegId": "010000000497",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Георгиевский. Традиции качества\\\"",
                "ShortName": "ООО \\\"Георгиевский\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "499.00",
        "FARegId": "FA-000000050689590",
        "F2RegId": "FB-000006014864432",
        "AlcCode": "0100606880350000011",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\\"Армянский коньяк Виват Армения пятилетний\\\"",
        "ShortName": null,
        "marks": [
            "187312090203240322001HMRYQTQUV6CVTLGVLLSHS5IIZ4JTZ4WPQBPDWS5PCCUI3BD3W6Y4NNXOACGJEI32FJQADC7ZWVOB76F5FXC54MMXTJLK56B3K4EJ63NIZXJKJEU34KF5K244ICTCAVPVY",
            "187312090203490322001B32YM4LKD5DJU4FMR3AYNAFPQMJ7B35IDSPRD2URMOOZVLJVZKEZAENJFOBFVYEFI44PPH72VCL6GWUNCOPRNFDTD76OEG5DIKZTZBNGWRFWOVWMWAUN2TE2RK5L3FUIQ"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\\"Гетапский вино коньячный завод\\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 2
    },
    {
        "price": "473.00",
        "FARegId": "FA-000000049615494",
        "F2RegId": "FB-000006014864433",
        "AlcCode": "0100606880350000021",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\\"Армянский коньяк Трехлетний\\\" (матовая бутылка)",
        "ShortName": null,
        "marks": [
            "187309047312380122001CI3HBWCXQZGXAE5WIFTFRZLLFUSWSRYXIJZ5KUOQPFAQAKNHTMSH3K5WNWWLA2MFPLV5CU2ZKDU37M4GX42F2RBMX2FJEHBQH5FBAWSWGDK6QDMD2QCRI7AP6H5LMK62I"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\\"Гетапский вино коньячный завод\\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 1
    },
    {
        "price": "480.82",
        "FARegId": "FA-000000050000391",
        "F2RegId": "FB-000006014864434",
        "AlcCode": "0100606976140000231",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный трехлетний \\\"Сокровище Тифлиса\\\"",
        "ShortName": null,
        "marks": [
            "187405579468661021001CZDH4JBGJTSZBRCBHO7NCFJRUMGAMZGDVKRT5HGON27C5WNXMIR7DHB4GHG53VJSSV53CFCTX4WNH7DMVKLCBXQ7NPM5Q4CBF5XBLMXTXO3QYINGDLBYVYKY2PMFFEN6I",
            "187405579468871021001KSYDOZAK4NHFFWN4M4GTTLNSEMWUDB25IU3PX45KBBVZVCHJOHZQDTGVPBDOX3ZGCKMUXYONEI47YEJ57ZJ3W63WZPNJ4I5HHD7ZKQDUUCGGLWGXSDYKRKXUXJXWLMFYI"
        ],
        "Producer": {
            "FO": {
                "address": {
                    "Country": "268",
                    "description": "Грузия, Гурджаани, 1500 ул. К. Короглишвили 38"
                },
                "ClientRegId": "050000043851",
                "FullName": "А.О. \\\"Котехи-Гурджаанский винзавод\\\"",
                "ShortName": "Котехи-ГурджаанскийВинз"
            }
        },
        "quantity": 2
    },
    {
        "price": "607.26",
        "FARegId": "FA-000000050793218",
        "F2RegId": "FB-000006014864435",
        "AlcCode": "0100606976140000233",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный трехлетний \\\"НОЙ ТРАДИЦИОННЫЙ\\\"",
        "ShortName": null,
        "marks": [
            "187415903771381122001OT62VEAPVHKIL7T6KIVCY7IFCA75XEWSVDMIU6ASHGZPWETTZJGXQXVNDA6FWSU6QKFG27TDXIKVE2VCKUOKB64RSBVG3NFMIXZTPPBTIOPTVNK2VOH5M3S4HJ4PKQWYQ",
            "187415903771411122001LH3FCVJDK7A6FKHIULRLNWBF4EI6FKYK4COQF5FZNO42UNILCJ7PEYBIUTYVGJ44GB2EQX2CD4FTUXXFPOOGNYV5DSHQUOEOJGDLUR6F7KFEAOD7UFXK2KP6LNBTLKUYA"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "0015,Республика Армения, г. Ереван , проспект Адмирала Исакова 9"
                },
                "ClientRegId": "050000057869",
                "FullName": "ОТКРЫТОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО ЕРЕВАНСКИЙ КОНЬЯЧНО-ВИННО-ВОДОЧНЫЙ КОМБИНАТ АРАРАТ",
                "ShortName": "ОАО ЕКВВК АРАРАТ"
            }
        },
        "quantity": 2
    },
    {
        "price": "428.00",
        "FARegId": "FA-000000050668087",
        "F2RegId": "FB-000006014864436",
        "AlcCode": "0100606922330000045",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний «ПЯТЬ ЗВЕЗДОЧЕК»",
        "ShortName": null,
        "marks": [
            "187416785938121222001CPHIXFS5QI3DGDYIOCGR7EFEMI4X4CAJBR2TQUS2B4UG6IXFOWL72VU5WK5TIN7ZTSWKOBI5VLCLLHBGPZF265P2FO67KHWQIPM33IBSS4GQN24BMI4H6KOJ4BZBKMDMQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,МОСКОВСКАЯ ОБЛ,,Долгопрудный г,Шереметьевский мкр,Южная ул,д. 1,, | корп. 21; корп. 21, строен. 1; корп. 21а; корп. 21б",
                    "RegionCode": "50"
                },
                "INN": "7722809347",
                "KPP": "504701001",
                "ClientRegId": "010060692233",
                "FullName": "Общество с ограниченной ответственностью ВКЗ \\\"Шереметьевский\\\"",
                "ShortName": "ООО ВКЗ \\\"Шереметьевский\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "154.28",
        "FARegId": "FA-000000051079939",
        "F2RegId": "FB-000006066737395",
        "AlcCode": "0100000004970000154",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Беленькая Золотая на спирте «Альфа»",
        "ShortName": null,
        "marks": [
            "198409856589241222001UVWBNXXI3YOOYLFOGKCY76S4CIY67DRW5X3O2LWQWE6A33ULEANVUWYXD73FOTKYI2PYI5GIUGEVRD63KWE2A3PXGZLIDVNPF3I4OCUSNDJFN7WXNNMQEYTPFETWBCH3A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Краснознаменск Город,,Строителей Улица,15 Дом  , | литера Б10;  корпус 1, литера Б3, этаж 1, помещения №№ 12-15, 20, 41, 43; корпус 2, строение 1, литера Б14; корпус 2, строение 2, литера Б9; корпус 2, строение 3, литера Б12; корп.2, стр. 5, корпус 3, литера Б5, этаж 1, помещение № 1; корпус 5, литеры Б, Б2, Б6, Б8, Б13, литера Б7, этаж 1, помещение № 35; корпус 6, литера Б10; корпус 8, литера Б1",
                    "RegionCode": "50"
                },
                "INN": "5006008213",
                "KPP": "500601001",
                "ClientRegId": "010000000497",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Георгиевский. Традиции качества\\\"",
                "ShortName": "ООО \\\"Георгиевский\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "241.20",
        "FARegId": "FA-000000051368661",
        "F2RegId": "FB-000006108574181",
        "AlcCode": "0100000054580000091",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"КЕДРОВИЦА КЕДРОВАЯ МЯГКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187316725264471222001HSPPWFR5PCBWBTOYDVBUAF2RWQN627ROEYAM4PVFZL27SGL3FYCJFWP55BTCIRKM27NY2IIC3ETYVACEQA77G57L26QWYXWJVINFKWM4F6ASXVQ2RZTIZLXC2LZOE3EJI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000051105702",
        "F2RegId": "FB-000006108574182",
        "AlcCode": "0300003247940000052",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Берёзовый рай\\\"",
        "ShortName": null,
        "marks": [
            "1873167462956812220015HOUGR5NZKMK3KMIQC5WFR5ASUGQ2NP57QQBIPTNM6IT4C54WNSXJQREPN6R34EQSVNUUDRCX6V7NIAY64VZXARZJHPSCWUARAD7IL3JJCVRX6OQQQ7PV6RCKGCLUBX4Q",
            "187316746295761222001Q7JLUX6P3ZE27LBJKXE6NNLPUMVPTZUJHUGUM56NG7TJJXOTZ2FTOYYGI2CS4JMRI3NULYTEU73UNQTB6AI2KQCJBL7IHWLV2GW7SCJNKBSM6EDOM4LQTB52AVPPFOKDY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Челябинская Область,,Озерск Город,,Кыштымская Улица,30 Дом  , |  | нежилое помещение № 1 (водочное производство), расположенное на первом, втором, третьем этажах в нежилом здании спиртоводочного завода, литер А,А1,А2,А3,А4,А5,а; нежилое помещение № 2 (спиртовое производство), расположенное на первом этаже в нежилом здании спиртоводочного завода, литер А, номера по плану комнат 36 (S=208,9 кв.м), 37 (S=67,3 кв.м)",
                    "RegionCode": "74"
                },
                "INN": "7413022993",
                "KPP": "741301001",
                "ClientRegId": "030000324794",
                "FullName": "Акционерное общество \\\"Озёрский спиртоводочный завод\\\"",
                "ShortName": "АО \\\"ОСВЗ\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "320.16",
        "FARegId": "FA-000000051459683",
        "F2RegId": "FB-000006108574198",
        "AlcCode": "0100000004970000102",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"МЯГКОВ НА СПИРТЕ \\\"АЛЬФА\\\"",
        "ShortName": null,
        "marks": [
            "187317171597171222001HI45YYZO2N2AQDUIGBMGDYLMAI3PPAGZI6CUDAHPHQLMIRCBQBMQWXC2JJEWDRFVDZH7CKKRSPUG372REQOA3Z6YHCVDHC34ARWR4Q42OXKSRU2MR6EF2U2RX7SNPU5GA",
            "187317171597181222001LXNJ7FPGCHPYZEBJIG4X3PSAOY7NZBD6F4IDUI2ETJVMKYSDLDP4LISN55FASNS5BE5AI66GINF7CCKQUSFJUN42KG6JTYBPGCY4E4FIXFQRRR54MYVYTTNLQZAGZ62KA",
            "187317171597191222001RX7F363ZXJHP5EL7BG5ID2IQDM4QHDUSGP4P3KCECNTWXG2BZSI4KAXJ6VJLYEFMR2JCTN5RKHHTOV5N7UVYTYVVI2GNEJPW7VT4S3AIPMAH3IINQT3I4XBJPKOB5ULPI",
            "187317171597211222001E6XJHMIR6F2D35ZHED4ZCU5ON4BPGDCWHCPFUOTPZQW727BPOQF7VXSGRYGEMMES4GKZBHI7YNTDEHLSAVRNCNELCM5N5A3YXBM2JQDDELFGB24VB5KE6O6MDBQBHEFEY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Краснознаменск Город,,Строителей Улица,15 Дом  , | литера Б10;  корпус 1, литера Б3, этаж 1, помещения №№ 12-15, 20, 41, 43; корпус 2, строение 1, литера Б14; корпус 2, строение 2, литера Б9; корпус 2, строение 3, литера Б12; корп.2, стр. 5, корпус 3, литера Б5, этаж 1, помещение № 1; корпус 5, литеры Б, Б2, Б6, Б8, Б13, литера Б7, этаж 1, помещение № 35; корпус 6, литера Б10; корпус 8, литера Б1",
                    "RegionCode": "50"
                },
                "INN": "5006008213",
                "KPP": "500601001",
                "ClientRegId": "010000000497",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Георгиевский. Традиции качества\\\"",
                "ShortName": "ООО \\\"Георгиевский\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "320.16",
        "FARegId": "FA-000000051262206",
        "F2RegId": "FB-000006108574199",
        "AlcCode": "0100000004970000165",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Мягков Серебряная»",
        "ShortName": null,
        "marks": [
            "187316372132541222001J5MYNJ52POTB42JVLRIIYYKV745CLFIFJSREFMLNGM6HIK22EQTSXLSX7C2RCGGI743UT56WP5CCZ3NLUBGJLNBOXWNBVEL547TDEN7NVG5ZJZGAR5767B42D2MVHG3UA",
            "187316372132591222001PKR4Y2WCMGKAB4ZH663QEEIZWMMGQFQSHM3TDXEFBLCNWK3PZ2WESWUUZDOFMYPLO5KJQTFFAJRBSMCDWRQQYHCYGMYI6LWS6BSR65MND6LWWGB2UKIGVOJ24XI35OZKI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Краснознаменск Город,,Строителей Улица,15 Дом  , | литера Б10;  корпус 1, литера Б3, этаж 1, помещения №№ 12-15, 20, 41, 43; корпус 2, строение 1, литера Б14; корпус 2, строение 2, литера Б9; корпус 2, строение 3, литера Б12; корп.2, стр. 5, корпус 3, литера Б5, этаж 1, помещение № 1; корпус 5, литеры Б, Б2, Б6, Б8, Б13, литера Б7, этаж 1, помещение № 35; корпус 6, литера Б10; корпус 8, литера Б1",
                    "RegionCode": "50"
                },
                "INN": "5006008213",
                "KPP": "500601001",
                "ClientRegId": "010000000497",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Георгиевский. Традиции качества\\\"",
                "ShortName": "ООО \\\"Георгиевский\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "297.00",
        "FARegId": "FA-000000051454788",
        "F2RegId": "FB-000006108574204",
        "AlcCode": "0100000020360000105",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ХОРТА-КЛАССИЧЕСКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187316823540421222001FVPNNCY5WWYKK62XMXCK4HUN6YPVKCWGSS4EBSP2WTTO6AALPFYC27WWSPGT4QSC2EVPUNSWB32MCVF3LWEKE4SOFOKK5LTQFJ72DV2PXGRHRZEQPGKDYILHHMG4OXUBQ",
            "187316823541111222001WJMUMGLRY23ZN3OORVADHAR4WIHX3XJNDKFODQEH3MGL55B245SMCC6O7MIJFZ2HHTRJ5KKMPQQ5YKOQNRMAB7XBIAAVC2Z6URM2M3TJTQV6RE7SC3UFXSQ2KN2ELXJSY",
            "1873168235411612220015E2WOURACTJNAMY4RT577HEAQ43UT2EFARG57PCRIKDV3NX3VBS7XQVVTBQC3OOBOVT2R7RU6QBYUH6KTQT35Y4MIDG66HXCYFAO4WATLRQI6JQ5ZIEDBKSEHPSA4E3GI",
            "187316823541181222001PUJ7MZHIFTWK4JE4BXKLFEHTSIXJNEQFH3J5J6YIHHRVU77Y57WKEH2YBTV2AG2SSNK6H24I74IYDKG4WZXU2GGRV6AA4QH73HFG4VV2MMLEG2LUBFHSG27LLA7SFHSOA",
            "1873168235411912220013W2RTIYYZUIUTYZSANGQDCCMAQI3RO6E4SDGC4U6URPJESZGUA57RFGE6QH4XHBYJ2EWXDTDOWG4ZEURU5I4JGVRGDUXWI4PGNBMDQGFCPBLFFXTOO6IY6ITPPKI5GPCQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,Вологда Город,,3 Интернационала Улица,39 Дом  , | - нежилое здание с мезонином: 1 этаж: литера А3 - пом. 5, 6, 9а, 10, 11, 15-20; литера А6 - пом. 3, 3а, 3б, 6а, 9б; литера А7 - пом. 35; литера А8 - пом. 36, 36г; литера А9 - пом. 37, 38; литера А11 - пом. 33, 33а; литера А12 - пом. 30; 2 этаж: литера А3 - пом. 37, 38, 42, 43, 47; литера А5 - пом. 52; литера А6 - пом. 3, 3а; 3 этаж: литера А3 - пом. 8-10, 12, 13; литера А6 - пом. 2; литера А7 - пом. 3; мезонин: литера А13 - пом. 1, 2, 3; - административное здание с проходной и складами: 1 этаж: литера В2 - пом. 2; литера В3 - пом. 3; литера В4 - пом. 5, 7; 2 этаж: литера В5 - пом. 16-18; - здание основного производства: 1 этаж: литера А - пом. 6; литера А1 - пом. 1, 3, 3а, 5, 11; 2 этаж: литера А - пом. 5; литера А1 - пом. 1-4; мансарда: литера А2 - пом. 2, 3; - здание посудного цеха: 1 этаж: литера Ж9 - пом. 1, 1б, 1в; литера Ж6 – пом. 1; - здание кондитерского цеха, 1 этаж: литера Б, пом. 21, 24, 25;",
                    "RegionCode": "35"
                },
                "INN": "4720027123",
                "KPP": "352501001",
                "ClientRegId": "010000002036",
                "FullName": "Общество с ограниченной ответственностью \\\"Русский Север\\\"",
                "ShortName": "ООО \\\"Русский Север\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "267.00",
        "FARegId": "FA-000000051231250",
        "F2RegId": "FB-000006163653912",
        "AlcCode": "0300006431080000158",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"СТУЖА ЛЕДЯНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187418128895971222001O7ZPC6OV5IYOFYBA7HO2HYRT4MZQLVZRRGWSZ2ZMJSCFMZMMSNH4B6MAS65ORZOH72Z4NRWYJPK7FTTRN6VJBDO25G66CW44WJF6USA5XJO5IH4LO3E6MLU5EJ7Y5ZKIQ",
            "187418128896081222001U55L5CORBYVATOVBBDO2MMR6KISIGQD7HF2UCDWS73LR3VOHBBDXO2HBJFPIAPAV2EKHUEWM4HUNSUN66UMNUA4BIYN4H2RDQJLRUFBABWJXLXN3CHO4QKRZVY7EWRHYY",
            "187418128896121222001LWKCCHVTOY7JVKLPEO7ICB3MSUKUGESL5JA6GAFIG2BC5R7RD2OQY7TVA5BLK2GV35TK7FG4L4XV6BD65GZMEU32EJVQBAY6BTD22KXM5BW4O5U57MW6IR5DFELDADJYA",
            "187418128896331222001YFQPZFXUN3TFU6ZFFKIVSWNEZQBK3MBRINC3LBYTTCT6N5QGPH7YMUQJS77ZFKGO4PU5OHVBLFLHSSSGPHGPV6NW37IOU2SB2TN2GCKDBZM5M5ADAXCQSR5CGOFCST2QI",
            "1874181288965012220013GMK76L2IL357RITHGSJ6NNTP436QWZMQZ6IVM3PQUSY44O3EANARGHNDXFJMDL3EI6CZ2LW2R72H6A2WKTATQFHC6LB2FMTFLTQRFWTJYY7LOF2RYMNC7SAFL4NZTJZA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ульяновская Область,,Ульяновск Город,,,Карла Либкнехта Улица,,д. 15 |  | нежилое помещение (S=3008,9 кв.м): помещения подвала: №№ 1-6, 8-13, 15, 16, 19-25; 1 этаж: №№ 1, 3, 5-10, 13-24, 28-35, 49-53, 55-59; 2 этаж: №№ 2-5, 10-23, 29-33, 42-44, 47; здание склада готовой продукции и административного корпуса с пристроем (S=2336,2 кв.м); здание спиртохранилища (S=387,7 кв.м); здание таропосудного цеха (S=613 кв.м); нежилое помещение (S=217,2 кв.м), помещения: 1 этаж - 25, 26, 48, 54; 2 этаж - 34-41; нежилое помещение (S=233,8 кв.м); нежилое помещение (S=672,5 кв.м); здание гаража (S=124,5 кв.м); нежилое здание (S=348,9 кв.м); нежилое здание (S=754,3 кв.м); здание трансформаторной подстанции (S=44,4 кв.м); нежилое здание (S=327,4 кв.м)",
                    "RegionCode": "73"
                },
                "INN": "7327080600",
                "KPP": "732545001",
                "ClientRegId": "030000643108",
                "FullName": "Общество с ограниченной ответственностью \\\"АЛКОГОЛЬНАЯ ПРОИЗВОДСТВЕННАЯ КОМПАНИЯ\\\"",
                "ShortName": "ООО \\\"АПК\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "557.50",
        "FARegId": "FA-000000050043607",
        "F2RegId": "FB-000006163653913",
        "AlcCode": "0300006431080000094",
        "Capacity": "1.000",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"СТУЖА КЕДРОВАЯ\\\"",
        "ShortName": null,
        "marks": [
            "189300526004501120001LW6AQDI6UDZAXWN2MTYUYS47T4ZBVEJCZVZUXD5ZPQHGXFJMR7UU5EPBHPDVW2BQ3TLDV6LRJT4PSGS53KT54LQFAMBURYMZFLQYNMGCUZQCMP6JJUTSG2TTGDJY3GW2Q",
            "189300526004551120001YPY3UB2EXWUKJRYLUP67PTA4UUPZP3YE4XDMSJ7TQHUN2AGYBR3QSOVNRGJAYJ5M6P63CMLBSM63R5Z62QO3XW5Z25K7JKCQ6M23GKQM2BGNJZ5ZLRHT6CK4ORDO5SCKI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ульяновская Область,,Ульяновск Город,,,Карла Либкнехта Улица,,д. 15 |  | нежилое помещение (S=3008,9 кв.м): помещения подвала: №№ 1-6, 8-13, 15, 16, 19-25; 1 этаж: №№ 1, 3, 5-10, 13-24, 28-35, 49-53, 55-59; 2 этаж: №№ 2-5, 10-23, 29-33, 42-44, 47; здание склада готовой продукции и административного корпуса с пристроем (S=2336,2 кв.м); здание спиртохранилища (S=387,7 кв.м); здание таропосудного цеха (S=613 кв.м); нежилое помещение (S=217,2 кв.м), помещения: 1 этаж - 25, 26, 48, 54; 2 этаж - 34-41; нежилое помещение (S=233,8 кв.м); нежилое помещение (S=672,5 кв.м); здание гаража (S=124,5 кв.м); нежилое здание (S=348,9 кв.м); нежилое здание (S=754,3 кв.м); здание трансформаторной подстанции (S=44,4 кв.м); нежилое здание (S=327,4 кв.м)",
                    "RegionCode": "73"
                },
                "INN": "7327080600",
                "KPP": "732545001",
                "ClientRegId": "030000643108",
                "FullName": "Общество с ограниченной ответственностью \\\"АЛКОГОЛЬНАЯ ПРОИЗВОДСТВЕННАЯ КОМПАНИЯ\\\"",
                "ShortName": "ООО \\\"АПК\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "258.00",
        "FARegId": "FA-000000051467106",
        "F2RegId": "FB-000006163653914",
        "AlcCode": "0100000010250000036",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТАЙГА\\\"",
        "ShortName": null,
        "marks": [
            "187418102078531222001NBMC2MSIITIGFEI7HLZZ7JQQLM2RIYCHDW6XTUPMDSRMTOYEBCGX7G2VT6HN3FHMEU25LAFT5RIFD5I3SNSAJG7K6J5TJQDWBZLYXP7J3MFRFJIBHO6OHR7CEOWC4L37A",
            "187418102078541222001KCLJI7ADG3GGW2XJBRY24I37VU6LDFWIP5YK7VLQIIYMBILBY6VK76E35CCLO2ELDPHFEFVEVMZGBYFEUZUA4YI3OJX5TTJKNAVWDSE5DR6GZPBSZTDB7BIH4HDCQCE4I",
            "1874181020785512220017R2FAFIQGFLI6D5FLMFQEXV6AYQ4K5SKLLL75MKHNBYCCKK6T3TB3APMT5SVKMBFXFDR7ZMZI2ZMSBCPZXLMJX62TLI322HAAYZ3JNDX5LYZLBYME2AQUXMSEKKKG3YHY",
            "187418102078571222001JRKMIIKKOBAKOWZ7ZE7IE6XCMEW7QXNH32DDDV6N2ZJB3GITW74MOVRPJLEOR6DAS4FWCOXUUPVV5O76TAVVZGKHKIAGRVUFB7OZXB7AO7LBAISDBXGLXQQPMYHVRWQFA",
            "1874181020798312220016XX4BPJC6ME6REBEUDGKOYHF44ZQVO7FMN3CWVPGC6ZBQUPWT3MBO64CZUEUAB43O36DG3NXU4S3QVE5QGOZOX2MRZSCKZYTTO3DZA24L7PDPT2IIBVPNXFI65W4R5AKY",
            "187418102079861222001PSEYWQIKHNC2QJROH7NO6AGUGME4REH3SPTDFHFRKLBJG26J2O436F3DOYC4VUIELUQMYS4PM523RJKCOROB4AO5SNKOCRPOMHJ2SLL2LZY5CNU4FXJZEEGLOX55J6QOI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000051480709",
        "F2RegId": "FB-000006163653918",
        "AlcCode": "0100606942420000004",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПУЗЫРЁК»",
        "ShortName": null,
        "marks": [
            "187419028111100123001W67EQUKCONXWNOGSMPARVNLYJISUKM5YU4YBTL22X7EJYHM7YRQMXEW6A3UXND5UZZJICYZ7WSZO7HTVIS7EADQOC4AVXOSMOMHGSA3STZRN6SVI63NS7KVHODLHOQWOA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "275.71",
        "FARegId": "FA-000000051766805",
        "F2RegId": "FB-000006165868562",
        "AlcCode": "0100000054580000147",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ПЯТЬ ОЗЕР\\\"",
        "ShortName": null,
        "marks": [
            "187316720057121222001CHDST77TH2MMLWCQVBH6DK52CMN77QU7MBBXQKT23NRZ765X7OEPJRO7GV2JAPPPDAYJOJWBVPJZVKR2WLTXKEZAEVJKY773JLAH6UIUIXXRLLVPXGNJNNVDBA7JXDIVY",
            "1873167200571812220013MARGN7RCGCMCK75MQO4UP5BNILZ5JBFEUP75U4UTO7EFI7SZM2I573QZCPFDKGI77YU4WFKHOOOJTL4X26TUXEBGI7JPAK3Z24SVR3HE22LSGOUTDSNWL4H226IZL2RY",
            "1873167200572912220013HNM3F2ROMKQST6HNNQDZVSLWE67INV7DJWBODTDWWJJOPN7KL5KSA3NPODFOFXAYVYHWBP4O4Z54IR3WGJTFCMJIYZPFFG6OZZDAINZZE3JHGCTALXCA444356LCRS3A",
            "187316720057711222001HSLCNDHHLLHKWXNY62GE4FXGK4AJSEEKX55HAP7D3CW5A5JVY73T66RHNHEZZ5FST5QMZD5PO5JAJMDUZ6P5EQ3CI524DIUYFOFUQ2JPLZKUB7C6DOVVEHU7QJKFVT2AI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "154.00",
        "FARegId": "FA-000000051236196",
        "F2RegId": "FB-000006203516207",
        "AlcCode": "0100606997860000032",
        "Capacity": "1.000",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\\"Совиньон\\\"",
        "ShortName": null,
        "marks": [
            "192310103301611222001S4X35N4HIDRNEUPWBWPNTEEYM4LVG7GT6FW7NNYWJB3WNFKTW5MSZATNSWLLIEJUXPZQNA5FMC4XBEJT3N3COM2SREDLFLJ7RIMOYIT43ZUJGTPFZCBWXSIDBD6WZTWBA",
            "192310103301621222001YQ5VUHDL2U6O7QQL43WTX3IUNMLHTRVB6GD2G67BY37LZTSFMQDNR22ADMWPFYSUUO2RPC2LQSOFCILQ5FT2JDSSZ22OCB7F3U3GJYRKO7UARDPFQISVQ3S7G4KSAT3XI",
            "192310103301791222001CMVEZFOICNL7WZBVHECUU3FT3AFUX5FNJKTUQOHYZO2AKIUA4WXDEHWQMVHFUZ37XLCQX3SPXVSL2FJBDTXUOD6KVBQQ3EQ64T37RIGUQ57IFIDKPTRVX64RRQTF7FWWA",
            "192310103301861222001V25P3LC3FLF7CB3PMRJKEYQ6NEXDJY4MAP5UUZDLJK4BRK6L73UWKQ7Y53JL33JJYQ26NWPLYZZ6QAE6I7RPQN32KCCGSEFN5XACMEGE45UF6W3ZN7S2WEJVXYOGLM4NQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Анапский Район,,Юровка Село,Октябрьская Улица,,1",
                    "RegionCode": "23"
                },
                "INN": "2301076247",
                "KPP": "230145001",
                "ClientRegId": "010060699786",
                "FullName": "Общество с ограниченной ответственностью \\\"Винзавод Юровский\\\"",
                "ShortName": "ООО \\\"Винзавод Юровский\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "154.00",
        "FARegId": "FA-000000051206760",
        "F2RegId": "FB-000006203516208",
        "AlcCode": "0100606997860000046",
        "Capacity": "1.000",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое красное \\\"Изабелла\\\"",
        "ShortName": null,
        "marks": [
            "192310108408601222001BFRI6LLZ2ER2PF7QWUOXPSKXAUFRHSGXR25AWNEGLXAI5I7CZCIQB2QJD3UQXNMLQDPCLDWKVZN4VFIQNRX6AJQCS4VYDGTYPTWWEMFLRWI6RZ2PATSRR2DT2EYP6CGIY",
            "192310108408771222001PMWJLASMXWKMIUNHMUZPAZC2IMHCW66TZ3I6F6CP2RFBSLO7IC2QF463KONYCH24LF2FBNB2MHSR6FQMYI4SYUYROBXBIJN3QBOLEHPWALOPH5TSXRS7DWZ6FWAQGRAZQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Анапский Район,,Юровка Село,Октябрьская Улица,,1",
                    "RegionCode": "23"
                },
                "INN": "2301076247",
                "KPP": "230145001",
                "ClientRegId": "010060699786",
                "FullName": "Общество с ограниченной ответственностью \\\"Винзавод Юровский\\\"",
                "ShortName": "ООО \\\"Винзавод Юровский\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "154.00",
        "FARegId": "FA-000000051182001",
        "F2RegId": "FB-000006203516210",
        "AlcCode": "0100606997860000063",
        "Capacity": "1.000",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое красное \\\"Мерло\\\"",
        "ShortName": null,
        "marks": [
            "192310102838641222001YOZXMMPFSZO7XOKO7HCDQ6K2DEZKDMJP5GG5TG7PIKAYGP3ZGZE4H4NBZLTRXEXYPA3FMBMV5622P4MIQD65OWWV7FF2ILBD5PDZGPAO33YGBYN2E343DFTN5RPEUAYQQ",
            "192310102839521222001UOISTZHLJQBE6Y46J75QSWJMNIQR5ETND2ZXJ6NAHNZXNYEES7LEWCTCD4ZRP25JLYSXAVNJCEJZNOWH645YGLVFT52ZPMGPYOZGU6XRHCD2OIBAFSDGKERINGOLTN2UA",
            "192310102839581222001RKM63TXQA3SCITJODVHQVPDNVYM6CZ3A2WPUKZE6EDEHWZYCKXTEHSC6VLIULVKSQXCYONTCTL3Z65BCQRWRKN52NZEYW67FSAEJOAZXXYR7T45N5NRGTKOP43EZCAP4A",
            "192310102839631222001XOIXUXTMLKJQHER55IIDVIP5ZUMSANNFNDKNHYCRAV4QTTCS3362COM7V5SGMBITSC7EGIWT2L6Z5XSYXCJVFX7JTU6JOPLCKZPYW7RZQJAMWAJKVTW5CY2TYINFDYWGQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Анапский Район,,Юровка Село,Октябрьская Улица,,1",
                    "RegionCode": "23"
                },
                "INN": "2301076247",
                "KPP": "230145001",
                "ClientRegId": "010060699786",
                "FullName": "Общество с ограниченной ответственностью \\\"Винзавод Юровский\\\"",
                "ShortName": "ООО \\\"Винзавод Юровский\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "241.20",
        "FARegId": "FA-000000051368661",
        "F2RegId": "FB-000006203516211",
        "AlcCode": "0100000054580000091",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"КЕДРОВИЦА КЕДРОВАЯ МЯГКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187316723025261222001RVRZ7R7MV7GFLASBN5MC32DF2UNUHXVHVJJF6PRXB3HXVKHSJJ43XVMEZL6TWCJCNTH23T2HMDGJGKB6C3OVGIGGPWL6WDS5WQGL3BLCZF3HFOJC477LGILJSAIDW23KI",
            "187316723025341222001HBDPGYTWWW5NMEEHKKNSYZ4QIQSHTI42PH7VWNFGHQJCPLCWP5BFRQPWBSCA4FOSYCMM5VHI5C2A2JGT4TB4Y5MJNY2K2A4P3HPC4DM4WEF62WYWALRFIQAJ7T5BBMKLA",
            "187316723025371222001CVVOSVL6CA23O5Z6BUSSZTCDNYZV2EDBSW7ZKUQ2W4LZMSXOIQDTHSJG3ZBO73XQCZUSBIOLKKHPK7S2DVNKJXL2UHXPQCG5NWNPNIKUSSI4IRVIZFP2K3RULTGLRGFDA",
            "187316723025981222001XDROE3CJB7CZ62SQHC4G3BB24AK5FKE3F3VOFVRY2BUZCDK73ZHUUYUCOXARPF7SP2XYVIAE35MJ7MUXH3XHLSJRHRXEYYLTDYZC6KHSKGKSBEISURRLKX53EMTNM7VOQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "145.50",
        "FARegId": "FA-000000051541757",
        "F2RegId": "FB-000006203516214",
        "AlcCode": "0100000005410000040",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"БЕЛЕБЕЕВСКАЯ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "198410830095490123001HFUS74AARCS65EOF2QLM5CECU45ZNFFG2VNBNUZ4YCKVF3U5P7KZYKSN3SG7W3O5XE3I4FJS56SQJUUFMTSIOQERG7HYQTIHJS4CVUJMOTTKBJSQGXPIFFFF723YIBXTA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "221.50",
        "FARegId": "FA-000000051831851",
        "F2RegId": "FB-000006203516217",
        "AlcCode": "0100000005450000007",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "1874206665025203230014GYNVXMME2BDC5SVK2UTBAGGQYPOETE45HFGAS4Q2XLC2DBBXCC2N7WTCEEOVF4N26EOQLZDSVUIL4UDDJUQ3OPK2IXUVGAALKTTQ3B6WX46RLXJPGWCYQW3W736NR32A",
            "187420666504970323001U3ANOADERIWZNN2OUCFQ6VYOWEZBATS3VU4DTBIWYSHCLHPRIOCQJZXN7Q3IW4JJH5VTRTCCKJA7Y7DTG3UKLIDKFGYJ5EETVEMLPYF6U47ZFWIDRAGDPNDBFNBGGZQOA",
            "187420666505730323001IHY5R5CKGU3TTRMFQV42CCRLMQYLXI7SD7H7UIAQVCOGIES4FGDFJCZA6HBNIERKUK3WTQPTLUBMBUGTVAWTK6Q6OOVCGNMQB3VQUOUU7YTLTPD56EHPTM575PSV4GWSI",
            "187420666507450323001CYKBKUDLYL7EBXMVYQXH4UZ7TIUM2YFVDPQKLFQM5ISRH7KRAB36YHHO5CLVP7SS44ZFQ6LPWHHFAGYJHT75H7UQ7BDAMMNTJVYR3YF4NZIG2UVFNWA2KSQUYNXE25VMY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "268.94",
        "FARegId": "FA-000000050712563",
        "F2RegId": "FB-000006203516222",
        "AlcCode": "0100000003130000078",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЦАРЬ\\\"",
        "ShortName": null,
        "marks": [
            "187417574036601222001ZDSDFXM5PAD6Y3RK6NY2FZZ744POJNDVWY5IRHPLFQT66MM76S6WJP5UFFPOOGZMC52QVCVFKG57F6PKP6S6O7WFSGDAPODMNDD6RAC7I4AGZCH7HJEQYLNMJ3HQJ4JCA",
            "187417574036771222001NBRIYZLQWBDZD3WARMKZQSMGVEJDYZURTSAW7EEBVXCK6HHDL73XXP6OENPOZTYWT3F5FR764Y4B6JWAI6EHFEO7VLMVOHZZN35GB5GIRQDWTMLMPFW4I6ZBJ45ZA52RA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Пермский Край,,,,,,,г.о. Пермский, г. Пермь, ул. Героев Хасана, д. 104 | Литер Б; Литер Б2, этаж 2, помещения №№ 15 – 17, 31, 33; Литер Б3; Литер Г3; Литер Г5; Литер Д, этаж 1, помещения №№ 5 – 7; Литер Е; Литер И; к. Б",
                    "RegionCode": "59"
                },
                "INN": "5904101820",
                "KPP": "590401001",
                "ClientRegId": "010000000313",
                "FullName": "Акционерное общество \\\"Бастион осн. 1942 г.\\\"",
                "ShortName": "АО \\\"Бастион\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "476.00",
        "FARegId": "FA-000000051488839",
        "F2RegId": "FB-000006203516225",
        "AlcCode": "0100606942420000118",
        "Capacity": "1.000",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "189400982831151120001NYKNESSNLKQU3ATB5MSMZECTPMPRFVGKXBOB4NKLHWDT2VUMJDVILTZY5P6PSJ7MEANXXBBSDPX5YP4MGXUAJLGTFZRLVMPY2MVB3OJQNISDXNBPDXRMSLU5G6UUELLCI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "151.00",
        "FARegId": "FA-000000051395190",
        "F2RegId": "FB-000006242859035",
        "AlcCode": "0100000005450000008",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198410210687210123001X4V4X5DWHHUGB733AXGCQTSBFEXX4WDIMGXZWBRZU2JF7SIBH6IRTXNOKQ4V2WVM3324E46BXOEHQDGQA5IKNH4RAFSGCLJ2H4MJBU4KS4DRYGG6LRVEHBORTPVPB747Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "221.50",
        "FARegId": "FA-000000051831851",
        "F2RegId": "FB-000006242859038",
        "AlcCode": "0100000005450000007",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187420666503270323001RUDUZVYKURMWQ54BHX6AHY4UQ4HCNVLNGXKXPAWNBBL6W7ZGN4VT63UJXCHMAXSHANMI3HOH55M55SXUCED57GBEZ26WEEMD3WOQFETUN3YUWAK7DZ7F4U24TCJTGFERY",
            "187420666503310323001J2W4IWWPKWJLWO7FNCKYBCTY3AZVDOSAZMZSCKK52N22AKLED7C567DSOLZUENLNMYE6RJXIYLZNP26ENM3VMPO4KABJPCCHKWDI5AAJCKDXMMWUZDTKPYY4VAUNIS5SQ",
            "187420666503670323001MPSOZJF7ICFIT55HAR2Q7DHVB4W643KTYJXEG5PKGHUDBXFXZB4TZWR2AY4JQFJX5SZJHW7KQDJM5RZYYFIVCXUKRJJOFJLUYQO7CZSYGROG3UADJ4VBHHTBHTQRQ5QLI",
            "187420666503720323001NBL5PRIQZ3LYVBIYIWMRYAZZYI2SAZOSKETSMJDPJE5ZOQJ24SLIIB6PUOPWFAXC43ZDHFI5SSAAXLLWELFK56ENHCJTMFABJX6UUQHVFHIIYTZOR62XL4KC7ZPCVKZQA",
            "187420666503880323001FUJEBKCVE34PWLJJOXRRSECVSEKLDCQHD7MHEGTUN3RMC3ITIDHCSZS4UFY4ZAJGOVMOIS3XKYZQISQYYB23R72HGD6PHAH5G2WSEDQCKC2APCCLIZ2453V6NBKFVLIQY",
            "187420666503890323001Y4E24KL4DIXPTWSUDNKFT2HBIM3KB5CZZ2VMSBCUJBGG6UNYLODKZJQCGVDZA7OIGJWSZBVAC5ZXFR6IAL5UV6MDX3T6BSIUZLCPTRSZCKDBJ3W4UXJ24E2TPWXKVLCDI",
            "1874206665042303230014KP5A6VUJHSZ2K5FDXEBFG7QCYDSTULPHWH5RDF3ON4VPPUBVXIFXEKU4LORI5MNVAQZGONRHW4CDXEJFKZURNMYA3MHU7ZHGK5AH5HTEWS5CKJN4A4B2FLWGDWS6A4MA",
            "187420666504250323001L3FGJYYHVFG5VFWGC37HAHFQG4WKTAA5NJP4BXS6JFGIUEMDCNNOSYNR43VXSXOICG7C7Q4EJ6MSQ4UMSIY5SMS4D3SF3FUHRWNAODVD7WBRCK6ULH54A66TAO33L37GY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "288.26",
        "FARegId": "FA-000000051605670",
        "F2RegId": "FB-000006242859049",
        "AlcCode": "0100000003130000078",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЦАРЬ\\\"",
        "ShortName": null,
        "marks": [
            "187418489670311222001DTHLJMYLDFNGA7UYDWJ6BYIO3A6IUGBYWFRBC5E5F6TQAYJ54NDYKV3H7MIMDJ6HEBKZ22TE4LUJJZH47B3RK6DVYCA3O2ECB7KWODAJ3AZNY2FMGXOEEKZJB42PQ2RTQ",
            "187418489670431222001ILEWUYTYEMZDWLDVZ3PSENU7CEMVCMRJBP42YORRYSTAXL3E6RW2NXNICBA3LE73GHBWDRBOK37V4UYAHK4PQHD325ZJWJXMOSR75MVQSUKKUTM7SRG557RFROVS4V5QY",
            "187418489670501222001RCL7S5LCYSXSHISM2L66FBIFGEMWPRK6QZ24M3SJIPSS24LDDLHO46L6ECXV7HKAOZMX6EUKGXY745WVLU5QOC2LIS5I7NMEYJRPGU7VLVP3OYQIUSB2QFHSMJ4EXXYZA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Пермский Край,,,,,,,г.о. Пермский, г. Пермь, ул. Героев Хасана, д. 104 | Литер Б; Литер Б2, этаж 2, помещения №№ 15 – 17, 31, 33; Литер Б3; Литер Г3; Литер Г5; Литер Д, этаж 1, помещения №№ 5 – 7; Литер Е; Литер И; к. Б",
                    "RegionCode": "59"
                },
                "INN": "5904101820",
                "KPP": "590401001",
                "ClientRegId": "010000000313",
                "FullName": "Акционерное общество \\\"Бастион осн. 1942 г.\\\"",
                "ShortName": "АО \\\"Бастион\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "298.00",
        "FARegId": "FA-000000051453452",
        "F2RegId": "FB-000006242859050",
        "AlcCode": "0100000020360000060",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ №1\\\"",
        "ShortName": null,
        "marks": [
            "1873168372422012220012RNBMR7FMNX4M4WTD7FIKZDEVQT6K3V4AC3UKD5KBGOXZGNJAGL2XZAZ7VSGSDLBCUIWIOSRSTZZTFHEFVQETCMHVV5KT2KHAIKLU4GCBHFQPVJDNAAV7PHCMOO5CJ2KA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,Вологда Город,,3 Интернационала Улица,39 Дом  , | - нежилое здание с мезонином: 1 этаж: литера А3 - пом. 5, 6, 9а, 10, 11, 15-20; литера А6 - пом. 3, 3а, 3б, 6а, 9б; литера А7 - пом. 35; литера А8 - пом. 36, 36г; литера А9 - пом. 37, 38; литера А11 - пом. 33, 33а; литера А12 - пом. 30; 2 этаж: литера А3 - пом. 37, 38, 42, 43, 47; литера А5 - пом. 52; литера А6 - пом. 3, 3а; 3 этаж: литера А3 - пом. 8-10, 12, 13; литера А6 - пом. 2; литера А7 - пом. 3; мезонин: литера А13 - пом. 1, 2, 3; - административное здание с проходной и складами: 1 этаж: литера В2 - пом. 2; литера В3 - пом. 3; литера В4 - пом. 5, 7; 2 этаж: литера В5 - пом. 16-18; - здание основного производства: 1 этаж: литера А - пом. 6; литера А1 - пом. 1, 3, 3а, 5, 11; 2 этаж: литера А - пом. 5; литера А1 - пом. 1-4; мансарда: литера А2 - пом. 2, 3; - здание посудного цеха: 1 этаж: литера Ж9 - пом. 1, 1б, 1в; литера Ж6 – пом. 1; - здание кондитерского цеха, 1 этаж: литера Б, пом. 21, 24, 25;",
                    "RegionCode": "35"
                },
                "INN": "4720027123",
                "KPP": "352501001",
                "ClientRegId": "010000002036",
                "FullName": "Общество с ограниченной ответственностью \\\"Русский Север\\\"",
                "ShortName": "ООО \\\"Русский Север\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "178.50",
        "FARegId": "FA-000000051331256",
        "F2RegId": "FB-000006242859052",
        "AlcCode": "0100606942420000115",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "187418725289200123001K2KET2QVSV2B7VWC3ZOE4OVNAQL642KIQS34VZP72A6OUG7CSWNBA4BIPYSNSWGEUOEKEEAVPDXKOZUKC2KEZNJKJOT3ZNI6NZCWZ5ACJYSHBZA6GRZELOR5355Q4JJII",
            "1874187252892501230014ATFJENBU5KJ6EAXEKRN2PVZZM7BNL6QG2KPZUOHFDBVUCMSPMYWSRHLRP7KGMEW7XXPXV7DGPFBMC2ZCK4XJ6I5AFEX5GROCAAQCZ2SJA5BHQD3XYLGL2K667RVPHF4Q",
            "187418725289290123001PLHKQ2PNSM3DCW4AWQZT63RRSQPW6PEELIDFZNJZXYCLX5B6DRNRWZD7PHBPXUV6E3W45EY3CFEOJFEHNAETLXV5JYNPS44R2D4GUJZLUHS4AYQIVQXEP5VAQBFD4BTMI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "250.13",
        "FARegId": "FA-000000051733508",
        "F2RegId": "FB-000006305538698",
        "AlcCode": "0100000054580000061",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТЕЛЬНЯШКА\\\"",
        "ShortName": null,
        "marks": [
            "187316968274781222001R7KEAIMKA4PPYGFSUIGV6SVJIALJCSBD2VTCRVZLUPUEDO7EXDGXKTSOLWG7IHKNSL32JSVONIX5657TUEQFGXCIJN6KN2IDUIPZXRR7YEQGMHSDXNCWXL76B5P67T66Y",
            "1873169682747912220015ASDWOR5JPYKEXR3XSBDJMNCBMA52CQ53CKE64GFJDVGN4HMK4OMXO46WVP43RRHEQ3WTVYNIE3WL26PGEALKJ5YRTD45WBHOFQCFAOLEU7G2GX6DB6YDXWMURE2HEMKA",
            "187316968274871222001CYVFCT5OSD7UA64ZBIUE57KKRQG4DUYB7T4OBAZDUQJU7FJRWTU365ZBJJ74O552KIVJFQ4BDS7TG24ZNFU5ELKC6YV5ZIVQJCAKF6EPXOMSOILISL74GVOQ3LJRHZ3YA",
            "187316968274951222001LYKSARNAZMFAGJMEVIJALZDB745FVSTKJNUV37BANCWQCEHVWE2SXPPC5VPA2Z4O7FEYAN6XT5TC6HSDPG3YMOEBNSKGIUO2QSX7HJIBZJEZSAWLBPSSK2S4POFLVV3IQ",
            "187316968275521222001I25JY3HHOS2OY7ZSSFHON2KZOIXOYBQOIS6PQUOYYPFF4VZMQ3L7W4XIZBBRSCOABF2EDHKD7VUAOWVYOTLACHO5GPMR6MSL5SNYBFJZO2SGKCJDKQD3PIXP3J2NPLNHI",
            "187316968281241222001B5B3MCJACQYFKIH7RCQ5OTLGKQZVXRAANZT32XFZDVRQLBLGK7MATP6LGYSKSASWOF5IBRJ7NGTHMD4KTSE74ZJWWNGRCW5PSDUADXMWPJZWDOLHCDTQCVHBBX4GE6UVY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "350.18",
        "FARegId": "FA-000000051628352",
        "F2RegId": "FB-000006305538699",
        "AlcCode": "0100000054580000062",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТЕЛЬНЯШКА\\\"",
        "ShortName": null,
        "marks": [
            "188302505575040322001B63RGDYDXOJD5E5ANWQZGD4KKYBHDJPFOX4ZVSVRYEFFEFN7HXNONAKE6RNNGGSQIOHTGZNCWW6RFMO24GTEP6PYVH22K62A6GTMVH4VLMHAJFYNUOZ6DAB7XVHRJZNII",
            "188302505575090322001G5ZXXFRFUE5LDAG23VEEZOVV6A3JEBA3FZEM7JG4IVGHSQCNG2RI3JKSWSBV7BSFHGVZNBVDKGE2D6ZUS5TXWUWJ56LQZ4WD5DCWWTBJJ24K7KSSMGEFAVH72GEW75VNI",
            "188302505575140322001HKHYGONO3BOVZQ3IUFZJNIXSMIKVMKXO3QMPIHKO7QAG3TWYCYVU5ZNN3PVT37H44C46PFFRWDYGSQ5H6RQRYFC67OOACDCKNNAUYMN6LHEDE3GRPHBFT36K3TLEVR3FY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000052023136",
        "F2RegId": "FB-000006305538700",
        "AlcCode": "0300003247940000052",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Берёзовый рай\\\"",
        "ShortName": null,
        "marks": [
            "187317274565431222001JDAXT3KA2WZ6YL374IFRSCORZ4T42E7HJCVW7GZAKHJCJON537KJYZ6MFBPPNTZI7NBJEU2Z2OZYEBBEVHQI6SRONE7UIYH3KXIN6UO7QJRGDOCXIHCHET7QZOM7HLZ7A",
            "187317274565471222001HD4ET7GRV6WX3XY4NGHSMK23RE4FE6FDAOVY6TGQ4XIA65OC25CVJ4KJRLIQBGQT5Y6C5OERNBY32344JTKNHIX3NRF6RJTDSTEQ5KRY5TQRLPZSOPPCGON6IBRHYJCRQ",
            "187317274565491222001IZO2NXZYFKYLBVGZ3XIRGGJPREGYAKJUOYY7ZFR2746SELY3B26QWFPZO6Z7634AD5KK7FS5CFXY2SI23GXN254FUXXTWDW6DN6TJI7KCAS4YX2QGLKIAILUJDJNRGUHA",
            "187317274565511222001TSND3BQJOHNBMDSMFXOZCYNTCAGKIRJIQCEFLM7346V4Z37IDLLPDIRH7EAL5FWKOXNCYLDCUMDKOVPQKKABQFDSJPSM2ODODBI6JOWEX3MVN2MW7FHPSJI7YFREUVCWA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Челябинская Область,,Озерск Город,,Кыштымская Улица,30 Дом  , |  | нежилое помещение № 1 (водочное производство), расположенное на первом, втором, третьем этажах в нежилом здании спиртоводочного завода, литер А,А1,А2,А3,А4,А5,а; нежилое помещение № 2 (спиртовое производство), расположенное на первом этаже в нежилом здании спиртоводочного завода, литер А, номера по плану комнат 36 (S=208,9 кв.м), 37 (S=67,3 кв.м)",
                    "RegionCode": "74"
                },
                "INN": "7413022993",
                "KPP": "741301001",
                "ClientRegId": "030000324794",
                "FullName": "Акционерное общество \\\"Озёрский спиртоводочный завод\\\"",
                "ShortName": "АО \\\"ОСВЗ\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000051912446",
        "F2RegId": "FB-000006305538701",
        "AlcCode": "0300003247940000088",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Три Рюмки»",
        "ShortName": null,
        "marks": [
            "187419736062360223001SMAM52TROASYED6DEXLH357BLQDXK5C6CG4CJLZYNMTP5RYKBN3ZUUK346E65NG4FKQASHW4YTK6AC42JAJOH25E6QIU3B4ZBUH3WWWRL2ZB4NIVQMW35LV5ZIR7EKXBQ",
            "1874197360624102230014WACEY46P32IEZMYQKOX2EG7F4FE34RGEWUUTZFHUFXANCVFPUKBIMKQEEGGF7GW4W4BXD5Q2ZQGAAZL5SJYW2YZJRZ4P66DBQKX2V7WWVAMKE7RH5BR5IMCUAQIKW2VA",
            "187419736062430223001RPEWNOQCTXJWMEI7QLJ65VDE246PBERPKE4ZQCMQ62UQAO5XFYABSI336SJKLMLES4M57TQRWZ53EOWA7VXNFBADREYMN6MD6BEZHZPQNAEK3FNPPLNSI7J5ZBIEZO42Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Челябинская Область,,Озерск Город,,Кыштымская Улица,30 Дом  , |  | нежилое помещение № 1 (водочное производство), расположенное на первом, втором, третьем этажах в нежилом здании спиртоводочного завода, литер А,А1,А2,А3,А4,А5,а; нежилое помещение № 2 (спиртовое производство), расположенное на первом этаже в нежилом здании спиртоводочного завода, литер А, номера по плану комнат 36 (S=208,9 кв.м), 37 (S=67,3 кв.м)",
                    "RegionCode": "74"
                },
                "INN": "7413022993",
                "KPP": "741301001",
                "ClientRegId": "030000324794",
                "FullName": "Акционерное общество \\\"Озёрский спиртоводочный завод\\\"",
                "ShortName": "АО \\\"ОСВЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "148.00",
        "FARegId": "FA-000000051806743",
        "F2RegId": "FB-000006305538704",
        "AlcCode": "0300006342850000032",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "198411080497150123001J55TGMU7U6CF2DZMH6SMUL6V6YTWNEYFX54YS64QY57BNCPZ2XW72U5RA7FKMFYUF4J3KOHYMM5TEZTYUKTDL2KEZLCZBKZF2QDSKH5YUUKDIAFYLHBXTPS7CA2SR772I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "148.00",
        "FARegId": "FA-000000051551989",
        "F2RegId": "FB-000006305538706",
        "AlcCode": "0100000005450000056",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\\"",
        "ShortName": null,
        "marks": [
            "1984106672072501230017MYML4YAHBJOALCBAZXJMPY3EIWEB2WOGA2LTCSUGIQ5A2DQUJ7UPSGKYY6D54UCRNIRWGP7657B23TLHDJCHBALPZCVABVLUTXX4R5QWPLOOXZCUWPVWK3ITYT7ETI2I",
            "198410667207380123001W3PS4QVWROUKM62AHCT23R7HRYYBS7S5KM6QF5XHYHLRHZSK3UJ75RVTWTVXTR6I4RCBFVFOLKANBOYOSL6SK65KOKLWJA4CC5MKJH4QVGXWGKMYZ3DKBEUPKX4PZFLPI",
            "198410667207390123001R3T5FMUSN3AT7IOI4AJ44U2EZIFC6T43ALBEEYVJZRWQ76COHHU5BHUAHGXG2J5LE56F7Q4CFBL54MS54M6XALGSBI46P7LALGNGMS5QL623HPSM6AXXKQ6NSUG2F6T7Y",
            "198410667213230123001IBPHZVPUCTJROMUEZMZSBPEMTA7JOXGUZLTYJX663VGIJP6LSGBWZXSZGYNHYL3NFOJDKTRQLHFXHDHMNS4IKV2OLTNFF52ZWMCFUDSPP6DCPVJUCDAAJHOYWLZ7UQDAI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "283.00",
        "FARegId": "FA-000000051628092",
        "F2RegId": "FB-000006305538710",
        "AlcCode": "0100000005450000023",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "187419970808970223001F7LB22EHK4BPJ6YER6FCQE65EACHXWNLDQJKXH2DLCNMISCVEDB7GPRMIR2BKGAQRP7DWJKYPUQ3ARBEGQRGVY6SOH7KCF3WA77KYY464TWQBD2OYZYCP6K2HIIHIC7OY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "292.00",
        "FARegId": "FA-000000051164835",
        "F2RegId": "FB-000006305538712",
        "AlcCode": "0300006342850000006",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"СТАЛКОВСКАЯ АЛЬФА\\\"",
        "ShortName": null,
        "marks": [
            "187417658627201222001ER4QACIDNC3NGDKQYNOXE7MOEUXF67QWR5SLRZMPEZM4YQJ6BWYIAYN6GSKYO75K4PL6SG5CKAVURDEZBCBDOR5H5HNQUILUALAGZLKV2NH7B7LTAIMRVY3VKNEGJLN4Q",
            "187417658627221222001BBXOI6IRXRKM7FWGYUSOLF7MMMOEHHL5PVWY44QBQTTFD7FHAVUAYUJ5WGVIQKOOFPH6BE7O4QMMKMN4AJHHQJMHOHP2RYHU6C44SBMLFZMMAXUL7FTEEHWLND6YG3F2Q",
            "1874176586272612220015G4GNE6TF7BNM4JXU4NOYRZ62ELKLX7YNBDNWSGIZ5HDJB755QTDJ6CBG24WDNCTCMFDMRCYVJOJ343HKX2JRZSV7OO4UJEUJNCFCAV5ULQLTK3XJ37XHIHVXLRD74AJQ",
            "187417658627291222001RHF5JDRZHGXDILCYYZAWKWTSTQDI6YQQ4Q5UXVVVQP27TYJBJEYD2V42KJGRRUGVN3EWDL22CWC4Q6ZGOGAKEXSUYPNC75C2YUUPCIAWSFWXY2MZGVV73Y536KUKQCIHQ",
            "187417658627301222001CK6TM5EKCLDKHFWDGCAG3A66A4JPIDZTWFEGJF5D2XB2GRUZC6ZRKYLTYJR3ATV36ZSOGIORVVNPH4CGTRAXUTSHZHPOYUZD2JDWMJF4IDBVF26GJVVWIU3PXEZWWBVTA",
            "187417658627331222001NTWVCZTKR4BXXG5MPIR4GGE47UEM3W7SS7K2WT6FFHKQ6QLAT2CR5APS7KGYULO5BONXTLTPRIF4WA3TU3M5KECVJNLCMYPUYDCXV37WHM6FVMWFCHN7CJGU4MV5DKUOI",
            "187417658627381222001G25F73ZZIZOX2XBYV6LSH3NGOIZ4KBTIZBB46YCYGVZQCTH54V5PTQ4NHPNI3AJWPM7ZUFPYY5C67BMYXFZNBEN7CZLRFUKLPK5A2BBOWNRVDSLY4UKPNECF3TCG4QVDY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "183.00",
        "FARegId": "FA-000000051810465",
        "F2RegId": "FB-000006305538716",
        "AlcCode": "0100000010250000020",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ХЛЕБНЫЙ КОЛОС»",
        "ShortName": null,
        "marks": [
            "187420710784070323001KNA3Y6IWWVDHXGR3YRIYTDEKOU67HJDO4JEEOMCJNJHMQPZMZBAJEIK7OTCIXN76NVEPKPNMXGF7M7QJIM6DCDTDRSYXO3JBKJSXZVXRYXO4FNH3DJ2X7GX6KHUT3JBJI",
            "1874207107840903230013WGIPC3ZSSWC34R2JGZWVQKZLEI7G453IQXXTOOEMAIPINBECPZA4EIANKDA5NQGQLJO5GT6O2QOBAPTGXRWL7J6RDMGDCJACZ2OQEFB3JPTV6VMN3Z5G5JTRQVV6VAUQ",
            "187420710784130323001H62EU6RWSCDTFCD3VNRELJOTOE7YDO2DXHQGLMMFTMH4W3KVB7JLZPCWC7ORRBTWLEQC5YN2J4A43UP44Q2ZQWZLTNQSEWZWEZM7NQBT3OI6SNEDG7QWLJOOAPKRHCXRA",
            "187420710784140323001R2DLPEWWUKDSFFOZCXNWIJP3E46NGE2SFKSKETCLNX6TXC5QBUVW2D7GSUDYINUASPS6OZCE2YJZZAR6AN3WBEHPR2K4OJHN3HPJLHM757IDYADCCDYBTTC7MYYWDLJNI",
            "187420710784150323001676J43KZTFHUIH2W4EXIN44OKYYTAQNBKJ2THHY3ERYW5S3TP25YT2ICHPMJHGGV3B2IJUOFMYUISSWEFEFCKNNRDKVCC7O2R3K27G57Y4LABZTW7YJEZMQFZ7FLDJYZI",
            "187420710784300323001WR4X5SIWINHWR57J7BKPJC6XGQGN5NTJ26HLNCDFYIKSX5BDRBH46HLAL2MYD356KOJQ6QH5REXZITFM6TK2I4WLANWML64N4V6YTSJH7EYSLQ7PLDLVWUT6JIHTTLEQY",
            "1874207107843103230012ND6GM7SHOJDIQGVAPJXB2NYNUBPGRBMNZZHVF5ZVKUZ6GRFGE2LP6GXUXK6RPIVAPOAFB5MFHPSPFKZYARF5ZWDUGGTRJI76NAHSKWXCNSJMBT7XSGIZB7R5NWE4SRZY",
            "187420710784320323001NQCQKJ6BQUTGKQMSRDRJEEWYJQBOLUQ33GGVZCVO3QEA72LIGATDBYSQZIVOACS37CMWK3EKXQV7FVLCORP343MDJ7V3GQ7ZT2R2X6V7LVIQERZEYMGZQMZMWIQH62L3Q",
            "187420710784360323001K7LNKOJF6OQBLVWRQLNRBMISJYUM5ID6AK7PBAMBOICDCCLIS5CJDU4G3WDF3J7RXVFULJWLOE2KW6TTCJAFSSGAYCRXJAGEUTTBPHLGEQ2U5FAUVZYZNFJJD5VV4PLKY",
            "187420710784380323001E5AECXHZKL2LK53NZ7OEOOKS5MPDSUGRVM5WKCQOR7HGCSW5AVAZJAMCA5JWVHSSDRW3FIXPX7ZO755QMQ7VEB3WPDQPVYAIKQVRKLYLZG33KDA4NQEUPEICG4VQ2UUXQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000051242348",
        "F2RegId": "FB-000006305538717",
        "AlcCode": "0100000010250000050",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ХЛЕБНЫЙ КОЛОС»",
        "ShortName": null,
        "marks": [
            "187417619808041222001GPR7C7VXEL3YMAC6TM3ABDB2QIPALVAY3GG4ESVHBRGTO4N7YU37T5I5TZYBFM2YLXI4W743BFJPR5FXBIFXDXOHFMOLTEGFQN2XHFESXUQQRSGUWFATJRH5IHMAUNNUQ",
            "187417619808101222001TIWJSOQ3C2HOZ5RA6HNRYC5ZEENEEJV5H6O5Q4KQGIKZJSFUOH7UYEAU3DSXTVQ32M2QS6SQXWYQK3OOPCX55GELHV6ZS2E2S66QKNKSATDMCRMWOJBV4IIAVZD6HGEMQ",
            "187417619808211222001GKSG3KDCIKRIHDQ6UBWL6GNMAIR3NN6FTESVOODIKUCKMKNCMEROTIKQLIS6K2XX7HWY4JLBUFOXWNIVQVXFNTUMXBSX6MSZN6XB5CK5PKNL5EXD3SDQQGAOZRATCYFUQ",
            "187417619808261222001QT6CEB327LVPGQ6V4OL3UEZ6S4LAS5ZMP3Y2RPSLPZFHKCY3GKLDLOUOOPIIGGIK2PQ4NA5INWY5MDWURGIJZMNOAE4TLY327JZQE7DU2QEJS6JIEKAP3VEO75I2OFFSA",
            "187417619808271222001TUPRKL7VB6WXAKC5TFI3TETWI4BB6N3YOSKBAHDJ35TLJLIDUKQ2KXEEHLNELPIBIG4KRLYGKLF4ZHJVJSOSJPQE33AXMRGLBMPRGKUGDK72XOZW7E2D7ACX2NUQBC7YY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "339.50",
        "FARegId": "FA-000000051843782",
        "F2RegId": "FB-000006305538718",
        "AlcCode": "0100000010250000068",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ХЛЕБНЫЙ КОЛОС»",
        "ShortName": null,
        "marks": [
            "188404092209511222001S7DCV3SZ2IOGA6S2WUYLTXZ6IARHMTEMDPNMXZVXU7RMTVIJTGDQ4Q4I3IFW3WWMQELTGHVAJRGIDJDDKKBH2YTGL7JM7LHPRYP4WNRKXPSXJGOVFYM6C36BXOSPIFRYA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "484.00",
        "FARegId": "FA-000000051923976",
        "F2RegId": "FB-000006305538719",
        "AlcCode": "0100000010250000058",
        "Capacity": "1.000",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ХЛЕБНЫЙ КОЛОС»",
        "ShortName": null,
        "marks": [
            "189401054034790421001VZVBEG5ZTZP4V5SJ56QKH4VUJIOTHNEK3SYC2V4BMJBVNHYJPCWWWLMHL62AWM5GZIVOHFEUXWGQZM2D2BSCHKKGSVNAATQJQEEPFYERPXIDINB3VCNBZGBKQ66XI3P2A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "178.06",
        "FARegId": "FA-000000051755475",
        "F2RegId": "FB-000006305538720",
        "AlcCode": "0100000002700000030",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Архангельская Северная выдержка\\\"",
        "ShortName": null,
        "marks": [
            "198309508002390123001T52FDL2KB3LYLUOIREOEZLCQDI3IVCUPBLTDP7NYAUIB6RTC4CYGRH3XIFA2PE25RZWGUQ6B52SKWMG35AJDZQ3JIN4YYU536LQQ5VJAGAMFFHXGKFTO2TWMJNIEWH7OI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,АРХАНГЕЛЬСКАЯ ОБЛ,,Архангельск,,наб. Северной Двины,д. 120,, | ; пр-кт Троицкий, д. 133, корп. 1, пом. 5-Н, пом. 6-Н",
                    "RegionCode": "29"
                },
                "INN": "2900000293",
                "KPP": "290101001",
                "ClientRegId": "010000000270",
                "FullName": "Акционерное общество \\\"Архангельский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"АЛВИЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "315.90",
        "FARegId": "FA-000000052018115",
        "F2RegId": "FB-000006305538724",
        "AlcCode": "0100000005360000067",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТУНДРА АУТЕНТИК. ВОДКА КРАЙНЕГО СЕВЕРА\\\"",
        "ShortName": null,
        "marks": [
            "187421528637390823001JA6LSNVBZCXGFFRRF2GYARIHBIE337FFWVCM5N5I25VLILKMWSKX4T642IPT26BJTTRNRBOTRPE7JLYPGJMDHIKDLTLWKW3AYGTIPJMBSLOYTMUXKJYF46GTYB5RNXOSA",
            "187421528637400823001HEXWIQPMJF7QDND3C4HLAXNQUIDK6U7FZO5QIRZNFYKZGS6BRMHPKDH4UUYCDNTEIOBY3MJ4OCZ2VZOA2VLPWNER4B7VUKESOGHBN56MPIWGKOB33OZXOHHQFDNVY2BEI",
            "187421528637410823001TVB7NCYAW2ATJ2UCDHLQXYFIMMSXXXRQY7VP6CNZIPKKBLHPWB4LW4F7ILMFA6ZCFPGTGOZGZHHWAIC3RHUFY6ICY3W7SM362VHQ4XJQAJBRCMBAUJG25T37TPVC43Y6Y",
            "187421528637570823001REU66AVLDPKLO4QFEM3FYGRC2YMXQT5VLMIZBFWQH4OAYKUNCOS3QT3MXO76VNOUJPD2EK5VESZQXMRQ7AU3WO2IGNN25EQ23FFWCSWCOQ7SW42G2T4BXGVXB34TYCEZY",
            "187421528637590823001QRGPMVKV5AV2FPLXNIHSTSYLDAMCASOBKU2BPC3TW2B4KJT5ZYHE3RDAI74DWR5NKDZXAPCA5GQDJSS2JEMCGI6ML57VON44DGVFJZLDJFWECPKXVO2CQVHZFQPHBO73A",
            "187421528637610823001NDPAIQQYRT2HCL2AN2Y4IWHZ2AMOB46Y5UXURZBQ3KE3ETFOGI5SKBCEVU5ORNMMNXK4HY6SO5HUHVG5246RENUCUVYZEMHCNWRJ6A7VDFWDJ4K6NW5A3BHE2HNIQQFGI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Турбинная ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902003",
                "ClientRegId": "010000000536",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "166.61",
        "FARegId": "FA-000000052025592",
        "F2RegId": "FB-000006305538725",
        "AlcCode": "0100000005360000066",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТУНДРА АУТЕНТИК. ВОДКА КРАЙНЕГО СЕВЕРА\\\"",
        "ShortName": null,
        "marks": [
            "19841195320288022300172EDNC5ZVV45X5FRCXX3DOD5IIPIAUFWTS24WEKT52OAPAZYVJFBQZSBKRYF32RT747X67Z26U55KXKLSLQI6AP2EORIMZTDTYKLYMVCODVLO32YNXDAL6Z3E7KUKCHOQ",
            "1984119532029002230013HPLPKHLV5OWMBSY3O5NG57NX42YRT5MIZPFWDLJGNAQ64SY7ZXKO2LBW44ZVINV4ZLEIR7TAT5Z25BLLNZR3AOTXGIM7D5KTNFKZ6LV7XNCZJBQMLVBHIVUK2UCQUW7Y",
            "1984119532029102230015JFURJ65JPD7MDSPZ4UGEMYYMYJFU3TRM7637CCY4BDUCUHRG5GW5XDPFXVRUZMSTA4LEEEM3YCVYPYOHPE52EBEWNF7BEO2C27F2LNGOMY254MVAFX243AQWXAE5OAHY",
            "198411953202920223001DY3PMOV4UFIHTJ6P3ZL2C6DV6AIGRLVSA2SJDKXDE5ZKNTB3LVNFVCFHBKCIKHML4D67DV7LQVURTPUNXLLUDNWY4YULWEXUMCMNOG5O7K6A4BPQUBFTTGCLD7LXBYHYA",
            "198411953202930223001HLTPK5XTMCIL4ZPORYNK6SK74AIA6MSVBKWLIS32UVJZCUCQ4ESDB3ZESCFBNEA2UXDUPFBHB7YHDVIQPIYNN2EYGMNLHS6474QYESAX67QUABLAGIYA22G7ABR46QMCQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Турбинная ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902003",
                "ClientRegId": "010000000536",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "166.61",
        "FARegId": "FA-000000051851668",
        "F2RegId": "FB-000006305538726",
        "AlcCode": "0100000005360000113",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"ТУНДРА СЕВЕРНАЯ МОРОШКА. ВОДКА КРАЙНЕГО СЕВЕРА\\\"",
        "ShortName": null,
        "marks": [
            "198411283129330223001E7YXZYX7SOCEMUTULQWYBUEO4AJ3Q2BXYPIMKZWQGEVCS4PCZCBHGNE5BFA2EFFRZE7PLYNRTXQ3XON7OOZ44RNXNFFO67HJVOUAQEC2CYZDHQY2D6ENO36EEWXKDEG3Y",
            "198411283129370223001LLXQTW3XTCGOMHUJNXUQTMISU4SVIICVD2AGIE7SIBGNF3VBNFHIPNJTFISO4NVWEU3I7YBN54A5G7CTNOMTMJN6V6PZUDVSOSY2TJOYCFM47JWT6LKFA6STHN4OZZA4A",
            "198411283129400223001NZEUIANPEFX653RQ23HWP6ZWXYZFMOUTXGAV5EB2FF4RG6V7H3MBBDCYHCQDMMIQE7GQIJXTQ56OLZKPIUZVE2DVVUSHGDA46SQLLMKTLQRLF5TVYGSCXQ6BR5QXYUGHQ",
            "198411283129410223001WZNI2WCKQIG3CHZJDED65KASM473YYTW2FTDESCVGEBHVXRKAJER7JMF3PLI4G5FSQX4J7ZITBVBRAUIG3TCSF7JXNPOJQDWUTXCJ3R3O6IO6SM5DQDBU22L2A626EMKI",
            "198411283129450223001VEPLR33JTQNNGGKIOGNDPDHXQIC5J5NOONXUZUNNBLAJSE65XUWYN6QE3YKVRKEQ65NYPLAUUXSC3SHQ4TL4RLYUCCOEIIWS2PO3DFABLWMMHXDEBFG7VIDDQHS3CL26Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Турбинная ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902003",
                "ClientRegId": "010000000536",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "178.50",
        "FARegId": "FA-000000051554386",
        "F2RegId": "FB-000006305538728",
        "AlcCode": "0100489413240000056",
        "Capacity": "0.375",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"УСАДСКАЯ ХЛЕБНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187419328484270123001IC5DLY24R66EYKCJZHCZXDIXQAK3GQM5OAVG23YHSJDFGLEL3ROIUNQ4HPNN73T4SV65EYVNJM2LJPW5TEFDLF7NKSN7PLCROOYDZJ2F4SZEX7MZZXMQCZL5W6IS6SQBY",
            "187419328489790123001UO2ZJFTJYXPL5GEQXBHKCGV4QQW4ITZ65SCWUCLLBHU3VRUMOKBW5JEVP3U6AVUN7X4Y5YGH2GBCHI6IR5NBBGKBFEFZ5W4Y56GK4XCE4QRHHE3TNCKAIZUXDJC7XZVZA",
            "187419328489840123001HIXC5JX7GWFMQV2TDV2Y46BWB47IAQI35COFNGZZIRZA26VAY5BQB6LJZ2WJKN7LLSDY2SVUCZNF2K3DLW43C4GNNKX7CPN45ZBGFYS4QNIMGWCAYM26BNJTTGQPWZU5Q",
            "1874193284899201230012SUYTFTSZEJU5VJAK445S5WYFYZWEE7Q4NASVZWAHKYUWF6SBKUROUAGX7DEBU73OLEVDAFHOFXM6HKY3XW22UV7ZNSCPDINTTD5IABUVDHNSIQAFAHEZQ2UNWCBC5ZYA",
            "187419328490100123001GHCAWPBJ2JLU4MAJHPN4GFKBG4M2UM3F6D2BJT7UO3J73WFZUE3EVOERHUPGLHMUWNLOZUNNA5ECQGXJRSLKI3WPKOAJXWA46ATU2ITPYLMEH5UE5MIYZUXZHB6U6WARA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "333.20",
        "FARegId": "FA-000000051353883",
        "F2RegId": "FB-000006305538729",
        "AlcCode": "0100489413240000040",
        "Capacity": "0.700",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"РУССКАЯ ВАЛЮТА\\\"",
        "ShortName": null,
        "marks": [
            "188403897027621022001CLDYIAMJYQQGZKYMXR7WGMC2UI3DCK3RND7JWOYGLBTLA4ETLMSWU4NEX5WQCY2NNUHWQLJVLDSCKFLPCWF6A6PA4QFRYFWFF53L5KN2YFM5DKJABHGAXS3BCYV2CVOMY",
            "188403897027641022001ATXOQJIUFR2SM5YYBG4XZHVPVQIBEJ4CZ3BSKTIWSD7SDTLOGU2JXJX73SE7DO3LXTT6RQEXEX4NHHDNJ3PFQ7BILL63PRNHKBOBJD6AJBLYIECWPTRNFJDOB25BOLBJI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "476.00",
        "FARegId": "FA-000000050805126",
        "F2RegId": "FB-000006305538730",
        "AlcCode": "0100489413240000041",
        "Capacity": "1.000",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"РУССКАЯ ВАЛЮТА\\\"",
        "ShortName": null,
        "marks": [
            "189300594510271120001GL6HX7SPYJYDZH3FDCDWFZZMIYMRI7XPUFKLM7VQNHL2QO5LHFL5XN75VN3UBCGL7GF2FXJKF2ZNPOBADWCI3G2JXHXX5DVWJAXNNODZGF6X7IJGTGOJKAXWI2HB4E2VA",
            "189300594511111120001HSIJB4XOZI6LFMIESPS3ZMQ4KY6VKAP3V5Q2M7R23H2HX7LCF4JJBHLB2OGEJSSGNKVCLYSBG4F6BVLCK3RZN4AZF2F4T2FKDD2SZHXPLFHE5L4FVKM3EMZVLBD5A57DA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "333.20",
        "FARegId": "FA-000000051212326",
        "F2RegId": "FB-000006305538731",
        "AlcCode": "0100606942420000061",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПУЗЫРЁК»",
        "ShortName": null,
        "marks": [
            "1884037451524110220013RO64IPIOREM2YZSJ2N6IWSMIAPPC5PWPZ5F2GP77GCXO3J7XM2LOLZZZKEXG77KAPWWE74A6DPO6RXTUF5FUV2ONH3JYA5LXQR2FXRLNAN42TWMWZIV7GCXYRDFXUAWI",
            "188403745154751022001OAHAOGTUNKKU6EPJYFZIGKWFXAXMVUULIY4XRZMOTVP7FNRAS2GZQPIN3A7QGX4L2RVV6TBXX6IFBZQ22WMMHE4KDZUVNTYJYRMDQDAXHITZS2KZ7NAU3A5FYDLGNBIEA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "476.00",
        "FARegId": "FA-000000050474821",
        "F2RegId": "FB-000006305538732",
        "AlcCode": "0100606942420000152",
        "Capacity": "1.000",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПУЗЫРЁК»",
        "ShortName": null,
        "marks": [
            "18940084092228112000176DRHGGYYCGNMTQUBTP7LSYXY4MWHRNRXVXY5R6WVCXVVA7KL4FT77OQWWSLRNSUZSRKF562XDGMCFF24RN3U3SSBI2X34VPHVTKMG5IRWPD74NSAUEHD5Y3KHMQS6JQQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "119.00",
        "FARegId": "FA-000000051142352",
        "F2RegId": "FB-000006305538734",
        "AlcCode": "0100489413240000052",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"КАЗАНСКАЯ ПРЕСТИЖНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198308895349500722001RZISXJZZVNYBWR2PMFXABFGXHEFS3SD2ZNL32TMGR6GMO5NOFLFT2MC2PMIR5QM4YZQUGYBSPUZQJ35HS67MDWL246EZQQWMQEJX3SDAA264GFQAO3ZGBEHWYYGRLAW2Y",
            "1983088953499407220015OPAWXWB54C2R22FCFSHITT3XE7COX2JWQOHVEEDCKFMCGYHLVB6F5UI4WVJYSCYY4Z22HXM4QMVR25GLJIBHAWRUQMF2RVQ24QECBQC4TE6IRJVI4S5PVVI4ZKGNGTQA",
            "1983088953500807220013BVNH3KBQFYG525QL4NFJMGWKQ55AYH6JFO7ILKIB2CW24SI4FBJCPSCE3JNLKJJG4TVRZVVM2LRQT7FCPR4RM3NA3X4O5FO4CRDSDB5IP32R5Y5F6IQXS5OVP4QK3B4Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "82.00",
        "FARegId": "FA-000000051806717",
        "F2RegId": "FB-000006363080649",
        "AlcCode": "0100000010250000019",
        "Capacity": "0.100",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\\"ЛЕГЕНДА ИТАЛМАСА\\\"",
        "ShortName": null,
        "marks": [
            "197405246782261222001C37QGJQWYEON73VDVEJNNCZQVQ25DWPHXN2EXWA6VVSDBSXMSAEQLUULXLBJLJKXQDZ6YF7NPGZR6ZGJK37W6GF6ZKS6E5RYNZPLJXSOTWRCEVVHRZ6VN3DPT32U4EICQ",
            "197405246782271222001ATI647UKAU5766HGXJRRJ4C5FYDQMEH2U7HKHKVOAB5NLIYSQ7PV43ZXUFNAAXWRIFUJSRLJCQPEX55GQW7VWYJDP7JURBSFLALZQAJN7RRVWHUADK7BS3QQQJTNWZK6I",
            "197405246782341222001ZLP67MTGWWOLLYZMDCD76WNHYUT2R7CUQFENXO7APPDM6ORY3ZFMNSAYWEKPNWB3EHZU5R2ADIAU5L7SXDVKTWJNXTBHBYFEC4X3H656SILXRGF2OAD5VVSVLQRHXR7SY",
            "197405246782351222001A2XFNOIYI6JCEMYVIMYDSCW5HE6GOVPV76M455XLQJSRNM75CQRFDLXODTEIHX23LFTHW7PZNGUHHL4JQRWQPSIMU32OAFLG3ETIY6AQ5TELL6P4DY4S7DYOBLBPK3E4Q",
            "197405246782361222001355NGVSTIEYEUP6OR4M7XNFXTY2NIKEM3EGKSR55UXJNW5JQTK4MY6LON2SEOHW2M6OECUXK6QKQ2EX7GYLO6TNY57YBCUNZOUOMT65TCYHOB7JZSWAKAGZJMEPHRVCYA",
            "197405246782371222001ZNYCFCONK6UVGWN5S5MW2U6KUQKAHFEYQNG6J37TCE5ATX4SDOM3PFKDUUQF5TE2J6JKHFF57DFQD2BRGHHSYXXWA52N5232BF2HWRYXIV2T4SNBKHA5FZ3DZM5ZEMWAA",
            "197405246782381222001GRMF26JO7SDD6BSRFUNWU4TAKME5EEPKCXHRJTHAMLBTPBV2S7YE6IX3PBUU2JNGWB5NHM45J2JHJEQOD7J4YGVRIXNNU6QZOBPDUZEIEAMI4W7LEX4OASAWFVLSLWR6I",
            "197405246782451222001E22GFBKDH2APHUENBOZK4VZAC4FUWHQIMXNY2AAIVW5JNFDZ2FXYQVWDQWPWAEZGT5LJMFHTLIAMQUE2WCREE3EJXGLSE5ER2GMIZXVCMYQUOK557FCMQCS5VMSAV2MXI",
            "197405246791511222001RFKSGCDOBXKAKHQCYLFJGNC7VILNK2QK44WV27YD7LM45N347BINGNFRDZAYERCVWJDTC2DXYWMUTMG4MBTNPX6Z427ZI5LIEJ4PV2QML55WOS5MDIX74LMRXXMJAQOMA",
            "197405246791561222001NOIQ4SYCVJJDPJBEDXAUAPQXMQIZNUYTFFRCGMDU7ZSNANXSVDGEA263GCNC6VCF3VPP4BTVI6GHELIERFL2DZMJ2SHZPQWEJPBDUX2X3WBT4ZL4PU3CEKN7PHWYSCUYA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "96.41",
        "FARegId": "FA-000000050463588",
        "F2RegId": "FB-000006363080650",
        "AlcCode": "0100000005360000024",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\\"БУГУЛЬМА\\\"",
        "ShortName": null,
        "marks": [
            "197404023296070822001AISL24IJW2TI7WLQOGTB6AIT6I5IURYZFHRQ27XEFPNNN6LVY3H4IH7GA2KWS4JRNSPYPNS27RBZEI5DBHIDCIB2K67JPVUMLE5PBZF42ZV66SIOPRBFKNWMSEY2LYVII",
            "1974040232963508220014XX3FKDAEUHHIH4SUAS2SEJ36AS5Z6M4MRBGA2GMCZF3YQHD7DZ7B4DJFCJSTTVNLXVRCHO3B267Y5T27EY3Z77GIABNESK5KODN2MTDXPZHRFDY26G2NQZ42MSQX4I2Y",
            "197404023296380822001TIIB3YYGQVOIGVGK57ALGFDP6QXXS6EGI6VJQHDTXZWM5WR4I2FZQCFXZTY35NWEH63T25M5PACSRLV3UY7AD6HF72E4XC3LX2E4JIHXNDBZKIQL7HS3SAGL5D3QKTR7I",
            "197404023296390822001TKZXSXTZMGFSRDK25A37IGRDJABLMCDSBU4G5IMG63KIVDROBHFYGJNLFCA5RJUVPFHMLNHZIWM2QBMAFYC3Y6Y6C5FYG3KUYJSIPJJE67KMQ6UUGZ4QXCOTCF4OWM46A",
            "197404023296420822001OG6NGUCOSIYB4USE3A7EPDR2V4UWR4ORS34QPI74HIGJXEVZFB3JVDUVYNFXC7TBXI6EMUZXSG6W3PX4NFEXRCC34C4EOJE7HALJHGC2Q43HXHSLU2OVM7EVAOURN3NGI",
            "197404023296430822001E7WGLHRIGZBOGGPDFBBWPKKPEQPGETI2V63IN2NIE653V7LUXRWHK4NF3KO737RMXN7OQTSOS5ZSAO4TQ2VRJCYOOHVB4L5XPEX2ETJC5CB5NF6AQDWARWIPCG2RSV3CI",
            "197404023311250822001MNGOTE2GVMHFGEUU3TRC5PDLR4WYR3VBIEQCTD2SJWA62UGTXZQWUGBQI6CJQXB4SZPCY2FLTF4BESJ4I4MIOYCVLIDROX2ENTGRTJKWNHE37K6MLO57EJQHRAZGWEQCA",
            "197404023311280822001WYPPLSJGSJSTXDJRSG3S2VJV7MTDUPSBOSCBL4KVZ7APCH6Y5BM7CC773FRWJLVHSQANLM2JC4CBVP65LVZJW22EWISHEWEFEIX2AXZDQL2C7WFKWOUMD6MIY2ZVE5SVA",
            "1974040233114408220017ZSAYACCUQD2QLJXT2JQGBEVDA6PKKACZ4PO7WBAXX2GJWE5QCSZF6D32ATIW3POF352KMPW4UYDTS4F772XT4YVBCPMED6E56HOZSETXEHO5N4MCTBNCXRNEQAKEXAOY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Турбинная ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902003",
                "ClientRegId": "010000000536",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "84.00",
        "FARegId": "FA-000000051424446",
        "F2RegId": "FB-000006363080651",
        "AlcCode": "0100606942420000046",
        "Capacity": "0.100",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам «ПАРНЕ»",
        "ShortName": null,
        "marks": [
            "197404296383720822001T6NVXFNOZNN3ESC7SJBKAAA2LIQLTKBADDJTZUR3BNLUTQ3NWMOE6JIWVZEW7RWO6MXYNM5V3MKKJWPSU5Q4XOHMROPILAWPYXQILZX5CSUCSRMRMRYRI33VHVGQRGL6A",
            "1974042963837708220015CNCI5CA6VCZR75XHFMBPARP2YKXGASFXM7MNYMOHAKHLDZ2JZRROPHTC7AL3SSWENXCS6DFGBGNZ56YWJTWYXCYLJVWSR23SPPRVD3BTAUHJNAMCTLVZID5SVLTOSANI",
            "197404296383810822001TEM2GPOCNK5TZQT3CB6MVBEFIAMJAOHYRMMUAONTHSX64LGSMZKY5VZTGRW5RSTISBVI2Z2JHGAH2SDAGOO7RG4BOO5EDQST755T4P4KKNJVLTY5HRPMSU7KMQAABS44Y",
            "197404296383820822001TA5JF3JFCVUGBUL6WBO4BQK3R45A3V3ZAFIHI5OSKKAV6EHXY2NDWFT52X2CF4VTWFEN4MYP55IINP3T3SFTFTEE3Q5IAKXS653KPV2C3V5ERLT7RAELGPJGEJLORR55Q",
            "197404296383830822001H3LTJPCF2X5OUHIDUDJZZMG33U4NDSL2NOHEGVIS4R3EH7JOT7XOHOIDM3MY23LTEFVQFID77PEMGKXAHGVVNLLLMCFIPJTJZHJA47ZD2FTX4JN4AVME67IVPRWKPAYEI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "299.17",
        "FARegId": "FA-000000051808160",
        "F2RegId": "FB-000006363080652",
        "AlcCode": "0100000054580000138",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"ХАСКИ КЛЮКВА\\\"",
        "ShortName": null,
        "marks": [
            "187420633638730223001HAHAV5FQXTHBENLFOIK6SEZFPMPYNIDPIMWFYZYOUTB5YXDM4YVY3XFFTG4ZAYAVBLOHUV4HDTDSGLDOS5YBYUL4HLVS2AC77WHE4NI235VJXKHOCBS433SARV3RAKDIQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "164.36",
        "FARegId": "FA-000000051624079",
        "F2RegId": "FB-000006363080654",
        "AlcCode": "0100000054580000011",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ХАСКИ\\\"",
        "ShortName": null,
        "marks": [
            "198309765795020123001TTQSSKVR74TLYIJQJEZ233DNUQHKJJ6ACOV7WMAF4KMSWU7QYVV7O6ZTZBMNGSV5J56VHQ2JHX2THNCWKI6NNC22RXZIN32G2M7HC6GE5XA6FOJOM7CEINNVI6GYKWLQQ",
            "198309765795050123001ENXJ4V7IMVHH7RHQBGXNW5XV3MTHBMGOOEN4NBQELJZYR2XKR5TINQYVNYJZJ4F5XIBJFVDMZ6YPOXSJGH63NDXE2XGPPLTZVDZITOXKG6H3QH3KAU5PLB2YF3YK4IXHI",
            "198309765795060123001RNBQXK5VFITWLCXTNHPYPDHYREAKVEHYBZ3PPBYIMQCHZHSDR3ROZICO5QESUX7GK5BDY4BTTZZDHCXOHVTOC272M62WJZZVRR76O372RBFY3GFRR2NIHFZNNY7EFPI3Y",
            "198309765795160123001AQAIP32UPEL6IU5O7GFL3WYLUIDQAXA7QIL5ERUKX5KDZCN3A3JP2GYHZH3TD5FGSDIPEXEFCENIUU5MV66L2XP5NDXG76TV5TAQTNA7NUCOJPYKJBDBFRURETKZJNY6I",
            "198309765795170123001DQIVMFE3YNKHSTONDBP7IRXAEYLUWXC3FMBVCSJDR3EV73O2GFAHXUKDJGUOMZNIO3RALP2MKOWFR7GRP5WC3SHSUKRHP2C5ST7XQ2D4FUMDCI7W2PDRG3WSUUVIA6G2I",
            "198309765795180123001OPOR4SDH6K3URYWCMJR2SUU66E26FIDINZ55R22AODHAF333GD3OV7DWW4ML7FYXFWYD5BTE76TBHKKIA4IGYE74XNU3VP5XSMFEJWVGI2ZJUXYGFXJ6KEOE6WS6ZOAQY",
            "198309765795200123001QS4E5IKK4ZOH6FOOOSFXZ27G2UYEXNJ22RU4VX5HFKBYPA52JO52VHSOF3BND7KCEWS6N5VCZLEQZCEQI45CTIVZCWIDJVM4O4RD7QFCBXHJ4INB6MIT4CRWSO25RWDFA",
            "198309765795210123001TWJ7BTKDANI2O7DVPZAXK42WBAGZ6RKOTXQLNCUJ7UMCJNZTDSOIZ6VS2QQBQTTJDM3NPYLPZFUVVNLQRB4SCFXFHN7TUMDZCSJOPRP72564YFTR7CFVFORURNUUHNSFQ",
            "198309765795240123001D2MR5C3WTOBMFNTGQIC5SGS4NQKMJM6FF4VFU7DZTVM5LT2ZZLC6E2WTWMPQWKJMPQHEQIQQEVN5PABN7QVMBHO33BD73UQWZZKIUKEBKYBJUCFHHLLNGGMSLFKKVZLWA",
            "198309765795340123001TM6L7W43SVZOGIM2EI3S3NAASIH6F2J3MMU7UMEUXMZPBYH4O5F2AEQZPD66ACO2VM5OLKGPFXS5SRMMXW2WG7C4XSADS2CIZPFNTZVONUJVO6ILSXO5GS5TJ3DGJO56I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "316.64",
        "FARegId": "FA-000000051946503",
        "F2RegId": "FB-000006363080655",
        "AlcCode": "0100000054580000013",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ХАСКИ\\\"",
        "ShortName": null,
        "marks": [
            "187318459314081222001U2BPKCREZVPWJTEQV6O6Z3Z3OIHQTVETYF3LXYQHULC6HARWRO37HJYGGSB5LEJ4FQ2NJE6E4SAWP6TC75RXUYW2QY66QLCY424WAPQB6VVS46YZNDDIVZQMQHKVRHO5Y",
            "187318459314221222001JBYSX622P7QBK4YQOEQGYPOLJU4TYCORXBCG3LKSCCNFKBYMG3ZWDTD2Q4WRWGA5BTFMIV7OII5BISRXFPNO7LEGA72XNVA5XFC6RILYVIH2GO4L57HXK6Z2Y273VP2QA",
            "187318459314421222001NDLEZE2VYQREARLU6C6K3EIXYA47NMPTJJSVHE7LJHIOSCM25BCQG27ZPQSOMD4WO6BO2CHJY7YQLIERE3BKQMI4XW2NHIT4RHV2T5J2SLHEBTADJ7KT5V266NQQSVSWQ",
            "187318459314471222001IR7ECP2DIBPI6QRIECJM5QAJDE7REGVCS77FOG3CIJF3RKXSU7BXSH7XJ6GIOQNBHYL5ITENKXHFWW6GZUWVQAJFUCTWG6NQEXZ722HFVPBGYQT3ELHWOV3M5TWF3HYPI",
            "187318459314481222001NDQFY5PT2KMR3L5Y4VXHHPVLUMOXKMRL6NYQTWWIWBELTNB5GNW2TDE4HSVFHB2AGRF76PN76SNDYH5H3HRRVPVADX63QK4BFRAKOSP7J2CB73JQ24XMGDZ7IZQLU4DJI",
            "187318459314861222001NEVWHJMC6DCN6RD7P6TGORJLUURX2P7KRWGQTVQDI7DLTWYVKDLHTST6G4QLMBJD6U5UKQQSI4X35DRFHG3VHI3DKEUSTGXXO6D3NB7ZAIJQJLBNHCBNO46TUNCO7FFSY",
            "187318459315041222001J53GIS5COND7F5O5PBTCCO4ZF4FK66PJD2HUX7QT6DEALYEO7OLA2DJJGUX6LDCCOGX5ZN5E5B6OJ2N2RHGKHLIXG3IUJN5Y26XBTGNP6CE7XBVAO6F2LPTRFO2AMM73A",
            "187318459315061222001CIFM2TM7GN5RPJFTB6CTBKN4OQVSW7S3MA5M3TJ5LRJYNIU7IYL5QXGUBQUORT4OGIU6JURFOTYHF7EIV4JJCTMR32P44CJOKPGVK6HDSKZ7EC33KVEKEXC4ZLT6FBHZY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "418.54",
        "FARegId": "FA-000000052089927",
        "F2RegId": "FB-000006363080656",
        "AlcCode": "0100000054580000014",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ХАСКИ\\\"",
        "ShortName": null,
        "marks": [
            "1883027453361307220014FXK5X3SXJ2KWJLBGLXU6Z5YBMNRZ4CM6EHGZH42ROAXK7WISTHJTPKOXG3WE3V5VNRBUJCIGGAFTFBA6LUJ7O5QYG2E64HTJCTZMAFI7BEPXJ55QXT7GCMAHIFC7QT5A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "151.00",
        "FARegId": "FA-000000051994192",
        "F2RegId": "FB-000006363080658",
        "AlcCode": "0100000005450000008",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198411825178460223001Q2WNFKBTEONGXZ5QJFSMRXGRJQZRXAWDI3ZGKHYGPBFNLUWMLUWVC7DNQG2CTU4HHFGI7UATRRCG63PHHDF33EDNMJWIHOPE4L6GMEWD36DLAT7RP7WEZT3T7UDLRRAYQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "148.00",
        "FARegId": "FA-000000051806743",
        "F2RegId": "FB-000006363080660",
        "AlcCode": "0300006342850000032",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "198411080500720123001BFA37MDWLYTBVA34HRRKH2JBP4S7DMWDB3BXF7OBZS4UUDPXBU5YK43JFPU6OQSXMMJRDJBER2VW4Y7LPLANNYI4TVG3PTIS5KNTT544G275QCV5YYJJ4NMVVKM257IJY",
            "198411080500970123001PZTO4BVSCU7BV2E7Y73HEIKVIE2FCRJCM645EGUUNVVBOX6ED5DG4DYT3UEMTS5PP4PKLKSZ547EJDQSD6NEYJI7MQGJ3FIM2MLQQMABRQ7C55XCM5U6Z5O4SRYXPOLEI",
            "1984110805011001230017F7ESGUGUXZU6U673H6LDZPGIYHMADZJ6M2ZNL4RJTPHN2BZSBJM37BS3SZGAQKYE3BT7ZIY7GODO2I47FMUUIEFNW664LCXDLQAPS22GJPOR6IUNOGOJH2F7CFO3WP3Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "221.50",
        "FARegId": "FA-000000051911905",
        "F2RegId": "FB-000006363080661",
        "AlcCode": "0100000005450000007",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187418772848870123001WW3TRGHKOKYSAHIF6L7S5O53GUUZBBDVKVGIRKCSUBEVWZRWR6SQK2ZG6DH7Y2LUQTIJWSMLNDDY3VE5UDBP4DL55IJM4AVZMIPCSJ43NZOCQFXKJZDLVP4QTPKZD7GHA",
            "187418772849010123001EE2S7AZ6SRJENS64YGRB3PDKFMKJSABYMYLK2RMLLNFBADOCKBTT22SN473TXPRCHDDCTZIVWY7YMG7XNYZJK6FEKFKZQIYRVO67IJ72LQNJNNOILAFTQCHWI627HH5EQ",
            "187418772849020123001554QCQLJBMX76RU2VSXALL3HXIOUBLMPMYHNTAMBLO2GXQDKCGIPGZKGQ22QXKB7F2RMOEIF755DIEVBFGYTLU5SOPGEJQ7JDWQTG4EB5BKJFNZLNNBIJO5YGLR2RNU4Y",
            "187418772849030123001WQRMBIXEJWSQVYFSPPW6AXLW5YUT3HWB64NQ7EIS3XZCERDLSHMOLKO4TP5ODCFSEBFPLQWNK32KRJ3CBNK3KQ6HVGX3GLDFOX7YYEAUHG3FPKXIZ4ZU2FNOBXL6ASOUA",
            "187418772849220123001HYYZK2QG7XZLB3Z7RPXKCGXWVQGGDX7PLJQ5MCZZNEALC2NQHVML2ZXKSO76QJJK2X3FR2VHWUEQQRAHMBWGLGW3J2WF4QQLHXVRB2RWQNCZNGZX4YA2EYY2CYHMWR7AI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "227.00",
        "FARegId": "FA-000000051116546",
        "F2RegId": "FB-000006363080662",
        "AlcCode": "0300006342850000007",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"СТАЛКОВСКАЯ АЛЬФА\\\"",
        "ShortName": null,
        "marks": [
            "1874177572987512220014A657E23MUIVW5NABXTZ33X6AETRECINKHQSYXWO4MDTPPDUVGH6XJQ4J6DP2WX4RAQBKGS6B72CXBJPTTGEFMZISQHKHFWIQ5DT4L6NVD2JURS5SAV6AW3BK7EWYVG7Q",
            "187417757298761222001SI4RZ32RKAFKWBZYOP75JRT36UCZ7GGIL3B6E4ZG5OEM3OENFMOV52KPQL75L7QHDDEIRCJ3F47AQA54QQEGM3E7N74DQ5FJRDLXNHSG4LY3PBYKHKUPFM3SYBPCRETTY",
            "187417757298861222001D2CDLM5A6SMCGDIUUASLE6GSJIPVOVCU7GHNXRSU5VHZFLNZW2H5XNYUMQTHJ2474BXA27HOCBUAKW4FCZASD55DBPFUQLGZYFBCTHGUF26U2B6SCTQAMCS44257KQ2UY",
            "187417757298871222001BMBAKZVAT7CY53XALO3AG6KHAQEJKDKBCC52NEXEN6GB7PR2NU2C5DEAMM22GAHLKHWFEE6B2F4XCO6MHL7QLTBH62F4RAHC3EEVRXPAGCRWAO7CKWCISPWTNFAQMYNPA",
            "187417757299871222001EHGYNFQZFPJ5BZ2OR34KQT4EDUUO5HMDJ5BUZENDXXAPGJ5P6B4OYVQORN4P2PZQEY5YUIF5B7V37UQWTDN5FVSNMYWVNGF33JCJMAMMRATIIQHMLGRF6SUJ5PHCZVE3A",
            "187417757299881222001STDOHT5Z6YNVQW5E575RW2JRMEO543EWOZPU62XTMSGFREID63IJ5MVPM6C4BG2YEBZNWUWLWNH3UUPD2KZUIXPBRNG67W6KPLF4RXCTJPGVFANIZLY7K2H6RJEOWJOTQ",
            "187417757299901222001OQM7X7PRBQ2CSW7QSMACUSA23EKUEP37GCEWRWRY2HF3ZJXOIKVFYTSPLVEECV5WABZFBUCZSYSLBLHU4U3K4FD2TEB2UJQYJFYCVNZ6SLFPV3T5TVSEZCUXBWBQTGDRA",
            "187417770950021222001EFXSGIJFPGH7Z3TIFXAMQKCLAIKY4DL5JZ4YQLMJGSCSSZB4GSO2CUJGLSFFACH32VJJGPZKC7U5YPV2AGH4ZBLGRGYMOB7VDFSFMZYYHULYKI4QHXGTZTWHFPFYDUHSQ",
            "1874177709501112220015HMJSLC337XEMGCF37ZVBOUKYMBYWAWT7ELNKNC3LHPJW7FGHGRP4QZ2QIVVLR2UN4LSPUQ5AFDSNQQ45AB4UFHVLDVFH45IGLDZDB77FBBFWGQXRKLWG77V73FJPIK2A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "275.00",
        "FARegId": "FA-000000052016008",
        "F2RegId": "FB-000006363080670",
        "AlcCode": "0300006342850000001",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187421739759800823001EQITVRNYBAMQKBA3VMZDUIS6N4S5PWRZ7MCNJPSALNDV7PY4OE76IY37GOFOMXCYUGIF6U5BCUPYJEJGJZC5RZ34V5AQZ24WQIR5P3RAZS375REBNSL4P5545PP3ICBBY",
            "187421739759810823001UQNWRNOX2LCEZPI3RYVZ4ZXEOAQPJ6K3JIU3DNTZDFQSZYO3XHUSERQH5PIRJUUIZBWFSHCPWPI6GEHMLTHWMZVKBYQVZFZ3RX45OWEWDPSSHO734KDRELM5VPZOD6KFY",
            "187421739760420823001YBNLWJTELYZ2ZMUFX7XWC4OBJUNJFJ4MZDIXDE7T3DUEQS4PAQVZPDRYMXQXC2MBFXRIY7MAKCLUPT6LLZWXRWIQTHHUM5PTV67IONXNHYDO22PGMKSGM6SLNA5Z2GFQI",
            "187421739760430823001HPYRGTO565HQQ2NTKLQT6MWBNI2ETBDAAYFYLST6CDMXIBNJQVSY3KEOJL3R2CZ7AIKIK2ZHTIMAF7S3KUK5QX2EGMJ23FO4FUGG6K6SRZN4GK3ZG65XZJ6XKSBUH2YJA",
            "187421739760440823001GBK4QBTO3ABF3Y6UOAGNATQOYACHBKAMDMEUJ2NLZBG3CBUVWDNJ5SILTQHTJR7YRVTNRVDGII5K7A63SINEE5V3U5RE37BHND6V5CGRPOEWSYHFM2RFIP36CEKK77O5Y",
            "187421739760450823001AU6QMPWQTUAQFKRBRJW45KVL6IFLYUCVCGDYRESPMZJRFUA2AOLXODTQBTFQ5TFLVETQDYH452AM7TSFL2LHXHBOGJ22G4DY3RJUKLBARGQEITCPBYGLZB3VQZXJK2O6A",
            "187421739760460823001IJJFNZFWPJ25J3GHIL3YAOLXZMC4OJKBI5FMXULFB7TPEI574WVSZPJ77AZRYC6MPZYVX2MQAXEECBIJFKONRBOVVNH4IDAV2T3VTMWDCSODMNOALZULZW2ANEDWB3YPA",
            "187421739760470823001IM5SES33YNTHEHQSOKGL2G7JY4DXE46NAJ2G7WBSRESIWUGZ6A7ZOTFYM3C2QUX5W4NO6OA4TZZ2FBU7UWAASLDNMJQ5FADRUBB7XZDIEIRRP42HVN6SETDNMYLJHNNLI",
            "1874217397604808230014JF5D6NQ5XUEHCTDFMFED7TCXAL4UDOVZ72TQL3RX34OTISWPFFU7KNPOKWUWG4G46ECXSZOX6F7N7FVCTWCJ3MZC3BXRKKDB3VWJDDHDXZUF5KVNEEGMJ44CW7A4IKMY",
            "187421739760490823001U7BBF6SND23SVOFCMH3N6JLYFAASRXDA5R42M63Z3U2ONOF2PIZWUDJ2HBR5BP73ES2OX25SN6TQIXDV3LHADNLVY74FKTLPQOJH3CH66WN7VC7JP2P2QJJUA4AYVCWHI",
            "187421739760500823001I2AG672C7PNC2XAAD76AGTRQCQMJLBLCWFL5OC25DS3MVBWLHSPALTQ2AXRRXGHGWOMPVOFV3U3VOXUIIWPA223USYIXPLCNDSHAQEZ5KNV3E47NVRFIRH27GMOMQIG3Y",
            "187421739760510823001PHJPDYEWYGMTLWMKXWH6I6YFOQXDGI2VUTIFZEDVQAYT3KL3R3P2RSL7PZRIPF7FTRVZAKNYEH52VF3ZX4N2U6U36NQRBSESJCSFNSF3I2BKKYJQJO56UM7GQVU4F6M7I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 12
    },
    {
        "price": "292.00",
        "FARegId": "FA-000000051164835",
        "F2RegId": "FB-000006363080676",
        "AlcCode": "0300006342850000006",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"СТАЛКОВСКАЯ АЛЬФА\\\"",
        "ShortName": null,
        "marks": [
            "18741765863040122200144PR3JZDVK3S3O5GMG5HMFVDUQ763YCKSN4CV5ZRJRG7AMLRK5ZY6DOWWY3RW3OAA2N3IGFO7WVLNYV3SBKC2AUSA6PS4ZHNGADCST74OSBJBZJS6IUSUEPOQ4KWCK6WI",
            "187417658630451222001PMP4NB7B2JR2JE4MN7BJMBFUN4XN3YBVMBOVSSLEIKN3GEDRIYYGQTU7P2ZGRSNSGG26ZMSSPDBUY3PLOOORVRVW6QCK2BB2UN7LM6KNT4IR363HRMGMQ2QD2TXILB3WA",
            "187417658630461222001AQ33UEPV2VA7H3AXLNXBN5SXOU2H2L2WTBQ7YPYUOLUCLMYYHDRZI2D72BBJKEDR6GWPXNEUEELCJUSWPL6MRWA4XR3FNFYHZH53JNSSSWFWNBV2XLEAIVTN4OWBXUJKY",
            "187417658630481222001F3A7UGOBJHBU4ED6U3IQZCLOIUY6Q4AK3XPH3H65JCAMNCT52XJWI2DK33MW267JWYDUQEQZ7AGDSQ6UYIBVCOZQYAA2MBYUCL735F736YSRKSAKD4IH3ONQX6HDZFRSY",
            "187417658630491222001MWFGBUFJRRKOXVXWQFGV56KMFQECDGRV2P2AD4OVOQPYUT4XOYPWIDGFNW7O6IX7BADYH6OTB3LPLSZPRUEA63GZJ2QD4XHEMYSRRKXVH4KM3QKOMCJ2TODA4GWBZ37SY",
            "18741765863051122200162WUEPR73OMJX54BXRS5MEHO34NVXM6E6NWMV5WRONHTZ7KPKKBT4TXDJRRM6EBCE3L5XLXZILR5N7O4BQ74NSFRK535SU6CWL6DFLHZG3SFMFFTEVDMRTWOTQL4XI62I",
            "18741765863053122200167AUEZWI5TOYH7I5MYXR4YQRLUN244CX6ZK4T44T5YQXBCEJVEDNEBCUKBTVEJ5ANKN3ENPFOLN2OSXW2VSJAVE6JHB2KAOICI2SA62ONQNFS463ZI4R4EJLAM3VTH3WQ",
            "1874176586305412220015IXUIXTP462FHJSYRCZNSCGD5UNKIYKKSY4AJR4Z2VGWOGYHTWS4OMXKLUD22ZSWLV4AYYYH2SD7TWYPBIRVOVCIKGMD3IEZZYCD5MYPO5GM3OCLSFGCL43BSEEWSBQPI",
            "187417658630561222001WVA2WASWRII6ZHT5OXLKTCWYFAFTPLBI4GUDGLNFEJNQCHDAHYBMW2MENU5XWXLHH43PX6NMCY76VBQNSQMWSAY2FQOUCKCQKQCJBPT3MGGCV2CG3DCHBIQUZBJLOPETQ",
            "187417658630611222001CIGQDX4QUXRQAZ47Y27DC3TSMY35PBEMB26DRB7C3MCMUPYIQWENSHM5H5TMBPLQBFZGA3TEHO2C35UYUFMFOXYAPUHG3L3JUNBRN2HBTG7PZCW432HXRHDDLV4Z4WY2I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "292.00",
        "FARegId": "FA-000000050119950",
        "F2RegId": "FB-000006363080681",
        "AlcCode": "0100000005450000014",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"ЧЕСТНАЯ ПЕРЦОВАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187414387696851022001TRW5BRRE5E2TDJJRV55SKRHEWIAUBPRCLWNTT6AVYJ64I4FAOLBBWJFEPBAT5D2A3F2XFWMXMEOTIHV4CEE6NYHKS3F2V2CPPYRZBJJ5EH3AXOE5Q465LW3NFZ6TITB2Q",
            "187414387696861022001ULHFFFJRFBLUZDBM24NNVST6H4XA7YMM6A4HKRKAGMQVI6FBTUAY2R5WWUQYWDGYJEEJP2WAN57ERUKD7QO7HV2FK4BNALNYUCZB2CXD5HBIMDMN7AYYFHGI7L2F6DTPY",
            "187414387696871022001GRFYIU43MRL45H4DGVLFYKHN5MY3DJ7AQPE2PVLLQYFKVUGRDDVWUFXCNJSXIEHV7ISMZ6J4ROM7OUA7LHKIROKZ4OP3UAT56H23WX5DI62XKWEDLLV7KPEPS37LRJYBI",
            "187414387696891022001EPJTQS7PUUDQETWTSTT6IKEMGYNVHXMEVTWXXBHDK4NHZKSHPKFOPTDUVIYWYQH5UUTJZFENH7SCLZVKWDDMPIAE6TA4KKGUOM3PCCR2HF667QKFQFPUZHXTWVKVUSCJA",
            "187414387696901022001T4J3QGTD4T7SN62NDMCKNKHWHUO634X7V7GU2DIPRFKLZUPCRC6N7H2SG6RD7KWX244F3OD24FAATQ3O2KODEITHKCKVZYA3LSNXHQVFWBZLSX5SZB6CFQ52LZYJRWRNI",
            "1874143876969110220015VHULJY5VRKFFTJPDIIJRKMFRYM67ESSNGVHP7WK2L3ZPZ5RSGLZ77GOWISNRDNKYHWJDKFKJFSEPCYJENPN47OPV27CHPTHL5J4LR76KNSH35BNFE4VLI74QDYDJOXQA",
            "187414387696921022001HBACOXCGAHXMMK47BUFHMKIPXIVHLNNDYCZMA7AQFP4PXDED4XVNVIWHDDROYSVEQ3EOKOQK3M6FWH3XSS623OFXHYGV77A7Q4BB3WZJVBG7VCCYYUTZWF7DJNORNKC2Y",
            "187414387696931022001Z2X36IWU2C5FEUI7LHOVQMAHCAQW6PWPLSPUJUC2AMU6L5LSNG4G2KMTCLSPKXFHRF6JIT5DRAOSA6FABVBXNWJLZYW5FIH4KFHBVLO3NTGHS5R22SRULE7FWZYZXMAUA",
            "187414387696941022001OFZYH2IJ76QO64VS7FJHL7GB4IA5B6FP4JNSETR6SA4MK4IHXHBEXU2Q4AK4LW3TKNSM7SL4OYUGE6MT3JVDTKDUKMMME7G6L2WONCMVGHFIKJDJCNV5B4JVQZ6SHUQNY",
            "187414387696951022001F724TWRLJXLY4GUGF4SEFIPZWA5VY6CC6MBQJNE5RWIS64W3TXWD4ZO5WZTJJYYZNVVAHZZCQFCUUIKSL63LT3D44B6MWMKKMQ7M552XBI4PK635YYTLNY5FRTX2XPBNA",
            "187414387696961022001XADFYYPPRC3Q57W4U7AMAN244UYFRXMLCT3KW2WGFGBD4HBOYUEULV2CFDQPYW5SLGQJJARU5OWBKK4KSAID3UAQR2AUYUCV2HFI5M4XVCFY5SS7BNOZFPKOJ24GQ2KZQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 11
    },
    {
        "price": "270.00",
        "FARegId": "FA-000000052043391",
        "F2RegId": "FB-000006363080683",
        "AlcCode": "0100000001400000077",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ПЕРЕПЁЛКА\\\" ДЕРЕВЕНСКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187319277240410623001GCED7Y645LKH4NL6U2L32OLH6Y73QESK47C57M2G62FB6Y7LNAHL52MPL5G4X6YWT6Y3RCUHLR6DRGDLZOPRGC3CLEBS4KENRA3R7TSH4SRXVVDMTC5MZZFFTPXMONWWY",
            "1873192772408006230012DILLLWR3H4NNGTPEJK6ILUJGIGCBPEQIB5TZJZVK7IEY45OJ52AUFHUWHVEYFQ64SXU65EP53IEJA54QW5YQT3KDFPOYERGGLJ5K5DYSKSM35OVZCVOBWCQHOSURDSII",
            "187319277240900623001GIK3RKDL7VZBSRYTSUMGZ6PSUIONGWT7F2OOV6NX3NAB3PA4CSQBJS4KJMDA2O57VCILP5NHUXW4U3ND4RTW5AQKMZTNMGSZ6ZEUGV3UEYPB32T6KXBFEBQAVDQA3O6JQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,,,,,Великий Устюг г,,Красная ул,31 | за исключением помещения литер А`, этаж 1, пом. 18",
                    "RegionCode": "35"
                },
                "INN": "3526000633",
                "KPP": "352601001",
                "ClientRegId": "010000000140",
                "FullName": "Акционерное общество \\\"Великоустюгский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"ВУЛВЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "270.00",
        "FARegId": "FA-000000052186001",
        "F2RegId": "FB-000006363080685",
        "AlcCode": "0100000001400000086",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПЕРЕПЁЛКА» КЛАССИЧЕСКАЯ»",
        "ShortName": null,
        "marks": [
            "187319677858990623001GJOAIOHJVYMGZP4JBA3NGAMYQAQCTJ3MINY7FK3QZCNMHI33LN3IX6MEO6XCND6KKITCB7GPS4KHEY5A5F7YTZH4EAGXIIQKVERXWS2QVXXYVCIMG5VBXXIIJDQFJQN7A",
            "187319677859050623001KSGUIUJZGK463C7Q2POEVUGWIURJLCNKK37LJSPNEB254T6TED5D2273NVXDA5WEZR3PF3OYANJUO4FCLDBBJRC47ICGWCPWMLE2V3RSVMFK2CPOMVINWBXV5RB52QBWI",
            "187319677859060623001IMUA5Y4GRTNMM7D2HOGMXWIOKYR35DXXC7HQEAELTDLD3X2ZLHBTW5T5ZH6T4XMVEKQ4PMCHROCCN2SAS7DASWNLF2UHRZ5VGCFLMFKSSL2L5Z44362UGWXFQNL24N2LY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,,,,,Великий Устюг г,,Красная ул,31 | за исключением помещения литер А`, этаж 1, пом. 18",
                    "RegionCode": "35"
                },
                "INN": "3526000633",
                "KPP": "352601001",
                "ClientRegId": "010000000140",
                "FullName": "Акционерное общество \\\"Великоустюгский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"ВУЛВЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "270.00",
        "FARegId": "FA-000000052168217",
        "F2RegId": "FB-000006363080686",
        "AlcCode": "0100000001400000033",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая «ПЕРЕПЁЛКА» ФЕРМЕРСКАЯ»",
        "ShortName": null,
        "marks": [
            "187319692722770623001NGGRIGVPRKNKFQNJ674EY2O4C4AFWCUVM6E3XVXNCNJZTZ2M54GPZMEHBR5NYDTAFRORBZZGOR3C5F2PHGTTMR2GQLBR77GYRJPA3RK24W7JZSRY7I3ORYEFIN6EQD2CA",
            "1873196927284006230016HS7LFNSGHD7GP2MYBX6SQKTPYYH65AGZBD2M6NSZVIEPKTTBJ2ZZL74VCEU3PDGB2WHTJOVFY2FJNB5PJQKQ5FIZLX55OM4ZHF2RI2LD5AH5JJMJJTYK67UVZZPVREJI",
            "1873196927285306230017GGS7ZQJPTAD2SWS3XKWCSAVLUPXTAKNKPORTANUXEPINDMXXXPUZUN6JPQQJMRXA7Z3UOX6NKB45464OI7X6BEJDOE23UVZGF4ZBDLEXY6PSJEC4PWNNN4JNJ2NIAMFI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,,,,,Великий Устюг г,,Красная ул,31 | за исключением помещения литер А`, этаж 1, пом. 18",
                    "RegionCode": "35"
                },
                "INN": "3526000633",
                "KPP": "352601001",
                "ClientRegId": "010000000140",
                "FullName": "Акционерное общество \\\"Великоустюгский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"ВУЛВЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "270.00",
        "FARegId": "FA-000000051933055",
        "F2RegId": "FB-000006363080687",
        "AlcCode": "0100000001400000035",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая «ПЕРЕПЁЛКА» ДОМАШНЯЯ»",
        "ShortName": null,
        "marks": [
            "187318054884061222001MH7VBYYY3FMK6G6ZASWZRLIYCITJWPRQ4RITATWQ6EQNSCPY5VFZZJQNQ7BT2WBP7TRH7V4R3EDMMDTS5AAG2F56QI5SHFV7TGLXMKYDX3L2ZFARJ3P4VCMHBDLFUSQ2A",
            "187318054884091222001SMKVCHAIXT4BODH3XZVIJWT5QE7TUTFJNJKT2X2WLIH7JCU4LMWA2UI36HIAYGZYZGMLGNKQK7ANDVTFNGCJG75ENBXWLIFG66AS3Z57LOXGJZL34PJLEG2BQZCV22A3Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,,,,,Великий Устюг г,,Красная ул,31 | за исключением помещения литер А`, этаж 1, пом. 18",
                    "RegionCode": "35"
                },
                "INN": "3526000633",
                "KPP": "352601001",
                "ClientRegId": "010000000140",
                "FullName": "Акционерное общество \\\"Великоустюгский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"ВУЛВЗ\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000051807443",
        "F2RegId": "FB-000006363080688",
        "AlcCode": "0300004334310000297",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"РОДНИК классическая\\\"",
        "ShortName": null,
        "marks": [
            "1874199218500102230012J337E6SUG33TZXNAY3L7ASKDUXQQIS6BVQHK7YAMOQW6DH4GXIRC4GSI6QHVW3JZUXYYW5HTDBKVFUUQBB5OLK6ZO65EFOWQ37VHUC3NO3BHPYTDUPMIF2YAGNCGLSEI",
            "187419923699850223001LNBVNSXGS54TWQXDH6OTFUXXKEV66SCPJPBZFPZGN6ZF5SQN2CIB5XRJWOBOBUJQQWQN5L3DBDAHQLNNPM6JIDU6ISEINILV3PJ62YFKB5PEMVUKQE4P7OQAKRZDY6LKA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,САМАРСКАЯ ОБЛ,,Самара г,Советский район,Ветлянская ул,д. 50,,",
                    "RegionCode": "63"
                },
                "INN": "6318036835",
                "KPP": "631801001",
                "ClientRegId": "030000433431",
                "FullName": "Общество с ограниченной ответственностью Поволжский комбинат \\\"Родник\\\"",
                "ShortName": "ООО ПК \\\"Родник\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "155.00",
        "FARegId": "FA-000000051938887",
        "F2RegId": "FB-000006363080689",
        "AlcCode": "0100000010250000018",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ТАЙГА\\\"",
        "ShortName": null,
        "marks": [
            "198409129222171222001CUZKBUYDA6WISOSCTDNMRZSLFIM4HWJLSS54KUVN2QRO7ACMRTBOS4CFJVNTLGFZ3PR7HIHVACYOFBNQXVWQXSLROWLZT3TDVR3FMSTX6II6POZFRVOH3FTVQLA4WTFRI",
            "198409129222191222001AWKHU3STNX7WGN3EUUTXI3FDMAXKFHUE356YSLQH7SD2J37TU5YBF6QT3NSKAKTEGMFZRTKHQMKDY7T2KUZ2LDMJWCM24VH6PENRP536CK7EXBUBNMLDGRW5BAMYJC4FY",
            "198409129222211222001NCEBXBUL3FY5JMMKRY335XYCW454Z6ADZVPUEVZKE6T7KXBEL4NTW2CQZT6XE26V54OB3YHCP3TH7VWUT4LFL7TV6VC5CCT4UHD6NUZ2ANUEXCIJN356E25DI3EU6FVVA",
            "198409129222231222001PDFVGTPCPBRFIXHVSPM6HGT2O4JBYCNXQOS2MHSEPLDY4R2DQWO7662UXTBXBSO7FELBZJNXMD7ONKLHOQR5B534IKMRIUAQ54SKUONQF5EPVGF2JY32RTDYUCEJ3FTWQ",
            "1984091292242212220012UAWLUJSZ4DY635KDVW5PQIKEY4CTQ35PQXIMHKD2LA33QXRPGZWAATZU5TEX7EAGYWHPG2KHITXBUTQRLWKGJPA63M27Y3SU2FR2FZKFQZ5PGFD5UGPMKIBMWKAF5GVA",
            "198409129224251222001HN75P6566J4IQACQ34IZCDXPCAEZWC2KFE3FQUJ3WCT6HANETQOFYRJK3WWTY5PXV26ZFUYMB674KOBV4ARCWFGVJCBDAAHPQ2NLYYUQA4EMBJSG2627NVTCC2INEQ46I",
            "198409129224281222001I5RPUUMNCCY62EAPNFT3N64TJMGD32XVBFXULMAY6TV5PX6BDEGPAA6HFPHVHQWRWCJFMMUM6PYWW3MOYNY24CBXYPDM44V4YDZLKFML6OKXB5ZZEVX6YVOZ4B7IMVQBA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "157.76",
        "FARegId": "FA-000000051794529",
        "F2RegId": "FB-000006363080693",
        "AlcCode": "0100000004970000167",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Царь»",
        "ShortName": null,
        "marks": [
            "198309891286380123001IORWGKI2KETTZQY3V2ZSQ6FZQQXC46PN2FBQEZAI5W7EEXRDPNNFNWVXAKNDFPD3TL5CINJ76FIYNCY37VX2I7OMAH3MSIF4U6GZWZR4KK5JIDKCPRCW64MTL6OKFTDDY",
            "198309891286910123001UZCSUDLN3HEZSHXSRC7R3SJWWA2PSERUX2FM4W46HHICM5SALE44MA5FK3QBLP256PR42VDZTGQRPT44WL3BVBPECF4DJSFOFBXTFCSPHTMG6WOFD4JEVP4K5DGGHEWSQ",
            "198309891286920123001NOQBUOZ4JSN7CCLLSEQEESX6DYD4UUEPARXD55WCFHHLUOQWET5BU3X2BNFDJVCEHVQOS3UVGHDDK3RK2C4KS7WN3AQXTIBLOG4IW2HZMDRTHBRQ5S6H2NQ6MH3PCNNQA",
            "198309891287660123001RZVVV6OX4RJYWA3PT6ZIJS44ZQTQKPZVBKBA734WN4TZDQFIUENBFSJMJ5FT5Z5SS3UCRKBRIQSOUMYTHRUDNU2Q55WBJUU3WCKBNFMMA2XHROWPKYCZ63Z32I55U56HI",
            "198309891287670123001YVOJWJM5I2KGWFXPTUWCSXO46UY3LMWZVUDCG44YJRDFILKMJLHIVTUCZMV4DZWBRYD6SAF5CVAS4BOAVATT5UOJTV5TC7KSXPQYACLPCIZ7Y2MGGRGOUVROKPJKC43RQ",
            "198309891287840123001CHGDAE4GVZ3CBM2PYX7FLTY4ZQ74QWYZXVCWOOEYPDTQVMXCEXGTCOSXMV6BQHIOZCP377YKOAVD6VKNLZE5EZFJHG4UZ3QZYUILGLZCZT3RPM4JAH4R65GB2I5AQIROQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Краснознаменск Город,,Строителей Улица,15 Дом  , | литера Б10;  корпус 1, литера Б3, этаж 1, помещения №№ 12-15, 20, 41, 43; корпус 2, строение 1, литера Б14; корпус 2, строение 2, литера Б9; корпус 2, строение 3, литера Б12; корп.2, стр. 5, корпус 3, литера Б5, этаж 1, помещение № 1; корпус 5, литеры Б, Б2, Б6, Б8, Б13, литера Б7, этаж 1, помещение № 35; корпус 6, литера Б10; корпус 8, литера Б1",
                    "RegionCode": "50"
                },
                "INN": "5006008213",
                "KPP": "500601001",
                "ClientRegId": "010000000497",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Георгиевский. Традиции качества\\\"",
                "ShortName": "ООО \\\"Георгиевский\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "178.06",
        "FARegId": "FA-000000051755475",
        "F2RegId": "FB-000006363080695",
        "AlcCode": "0100000002700000030",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Архангельская Северная выдержка\\\"",
        "ShortName": null,
        "marks": [
            "198309508001690123001VTLQLLJA2KQB7CVCK5GDQVQAUMKLNP3EE6IKZU664RFW3BO6TILY6I56S63B7UHCTA6IQFUELVF5OSEFRRIFEFNROGVIUZ6AZZ5D4YNPM5YMAJUTDZBLOBNWNVX7HO4TQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,АРХАНГЕЛЬСКАЯ ОБЛ,,Архангельск,,наб. Северной Двины,д. 120,, | ; пр-кт Троицкий, д. 133, корп. 1, пом. 5-Н, пом. 6-Н",
                    "RegionCode": "29"
                },
                "INN": "2900000293",
                "KPP": "290101001",
                "ClientRegId": "010000000270",
                "FullName": "Акционерное общество \\\"Архангельский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"АЛВИЗ\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "178.64",
        "FARegId": "FA-000000051232147",
        "F2RegId": "FB-000006363080698",
        "AlcCode": "0100000004970000164",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Мягков Серебряная»",
        "ShortName": null,
        "marks": [
            "198409827170991222001SBNKJOW3LUX2KU6EWX3GMPQBWATD2ZVVAEJPVQ3XTMWFKBDV4Q4ATMTLKRPYKGMPZTK3CORBCU4LPWEMJBF4DKR4TWHR72PL56RFRIOCLVLNETOXIQLHEFEZ3PTQYRANY",
            "198409827171001222001UO7XDMDWMHG4TE7PPTLW6QX3M4DZYGQUHKD3SGIOYGDCHP3MVI3ZX7DVL7TMPAIXDAO4JUTQU4UZOPZZTXM4QG7RQN7LGT6LBR3HT7EU4TLFCMOENZ5W2734FWSJYDJDY",
            "198409827171011222001NK3F5D5BWFC3HYXKADRVKJJJ34WAUZ6IRNWCLHJGP44AXGCGTJ5LTAWSWR5NXBHGBJL5MADGBB3GU75JFHFENQ7TZ3O5WTWDPBQI7ANVQFZYSXVSZSXV7JKALLGDAXABY",
            "198409827171021222001GR2JMYRBDHC7MYTZOBQY5VA6HYXB57SSLR5KLFNZ2HHKG3ACMXGOJPQ6JNIX5NS6CSRD35CRTPBTSG4UJF6Y426IGFOXRMUEEGA6YUEJRNWCMHUTS73SVLG552QZFFJKQ",
            "198409827171031222001H4Y5WTNHJUCIXAYRGVU2J2EUW4PY2I2D5EQNQRKXOE2HTXIXHYM2FZZCA5I2U6TTWJZEEZABTMIA5YIQIP22GOE4SBBM376ONYT2DZHDFNLMUXO4DBPLEAVBQ6GWHCNLA",
            "198409827171041222001GFLFPLFG6H4BPGYLIXGBIP7T2MG6T5X57HN4Z3TZITERCUSPMIP3OL6XVJMZ7TJIU6JEQ6UPJTEEF4XV75UYTPHBVTWZJHPI4YJNAQY77L4BXBDW7CSCHFLPEUZKIWUWI",
            "1984098271710512220014ICX4GZZRYB6FSS4XZCO7V7NHESZJDZU7Q3UZFP6NB3XCMM5QWNYGUOX5WT4WTYT2YTNJZMD6L6GM64OQG5WKTU3LEEN257NEBPBZQTTPUD43R7EI2VJMHVUNZKMHP3UI",
            "198409827171071222001A4IBNMD4BFLGFD5UDVV47D3OCELUYC4ST7EVJ45S6LT7FQ6ZTVJHB2XTSEOIA7F7OSMWK3ELUZ6B5AGHIOV66JEQXZXHIZ7QJG45GXMFTPSPJJTLNXXBG5Q5RI6UGKI7Y",
            "198409827171081222001NMZR2QC3OMJE3SJEZPFCTSJN3YLGGYMGFUAUQEO3KIGASRP2ZHWG6B2CJDWPBSQGAUHSOZFBUEN2J7ZI7NHSXJ36MM4JGYHXN6PM3ERAFF4HAOSK7LI7WO4PRSM3YME7I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Краснознаменск Город,,Строителей Улица,15 Дом  , | литера Б10;  корпус 1, литера Б3, этаж 1, помещения №№ 12-15, 20, 41, 43; корпус 2, строение 1, литера Б14; корпус 2, строение 2, литера Б9; корпус 2, строение 3, литера Б12; корп.2, стр. 5, корпус 3, литера Б5, этаж 1, помещение № 1; корпус 5, литеры Б, Б2, Б6, Б8, Б13, литера Б7, этаж 1, помещение № 35; корпус 6, литера Б10; корпус 8, литера Б1",
                    "RegionCode": "50"
                },
                "INN": "5006008213",
                "KPP": "500601001",
                "ClientRegId": "010000000497",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Георгиевский. Традиции качества\\\"",
                "ShortName": "ООО \\\"Георгиевский\\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "303.64",
        "FARegId": "FA-000000051209283",
        "F2RegId": "FB-000006363080700",
        "AlcCode": "0100000005360000036",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"ТУНДРА СЕВЕРНАЯ МОРОШКА. ВОДКА КРАЙНЕГО СЕВЕРА\\\"",
        "ShortName": null,
        "marks": [
            "1874177242659312220017JG2L5QOERS3W2QM7UOMZ4EAM4HU5ADKBVVFML4XPMUHCYHNTD43COQTD3W2DOWXC7W6CKFN4WRRSPJE3EAWQ4OZ7ECSZR2T2LM3T3WYZZ75D4WNH3XD3E7JEXR747AXA",
            "187417724265951222001L4OGMNO3GN5JG7MECFUPFOQ5SMXZWIYGPYTYIZVCNKOAYAP7HEOCIGXHDTPABBBPDS3JHCBAE4ELCADY3W7XWJQQ3YADHRXYXQ4Q7EHMO6VYDOGRMZ5IFV6YR4GTFKADA",
            "1874177242659712220015T67JTJQLDW76U764H6DMQGWGITRN3FUCHVXKSABPAMWIWGVR4KPR5PGFLHDWEA5UB45I4MGKVSZYTJTR2QCVAXLFL4ZLAKRHRH2UYNX7CJZKA2ARI7CTXFS2L4PY3CEI",
            "187417724266131222001IGAETK7X6EU2CC7XS4RPX7WQ24JL4LSYRCXVADCXFRKFTRQMUDYXZ2CMOTWWZR42JUUFINLQPNTOYJBGEXF7FMZ6FUFY6HI56UZVYDNTYUY2HTZRRTHMOXGMVDHCQ6VTY",
            "187417724266141222001EN76SXWS6DB6YPME2FM55VGMIUYB5CJITEOBZCUXMHW4A5462BXJMH7CCSNTGONHX6CAQAF6LUMMIWRSIKR7O7WH23XNLNIMGEEHPNHS7DBQ2MAJ6L5ATK65J3VXJ5YRY",
            "1874177242661612220016YWC7KY7HHRJHNENZW6CBXWGGEEVVJGOHBOPSUR2VTGUCBJ2HSZPDMGS7WVZUNDH24BC5C5RSIZOG5J45XL344LG54C3ZV7GZXEMBU77EGRZEELWZFPYNFKDFJFTG67KQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Турбинная ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902003",
                "ClientRegId": "010000000536",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "273.15",
        "FARegId": "FA-000000050888541",
        "F2RegId": "FB-000006363080701",
        "AlcCode": "0100489413240000009",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ГРАФ ЛЕДОФФ\\\"",
        "ShortName": null,
        "marks": [
            "187315651341841122001G7FCOU4YW35RUJOLUHYYHVJXTUN2PKRYL6LZEQCS4NT6MVUHFVNMVYRW7BDJN5XSCHSFFYL6JHKG27IKPKF3AKMZCKHMCYIYPP7MTEVFD7PMR6YNHFDP3OQLGAOMKXO6Q",
            "187315651341881122001RWO34T5DW6SLU6CI4SHVPMIGNQUTBX3JAGEN5LKIZNFMWXPXXQKJI4CS5VKRK6KUNIIGZMUAJIUZACR2JJ4ZXFMNHT2MPOXA5ZVUEZYKSIR55JR77WLHSGIRJHTALRW5Q",
            "187315651341911122001OLH3R7EFJINQELFFT2ZB3OQ5PAJPJWAILRSZDTUVPOU52XQCXDTXZJUGWRYIEUFCRT72632BKNAIFQGV6IYICNKV7RNWHFORFTHYOAI7IBE3SJYGY422P4BSAKRC6QKBY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "273.15",
        "FARegId": "FA-000000051209186",
        "F2RegId": "FB-000006363080703",
        "AlcCode": "0100000005360000011",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"ГРАФ ЛЕДОФФ ЛИМОН\\\"",
        "ShortName": null,
        "marks": [
            "187417714089311222001TS46CK5K7C4WJSSSI72UPOWILU75AQOPKQUN652PNL6ZWF6NTAX42OIQAZDXEDVJ453Y6HVXHS6NE5MOYKF5XPJVPLITULOLWTVXRJNF7V4WZFS56UC3DJPRDO37KNMJQ",
            "187417714089361222001J7CRPC3IMJPN3JZK6FQ34YEP5MQVABZ4NJS432V6U4H426YHTY7HXHC5IFOTOLOVAXYY35ACDINP6Y2J5WAL4ZBGGGBH7TCPHIUO3UUSTB3RK3RH2FPNZBXGBU4PFTYSI",
            "187417714089751222001DJ7BJYBDQBECFESEFUGDOFDXBEVOLY4X3UHX4IY6UZRL4NF3WKVV25YBCKJQGFOS2E6HGKCXE3W7HTCVCHDNERZASSGZP6SEGLK6Y5TLPBVCXQVL2MK4WBPCYG6GOFFLA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Турбинная ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902003",
                "ClientRegId": "010000000536",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "298.00",
        "FARegId": "FA-000000051418953",
        "F2RegId": "FB-000006363080704",
        "AlcCode": "0100000020360000065",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ №2\\\"",
        "ShortName": null,
        "marks": [
            "187316847160871222001XOFZ64AF6KM7P7XO4GKI4SGZQ4QBTRHE4VL2TQSK4Z2PQMATRBOGHFXAEZUWYAKGCT5HPP3L4BLSJY6LSGVTX7IL6C3DGRCSH2LCTOPB45OK7QQNPCRPOPHL37CPIVXJI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,Вологда Город,,3 Интернационала Улица,39 Дом  , | - нежилое здание с мезонином: 1 этаж: литера А3 - пом. 5, 6, 9а, 10, 11, 15-20; литера А6 - пом. 3, 3а, 3б, 6а, 9б; литера А7 - пом. 35; литера А8 - пом. 36, 36г; литера А9 - пом. 37, 38; литера А11 - пом. 33, 33а; литера А12 - пом. 30; 2 этаж: литера А3 - пом. 37, 38, 42, 43, 47; литера А5 - пом. 52; литера А6 - пом. 3, 3а; 3 этаж: литера А3 - пом. 8-10, 12, 13; литера А6 - пом. 2; литера А7 - пом. 3; мезонин: литера А13 - пом. 1, 2, 3; - административное здание с проходной и складами: 1 этаж: литера В2 - пом. 2; литера В3 - пом. 3; литера В4 - пом. 5, 7; 2 этаж: литера В5 - пом. 16-18; - здание основного производства: 1 этаж: литера А - пом. 6; литера А1 - пом. 1, 3, 3а, 5, 11; 2 этаж: литера А - пом. 5; литера А1 - пом. 1-4; мансарда: литера А2 - пом. 2, 3; - здание посудного цеха: 1 этаж: литера Ж9 - пом. 1, 1б, 1в; литера Ж6 – пом. 1; - здание кондитерского цеха, 1 этаж: литера Б, пом. 21, 24, 25;",
                    "RegionCode": "35"
                },
                "INN": "4720027123",
                "KPP": "352501001",
                "ClientRegId": "010000002036",
                "FullName": "Общество с ограниченной ответственностью \\\"Русский Север\\\"",
                "ShortName": "ООО \\\"Русский Север\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "288.00",
        "FARegId": "FA-000000051420213",
        "F2RegId": "FB-000006363080705",
        "AlcCode": "0100000020360000002",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ № 3\\\"",
        "ShortName": null,
        "marks": [
            "187417563133941222001C3TZGKOEKJPHHNLTK4FDHSHJ5UF5IJC2KKETDHHOGMARPPRNNBTEA2JAZ7CAPCQ7HHTBK5TJR772ZBU7P3CVDJH3MQWWP573ITLJECMVUJBTGRYPEATZKJMSGP4LMD66A",
            "187417563133981222001EXJOEXHNJUS7TET46DKM7YTW4IL7ZXRHPDQN4SWXZIXI6SOJMJBAB5UA72KBGDW7O4VI4Y56USGDEIGQKUXG4KBPIFQREJPH3C4E5OGWIMJK6IDTHEOS5K5AVNFUVIJXY",
            "187417563134011222001E7EHRD7BQ2CCAC54O5PUHALF7INYANZVDV3KDL6LC3YALNVZ3XRNNR7PWK2DWY6FFZQGDZBOP5AURBROCBC7U2GNEQ4KYSAXZVGG5X5DR5YACJGUCL4QDQP72H7YJRLWA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,Вологда Город,,3 Интернационала Улица,39 Дом  , | - нежилое здание с мезонином: 1 этаж: литера А3 - пом. 5, 6, 9а, 10, 11, 15-20; литера А6 - пом. 3, 3а, 3б, 6а, 9б; литера А7 - пом. 35; литера А8 - пом. 36, 36г; литера А9 - пом. 37, 38; литера А11 - пом. 33, 33а; литера А12 - пом. 30; 2 этаж: литера А3 - пом. 37, 38, 42, 43, 47; литера А5 - пом. 52; литера А6 - пом. 3, 3а; 3 этаж: литера А3 - пом. 8-10, 12, 13; литера А6 - пом. 2; литера А7 - пом. 3; мезонин: литера А13 - пом. 1, 2, 3; - административное здание с проходной и складами: 1 этаж: литера В2 - пом. 2; литера В3 - пом. 3; литера В4 - пом. 5, 7; 2 этаж: литера В5 - пом. 16-18; - здание основного производства: 1 этаж: литера А - пом. 6; литера А1 - пом. 1, 3, 3а, 5, 11; 2 этаж: литера А - пом. 5; литера А1 - пом. 1-4; мансарда: литера А2 - пом. 2, 3; - здание посудного цеха: 1 этаж: литера Ж9 - пом. 1, 1б, 1в; литера Ж6 – пом. 1; - здание кондитерского цеха, 1 этаж: литера Б, пом. 21, 24, 25;",
                    "RegionCode": "35"
                },
                "INN": "4720027123",
                "KPP": "352501001",
                "ClientRegId": "010000002036",
                "FullName": "Общество с ограниченной ответственностью \\\"Русский Север\\\"",
                "ShortName": "ООО \\\"Русский Север\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000052219167",
        "F2RegId": "FB-000006363080706",
        "AlcCode": "0100606942420000004",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПУЗЫРЁК»",
        "ShortName": null,
        "marks": [
            "187422058081380823001BNIFXXC6DLTO26WTUW52TAD4WQIITFIBREFGJF4VRR4OSDNPYTRBHR35AH2V3PC6RMT23RNWJML62VBBLYR67FBUDW3EITYJ2ODEWSGPZZEYQQZJZWF2GHPCVXOLLD3UA",
            "1874220580814208230017AATAHOBDHVSRPBAQ7MCK42XREWQAIKFMHGM3NJAQMM4EUZH74VMIF6JE4BF4BHHNHMLACI424KEEZP4TZJI7NJKGLDUWDS5MVRE7SKQ3DLNGFKLUGJ225BUWZZILAKNY",
            "187422058081490823001WKEXG3ECB4KFMCVR3EMUMMJO5IZ2W56UZYAQVZQTYEDCWYTZ27M236WMSWB6V2T6WQ3R6NWMQJDCF5XSQVBFIQJJ2SXD6CJMVC7577YBUKND3FSZG447XF6NL2CUN2GHA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000052205388",
        "F2RegId": "FB-000006363080707",
        "AlcCode": "0100606942420000116",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "187421880450430823001GYUMQ2LRGQNSIR6AHDC62Z5W3UTI6RW25OUOTYDEXWSPI254SVBVV6P63AS6DLI2RWDNHAHXQNUXWPA4SVJPPRHSDG5UXUHTZ3E3DEIA2DCZB6DITBKBW7J4QAMJ7YK7I",
            "187421880450440823001BV6X5TDDSWBUNGZOGGLORLKIUMVNYZN3E6ZM3Q7HEP6D4K6BUVKPMK22SCDS24MMK6MGY7MBDC3RDZP7T4G6JXDDBSZWYTN52U44V4WD7MNJGRSCYLLEN3TZE6ODSK7DI",
            "187421880450450823001EYA5R3KD6TO2GGT57VTL47OQIAH7635MVIXPODVGTDUJJYGCGN6WOGCT7EG7H335A75TXGP6KGKIISEOFGFOJAR3B3OT2WUTVLLEPWZNPSMYTHN4HU3XDSHRV5UQJFW5Y",
            "187421880450490823001NFYKYIH5UUUNCOFFQGS2S74LAIWCKQV643XQPMHIUVHVNWWBX73QJI5TW3DTFTRJNGTDVSMAXQ27WNK7TES7WIJJJ63GB5PCDZDQD4D6LQLD4ZSWQZ2V4DYMQLHB3FJIQ",
            "187421880450580823001M4ZKBADIDOJMFX4Y7ZVTCZ7OFUFGM56PQ63EUYFDWDUNSZYD4FLPVJ7N3CM5PWGMBDL2F2GH33IE5UT6EYUMAD4NNK5VGII5T7YJ3UC5DZIYGJXIDF2PBOKY7OAEZ7DOQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "87.00",
        "FARegId": "FA-000000048100766",
        "F2RegId": "FB-000006363080708",
        "AlcCode": "0100376601030000006",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "232",
        "FullName": "Бренди \\\"Российский\\\"",
        "ShortName": null,
        "marks": [
            "197300865235591120001EU5DCGRDA6T2XGMYKRV6O6AMKAGS3YIA72HQQRNQOFVFR2AFUOMUQRCOUHD7GPLA3ZXH6IK2WDGLQVFX465T7MOTDIFE6IHA276CEI4MLK4IY4G5HYU4G4F2FMBDIU3XY",
            "197300865235821120001MPO5P5LCENFAKS7QH5R7R5FG2ESZIP74EJ4CH45XZWXBPCMQGML3TZNDV4IXSVHAPYFLCSECPWTUBXV7DISG3N6XK7BUUACWA35OFAOM7S67VVBVI6NPKZXPPMFMV5A4I",
            "197300865235851120001J2SHZOTEXWBEHFB3GAJWQ5G6DAA6SBISEHBBL62AY67ZE43TRUSS6ICKCCDIBT4J2ANGWHX7BJ6XOJL2UOQX22BVFI5RSN6PWKZY7VNJGR4LJR53Z7HNMA2NHKPCF7IEY",
            "1973008652358611200013WOVIYKDCEEOOFH6RA4RZ4V76Y6V5SKOXITWOZLKXCOFDSUHGAOUOSIXSV2UYEGIFPUENGUGF55HOQRXJ5MTU6YR2ZYNR2U5Z7PWFGJXIU4NIIQTHGFYCNL6ODW5TQ3FY",
            "197300865235881120001YAZPGJRXVJBXH6EWFM6ANFMG7IPZE6OLW4IAINWLEIKBMEY3QAAYMCSBMQXO3HNR2JTSORZH4QJWHPVGPYNYAH4WYHI7HVLZ6J6KDORSZGIDAXOEE5RUAKRISVZEOPBVA",
            "1973008652358911200013KBCFHZNG5OGKNXUKQABDPSRLEPCCYXFFYFFAMIEHXPXBIBOK6OIGMUINJ72KV6IFQLINXVYGWZLJN4RPBDJQWVZTZMG7NUM5CFJ7DRALJT7WYY4V6H4UYOZB6Z6YN5QQ",
            "197300865235901120001LNXTWBSZTB3KDOAVF4CDN2RTVI4PYWV6I2MGVJVZC6ESZTSCGZON3TCOPOTVBXXKPXM7H4T6SS4S2TZ3NT3IBL7OMWMQL6E4FJ3SA3Q7TULQJ3MOAZSWHGKKZFDUHAFOI",
            "197300865235931120001ZSCIF5LU57UCCBKZADUGSHNKFIC7LBY57P6T7G5OM2EQEWCFOGOOYLQGKTKZQS7GIMBLWOM5LNHMFMB5SUUGKF3T7FZ23C2MMKSJ7TMJOTAZDIW7EQ6HITOMCSDZ27O4I",
            "197300865241381120001DXJA2H2U5YZ4XQGPEPAMAO35XESJO67NCO2GKGIAVZ4CL427IEAOWXQSW7IGJO47P4KYLWMEPPISFPBFNE4W2W32QHHFBJX7UH57SJADCWRHME5EKCX3SI7HFKZG7DH5I",
            "197300865242531120001Z4SY3UXBU5CVSZ46JAIM3D4XSAYGGASHBCTNIBPAHX6WJO2WCNQDN34X6QXSPZQGG6UEAFNZ7OHZJVOZHXN2UVGP2KQIF27XE5UKEIRY7QCOSS5A34FGT5JHSMIUVTWBI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРЫМ РЕСПУБЛИКА,Симферопольский р-н,с. Первомайское,ул. Дьяченко,д. 5,,, | (за исключением: Литер В, кадастровый номер 90:12:120401:79) | за исключением здания с кадастровым № 90:12:120401:79 (Литер В)",
                    "RegionCode": "91"
                },
                "INN": "9109005701",
                "KPP": "910901001",
                "ClientRegId": "010037660103",
                "FullName": "Общество с ограниченной ответственностью \\\"Завод Первомайский\\\"",
                "ShortName": "ООО \\\"Завод Первомайский\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "116.00",
        "FARegId": "FA-000000051772367",
        "F2RegId": "FB-000006363080709",
        "AlcCode": "0100606880350000128",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\\"Армянский коньяк Виват Армения пятилетний\\\"",
        "ShortName": null,
        "marks": [
            "197404998358871122001RJYPYRVXXVUIYT6O5BR2B3ULYQYJQG5QC3NUWSWKNKCA4C75MFDHHN2GKUR4XT2I2IH7QSNCF4UZ3QUUQXXLSQ25SHPOKO4M6DDGBTR2E6YOPGEDRQU54BX4KMGSCTREQ",
            "197404998358881122001GID5KUWZFGYYG3E53XWWJMGKZQPKJP37F3WKFPJZNGVPWPH2D5MH7IPELL7FXZ4MJXMJKRUD6VB6CDAPQNHZ64O5XBXAOV7JDKGGOFRCWHD4E74HPMMWJCXMCIWNXQLUA",
            "197404998358891122001QUWTY6HQZ3QR2HPAVDQB2RXPJEFEHNVUNLHGKD4QPWNMD7MDK3KZEUWAWQKZ3DH6UIEWAVQ7PGMJ7XETQEKCZXQDREWRO2NM3GXJ543MDDSZU5JRHDIVOSKDXVN7RD4OQ",
            "197404998358991122001NA665QXSQTXGBDX36OKDFVVVGAQVPC5BFNUWNARCMEDTXNHLO5BWWVSK3EIXIEWFEY6U3QDYZR7JWX53GWN56TIBXL4FSH3C5CJAC6RKJACPP53RMHYT5NSL3OADRGPQQ",
            "197404998359061122001Y6LUUUEYVPW367ZHAX2R74HSYUXCF2DVFYMG7Y5HHUUGEPTAIIWKAQNPHMAUASCYPZT57ODULH5R337E4FUICDE6XJT3ILQ4UCCI3IMIAZLBTAHE2KILULFHZNOGLO5LA",
            "197404998359201122001BOFG7SV7SKIPI4I4T6AENNQQNQBHCCWHGIPGADTYF3KSPNO7MT7Z7LTZPPBWD7RJC3U3OWKVMDYU5XVLCR2NBIW5CDHDJFWVAPHFKOC3ZHLJAD6AAQTMGLBDSKAIU4K2Y",
            "197404998359211122001Y5O7W34HWEDEG2WPWCDJUIUUSARFO4LWLMV7CUK2O4GFT5OBEPUOC6W32XFHWHTM3J3J6NI4R6NOZC4F4TAG2YB75M7RYTDZGOS6SCZK25G4DKYFUUX4HBKEQW7LQT2XY",
            "197404998359381122001EHCA7USYTMKHYFJMR4AV2BHEPEBPVJBYX4MXCFF7GQO4L4LUBV57ZUJCTBI5LJ6IKQR6UEBKY4GDCZ3NDJSSITO5RWXDNUGYXGUHL7ZPHJCF55TVHNKLL4ADGX25ISAJI",
            "19740499835939112200175WHUYV6ZQRQ34TFRQRFQEFOYAMLD7NZMSAMYKTSKORG3O6ATWFM2XUGYK7VMOTIZ44MDTJS6GEBSUCVAA36IYZIARBJYYDISRP6GWAFM3PSJSDE5LXSY3CNCAHTMIMHA",
            "1974049983605111220013YPAPJWBTMR2I3ZQJXY7OYELHA7RDNFCN5P6KG5UJQ5BT4OWPDURZHJASEYHMT2IDFWZ7OHDV4NI5S2GXFPUAORQWSCVCQSTN45KSGKQ26ZUZLVLHOX6AQIYVQIQMBYLY"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\\"Гетапский вино коньячный завод\\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 10
    },
    {
        "price": "116.58",
        "FARegId": "FA-000000050942177",
        "F2RegId": "FB-000006363080710",
        "AlcCode": "0100000003130000065",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\\"ЗОЛОТОЙ РЕЗЕРВ\\\"",
        "ShortName": null,
        "marks": [
            "197404176966090822001XTUPZ2MVXD7ZBEMH4WRWUD7RKQWSJTXQTBYLSENMKHALI7D4UKJ7WMLDVR45HMEFNXC4MMTDT5YPPTRM3AMB4VVYUYFTZM3O25SCORP3RLE5E3U43PCNJAORXSPNROBCI",
            "197404176966110822001SRADSJWLVFMSDAOAKVVRY72H3YDSTYSPAEKX2NBOH3XFIC67ZV5WZH2JPT2ALJOJGHO2QRU4BWFMEJ3ZGNF476XLF6CESTOWQRZ2XXXBSQ4LLATVKTSPKCSHS3FMHOG5Y",
            "1974041769662208220016VU3TJD7HMO2W3UEOBVACKCG4URKK6N5QNO2XYF4GMGAYVY7P3Y3NXCW45FD7WW73FFSQ4N3MTBXFWFDDDBDU6QRFLYVGG6NL6WBIBXMO74QL6LZTBSWVDSCPZRBE66XY",
            "197404176966230822001X6EBGBTWZU7NAYGSSK3NK4JTDQIRUMA6NW6FQPRGGPFIXMPZQC6JFVUFUE5L4OCON2CGFYYA44WY6RQR3DMMVXBFZOGNKBDC3DI55AO3T7XHYXZ2M6HSWAMWXTW2VM3HA",
            "197404176966240822001BQI2MHAK65ZOKC4ZXVUXZLZSA4AEZ2I7A3WA7ZZIXF6UM24UCUBHIALJMX542JMQLFNL7FJJSXA27SXPDJTLIIJNO7ANZPYDG37VNPPHFEEHAF5FK5CJAMRF7FVUN45NQ",
            "197404176966260822001MALKIZK2KTEQ4GTVQRV6PZ2CPA3PE7PMYSHAY53SL4OS3PLG6J7W6YHZQVYSINNHOVAHU5C3EMOG654E5DSDOXEYHIH2SFXDAUGCQID6BY5YYIQUBNW2HLTRZFMX5NZBI",
            "197404176966270822001FH7ZLWGEMYH7I6ZQ7R2CQFGI7MEGFB6MPUODDFVCD5SPYINYEGVL4ZVHYTQYITSLGR6DM7I4OKLL5MOHLSERQGYRLZFLLATBGMKIWYWXXXOMAH5UDUJ5OYL7PI752ZQGI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Пермский Край,,,,,,,г.о. Пермский, г. Пермь, ул. Героев Хасана, д. 104 | Литер Б; Литер Б2, этаж 2, помещения №№ 15 – 17, 31, 33; Литер Б3; Литер Г3; Литер Г5; Литер Д, этаж 1, помещения №№ 5 – 7; Литер Е; Литер И; к. Б",
                    "RegionCode": "59"
                },
                "INN": "5904101820",
                "KPP": "590401001",
                "ClientRegId": "010000000313",
                "FullName": "Акционерное общество \\\"Бастион осн. 1942 г.\\\"",
                "ShortName": "АО \\\"Бастион\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "89.00",
        "FARegId": "FA-000000051967894",
        "F2RegId": "FB-000006363080711",
        "AlcCode": "0100000005390000038",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\\"ПЯТЬ ЗВЕЗДОЧЕК\\\"",
        "ShortName": null,
        "marks": [
            "197404526678701022001ZS7EXH42CGHSXNANCZ2UWUE7KYW774QETIW55OKZQIVA2PEQ5Y5PD6QJBZI566LKAZLCORW46LDMDOKQGOY2SAI6DOYRCXO537CP6ETU6BMDDDRAHHRAK6NZBJYZLD3BA",
            "197404526678761022001RVBDEBOIRJEZLSBU3WQT5IYTYAMISKEMOFOOJ6BSMW432CPP6UECCY5YUZZQ4AK5P7526F75NJZA2OD642ABMMVJ5UM5J43225GXBLTL35OBGUFXPEGCVWIUALF4IX2MY",
            "197404526678901022001LYAFZ4YRYMLM76CMODZC4QFO2U7UL7WLTNYFP6YJSQBHYYXK7PHB5GVSIMC2Z5YNBRI25G55NYTROTPPPNDLS2UNMJB7NYHHOLXKSXYDJUFWGOLDPU3RPPVF6N2KOH6RA",
            "197404526679371022001FGD3VAZLWJUQJJ2PKFHFZBAWXMF7YN5CE5RJGOEIVO4C3YJKS6253YUKGSHGNDDT4TKZLMBUGHH7U77CREA5A2IKSCGDO65JWDNTD5JR7AZXGAIP4ASE36BLJCZ5XNR7I",
            "197404526679391022001NHCQHF3UJOPS2UF4ALNQQ36GV4U4V5WBAELNDFJTBY2E2CPOXKVEZ6QRAFSI3SBPYYGM6PHTBR6A6IJJAFTLJQ7GH7FC2OH3YR32PUXZLBWUMFYFNO73YLL6NWQT7R4QY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Учительская ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902005",
                "ClientRegId": "010000000539",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО филиал АО \\\"Татспиртпром\\\" \\\"Vigrosso\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "87.00",
        "FARegId": "FA-000000051746592",
        "F2RegId": "FB-000006363080712",
        "AlcCode": "0100000005390000041",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк трехлетний \\\"ТРИ ЗВЕЗДОЧКИ\\\"",
        "ShortName": null,
        "marks": [
            "1974049374693711220017FQUL3VSH334BDABKWEHJTYAGEWJE77AGJUQVKOPUEFEO3OETUBNB5IDE5ZYBNOVRB52ETEZVG7NTBFC5KCBYYSMNXOMUWBEJ2PWYUJVC3PLWZK6JSCXTRLKOKIYUEOSQ",
            "197404937476381122001CG2E4LI7Y2YTG5IXV2D4DEVFF4VMOW3TFPYYYOMU7NNJ7SEAYGDJFOVKASY4JXNMKA5BUN6CQOPGQZC35YXMIUVPCHAI7K2FD4STNACL7YPH5QNPUQP2WGWC5AMDCENXQ",
            "197404937476441122001DODV6XIJVXIGMN2ZHLC3BMSBY4AJ7C7GKKD252FZDKTB6MO3HFLAUZVOUZ4ML4YPZUQGMMXVNG7MQBBU4CBLKJJ64DKC37DPNCTGU6O2KCNCUPRIOA2ZR7SBGWGNGCUSQ",
            "197404937476681122001AXBVNGW3WTHSJTEHGVFNKMBNKESILB5XPMFHNM5DI2CEE3ENJZRLABCGLU76EZWZUAJULUJILLGBC567HMZAOLGUV76SRCZC32AAVYENSZT5FMCYWLBDD7JBQDJXJ2SZQ",
            "197404937476711122001S5CZ5JTYKLFQ6DS7EH3ZTJDSTABV6TFD36FIJZSFNLS6N7GGURUA5UCJFVIZZOA2FLHR4QHYTYRJJOFCDAQPMDHL2GY3UD4GKJXSVL6XKKZKG7ZXP2QXIBVIOFVS7JE6I",
            "197404937476751122001SRQ6K5SMWN25YI3IP46MJH6U3Q6KFBYXRBVW62OJV5DBQHLFRPYJQEWZYELLUNURXHK7JKPL4OZ63P4XQ5V4H5GK6DHNBGPPMESK23UFFTRHBO2HKZB44DKOMSJC4T55A",
            "197404937476781122001BYKCZZCSG32RNSFB74MTGA7444V5MVJMPGXMYYJGNKSMHRE3QWIPKTVEO7PW535HVMS6V5P4G5PUWWMM6QCINFTFSSZ524D7TVMKZFQM23YN5JAUHVR45Y7TYOZJ7ACUA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,,Казань г,,Учительская ул,5,,",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "165902005",
                "ClientRegId": "010000000539",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО филиал АО \\\"Татспиртпром\\\" \\\"Vigrosso\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "101.50",
        "FARegId": "FA-000000050957561",
        "F2RegId": "FB-000006363080713",
        "AlcCode": "0100000005560000254",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2124",
        "FullName": "Коктейль \\\"ШОКОЛАТЬЕ ДИЖЕСТИВ с ароматом шоколада\\\"",
        "ShortName": null,
        "marks": [
            "197404469053651022001IS7O5XP2OSGSCOAWSSFUYHEQFAG2NOJAU7EGGGK7YKEK6J7GWBBLWBRQNZ6TQV34S3PVUBEXIPAWPG2DCXINK5SWY2EXFFPHPVVKTVBJQADJU2FLOJ7MDVCQ7ZDPBXNKQ",
            "197404469053681022001FGBIVIGBX6BF4JZ7WJHF64WBJEXUTQR3BOU6N56D2V47N245EWABLUTP55OQAAKKZO7AUTSFK4Y6RBSANT4A6GQQSVLT7OEVBEB5LVHSEZUTSO2DDSISSITLQONJ6QK3Y",
            "197404469053721022001E7W3PJX4UZ5HE2YCMEZHWEPNMQGGMPCZE5IDDUKNJO2D6T4NUKD7NJHNCCU5W2XTILTFNBGURG6DUYVL4I3ST4D4SWR5YRYKR2GPRKWLXJEIGPQL2YWHJABZNCTR67BGA",
            "197404469053731022001VM4POAEB5PSJOON3R6CXKDWYSI4KCEGL543PLXIEMRO7L26QOORF4522PEE32GKZJ5QFYLHZCYULKLWRISUX4Q2ABRLBW53A6Q6BXNCTFHK4JDH2NGHL7YFJVVRGQPDCI",
            "197404469053831022001O5TJCLDASV3Q2PYY4TF4MTYVPID6E6MM6IW53TFWIJ4F72KRPU474PVEFGYBQ7HZPRE36ZZMDL65IQWNU7PXXVRYGG4MP5UVULY5HDMOUDHUQ3B3HUTQFMAWDHEZHQ6BI",
            "197404469053861022001HCPBBWEMUPOPVXUV6C4YGDKVRYINNLT2IJBCWDE6ZZIGGS2PYSFF5BRQEVAOIST2GUAO3QDLX7O4GER3CQKQ5CYPQ7C6IXPZZPYWR3P4YMXSN4LC6L2HBUHAQJILTYRVI",
            "197404469053871022001HJORXZGWK7ZGARC6PKUCBSKUKYQUC427JMLPO5UE5Z24YLZ7YS7N5MBWHY6DKNREBWF7YDCXSGGV52M5XKBVMJOQRSGSWPIEBEJ756OILLDC5CNZHY2TI4J4FZ3UKAKAQ",
            "197404469053881022001K7A7WVCRMSVPIWV4LHAPDPSEIUXJJ2YZQNQJQ2VFCNQE3667A5UXFYRN2U4WNZFMHNGQHAM32GAOWWF2SLJQOKVMJ6CGN3RS4D6PP3C45ZDVEJCJQD6R76VMW6GAM6VJQ",
            "197404469054141022001V5AXSMIFV5Q5OEB4VPKADVVLGM5IUZUGSCBXLDOEA4U2X6HIN45A3HTBSC5ZYOD46UIOOL3BOQ32LTCSMGNS4GMWC4B6WP2N72VJRPZKUQRAS22KQYFUQMCNYMIVA3W4A",
            "197404469054151022001TDH4W77RN7RDEDT2PR5RXJY6VYTHJ5RHPQH5V2VWNP4MUZUJ2INUL3Q23K3NKMRFOTAWKRVNPS45OXS3GG7FMJNBBJBPVZIIDZFV7S2ISTX5HG7W3CQUZHVMOPFLJCEJQ",
            "197404469054181022001WTTZC7FQEG6565CGTAVH2TSLEUYN77IYFEQ7JOFGHVHLMPNGPDEOLLKMKS7O3QBFGSN2N2E4YAFWDHUKR56QLLM3RU45PEZO4F3EVLSXBUXX3RNS5JM57NV45N546Z7XI",
            "197404469054191022001OWDTRXZR7CZWVND6KWHJ4WY3XADVICQZQW32DW5NMQ3W4H6UFKTOMUXMZG7H5OUUO6LD33R2T2KHHGBZ5TMSICYXRQO6TWTLAYU6ITEY6LAPLHVEATS6Y2SJXPGJ7Z25Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Мытищи Город,,Силикатная Улица,,вл. 17",
                    "RegionCode": "50"
                },
                "INN": "5029047184",
                "KPP": "502901001",
                "ClientRegId": "010000000556",
                "FullName": "Общество с ограниченной ответственностью \\\"Родник и К\\\"",
                "ShortName": "ООО \\\"Родник и К\\\""
            }
        },
        "quantity": 12
    },
    {
        "price": "241.28",
        "FARegId": "FA-000000052010706",
        "F2RegId": "FB-000006420908865",
        "AlcCode": "0100000003130000135",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний «Золотой резерв»",
        "ShortName": null,
        "marks": [
            "198410641520460123001BO5ODKC4WFNBPEFP3EWBYWEHNEEQS2IYP2SJJSNGTHLRVJBOL6F2H63PD3UHBGXGLPECA3LJF2MT3TY6DHY5EQ27NP4XZ65JJECDBX45OGUCYWH575UA7JYQK5N45OS6A",
            "1984106415204801230012Q5XULM7RQ7PCQO7APVWVCFPNIBMMJIALB7TVHNYMRM4WYHYI3XXURUGBSZOBENSNWV67EDCJFKTGJL2NC2TMHSRZLCBYXRTLNYNLPKQDCO2JXSAMKVFT77PUI573DAEQ",
            "198410641520490123001P5A2MFEPAFR4LYRNK3OELWPPNQC7PZ2BW77F6XOE7X5PZDHROPN5GCFP2ADRNVOAYL5BMDRQ7SBLA32OH76LKXZJ4SOENM3F3XTD7HC4Z5XJY7SCOV5OV47MLCVTVU5YQ",
            "198410641520500123001OIS6VNHUJ3QE2FQHB33ZMJXX34PG3FHIMW2NH7GRNTFESE7B7QDRFEBCCHZXV7GWM76FX7RTB6DBNXNDZLXSDIAPOQJQK2DRZYM5BZ3SMIF4B4PTIHSFXOBMLIPNNUMBA",
            "198410641520520123001TIMDOZQXIAVJF4UCHUM5AA77OIRO7YI473IPWDLL7LRCD34P5CZ5YPJTUN6BGD6HKVDF6KH4RNDX5XSXCZMETVQJPNAQI7LES2B3PC7FSU7MNYIRFVVZVNJDNT3VUXEDI",
            "198410641520530123001CEM2RBLENZIHIEUWOGKGICWNHYJNPM4KMW6HEWPYBC4YHTBAK5RH3D2TNN2T44YQC3UBQWFKHVXPXMYPYNLRUAMQDVNZCBORTP6NX63K2U7RUAE6H37PATSAOEUNMT46I",
            "1984106415205401230016GNSOF56RUWMQK3B5BMY2P6PIQUI7Z7E6FT7RVORB3S623LAL33VJRCN3DFU6OUUDQC47XQZCV7IOQXIGSMLIIN75GOB3NLRWNOHVBZ2YHDS2H7DIKSU4XI75QIETOVUY",
            "198410641520550123001GS7CFWQ57M56UAH2Y6SJ6LQPU4UHCQEW74NA3RADGWZAXF2DSPMQO7YRXHFSGIWV6DS2TZMFD76RW55RWUHMHQA6ZBY5CCHPXSWJK26IC2RDMSZ2RFDDNZ7AKYEHV55LQ",
            "1984106415205601230013ZATVUL2TLLHTU46UJXO464R6MXSD5U5UQNWZVPBPOFK75HFMXEZEUBMKIK74POPMUS67NWRCTDV3YPO2AVGK5FZ447SU6KJA4AHSK3SQPSS722TNDB3GR7CTEOG6OX5Q",
            "198410641520570123001AHJXUSFMWLVS7TTDJGDKER7L5UEWCQ7K3J2EKBVECUIMWU74JXEJ32ZSYPZV3SNKCDTASZHXKFCPKPCISW4QY7N3QITIMGKSSHQMVWV25WTFZQBEJZVVTVS2IITLZPDWQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Пермский Край,,,,,,,г.о. Пермский, г. Пермь, ул. Героев Хасана, д. 104 | Литер Б; Литер Б2, этаж 2, помещения №№ 15 – 17, 31, 33; Литер Б3; Литер Г3; Литер Г5; Литер Д, этаж 1, помещения №№ 5 – 7; Литер Е; Литер И; к. Б",
                    "RegionCode": "59"
                },
                "INN": "5904101820",
                "KPP": "590401001",
                "ClientRegId": "010000000313",
                "FullName": "Акционерное общество \\\"Бастион осн. 1942 г.\\\"",
                "ShortName": "АО \\\"Бастион\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "470.96",
        "FARegId": "FA-000000051439469",
        "F2RegId": "FB-000006420908866",
        "AlcCode": "0100000003130000027",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\\"ЗОЛОТОЙ РЕЗЕРВ\\\"",
        "ShortName": null,
        "marks": [
            "187418392712851222001IZCFM5OM74KV5LCXJINO2EQBYQHKFKVJKQLJXXOBVKIO25V46M53B34ELWSZW2AO6JDBBMY2X4MVVTDESFTA76G6AUBEE4WJEXK5TV3C5XCUI3ZQF525APEC5WJJEQRAQ",
            "1874183927129812220017AOZ6KZZPECPWCR5PNPKRJESWQ7HINEZWMXN3TDIMJLHWCPKJROXASIBZUSGY5BO3UJ5M5DAENXLXTGKC3WIMQML5ENYD62BFAC5WNQ75BKV2OU4J2WJV77BQ667MD65I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Пермский Край,,,,,,,г.о. Пермский, г. Пермь, ул. Героев Хасана, д. 104 | Литер Б; Литер Б2, этаж 2, помещения №№ 15 – 17, 31, 33; Литер Б3; Литер Г3; Литер Г5; Литер Д, этаж 1, помещения №№ 5 – 7; Литер Е; Литер И; к. Б",
                    "RegionCode": "59"
                },
                "INN": "5904101820",
                "KPP": "590401001",
                "ClientRegId": "010000000313",
                "FullName": "Акционерное общество \\\"Бастион осн. 1942 г.\\\"",
                "ShortName": "АО \\\"Бастион\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "209.00",
        "FARegId": "FA-000000052083841",
        "F2RegId": "FB-000006496467993",
        "AlcCode": "0100000001740000741",
        "Capacity": "0.700",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\\"Татьянин день\\\"",
        "ShortName": null,
        "marks": [
            "192312333533030123001MLGETKLRO3VFGRYGCN6L2N6IHAMXA266O56WPBD3QDBHM3RMX3QRSS4YTL4ZACVWWKEAF6BY6NNHMYAKVOC5GPQJEYGUCXSLRQOU6PP37BMQW6TQBIEMPNJONR7TRBQPY",
            "192312333533360123001Q3S2GMBXLNZIPO3ARSYGD626AA7AALDETPC2JNLDWQSJNR2V62GIE77UVK762HYJWAGL3EQUWWQH5SB74GSVIPAEOSNDI7PMUZ6OY7UJWNZL7WJK5F7UMZZFSXY7FPOSI",
            "192312333533390123001R4KXYBGSAZ2FLJNNXLYOQWMSOQSD5RXKEFRY2T2IOZLS2D34PGMU7QNPPSO57HIP4EH3LEUMJODZWQXH34VLSEK7N3O3AQTSTAUHKP3SKN6FCQ464NZJ7RE7PM7MWDG6I",
            "192312333533480123001Z2P53MDTQURCODMQBIOZHVUR6YLYSKEPTIUZH3H2VWOYOPG3CBIPWN7W24VOC4E6B2SIOABGKFRDD6JANXXYEBURRXJDIQLUNG57MLWSV3W6TPW2JFZUCF3WP5QJM2RIQ",
            "192312333533520123001VDOBVPULTBVQKSVRQHQCIHRKOIZU4XGZIUYOV5JXM5THBR7OW33SUDG5WJ756UJNNQFC5VTZ5WTGIEBATJ2SYD6FWOCIDORSSCU2CA6JFTJZIIBR4UDO3Q5CH3QNWM3BY",
            "192312333533530123001THUCUNDOWQR2VS655HCRKBTPBUKJOCZUYHJCMNZ4JXZMQ2VG2WB6ZJJ75D3VA24STCCSOF3G64IOJXSEMJYLQXIME7DX36YPKTLILFJOXPRR6XX3CBHB3PVSYX7ZLZOWY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Темрюкский р-н,,Вышестеблиевская ст-ца,Береговая ул,45,,",
                    "RegionCode": "23"
                },
                "INN": "2352032696",
                "KPP": "235201001",
                "ClientRegId": "010000000174",
                "FullName": "Общество с ограниченной ответственность \\\"Долина\\\"",
                "ShortName": "ООО \\\"Долина\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "153.00",
        "FARegId": "FA-000000051427955",
        "F2RegId": "FB-000006496467994",
        "AlcCode": "0100606883410000125",
        "Capacity": "1.000",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\\"КУБАНСКОЕ Белое\\\"",
        "ShortName": null,
        "marks": [
            "192311106689451222001AYEMWG6UUHLCRZKBAISZHGQLTM7QWYVOCFGCXZS7AYBQRP4CJK3MFHSUQPPOAMFQPZTLRF3KYF4WK2JVQYKI6BRROD6SWMQBGYBEOPGUW4BSNYW7M7GRR6MTEAHSM3JNA",
            "192311106689461222001S7U2EEZLEZT55VTW6BFBZKNW245IX6D44SNZROOMGPVCSAOZU735OWJYR4M5TZGHZ5A7DJ5SVP5SCZDGS7C2USPJIBBKMH4U37SH42QZLWBM6LWEMO7R32VPZ6EXUXH5A",
            "192311106689471222001GW2TNQPOV3RMYNS7Z5GF3D6K3QRJPFFSGUPVASGFK2RHBYU4JGICMPP272BE2YJ4C6J7SZLM2S573K7JA7JCBATUIGMGISGY7W6MZ22YBN2SKKGX6RT5OM3LJ3LFHC7ZY",
            "1923111066894812220017Q4NLNPSD2K6CSTEOGB4GTKVLY46QEFSW53D2F6KKWPHUATRZ5SC3UXJRNQRDV5ILFWG4EF4TJZZWOAR2JO63BTMKCTG7RMSEQOAN6A75UGYPNFZIBVPCYXBQO2KP6VGY",
            "192311106689491222001XEKDZBYBQ2Q74PEWWNJLFCD63E4KBVAF6IQXNMI2FAY5KHOUUCCIUBPH5R2VSZBAU6M33QTLCKKEJNNSN36FLJGZLNSTTYVTMGF5FROXDMQTO3LTOS2MBGXTFD362FYCQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Усть-Лабинский Район,,Ладожская Станица,,Коншиных Улица,,д. 111 | за исключением: литер Ф, здание с кадастровым номером 23:35:1006004:302 (S=488,4 кв.м); литер Ц, здание с кадастровым номером 23:35:1006004:303 (S=488,4 кв.м); литер Ш, здание с кадастровым номером 23:35:1011002:282 (S=49,2 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2356046996",
                "KPP": "235601001",
                "ClientRegId": "010060688341",
                "FullName": "Общество с ограниченной ответственностью \\\"Кубанский Винно-Коньячный комбинат\\\"",
                "ShortName": "ООО \\\"Кубанский Винно-Коньячный комбинат\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "153.00",
        "FARegId": "FA-000000051433586",
        "F2RegId": "FB-000006496467995",
        "AlcCode": "0100606883410000021",
        "Capacity": "1.000",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое красное \\\"КУБАНСКОЕ Красное\\\"",
        "ShortName": null,
        "marks": [
            "192311108233391222001MHJMUFOET7SM72ME3CPYY35R5UERGMEZLHEDDUGVE2NLPMVSRHLINVFWQAHTQ46HUGHEYWKWHGKYS65RXYKLLU4O3U5EQMJAI6IDLNIUJXHEVTJEZLXQWHOEGVOPAO6LA",
            "192311108233401222001XPGDNH5FAIITIKP4XRUY6EXPLYAQ2JY4YWZYDEUQR64ATR7L2UZXC6YM2LLXMXHQSEWPUOP5B4ECUM4TV6GZKJRRAJ4CYKRKRKTO7VTPN34Q52SFGGTDAORUJHZQRAZVI",
            "192311108233411222001E2KLMR252SGQVFGDASTINDHRQYK4DU4Y2MXBXPOL3JP2SD25UFQJIKI7J4CX752KPUKQPY2HJGDF566KYYDIGE6DN2JD6USJEIIXVD5FD5VYLKKHEDB4574IL3Z6DDOQY",
            "192311108233421222001AK5QFZIX7LR7UZV7UN2QCWJZJIB4LEMDD67THGNYETDDCLSDVFOSDN2LGL25XJLAQS4OEYDTPQ7TP6PN56SCDU2HYS5FRIR2XFO3X7WOLMRKVERKOGXZU3EXLR3MCEIGA",
            "192311108233431222001WDKQ5BADOKU6ALQKR4DV4PZGT4BTRLWATWUQHR4KPHI6EEJCP25PKTTSXFD5NNRYZOYYO753KHZDR3G2LIMV5I4HEKDEOUD45UDHIGJLOHNQE3443GOOAFM2V5JTB6U3Q",
            "192311108233441222001EA627OFAIEC2CA3EFPSTNKQK5YKXBPHYXYUNREFRHOVZN2E2TLJW3EJWJG4RD2LQWRTRU4MKHJ2EADNH4L4AIO3N3XQKSJ4F4ZNEPZTWZFSXP7Y74JJ6FKRRKC2RVRWJQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Усть-Лабинский Район,,Ладожская Станица,,Коншиных Улица,,д. 111 | за исключением: литер Ф, здание с кадастровым номером 23:35:1006004:302 (S=488,4 кв.м); литер Ц, здание с кадастровым номером 23:35:1006004:303 (S=488,4 кв.м); литер Ш, здание с кадастровым номером 23:35:1011002:282 (S=49,2 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2356046996",
                "KPP": "235601001",
                "ClientRegId": "010060688341",
                "FullName": "Общество с ограниченной ответственностью \\\"Кубанский Винно-Коньячный комбинат\\\"",
                "ShortName": "ООО \\\"Кубанский Винно-Коньячный комбинат\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "153.00",
        "FARegId": "FA-000000051427954",
        "F2RegId": "FB-000006496467996",
        "AlcCode": "0100606883410000019",
        "Capacity": "1.000",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое белое \\\"КУБАНСКОЕ Белое\\\"",
        "ShortName": null,
        "marks": [
            "192311141158651222001KATUEHZIAJ4MTPD5MAPJZWEGXUYW4PLZB5HUWKVFONLV6GJJNFRCYJOC52522TAVT7L2HVVQXUZYYBVKANMJXNDQ77PKX5OS7WBJF3HIQBTFH6MRYITLGH2WS6ETAIH3I",
            "192311141158661222001F7UM5YTMOO4FNXT4TEN2SIDFC4WMYW7HK2PSEBMDTTTJ66U2XJDWQNW4VBAB4J6ZJK3MDRV7SFG3ZRVTVV7VYDBSPDPUSFSC3L3G7O23GDCL2NRPH7UPYG6GVBI2N3KYY",
            "192311141158671222001ZJDEKO5MV6RAIV3GXHZP2DR5GECQNA5EMRWWZLTZL3TK2DXMX753UQX42UY6SEYUV3DVFHGWVJTBNXY3ATQ5EO3X4IDSPCKVUL25HQE3KI2I7GTOPJXJS74HGI5RHH7UY",
            "192311141158681222001ON5AZULVTZSAXF4HJJSUQP5VQAE27NR3TUR2I4FJUNRZOFK6YNSVYJGEEL4YDFCG4Z3K5XZFRWHY5YOH7FWRLQ36F3L4ILCFADNV7XSO6SUOJBSC3NTORUSQ2VFGUY6QI",
            "192311141158691222001QYBY3BNL25YJM456BSZN5CEAGEOQSPO6WKNT6B7GSYW2JXEQ2Z7JTAUTX36SSPFGTM5NNZXNDOAMV7F3UMFBOOF7SJQHH6B6UNS6RE76IQAT2WDPCRHEJNP6LWA56ACHY",
            "192311141158701222001FQ2SPYNOQ5AF3USQFHNP3UKLCICU62MM33GDLEUM3ANKUEEDU3QLJ7WW34UURLADDLGMY6C36NKKYZ64WI4HOBMPOZPH5ZCN44SQ5TGKP4KP2PUCG7Y7MXIRSSCQVEMIQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Усть-Лабинский Район,,Ладожская Станица,,Коншиных Улица,,д. 111 | за исключением: литер Ф, здание с кадастровым номером 23:35:1006004:302 (S=488,4 кв.м); литер Ц, здание с кадастровым номером 23:35:1006004:303 (S=488,4 кв.м); литер Ш, здание с кадастровым номером 23:35:1011002:282 (S=49,2 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2356046996",
                "KPP": "235601001",
                "ClientRegId": "010060688341",
                "FullName": "Общество с ограниченной ответственностью \\\"Кубанский Винно-Коньячный комбинат\\\"",
                "ShortName": "ООО \\\"Кубанский Винно-Коньячный комбинат\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "153.00",
        "FARegId": "FA-000000050001462",
        "F2RegId": "FB-000006496467997",
        "AlcCode": "0100606883410000020",
        "Capacity": "1.000",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое красное \\\"КУБАНСКОЕ Красное\\\"",
        "ShortName": null,
        "marks": [
            "192308218576070622001DYBBIX4UA2DJUQF3POCZDOOMNAIHHHKAEUR4B4XI4XAFZTFBRXQ2VLSOC3SSSGVCH5SSXR65A54IEM24A7L2QGNZCESVBCP7JSJQK32CGKLVRXP2N5KBJEBIPIUIMO6IY",
            "192308218576090622001ASSOELCGGRMLIE5JGZRCFSLUSEUHENSBULWLOFFS32Z2OTN2QQ4LEW7GCCL6R52S4MGRFRVM3FFSKAJLMZQBZIYMZ4SCZ3VRK3532GEYJFPDYE5OEALJRH4ACVUCGKERQ",
            "192308218576110622001SCJDYXI42CR32X7QYBQP5QUSPEPFS3A77TY56EZ3BKXDLHPE2J3EYFCQ4MUJQNR7DZEUXP4D6UBR5XJHWEXQY4UKV5MT6VTLHBL763HOQ46ZM7J4VXKEQEGCOOABBT4JQ",
            "192308218576130622001EDXZMQYH7DHAN52YYQ5IHVGFX4FTGR6L3Q32Z2WYOIPT6MI6UKCKQFKEJNAIET7QGH7WEHL65473HTNXE6Z25UJN7X7OYBIW3O3VQQ3ERT4OBDUBTC6AUA2IVT44GUYVY",
            "1923082185761506220017PQYTMPS5QBYMR3TPEHM3QXXOEI36ZDLO5PW35PSBJV47NQKB5SWDBXSNJJG4V36U6FAKKWCDC3PDEG4UI3ITTNVVKX6AXXK5H3JVGEADCETGI4N35UU76IJILNZEKDRY",
            "192308218576530622001LGVCKI2ZLXIMJNPINNYA3WBBMEREC7SO6RL4ZDUPTKA2W2LSOAEYL4445P7HJIJAQJ4JDJF46DQQR7G7NN3DUE5DRMEXWOU5LOALYSX7IJ3E55NV5FGLJOZ4UAONH6MMQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,Усть-Лабинский Район,,Ладожская Станица,,Коншиных Улица,,д. 111 | за исключением: литер Ф, здание с кадастровым номером 23:35:1006004:302 (S=488,4 кв.м); литер Ц, здание с кадастровым номером 23:35:1006004:303 (S=488,4 кв.м); литер Ш, здание с кадастровым номером 23:35:1011002:282 (S=49,2 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2356046996",
                "KPP": "235601001",
                "ClientRegId": "010060688341",
                "FullName": "Общество с ограниченной ответственностью \\\"Кубанский Винно-Коньячный комбинат\\\"",
                "ShortName": "ООО \\\"Кубанский Винно-Коньячный комбинат\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "132.00",
        "FARegId": "FA-000000052389484",
        "F2RegId": "FB-000006496467998",
        "AlcCode": "0300003247940000055",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Берёзовый рай\\\"",
        "ShortName": null,
        "marks": [
            "198412645361300323001CB52IHCVNOH6IX64BLRD4HBDVQSWKQREQJ52SJRXEUN5UUC6RXWVUORJUA6HZNNYEVSFD745JPCRUDLCI2QB6RC3GT5YOJ2ZBVWPQKSG4PJZ5P5NTPMWI73VU2TOOKCOQ",
            "1984126453614603230014XZRPHO3MXI2XZ2C34NU7ESOQUKFWB3U65PVSTGNTNI2TU5ZI4NK6RPAEXZZM27QUT4TNZWICAUG45AGNJ3LJNCKVNWFTFDY4VJS2X3LHFNMVGUCLZV2AUX2S75EODHRQ",
            "1984126453614703230013NKPWG22Y6HUT73542TXRTS2GI5UFUDOUF6NMRKBIQQSARAXASLMQOKIL46L6IQJVNW6ERKRJYHVGCSTP52JAGEVIY5OYKU2GE33PL5WEECPUD2KFXWC5SJDDURYT7OIQ",
            "198412645361480323001SJXOK4KCRZOHHCQS7V64LIIE547RZSB4B7BK7S6OHVYV3T5TMHEJ7AEOVEYLO2OY4KSG6XPCTYQBLJNJKD7K45RW56D5WVFPJIP3MM6HCNUGKG5ZBTFJ4NQKEXJ2LJFWY",
            "198412645361510323001TO65GGEU6EX7CXGGZNUOBAPE5QRR2LKZXWIR4WUK6EDGC6DU7FHA6XNTPARPKR5BZ42PFKDLIADWI33LZJZTCL2MK2ANF76ESQ5UPBZMVC3OGFDBLWK6KL2F2TH7JCMOI",
            "198412645361520323001NIGPGPAEJANFKUVZHAYDGITG3I6KULRWNACGDHFJH3AG3P6SYCMMM7IH2WGQEYAJNRAANED6VM4LXRWUY4I4NEA6LDKDKYNLO4ITHHK2OKPFJ5PFGSPGVB3VOXTJL5AWA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Челябинская Область,,Озерск Город,,Кыштымская Улица,30 Дом  , |  | нежилое помещение № 1 (водочное производство), расположенное на первом, втором, третьем этажах в нежилом здании спиртоводочного завода, литер А,А1,А2,А3,А4,А5,а; нежилое помещение № 2 (спиртовое производство), расположенное на первом этаже в нежилом здании спиртоводочного завода, литер А, номера по плану комнат 36 (S=208,9 кв.м), 37 (S=67,3 кв.м)",
                    "RegionCode": "74"
                },
                "INN": "7413022993",
                "KPP": "741301001",
                "ClientRegId": "030000324794",
                "FullName": "Акционерное общество \\\"Озёрский спиртоводочный завод\\\"",
                "ShortName": "АО \\\"ОСВЗ\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "131.00",
        "FARegId": "FA-000000052191177",
        "F2RegId": "FB-000006496468000",
        "AlcCode": "0100000005450000047",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ФИНСКИЙ ЛЕД\\\"",
        "ShortName": null,
        "marks": [
            "198412360742230323001ASEIMUBRFI36RDHOV5ASDYXEWQJUTHLRGSNG3HOJ7WM6QYHZ2MNUZEP6AM4UNRAZHJEDLUQZOJDLP3TAU6QQTS6Z7QPMZKBK3U22MWWDCN5OUWSBF6Q3WMGMABAW6KHJA",
            "198412360742360323001VHRDAGNU4MMC2AEWG3ICCRYLHA4HJR6AYGRRBPZT3QVJEOURC4CCN3W22WPKEOQXEA47TCISAJCLQAIVXQDPL2ZGJZVE4QXXIDVDABUW2NSSYRU2VHQYZML3RCKFTVZHI",
            "198412360742380323001XGO42Z7AP3MURVAMCVJLDEBPBMZNKHT46VCBN6XJEM3EWYIFDBJJJXSCQ5XJU4JMQYAFVMPWIU5JZCSEHQKWGFX5GW2EFQ3VURUZBDBKY5CR6ZDM4VPWHJ47XDL7HJJGA",
            "198412360742390323001KM3L3YQXABG6VS53USDEFVJ2CUP2D2TLMEVIP66ZV4ZA65JQLXTWZ62BM6TLBQV6EZ5RAOP3AON7BNSPLPU7OL5QJTEZWPN2DNWQP2YL2B4IXFUFVYAWHLSCNJ2THZSOI",
            "198412360742430323001L6IP3WQFVI3POKVZ7R5RN6X66E4A5CMC564QPLIKQXVDD7UBLL4GCKTZFYA6DR76P7T4WZQPGURBTSLVTSCTCT43OY6DJWHSGFJYW7PROHYENV374X4N7QX2CZ2GNPUQY",
            "198412360742550323001FAK3RIOQ433EHW6AC6IJDRC7RE2W6WW7QD6JGIKEFDFJWQQHA4TQKHOF3L45G5FEGX35AOT2TUYQ34YNFSADFSXVLBSV7RCPVTWND3RY4XICG6S72BYROIL2XBO4TH7NA",
            "198412360742700323001MCPWZNSB2MIJCUYAN3QPRJVWI4BVZH6FEY6PCI6CEAEC3FYJDCIKYSZHI3EMZBAB6EE3QRSDSEHF2D6E2DFUWVZAWSUNEC5ZXDRMETSJLSQGBZX4MSBFNY45RYERWHGZA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "145.50",
        "FARegId": "FA-000000052148289",
        "F2RegId": "FB-000006496468001",
        "AlcCode": "0100000005410000017",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"БЕЛЕБЕЕВСКАЯ ПЕРЦОВАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198411873544130223001TRHSF66RPOLFACLVFQR4R6GN7I2F2Q3VZVM2WEI6LHDSSTRZXLMJOPOQDARKPW4RSWDZROOBVUTHJGQI6QT6ZWZXXKIE6HUBAFDDVJPMHTMMLADHFGMBUCBFLI3HII6SY",
            "198411873544190223001EETJFFM45IOVLC6A7AOM3CD66IJABS3BHOC3XC2P5O6U3SBM4EMOFG77BHSUD232O3WPEMW3UY25UUTLRFFX3CVCQM73IBMF4SQAECO545GCN6NHUJQKMVXGSFGPF6IBQ",
            "1984118735442402230016AENQ2UWRAG7J6EOEKOW3N42KMKG3SK3RJYKGHV3NKYAKXH4ZDEJMOYWXI3JNFSMXS2ERZ5HP2HQRSSK57QUVDL5AHDONOWTR6AKZBHP7RSSEXUEM2XSVP63T6QID657Y",
            "198411873544250223001PNWYMQCPDPHCQZE5L6K3XFBTGEKNQG2UJP6R4WZL5DIWSDABCIEB2DCUMRV3FTA5ZGSYJWMP2EJ4FYGIDNR2WBT7CMF4ENVO4JOTMBQDNBPNH5WXHYFDNFHPKKS4X7PWA",
            "198411873544260223001GDS2TMFHUWSYPKON2YGH6ZYJ2IZYNHVD65I2V3747FTVL4P2UAQMA3LRAB6FSK3ICCUNOHKZP5IFTMRACA6HEKEUXW4CRT3INRE3YGY3FIFZJ3OXDENJVI4U2JRLDGMKI",
            "198411873544270223001ADRCZLDUYK6NNFFOCINI74S3Z4E4WSR2NTRXNORW5NVUPH3FKNOVU4BXPZ3GXD2MEIQO4HLOCZ5YT326AZ5EQUJYLREZWBSHAPPWGYGWK3BEPJFTMFU5BN2OIYGW5YYJI",
            "198411873544310223001T4LH5ZOKPTIIIWSYTWKA4IWPDUFCOGLPMPGKTJAQGFLWI2VCWWJMUWMQHPIALOX4UEEUQ7MYIJPLVTECEGK6PY5OWRKU4VZHHUJHQOXU642C7DBDAMOLWRUO2O6OSHVTQ",
            "1984118735443202230016YCML55HJNZQNAXGEVSWTCNTQAOONT744C5PWJZKDVHOGODN4QGQVOT4SRGAQY7SPAQYUSKJZMHDOPLTB5ASKL245LIEGSMB6M24T4EKLVO7ZY553NP2GXAWL3HAO2K6Y",
            "198411873544330223001PL7MI5JWLQYLRHWTZFVX2NRIXEFYUXAQJQKZX3NIDKURW6JXFB5AI5CVG4HC44U6KMBFUSGLCJOEPWTRLPY47LOAHOHMZCG5CDVIS2O6ZJ5TBSZI37M4BFLX3FKHVDRDI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "60.00",
        "FARegId": "FA-000000051864651",
        "F2RegId": "FB-000006496468002",
        "AlcCode": "0100000010250000073",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «РОДНАЯ ДУБРАВА»",
        "ShortName": null,
        "marks": [
            "197405237957801222001SGLMTZECZBWKY32WRMITIES424UFYFFTX4W4DWID4K6HL5ORGSHEWESDNDS4A6DLVQGBAT2NADL2LSNKL6TRJ4OGXXQKP44VIHJ4IKFKB5BE27Q3GSCVEWLSMG3BIWTJQ",
            "1974052379578212220014YMPTXL6M4AQZ3JSK6VJ42NZS4C7FZFMO3BCBDKSX5VXWDRGET3KCOF4FYL6WF66Y4QFYA6HSHB4UZCMREB72KYOWTG5YTWSQPFVQGGWSQ26BLD7Y5X5R2K5WPKRFGYWA",
            "197405237957831222001P7V2PGLXH2DGD3VVYIEUMHVWMA6NL357BZPOTQFQ7QZSLS64JYUEVTGKTHISQ2HZNCTJGBUBZKDKE4IYMGQTCMK57GAWSBA7YOAYTQJHA4TJTIIKGVF3CDQXIK7D43RAY",
            "197405237957841222001LKJ5TBWEZYQL6PNGY73DMXAOSQONENL76D5OXXHH5YRYPB3TL2HFSK6N5ONBKQKZQ5OESIQFTXAXTELOSVNTAWQPP7KCMN6SMZA2LGM65E66FP33LSKEBMJHVQCCSVCAA",
            "197405237957881222001HESTGGQOBBK4UK5HDRGHYX7BJUYJC6WDWJVTRS4ZOOIBBFRTM2MOZCNKEMTIKVKCMVFAV53QE5EJS47IIWXFB2WVNNTSJYHXCLQTONSLSM5FHKCBKNDJL22HRFOJMRUHI",
            "1974052379578912220013CTG6NSSQGPGLNSLBTZZF5QSOYADSNXZ57KKKPZUG2NK5B4Q5QOR7HP74KFYGTBZTUBCPTBICXUGC7O3FB6QLQATSGJ626YSC3BAQBU5NGYRARQ4HKV6OOORH2QDAXCNY",
            "197405237957901222001OYHNKTHGTFCMAR7STJUZCZROSMLS4KLFEN3HUEGBPFYSEW7IHCQWJDAJJ7VCHXXBEQL5YQ4XE6NPGLARG3XCI5GAKJDDUOHHHGHYD4AIC2EIPME5EDH5DSPLYYQGMHRWY",
            "197405237957961222001XZFKJQKONM77VZLXRO5N5TTXFYP6DSN7M35ZKWZFDOPOIURIHOCMKMUAJ3OYQIRVV4K2647KR6XEODLNOYDKXCR3YN3DPLQKZZR7WJ3YFO4356B5MVL5S2AXFCXRP6IZQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "62.00",
        "FARegId": "FA-000000051856250",
        "F2RegId": "FB-000006496468003",
        "AlcCode": "0100000010250000059",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ХЛЕБНЫЙ КОЛОС»",
        "ShortName": null,
        "marks": [
            "197405237738391222001F3HZHASYI2FKJEIOY4H47PFEWQO245YOBS3PH5WEKBEXBHLLIJBFHC4ZRQ25MZZ62YXI3GEQE76IMRIC472VNEL664JBVZAQKSGR7JWLOKKDWWKAUTHQBEEBEDD5YWCWI",
            "197405237738421222001JJ3MJL3UQYF6TDWJ4M6MVYI3DUYQZANOOSWRNWAAPPQJQFE6R7J4FVU4KZNOGV3VU4JKXBG4OGVD4MD5HE5NTGWYQB4IK4TAYZL5ZIZ4GR2PJZZJ3CX24UV632BVAMUNI",
            "197405237739291222001QL2WYVEQG5V6YAV27GS5CJGAXIMPPTKYODGLOVE75VS5SK7GZAER4NA7YU43RJRRNBPI7VQLVVVIVKOJSFAU54HA3NMSXKFGQECXH4WAM7NA4CBUXPFMEWXIUU2CMJ3NI",
            "197405237739301222001IEJ6JW2XVJJLYV6V6ISSVSQ3G4KKN7WJ3ZBQYLTHM5UPCUBHXBJK3COWRFPCOAI4GO5SEL6VKGF7ODXFT4PXCX5G6CZHL2VKTNWH4FEQIZTUD54BJC7LUTBNB6FP33EZQ",
            "197405237739321222001PBE3AZ6Z6HVH5LNPGCFONKR6YQTIZ56SPLBGW5F3FYZYIKR6GU7XBLAZ5UXEPITW37DLXTDRZU4WLHJ7SR4ML2L7RUWDUWIZ7I5CD2VYKY2AKXICPWDKZTPGA3YZB5ZOI",
            "1974052377393312220016JIDGZEKI4CGU2GYVOGJGVQ3RMN5T57E56ZHLKKJ6DWT7U6KKNGMP6WNLQ4SLMQV6ITWGCNFLRO3L2KMPAZOILHR7IOI7V2LBVJTQVO6LR2CRKBERRTSGOKY6XJ4NYCYI",
            "197405237739341222001MVFJQPYH2TWSAEAOIUEZI4AISM5443Y2ZHT5R3GKDLESES4O4JLLSATAF5KBUTCHGLLI3I2ZYVQF5736KZ5OEQUHNREBXNUSNFKZYW6RSEJ43YBZLK2ZAI5UFPSJ55UGQ",
            "197405237739411222001ICSOF7HSM42Z67G7GYHFABIHIQYIVY4F7OQVVP5B3FD4ZIRX5ZE4KUSIRJ3YEISTVEIEIY54MZLKCHNWNJJU65UCT4WX46NHY43NJW6J6E3RVR7WRBZDRVNOSUS7ZE76I",
            "197405237739421222001XQ4UGILVGEIEYYJUOXBDIATFMYQQ23P2BSOU4JRYYDSV3BIU2NCDRLL4EWZC3QQFHDAR7O6SXZDPENK4BWFZDDN6EIYBTFRY5NIRAEN6GT544BL2PABASM6GKEMR6L5TI",
            "1974052377394312220015AAVRFQXJB6FRFKCH7C5MQ2SO4V2GBTAA5KVROYT75AZRNQKPSRA5VT3OTOZ4IV2H7DENGVMYSDKCHRMMXM3DT45OG55LF3LMZN77QX6RIK4XEAQ7OYIOZ22UKMIHRLSY",
            "197405237739441222001I4Q4ZVY6PFRROCT43A4AVRRG4U4UB4WTZB3FKR47BQMIMG75XEJND72VPRB3SXV6QF25ABETDTUKSFABQCESPOHYY4NRLBQCXSN5LJNP42XLYAV5LQSZ5PP5PK7POB52Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 11
    },
    {
        "price": "119.00",
        "FARegId": "FA-000000051142352",
        "F2RegId": "FB-000006496468007",
        "AlcCode": "0100489413240000052",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"КАЗАНСКАЯ ПРЕСТИЖНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198308895343330722001AAV4BZ2FTBZAS3RBCGZGD3TUYEXBUN3BBUVPVYBWGFJAO2SHGV5ZZBNNM6M4HN74LDBFJ6R6YV5AOQRS7RCBFDODZ5S2IZ5UQCDF46XIW3NAKX6HUDDP64JLDQ5KXFMWA",
            "198308895343490722001IQTEAL2GKCZ6VHZKAJDHH4NAKI64GSCKEXERH2TBCMCASAHM6VIZZOIW4NOUQC3S4N74VZ2TVSXCMC5DQKUITTCUDF7ALZLEEGCIX4UMGQVAXKOXSFF5D5E5VF4X3PKIQ",
            "1983088953436807220017MG7JGKNT2VKUQZDRVBJ5LUBSAPFTEDLQAJWWADYT4GXHEB5CEJC3THXCT6R6ENC6BB7KJXWGJK6QBUD5O7GOCZZ4EQ5WJMEABG6YC5V4FSW4NWL6ZBMUF4VYRFHY4VNQ",
            "198308895343720722001XZ65C2GBCCN4QDTNNAD73AK2G4B2T3ESSUTPZXKP3FYJ2QPFGZVWIF5R6MO7K2PKK6B2ULLBMT4EGA7ZPPGUQSVARH2FCWJACW3ZRNUCXX5Q3YX42EXDNRXZMIRUI4ZKQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "119.00",
        "FARegId": "FA-000000052027419",
        "F2RegId": "FB-000006496468008",
        "AlcCode": "0100489413240000055",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"УСАДСКАЯ ХЛЕБНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198411246601130223001HIXFTCPFKIJY64XK2X7W5TLOIMYHMEYX4LSV2AAG3R2DWYNJEZUKZHHZAV6O7GAAREPUSG5E2W2OENVITLBE3TY5ONQO4V434J4YQPUU7KO7H2BERLPZLWV5YQKRAYN5A",
            "1984112466012302230017PDLSOMRUBC3KMXD7PLLIRAT5QUAWMVUGGMBL4MS7U6HFYVX2GQXZ4TTGT5G55Y5KBNTJ4ULOGTL7ST556575SCW222JYXBW33EQ3ZLL2TYKNO7CDLPUAW5EO5KILZKAA",
            "198411246601300223001WT4YFKBWZS4M73KOHL22EJE53QQ4GPTYGV5PXDJXQU5DTGGAMJEJ5C42TMOLYMYB7E4BIIU5SXKXYNQ4YUSFRUZXWN33PPW5PJYC4EQIOHTGGHFT5HLMRYDJEKVA6BB6A",
            "198411246601340223001U7RZG4YYQ244NJQLSLVNS27DMQYD2CSZMFIW4F2NNEWJDLTZ4BANOK5I6Y6DZQY627WGJMSUCIC22XEAKLOUIHXY7KTPYTBLC5G57GCX6HHYRNSSBMOHSK52BB5V7F4CI",
            "198411246601380223001MQYMIWM7FG6XDBRPZ24XLYTGC42T6PQVN7XMCGH7D4RCTZQMMYVI2OTYZMBLW6N3T6ANKU476DFODCV6LX4WIM534GMV4QQWRMAF6J2VZTBNFW5BV6EPTSHPHKGCI6HBI",
            "198411246601410223001IND32EZ74X5FOTOCB72MURWPOQN2V54GYV3BZN3DJSEN3QZHBSEBZ54X2AZO2TOWPCJR3AO3GMSAB3NHF3SUKBKDLEA2EINFKUDIWFHTWH6ERO257UJCYXGINFQPKTVMQ",
            "198411246602140223001PBE7GO2H2G54AKZNH56MMJ3MGUGJ4RWW2LCNXGJRBMRI77WDBFDG6JZZFMLAVQHGDS6TNFWBEQEQIDPSMHP77YIMMXAG43627XFENF6NRBJCZ55EISCOQKDH4F36WQJ2Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "119.00",
        "FARegId": "FA-000000051779523",
        "F2RegId": "FB-000006496468009",
        "AlcCode": "0100489413240000038",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"РУССКАЯ ВАЛЮТА\\\"",
        "ShortName": null,
        "marks": [
            "198410806670770123001VRVSGKTCN3ZGIP6P2VGGASP47UXITLGBQVYQUO6VWUTND774YFWAPR6ZPMFQEWQJIOQDC2LO4YV5G6OCJQUHIDZGXLUW4ADIJPWCDJLK4WQJZS7FXSL5P6BD72UN2XXTI",
            "198410806671060123001ZRNFYE27SEKCUUNJBCTFKEAM2Y74V5L6K6ZTRR5WG6N5JHKCBIRPULM3BWP4MSMZP5ZLTRU6UHMPZA2QWJOLWZFRMKKOOSDIQ5U3YKWUBDQN6BOHGP34G36XGV7ZJX7NY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,ТАТАРСТАН РЕСП,Высокогорский муниципальный р-н,Усадское сельское поселение,Тимофеевка д,Профсоюзная ул,д. 4,, | за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж1",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\\"Татспиртпром\\\"",
                "ShortName": "АО \\\"Татспиртпром\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "298.00",
        "FARegId": "FA-000000052397384",
        "F2RegId": "FB-000006496468010",
        "AlcCode": "0100000020360000163",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ №1\\\"",
        "ShortName": null,
        "marks": [
            "187320498083930623001YPMK2CHWMAP6QZB4IAR22MVGF4NVCUI4FT2MOJ4RETR4WEMUIQ56RAK5SURKUERHBBN5QRBLTYEQO2VDVLSD7LVYS3ELGR25XGVMAPFELIAZ63U2VW5XN6HPN6VOTYFJQ",
            "187320498083940623001NKZWTRZLJ22DOE4DVKND45MGHALWOVTKHBUZ57XV35RWVSF6ZBIQCPOUYWFLC5POYYXPNT6F6LKGB5CWKXHAP43NFYCXU5XUOUWM7AO7URTXNDI2C7RG6QONWUUH57EYI",
            "187320498083970623001HIGV6ZGTUSLUAIIRYUSCPNEQOEZONQEODNDUJ4AH47EO6MMKAGNOSGSVIQCWSHWRC52VUVRWLHLXIGPMS4N52AJ4WMTSVJHMROLGX7E5VWQY5XQAT3Z2GUXKZT5HPSJZQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,Вологда Город,,3 Интернационала Улица,39 Дом  , | - нежилое здание с мезонином: 1 этаж: литера А3 - пом. 5, 6, 9а, 10, 11, 15-20; литера А6 - пом. 3, 3а, 3б, 6а, 9б; литера А7 - пом. 35; литера А8 - пом. 36, 36г; литера А9 - пом. 37, 38; литера А11 - пом. 33, 33а; литера А12 - пом. 30; 2 этаж: литера А3 - пом. 37, 38, 42, 43, 47; литера А5 - пом. 52; литера А6 - пом. 3, 3а; 3 этаж: литера А3 - пом. 8-10, 12, 13; литера А6 - пом. 2; литера А7 - пом. 3; мезонин: литера А13 - пом. 1, 2, 3; - административное здание с проходной и складами: 1 этаж: литера В2 - пом. 2; литера В3 - пом. 3; литера В4 - пом. 5, 7; 2 этаж: литера В5 - пом. 16-18; - здание основного производства: 1 этаж: литера А - пом. 6; литера А1 - пом. 1, 3, 3а, 5, 11; 2 этаж: литера А - пом. 5; литера А1 - пом. 1-4; мансарда: литера А2 - пом. 2, 3; - здание посудного цеха: 1 этаж: литера Ж9 - пом. 1, 1б, 1в; литера Ж6 – пом. 1; - здание кондитерского цеха, 1 этаж: литера Б, пом. 21, 24, 25;",
                    "RegionCode": "35"
                },
                "INN": "4720027123",
                "KPP": "352501001",
                "ClientRegId": "010000002036",
                "FullName": "Общество с ограниченной ответственностью \\\"Русский Север\\\"",
                "ShortName": "ООО \\\"Русский Север\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "288.00",
        "FARegId": "FA-000000051420213",
        "F2RegId": "FB-000006496468012",
        "AlcCode": "0100000020360000002",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ № 3\\\"",
        "ShortName": null,
        "marks": [
            "187417563134071222001ROUNZDIKZTF5B53WRQJSQILAAA2Q2IKNG4LWQ6A7PBSX7IUMPGED2WVTJOX3D5QJBGV7FZDOCFIFZ525JPOT6JUZKGUQ7VZ33GZJMWMNFDHX254TD4DVMYLBWVWA4JY7I",
            "187417563134101222001UTYLBVT6OSEEEYKHSVOFIICOVASX2YCKRP2CQCMVLMKGSSEPN5WRTZO7LLT6NW2A65M4N42YYMSUDWVRX3K7PJYF2NE3NERUZEL7UUQMC6DFYSSJFZIMQPKOMMEPLUGGI",
            "187417563134121222001PDW3THKWR7BUDE2OIQD64UI6BMP2ULABHALV2T23FIGNEEJAQP3CUE5WIXPCB7JNLLCC7LIS5RSSDILSHDDNY7LNWB4UI6LFKUDE3SJSUDX7MH62FS7BTRA2KU76CG55I",
            "187417563134131222001CAW7HADKQCIC54TTMWEEMPMQUE5RWYFEGMEMDTU6LUUNTZ23FVTL7TYU5Q5AD3NLODZJ64ON4AFDKJAD2HO4ZMSA5UE7HV2CJSQA5JFWTOG76737LJBKFIJGNY67HSPZQ",
            "187417563134161222001CPDNUJV3IKWSKCRDEIWV7MEO2AF6Z65Q34TSPHI7WWHDHMRE6UYQ5NIDFPGI5743VXYV4VULO5YIRM5ZDDDQBKD3ZSMAADVCH26RQ3MNUSO6GWS2W3R5OA3KDX6KF3ISY",
            "187417563134171222001DODOY42XWM2YNUMXMCTUMBLSVYPP6ZPXE2DQPAD2YFPT3RJOSA52UOI2LBVR72RZ2T3NY4C6LG5PLIMPCGBJ7SIHGPMROPHQCGWXEEVGYOZXD4OBZ5SNUMGUIBYQKNNMI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Вологодская Область,,Вологда Город,,3 Интернационала Улица,39 Дом  , | - нежилое здание с мезонином: 1 этаж: литера А3 - пом. 5, 6, 9а, 10, 11, 15-20; литера А6 - пом. 3, 3а, 3б, 6а, 9б; литера А7 - пом. 35; литера А8 - пом. 36, 36г; литера А9 - пом. 37, 38; литера А11 - пом. 33, 33а; литера А12 - пом. 30; 2 этаж: литера А3 - пом. 37, 38, 42, 43, 47; литера А5 - пом. 52; литера А6 - пом. 3, 3а; 3 этаж: литера А3 - пом. 8-10, 12, 13; литера А6 - пом. 2; литера А7 - пом. 3; мезонин: литера А13 - пом. 1, 2, 3; - административное здание с проходной и складами: 1 этаж: литера В2 - пом. 2; литера В3 - пом. 3; литера В4 - пом. 5, 7; 2 этаж: литера В5 - пом. 16-18; - здание основного производства: 1 этаж: литера А - пом. 6; литера А1 - пом. 1, 3, 3а, 5, 11; 2 этаж: литера А - пом. 5; литера А1 - пом. 1-4; мансарда: литера А2 - пом. 2, 3; - здание посудного цеха: 1 этаж: литера Ж9 - пом. 1, 1б, 1в; литера Ж6 – пом. 1; - здание кондитерского цеха, 1 этаж: литера Б, пом. 21, 24, 25;",
                    "RegionCode": "35"
                },
                "INN": "4720027123",
                "KPP": "352501001",
                "ClientRegId": "010000002036",
                "FullName": "Общество с ограниченной ответственностью \\\"Русский Север\\\"",
                "ShortName": "ООО \\\"Русский Север\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "62.00",
        "FARegId": "FA-000000052205434",
        "F2RegId": "FB-000006496468013",
        "AlcCode": "0100606942420000119",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "197405349673341222001IUA7O7KSMAFKY3YUNHUIAHQFYU7SHULI6YDM4ANAIL34Q7NVREVVCTJDOWQLC2V5U7PMJUPBIM72YTHY2AGCCCA4ZZZVMXDPBCIRP3JBDX5Y6NCF26OROVWLJX77DH33Q",
            "197405349673361222001UTLN7CNNGU3SVHENTR5RCGQRHUTSQJGOOLG7DDEK2T7WCCZH75UBTTNOAQAKSNDKTDL7XEEPWFEAGPTC23BSNYCQDF5EAECEQ5NRTW65DXSJLPK2XJEPEA2QNSQM2ALVQ",
            "197405349673371222001LAR5I2HT4YVWX67DYQZF775YVQBWHWJBBJ2K4L2QEXP5ECKMM6JMZAILCUBC5XW732QKGQW5MCNCRU7KGF5ROKYI4PANWCO2RABFNMOKXFAIXXKA7BNZQRMLIGYDV4YVA",
            "197405349673401222001QXTJYVBM5S5AP6TJ4UDBQ5A3ME6B6AQCHW473TGO2AIOG2DOGOTPQTRHNPGGJGM2SNXJNGYYE3W3LHO3Z324UPW7UZ3HIGPVZCIX7IFTAGUWSFQ6FKKGG34675Z7T2MBY",
            "1974053496734112220012TWZVRLWIBZZLGPTT63Q3RMARATVGVLWHRQH4WEKB33IVXCCERGLBSPXSHTPIBVVI4AOD4CQ526BEY6N33NQOQLF7IJRCLSVDF3K5EFFKDYIOFIHSOHBO57L2H5PO5HOI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "198.00",
        "FARegId": "FA-000000051942078",
        "F2RegId": "FB-000006496468014",
        "AlcCode": "0100000002030000154",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "46111",
        "FullName": "Плодовый алкогольный напиток газированный полусладкий \\\"Лаветти Оранж\\\"",
        "ShortName": null,
        "marks": [
            "190301149933340121001RXL2Q3RP3G2P7KAG3QDIQCBLJ4AFNYXBLFYRGZNO336K4GQISDJMQB2F5GNRCG57YQJKJ3CRD7AHR6FMAQOQTUYWGJV6F57HG64L6R6NUIWDN56CLLXES4FPERDQ6WNIQ",
            "190301149933480121001UEFK5BAAVOT4MWTXPVMOPC5XAQF6E7SC2UBNOWWIOYD4WNA7R5CW26ZHO5NEWJGIKA7ECB3NVFJVVZC2QNSF5EJVP2P2FN5IG6BGIOOMH7QYQ5WZ2O5WV6OZOPUTYHO7A",
            "190301149933500121001AQFETD6JIAQJMRAT3QAGJSL7HEIXX3APV5QYM7KC2UUPXZFYJNFMDCVGNSI7EINYQL7FXGU3EEIEDUP6AF55EP6HMDXPU5UX57X2GBKGU2OIQLLFEYGWACZSIZKI5TX6Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "198.00",
        "FARegId": "FA-000000051861270",
        "F2RegId": "FB-000006496468015",
        "AlcCode": "0100000002030000153",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "46111",
        "FullName": "Плодовый алкогольный напиток газированный сладкий \\\"Лаветти Ванилла\\\"",
        "ShortName": null,
        "marks": [
            "190301136511510121001FLJWOTUMXZR5D3ZJ2EOGFYN4HQQPT723WJCXWLSG3RWC5MTQZPCRWNAOXR3FA44AIIVZG2S3T5Q3XMMM5H5PYU7MO2OVO23ITZHEOGJOAOSRPRKZSWBOLP2AJ3I5ZXFLY",
            "1903011365115901210016YTV7SBBPV4UJ42UFO445JQEIUUW6C7FTRMQATIVSJIWTWIJLFKHA3EHBMGPAWC5YHJYMSRBFQC3QQRR7LLL52PVERUIZ42VWRGSEBPFFZVOPITLVOLDICF2EYEVLRY2I",
            "190301136511670121001QICUQ2L6EJSHBDU52FIZI2FY44O742IQDUHC2NW6OZOOOLBPTB4AKPS6OUJOFYDKELAODTPMY47TYNSVT4HZQOM6RMZQODTLHW6NLIUSFU4V6J2DLLED5CE2XZVXLJBTA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "198.00",
        "FARegId": "FA-000000051934852",
        "F2RegId": "FB-000006496468016",
        "AlcCode": "0100000002030000126",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "46111",
        "FullName": "Плодовый алкогольный напиток газированный сладкий \\\"Лаветти Классико\\\"",
        "ShortName": null,
        "marks": [
            "190301151697550421001O7MNDY7LXHAA743MNOSXIPICTQYJEMWW5OVXXTXSQV4DO3CMPKWSPPCT2EXTUGB7I5N36SE5RAKY6U2Q72CIVSCBF7LZY744FMWC5QXCJYQBGKCTI56YGLEEXNCAEYINI",
            "190301151697710421001N5TRIZX3LWF6JLLVK4WJXEZDSIVXWAMJJSE6ZZU3PZEQABGVRZDVOPZT2RGDTMFBDIARLV6YOE4GRBPRKO4F4BJ3V2WJSVLVZWN5XWFH7FI2CE5ZTNTUPF54DVWHYTJNI",
            "190301151697910421001K35YK7KMMS2MA7RMROLYL2J3YACFGACCPHH4IFG5VNACGCNEH6Y4J6JYZVOAQ3GELROOU2STSRMQGNX2MPVB3KPPQ2WBOOBXFOYBE3IOHN77IDQSPF2XZY2KRHY43KSTY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "198.00",
        "FARegId": "FA-000000051875735",
        "F2RegId": "FB-000006496468017",
        "AlcCode": "0100000002030000019",
        "Capacity": "0.750",
        "AlcVolume": "8.000",
        "ProductVCode": "46111",
        "FullName": "Плодовый алкогольный напиток газированный сладкий \\\"Лаветти Розе\\\"",
        "ShortName": null,
        "marks": [
            "190301132369240121001UGKLEWK77BQBAIPG2FFNSWCKWMTIZEELNQVONDYOUKI2VFXV4ZM36XWQWTRM7T3ZOQ76QCLNQ6IV4HDT3DFNMXQDQQCDGP6VPTPOAGSSPPPQQKSWQ2BEJ2FIQNEQBF7HA",
            "1903011323693201210015CEZI32KLYSDQZRNMZPOVNDSJQVT2BQ7SHVWZNLZIPME6PGHJVW6KCQHXHPYHGKZ6DMTDRC6NHPAVLULSXICXPSHARKBY5GSPPVPAH27HWO2DGGEFBPG6SIYC45X5LJQY",
            "190301132369400121001BCP6JXIKIZ2VXX6GEXR34NNTWEB3W43DF72O6AZOWEGNQVXVK22EOEWA2Z54PUN5LVSMR56VJ2W6TTBNDFRDKG75FIZPYRBP6L4HUVT5EXV5VAHPKABO5V333LHMXC2WY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Крымский р-н,,Варениковская ст-ца,Леваневского ул,д. 100,, | (за исключением склада тары, Литера К1, S=622,9 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м) | (за исключением склада тары, Литера К1, S=622,9 кв.м, Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | (за исключением склада тары, Литера К1, S=622,9 кв.м; коньячного цеха, Литер Л, S=711,1 кв.м) | (за исключением склада тары, литера К1, S=622,9 кв.м; Литер Л, нежилое здание, назначение: нежилое, этаж 1 (Коньячный цех) (S=711,1 кв. м)) | литер К 1 (S=622,9 кв.м)",
                    "RegionCode": "23"
                },
                "INN": "2337028367",
                "KPP": "233701001",
                "ClientRegId": "010000000203",
                "FullName": "Общество с ограниченной ответственностью \\\"Союз-Вино\\\"",
                "ShortName": "ООО \\\"Союз-Вино\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "309.50",
        "FARegId": "FA-000000052364577",
        "F2RegId": "FB-000006509950419",
        "AlcCode": "0100000042540000017",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ДИКИЙ МЁД. НА ЛИПОВОМ МЁДЕ\\\"",
        "ShortName": null,
        "marks": [
            "187422718704050923001CXIYKICHZYFQS3M7Q5FRC3L3EQ6EBWDU7QLN6ZPDLXBMNAWLKZOADZ5IOJU3BUCAHEDBSVP24GH6EGYMJNOFTIUOIGLRT7BVLZDCF3E4ZTP3QL5MNEF6HIGX5C6ZAENYY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,Стерлитамак Город,,Аэродромная Улица,12 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "026832002",
                "ClientRegId": "010000004254",
                "FullName": "Стерлитамакский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "309.50",
        "FARegId": "FA-000000052391506",
        "F2RegId": "FB-000006509950420",
        "AlcCode": "0100000042540000015",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ДИКИЙ МЁД. НА ПРОПОЛИСЕ\\\"",
        "ShortName": null,
        "marks": [
            "187423223739300923001T7HG2QBY25XAVHBNIYPI45PJUQXNJQNYKNBRRCBNCEK7CP2CS5JT4PNB6K4QBRC7TPGBHLS6PBAAYTWAGBSDUFB6DORUGQRMYUWBN3N3IVSBHFF7NICHCEADGSTBJVIEI",
            "187423223739430923001WSN5KXPEUADSLXR2IRNVMGS25IFRE3BOUMMRXCQU5AYTPBIBHR3XWAPBJFKEGUUJTJGKJE4T2LMIYUBDGEU6VH23TR3T3LCO6RCNRZMYJQPVWNWHDLNDOVCT6ZTKF343Y",
            "187423223739440923001SREFOYVG2H4AKFWDQ52WJSY6HMNKI5A4U7OZCRABB2VDF2K4BNE4NJGJE5L2WXE3TYCB363DZBPCQL5DI6M6YTDHSVKK6D34TSSGNKI7K2746BRIVFBIMHA6MPCDG57RQ",
            "187423223739470923001OIPXAS5JYJDSQDF7FDWVEDDXAYV3YA2F3V7LAMWTJRGLCFOCCJ7T2ZP2LBM4CYGHM2GUQ5NMW4CTVN6GIBAJIWMHXUUO2C5YVQQNF5COP6E3JAXFLI47N667FKTPXCPAY",
            "187423223739480923001YYGIK67PCZA4XVSOYLZEM7GIQMPSKOPUT736EJRG7GB2DEPGYIOFZFFVNRY2GHEPTMHRUUOAERI37GEP2JJBZT3RUXFRFJU6KPVAKZFWJIQRRWTS5FWS73FUUP4UPWLUY",
            "187423223739490923001W75JCOQZKPKDJOEIMYILRHYSAUV2JJIYXGFL46ZOIJO7NWGCTXMDOLG4DJC3TVGSOE3QOREGC2YUU6J53U23APD65PRUIDM6ULIEGKUKYGRRVIROGYCCYIU5DXJDUDRSA",
            "187423223739500923001ER4GI5ZV2Y3CWISRDCXYYCKXOM2O4HXMB7OGDAR5DXTAINAP6SZBBZX7G3H7Z3N3HJRBAS6ZF52GBBNPBU4RJ37FUYKOW7O7YM57FNZTLB5MUB744BRGTQP7GQA64NXLI",
            "187423223739510923001OXXQF5VLTWG3FNIWKYT233QHOQVKD2RHOPE6LIC3E27KTFJMIOFJCHYZZWKYYMCPQHAPNRXBVXJJWX2X4FVPASZS7VRWCD45I5KJ6AYQKQFOJYNZ3HAHZ5ULL6QSPF3MY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,Стерлитамак Город,,Аэродромная Улица,12 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "026832002",
                "ClientRegId": "010000004254",
                "FullName": "Стерлитамакский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "207.50",
        "FARegId": "FA-000000051699699",
        "F2RegId": "FB-000006509950422",
        "AlcCode": "0100000005410000053",
        "Capacity": "0.350",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"ДИКИЙ МЁД. НА ЦВЕТОЧНОМ МЁДЕ\\\"",
        "ShortName": null,
        "marks": [
            "187418188158691222001E6SK75IM4DNYFJNT2CDBRLS3CQP7ULSWUD6OR6XYBTIHW657NBXRDKJ6WZ5D7WUHVEPTER75KLTS6WO7HWJQZZC7DZUAGVYXYSVGZPMALGPAHTKHQ53N4TVCOES62ADDQ",
            "187418188158821222001JRWFF66ZFX7EM5DKCJ3XAUUCDIGZ5PTPIP2AJXYIZG7VACZ4J2FMJTSXIFQ6PMGCJEIZFEZW4Z7I6R6PCGW7EKAXHEHH5WEYMOVCMBYCQGSQ5BS54U3IOF3H364QZY6QQ",
            "187418188165971222001IU4WEQYDMGXVFWNUIU5KXTPQYYHRXQRRWJIGJKCEDYLBPU3WEO7WFJPUKAMQLOANM7FJ4EKYJLQMWCYNWCQ3U33EXT67GZVZCME4JXW672JOA7BFNT7OOQNBTBADVDDRA",
            "187418188166161222001RUJPLS7AITOQEJ3U3JBLWXR2LAOCJEZSBFGRIXYPI4YDCYMRJJSUPKIIUOFBCEAKRDMWBG2PXXKNDDLEW4Z5GIY6TUYHIE363UPWU7XM7NQDK3DCEDKX5I7Q2WDRXTIYI",
            "187418188166191222001FOWUXWS5Q6XPTHRIZ2TETKKI4MPISYL3H6YBJIG46DZ24JOH2X7KSEK3CTSUACQXWXJPVYBDCNX56RLTEI5V5CT5VOVECIMOM57ETVZKWIQJ3C45LVINHDDS6WGUGGVAY",
            "187418188166231222001HY2UTEO5IABRXOFYS5HQMSKTWIZ765UMOOQ5I4NYTLGE634H7257C7MTYTVT6PGXNGA3SOYHNKLJAPIC455YP4NM5V56POZGFJ5T5RFNCB3WROC43STXBZ5VWS7TN4U3Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "221.00",
        "FARegId": "FA-000000052042360",
        "F2RegId": "FB-000006564061591",
        "AlcCode": "0100000005410000008",
        "Capacity": "0.250",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\\"АГИДЕЛЬ\\\"",
        "ShortName": null,
        "marks": [
            "19841194008699022300135PFVKYB5MXAY2L3MIG6P5BNVMODN7T5M4RGFGCWO2Q3MUG2ZFLGWUJ5TA3IR44FSGLZHQ5GQGJRSCT3NT5ZGYBT2CI4CYI3WXLJX43M6IDU32YMOG2DVTGC5BABZBKMY",
            "198411940087200223001WBKIEQHMOR7FRQG5S3M56M6LNIJTC5OL4UD57JZASLSYUFCNWXV5GKGKUE5ZPRPUXHTNPKMAB36IOLNY7AWA56IR75G7XXHTL3UXLRRNNLH77PLFCALWL6UVD6UULMSMY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "170.00",
        "FARegId": "FA-000000052143358",
        "F2RegId": "FB-000006564061592",
        "AlcCode": "0100606942420000047",
        "Capacity": "0.250",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам «ПАРНЕ»",
        "ShortName": null,
        "marks": [
            "1984104195698701230013EGHEGFU7MDXNGNZX77EK4FFY4WN7Z4Q2NZD5UVBDNNZBZYRUUMLPQQDHKBVCLDRILNMEHZAXYQ3O224BBAORTM34OMZKV4VJDATQX5DELUM24YWKLN4GAOY4USMD7IDI",
            "198410419569970123001ICZMGO6KCC56H7OQ45EO7LW4M4HGXG2PNCY6NUVN3DJPPZAA6JMFCSYIAWL6K4HJC6LBBADUGMSND42B7G5SXBQE435MJ7BCY252B37P3UNWRNGHFFFNCHQVIWT5OJL3Q",
            "198410419569990123001WO6AHXRI25VZMRFHDB4YNJNB7MZ2E3LZTCVCXY7VHEEKHUIBDMIQRPZGQVOCGRMVHI5DASO7YQS3LXQK4ILDOR5S4D2NBPR6BRGG62XXXIOUKB2JSNKIR6HPI7YAUNXKQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Чувашская Республика - Чувашия,,Чебоксары Город,,Константина Иванова Улица,63 Дом  , | за исключением помещений 9 (S=6,1 кв.м), 10 (S=4,2 кв.м), 11 (S=7,0 кв.м), 13 (S=63,5 кв.м), №№ 17-44 (S=363,4 кв.м) в здании заводоуправления, 1 этаж, Литер А, кадастровый номер 21:01:010211:115; нежилого помещения (S=178,8 кв.м), кадастровый номер 21:01:010211:918",
                    "RegionCode": "21"
                },
                "INN": "2130179610",
                "KPP": "213001001",
                "ClientRegId": "010060694242",
                "FullName": "Общество с ограниченной ответственностью \\\"Чебоксарский ликеро-водочный завод\\\"",
                "ShortName": "ООО \\\"ЧЛВЗ\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "61.30",
        "FARegId": "FA-000000052507974",
        "F2RegId": "FB-000006564061593",
        "AlcCode": "0100000054580000105",
        "Capacity": "0.100",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"КЕДРОВИЦА КЕДРОВАЯ МЯГКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "197303964175991222001GSSTRNBRCNROGCKMNFBGK64WWQTQG4Y2VPV2GRESA6LS3MKKYEP23MO747Y2TFAQPJZ35UJ2SMXVPK6PUJSRVKJ7U3JOWBXZHLRGX5WKU43ENP2BP5Q55RVBUJS7YSKVI",
            "1973039641760412220016OS62WSRKGGC6KHLPAYBLSNPMY7RYDSNAUPU4AKJ6CW3VS6GPX5ZRA7Y6QQVLB2G2VACYXSMEW45IRGPZAJEKDWFVU757GHNJ2XBOUS42JZJBTRSZG6TRVMUY5ZWJ3CIQ",
            "1973039641761112220016QN36A5ZTHWEXCKJ73NOFYTZRYOJUAGHUQNYS6AX3O75PDRQRB5BRADJ4SR65Y3RSZWWEU424Z5VTGLWNULKBCZYVYMS5SHOL4QEBTV26ERACMLMYP6TXEEMG3QSO4C2Y",
            "197303964176151222001G4XMQFLXQ2QQMWJONPLBR7EU5E3R2IBJBGXR2Z3WZ7IA3HZWMPAECJ3F4MLNH4JARCOIC5LYPHWEW2A4VP7PAUZJ3OV2IPYQ3OFW2APVTAT6VTZWB3NQZLPRBATCYZHFY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "130.30",
        "FARegId": "FA-000000052086853",
        "F2RegId": "FB-000006564061594",
        "AlcCode": "0100000054580000090",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"КЕДРОВИЦА КЕДРОВАЯ МЯГКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198310490316350123001Z5MWLODEMXPR5YPPBMKI6TELPQDLZQDADKLW7VEMGQ7NQALZ3YN6G43N4Q4RYSBQNQ2AZ4JI2XWQACWMED2KEL7ZJTOLTWTHDHPAR3O6TECT74TIP2BKKZKH6XIB7RIQQ",
            "198310490316540123001YR6Y6GMD6Q2HTHDHGMIDZDEALQW7M3ODZ6UOP72ZSXBMIX6V7G3IMKTFKHDEDIN5KIX4WG7PJLKOFOKIYBKJRJSK7SZ4S2WYGS54GEAAYMOBIVL4NRDMEW4WM3NVPURWY",
            "198310490316560123001Z5UBNGDNPZL5GRU6DKPLFNXFWYKYHFG4L3YS52QYVU4H2RANT4X5JF5GWT5AINDQO4O7APRSXQJB5T4ZUNS5CR4TK2A46RCZDWFDAMQKCS2M7VHVIN3VALCS6BITXQS4I",
            "198310490316570123001IS3URLYLWCPDR3UKFO3GT22M7IVNCFIIMRUUZWZZBTVCN6FYMS3XEWGGIGXDTFSUD5TANW5NQIKMQGKJCJROBYH736GGF2EP2BTG5ZGC5L3625U4HAO422ZGPFOKKYPAI",
            "198310490316580123001P6CLQUXVM75VJUCAB4TLVBRXZ42WCUE6OW3TLDDI46HEDYBMHDDFBDPU3L5FPBZZRPDIOJWG567Z2Z4G7UMWL4KT5UHC4ZH7NBUEQGA26ZBORHL6R5AIIJOLO7X4SMNMY",
            "198310490316590123001XF37M2GI2W64XAYDGP6BERHZYAISCXJ6OFQKRVXGR37ZNEBGENELMP5NNJC254VULBFR5I4GGBVRFTTI7SQLVZILQBDUTMCQE2DWCFNHHXWTWUUCLNK6QEN7ENR5UIAOI",
            "198310490316620123001OL7YX4PEQKPAZJG6JBYRCSYOKYMRD5F4SC6GXNBAPYXXQRKMQMYTZU4BWFLZ6DKOQVIHDK7U3XFC4EMVOSR2Q7P2D6IAVQASMIBDVFUAFXUKJVL5G2VD3JK7MTSSCBMYY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "312.63",
        "FARegId": "FA-000000052328694",
        "F2RegId": "FB-000006564061595",
        "AlcCode": "0100000054580000138",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\\"ХАСКИ КЛЮКВА\\\"",
        "ShortName": null,
        "marks": [
            "187319711545390623001O2ESLC7WZ6Y74IP6S5AF2NAVZAHQTAXPG4DSO46UW6S3XUMXFATNLYA4V52LYXYP2Q22WNMXX4TDD2GJOKKIEAXZN4TU7JHA7766HHMP22EMAIQ4A7UJC2XEEQHMNFBHY",
            "1873197115454406230012QG5ADRC2Z6PDAHVPTTMHQNFR4STD4UFJ623PXWH5KPIG22JNGT62EI5EESJVBUMEFZW5L3H5I6QZREE7G756NBVP4BCJ4D4QPBCJMS7KKYB3VVT4WIAHSWSKEFVE72GQ",
            "187319711545660623001TJCP77S4JMBRIJ4SF2NVGDO5BUCEW43AQHIFY2KEQPZT4KKRJDFJP3ELBUDMDTXQSJTTXPQNO5KLPOQ5THSBZZVZJRCLKTTLPTK6MLK4Z4XYNEFRDVXKKE36VNAA5GBBQ",
            "187319711545670623001G6GSHIGPQ42HAPXJDQY4WKMXTM4HJOFB4DRTC6D2X446IY3QDI5YYLGQHZ4SH2RSQYKBE47SQVPSRAYFAOTY4NRTQZFBOL6SHWBNJAVXH3E44SOLB4GAJY5TSV2D2AOBA",
            "187319711546100623001TWLJCEKBBABYT722BGQJGPS3GAQNNLIBBRGCPQPIJLNGIP3AU3NU3MU6QPEVXFVNR42RZZGBN4IHFLEBGTCNZV4EBXDP4FN6ZSGAQUPY264PT3QHICZ5A2Y7L33UTKGUI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "312.63",
        "FARegId": "FA-000000052566617",
        "F2RegId": "FB-000006564061596",
        "AlcCode": "0100606933430000077",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая «ХАСКИ СЕВЕРНАЯ СМОРОДИНА»",
        "ShortName": null,
        "marks": [
            "187423521092631023001YOG4N6GZLHXJ3PRX7PI2T52CYMVBA5HS6F2HKDCI4KLSY354BAD2GI4IIYKT3QI6NGGBQI46INJ3KTCG62DTSPLMZ4DWG2SZSRNU6WOQ2VOQS7EN3EWYS7YLP3ZGDRT5Q",
            "187423521092661023001WUKEV2WDQYQ23UFFRXHYMHYNBMMWPP7C6OGK2CWXYRVLNJW6KDHSDED3DCATCHK674E6X2NWFKF46WYGTP5LL6BUM3NUEK4OR5ZA3EBC64Q3XL3MDKAXYKJ5H4MCAAX4Y",
            "187423521092711023001DM3G7QZCMAOZJZOHRTXM4C4TQUA3HEBV23CLLB5YSC5SWTN7RIWOTUY7UMNUVWYJGBBMPIA5G5CJN5ZB667CPTRPSUA5QMYNGDK3KREIJ4WRNTKXFFC7GG7K65VXJPBDA",
            "187423521092751023001VVMEVBZBXTCSQ7KLDVB2DIDBFA64LI5EQ7EETADPQSSPDYRJE4U2M3N2CTR3VHCPX7MKNEJLPCLZB2XLCQTU7C42WHRLRK4GHIKWMEZQELIFVMHFBWCWSOU27R6V5QFYQ",
            "1874235210929310230013XCWXCC4KJS5ZVATHNS5LRCLXECF2YN7QC5ES7QSE7BN27Q2VHDBTFM25PVZ3WOXBBDBLXOKDDU36R2XY7WS4LSOXATQIPAEKDNLHAXXNKCMY52LPOOBR4QYMNXGVJROI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Руза Город,Горбово Поселок,Центральная Улица,1а Дом  , | производственный корпус; спиртохранилище; складской корпус с бытовыми помещениями, этаж 1, помещение 2",
                    "RegionCode": "50"
                },
                "INN": "5075029180",
                "KPP": "507501001",
                "ClientRegId": "010060693343",
                "FullName": "Общество с ограниченной ответственностью \\\"Рузский Купажный завод\\\"",
                "ShortName": "ООО \\\"Рузский Купажный завод\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "162.27",
        "FARegId": "FA-000000052578264",
        "F2RegId": "FB-000006564061597",
        "AlcCode": "0100000054580000011",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ХАСКИ\\\"",
        "ShortName": null,
        "marks": [
            "198311445419210823001Z2NDP2P7JN5Y5C3HISGZAUWRQA762QCHVJBR56EEW6GPZLMU6XSC7576ZOX7K7ELJZJOWJESKFDSJJR3PGHKRBMEKGJQH4XENAXY4GUCLUMYUUACO6QV7CSVE763HETTI",
            "198311445419290823001ECBEBYUNH7FEODOGVLLDSQCKGUVH3WNOT3HSQ5LRX7JXR75WZFSZX6C6ON553I4NP35RF4GPS3RAYW4DJZE5W42AL7SK6K7DJCLYAUG2SZZXTLVZAJE7XT5QKZWJAOQKQ",
            "198311445419350823001HEEZYYGX72ZULMDNHJFZMWJZPMHC6NSNGXZUTAAUHNPYN3LITL7QXWRE76MPKSGFGTALHWSVWVW6OM3GFZW4UFVUYYAGRAKOCJ5EPP32LWAHJNXMHVBEBGEBIZN45ONCY",
            "198311445419360823001L2HI5TBR5DZQDUHN7PJTEFAQHMKBGQ6ZENWRSL7RVJHVXCST2BGZSKDQYZRGN4NJES4KGOFJ4YBTJAKCIDL5IH2YXJ524NOTJXAKQYEISC5NBFUPWTB6MTG2FBMZ7JTCY",
            "1983114454193708230017X6RFDXFDBAAIQCHP3DHL6RPHQRCFKZFJMPSLAIYMYEN3LGOPFRQIYVVGOX4RS7O2NG2AHRHC2PJVP75TWHAO4WJIS6LE36GVE246FHAK4GPJQMRPUAWPJWAAGGQLPWKI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "312.63",
        "FARegId": "FA-000000052529382",
        "F2RegId": "FB-000006564061598",
        "AlcCode": "0100000054580000013",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ХАСКИ\\\"",
        "ShortName": null,
        "marks": [
            "187320429014340623001XWKGMBJFAIZWRWFCCPCPWFEVTMYKTAPLEJNW6KTZ4QKO62Y3QC7DBCODTMSXC5N2W5TDJZ2EVWBE22M742DKKDBUO35STXTHCGAYLQMCGMQGJ3JMWGDSHZHOJSN3YX2ZQ",
            "18732042901437062300177MNKTQ5ZXFQELZMYX76C7FLSMA6WVWYSAYHK4GKNMJHYNVC7IR4DELMPSZU6F7LY3SBNQXW6XGBXWMZ6ZXF3H4TX7A7C6BYVFP5CEUNPVOUMNLH5Q2YBY7BKWWK7YU4Y",
            "187320429014580623001JOV3NCBVW6WLIG226PM35D6N3MBOOEFTKDGYP43H2YFSFTG3RDJ325AAIIEFDUQ7MNGOMDFJSAW5BD3IOCVGUWCDV3K7YZLSD442FPDIZYGBWIM4ZHOPLB7TFKGIJIDWI",
            "187320429014730623001SDS6GIN4ECNGSUZT77R7D4PNRY2NVHIP5RY7KZQFEPAGMPP363RXFQL7LXN2RYPRGJIHBU6EKJE5IOPY4QJVBNWFZPMRQECOK2ZERHDFPDZFVZWOA5L65IAYV2QCRO2FQ",
            "187320429014800623001QWKOMRCLUMBVFLJ56WF2POVQ3QRCTZC22VLER23RQIFLZ2S7FBBMCDC5KR5ZZW5NCJRCOFRKTHJDRQKEAV3DSZ2Z7UXYRPLWWMUSMTXI2SM2ZKRTPS6AHLDCHWLCNFIFQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "437.37",
        "FARegId": "FA-000000052567263",
        "F2RegId": "FB-000006564061599",
        "AlcCode": "0100000054580000014",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ХАСКИ\\\"",
        "ShortName": null,
        "marks": [
            "188303060263391222001WB3OB6POVGK6LBNKDUSDEARZVUZA5KDLNHUJGBOMZBOBNMPCPMRA7X3ONFJC4G53K6ZPY7RRTYNQBH62ZBRU56CP6ASV3XHUM4N3C5JUWXBFQSKE27LFQZG43RW5J2H7A",
            "188303060263601222001CTGVJETKL57UJ2JUHN7M2DCOYMII5U26XDZQE32MHBLI7RJWXD2QZ72QLW3W4MR5LWDNIWPUEOG2M3KULG3QFP7ZPKRHYUDSRSOWK2Y4AENC7Z33XVFBVSRYDSZU4ALCQ",
            "188303060264051222001YP3E2SBAFESMUTR3LR2YURPUYMAMZUF2PFFBUC7EWWRQNM3OQ47V6OENAU7KQWRZYHNCNIBAKLFBIVYK5I2IBHP4PR76M52EDJPVOFH2NUZRAT7U767KQSISR7EHFHEWY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "312.63",
        "FARegId": "FA-000000052530541",
        "F2RegId": "FB-000006564061600",
        "AlcCode": "0100000054580000136",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"ХАСКИ ЦИТРУСОВЫЙ МИКС\\\"",
        "ShortName": null,
        "marks": [
            "187320318793670623001SIOY7HY6RKYVF4I3HVUJDT6SVESS7E7GUKRNICZY34UPOR4FUPRX234IUMO7UQFJTLWRV7USER377GFLWKPWS5U53FTXPUIS3E4JHJDIDUCQGN75URCWYU2QPHK2M4HLI",
            "187320318794230623001VZ5CTB37O2QATKO4RAO2LI4KXQHE5VAHFBCC4WI7EVAB66XOEVUEF2L4GMJFKC7BXV3F4UXDGHRLIGCTZPCYH47PMDPU2CUAG5B7QTM5Q2WQEAVRXDV2FE6OJYRG4GKVQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Омская Область,,Омск Город,,Разъездная Улица,,14 | Главный корпус, кадастровый номер 55:36:040112:931; Промышленный объект IV класса опасности «Реконструкция спиртонасосной со спиртохранилищем на территории ЛВЗ», кадастровый номер 55:36:040112:2887; Технологический цех, кадастровый номер 55:36:040112:1101; Винохранилище №2, лаборатория, кадастровый номер 55:36:040112:1157; Цех крупяных палочек, кадастровый номер 55:36:040112:1156 (за исключением помещения № 22 на первом этаже); Винохранилище №3, кадастровый номер 55:36:040112:1120",
                    "RegionCode": "55"
                },
                "INN": "5506006782",
                "KPP": "550332002",
                "ClientRegId": "010000005458",
                "FullName": "Общество с ограниченной ответственностью \\\"Омсквинпром\\\"",
                "ShortName": "ООО \\\"Омсквинпром\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "132.00",
        "FARegId": "FA-000000052389484",
        "F2RegId": "FB-000006564061601",
        "AlcCode": "0300003247940000055",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Берёзовый рай\\\"",
        "ShortName": null,
        "marks": [
            "198412645368860323001EZENBUU2TRWTFW7AYUXL4UMTUUGJDUYBQ4WM5HJWIN7B5A6MJR6KPN7HWFXU6BFJZCVDKXNS6Y66ZKNYXNBVHB2JHVZLVNCV7UMWPUUDMMI7I7J7YA7JYTE3AVRIR7PYQ",
            "198412645368870323001WNWJ2RSHZRRKWK3SVJV4AAZVBAKG7RPWJ2BN3Z32ZKT7D6POZAJK4TRNOZMADUWWDMFIR24KNHSFISY57JBVB5X2D3YMZ4N6HVZ2BROVFTRMKFZAQT7GVT42L7WJYP2JY",
            "198412645368880323001VSSFEHLYID5JQISVAXEZSDGENIJJKISPMT2OV54MOXD3X2CANS4M6USVYOHITWUVPKBWVT5WWJI34IDDCPDE6SUSP2IP6YQJTQJJDR7OMPEDSJMKJULBV7APA7273UNLY",
            "198412645368890323001SEIB53U3CFKHOHDWLKEIJGDRRYYA233FQX3SKPDSC6YZBMENAVJM2PWW4B7QQWATPPTWACXJP43M7EFEWGCNVIPMUQ5C32FGOBT5MIZIRQBALMGC62LOY6DZEV3UQT3KA",
            "198412645368900323001T7ZIIIX3QDWUS6NZ6NW5JYWNW4JX4WO3IHDXJBF4EFVCDHNCO7OUS76V3WYOBNHF7ZJVNWLXG3VQ3EOFGG4PUM4MSELB42SIACE5IDBOCIUKYLCEDDBIVPQI3X3KNP3KA",
            "198412645368910323001X722CFWQNB6QA65WGWQJZPDQIEP2DBZCKMI663NDWQMQZI2HHLDZLDGKECTVACEOX7R2WQWRNCOWQFQIKWFSVP46W5P34SI34QO7KO3OG5K7ZUO6CPPDZF5DNI4E6VGPQ",
            "198412645368920323001GK4URI4KUL3BZPO5RKWFVXVUFEFIEJB4B4RBXJG5C7CVFN2WVSONET57QLMPTLRKTHMLDLDZ5GFYDXK577S5ISGPFWDK44ZC7TWBCMBQDACPXWRQVVUCJCIQGC7FL5WQY",
            "19841264536893032300134DAGV4TN6FFG6JCYPPPT7ANII6H7EBA2E6GLTLR33OCUVVPUOZX6AMNKCPLFWT3CIOYQHGZ6MCRJGLISNGGFA6NJXM35TRLVGOP6DY7KLN5MYNFX4BY7W3IXBBOG2JJQ",
            "198412645368940323001NJC7P2NOLGXFV3OJBEOMLWL27UMPGZ4SP4IEBIRLEDOWUZCFLRQTYBSDA3GGQGG2R7FFN7VJGGOF3NX64I6TISRUJEIVYKBANO7CX4TOFMF3WURHDGRNJ252QESVI2NUA",
            "198412645368950323001XJDZAKJJHP4VA5PKCKG3ZSYVPYSKGOMSYDDKNTDLYMTPMU36TR6X7ZEDSR4IDLCWAV7YHF3OEIT26PVP3ZF6LLMSBNUEWC3DWS7QVSLXWZNBWB4LF7ANR6WTDWZV6Y6BA",
            "198412645368960323001T2FCZH6WHGJRTTPOASCH4BQ5TYFQYENYIFGPFST6PXZ45UMYAVPC4GFPIUVEQL5H527IZCD62PGUBCUDESWKZO3DYB4OAEEBDQGG2D7L3WCACQFVOWBDUVA4ESKNYY3BA",
            "198412645368970323001RTOCF3KD5AOVZ6J5SIWHESLJNU2RQ55IKZZS4AW5NRIH74Z3WZWVLX6MFH53GWPIETCM4WIMDCVEGRB2UI6D6YZJPQC2VOK5NNFDK42UK54WUAOFMFK5R5AOLDVRR3Q5I",
            "198412645368980323001CXOXRU3YX7HN6RENQZM7N2L5EMHOYOUBY4RCKQ4ACNOPP27TWMAJIRQQYJIQATRZHOFBW4VIST7ZX42MHUFNXHTQZMPDR565G77ALO5MGTKUHC3PNVRR3TQFHHDE4G77Q",
            "198412645368990323001DLSOCIQXQKGC25MPCAUG2LMHQEZ3NA4LZXYLHEW2GS3PA5QCI6C6ZPHOHCEZW34OVPHIETOJFWPFYRYGNMW326RJOBR444N32SMMICBFWU6X3CROBWZXMP6GLLAKKYGII",
            "1984126453690003230012C5E6FPQXPC5L6DICB6754WC64NYKB5LR6FMCLJU4HQAOYOGL6TQBHR42RQBX27LXXSX24RKREDT65WZWLDXNVJVW3NM6R5UUFBBOBMFAPD4F3UZGG3D5VJB5GLIF645Q",
            "198412645369010323001SK47G3QOQHSXXIGJL3TW4WNVRYX3HHL2E43R6GYY3LFOLIXZVYXPGJO6DIIFWEWZIUT5SKR77XZH5DOK4H5LQNIVKJQHMCMCNRBKJE7LRI5W7YDQXJPCVZPJEUNCAIADI",
            "198412645369020323001C5CKSJUF627XZM3YXNZJHRI3AQIPXPDHIOVSXCE2O7MMPKE5G7DHGTCONASNDO3U2MRR2E6SWIWLZVF57VJKH32VMNHFCF73KM7TUFURYQOR6CAIM6RNLPILPYSJKMB2I",
            "198412645369030323001NGAITOYWGUFJJW43LCIWNVW76UCNNIVEI3QWD66UG5ZHFTZ2KOWVI6OIGI24VOTSZHXIV7LSYWORJKQVN77N5DCD4KDA7F355HA6OR7KSEI4AAXV2NW3T3WRQRJQAIC3I",
            "198412645369040323001TRI5OAWWISGFKHNLOGWOLAIGAIVHDKJD5TPZZQQOXDKH5GXAADIPDXNRGKQMFUPUJNOBVTFP34AO6ZR5FBBIK27OEAKLLFJYTVAYTJKSBTPGUMKO3EIWG4XNTFM6QIJNI",
            "198412645369050323001A6CQVYMT43LVMXBZZRVFRJLOM477G4VDAPEKD2XKFCKMHPYNXWCZTDA22FGYM7AZOAVGPBGCVFLIF6H3C4D5BCGDZZ2F6WYPAWYQ754CP7FHJEDPMTVIHPCYN3VRLZRQI",
            "1984126453690603230016XC77HCDN3VZRJ3LMAZ4CFYNDY63R5HDW3BJ3ELEC3UDDSONXLUQ3GA5ICNMVOJH4QZU4NEWIBXA4UGMXBB7EZZHRBYWUOEVSAKLXJPTG3S7AOX5JP42MQ3ILSWSZ5ADY",
            "1984126453690703230012USL3JQ3W76SIL4Y54TR4XHKUEV65EIFE3IRWWJHZ2LV5RZDVHFTP2FI2DW4V2G3SE5Z6ZYEAV235FAP4EF67OX6VWBRRSCKOXEC57FFE364HFNFY6DKSZBGE5TO36E5I",
            "198412645369080323001JNQGM7532UIYG6RBOMWJQQINJAHCSMXUQTOGEJYU46LGJ4S3SHATFR6DKRMRGKMS4E25H7JUFCAOIXUSW5I32WSPVLTTWLNQQF2ZPHEGSEZI7WCB6YE3ADSM4FC4EENVY",
            "198412645369090323001NO3FVGNRZVO6VCXHHP65K2HUGM3IOMSVTSVK3WKNI3A537J27IKMEXKZZQLM25RSFQ6NCNFC2VUI5ORTA4D2UVV3MFWIHC45HBFZ5QTOJUBW3U6YURDHTNSWUFWQYTK3A",
            "198412645369100323001X22D4DGDBGSH2RJYYCQ5X4DBU4DM3UNKETAPU5UWFZ7HQE4RBKNMGSKA5K7PZSLK5YJX7UF277FUOKFZSIW22CVVPJQYYHWQM3T64PPZ22PTNKTWOKTTDD4E3MNYYUACQ",
            "1984126453691103230014YIXVLGM6Y5C23WRW3YT2FTQCEHYBL4LYM5RAG6G4MIP3O2ARYYSMGGXZC4QFTRMCOP3XPNSCOHR3ZDZNV27ZO7VBUMMZWQJQ33LG3I7JCJK4ADL6TNBPFZIYBSUVSTYQ",
            "198412645369960323001CTY6LI6JV5LWREB5FYVVGJTFCQROK3L3FKY4YHVPMEANXQSSYGEYESLK74ZSJKZYMNWS5MGC54KK7DTNVJAKCO7VQHIUGAG4CQPQD77VV2YTHWD3J5S5QXWVJ3BC2NUHQ",
            "1984126453699703230017V5UZVJURH4BELQISLKXG6OL34BSWBPCSD4SSPIAA3QUZTIBG2JFW5NXFDWE45YTCKZR3YTRFOISN4JB6PICHLVDJJRCW5YEIPTEA3M4P3U5CFGVWPMYO553YO6PQVDGQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Челябинская Область,,Озерск Город,,Кыштымская Улица,30 Дом  , |  | нежилое помещение № 1 (водочное производство), расположенное на первом, втором, третьем этажах в нежилом здании спиртоводочного завода, литер А,А1,А2,А3,А4,А5,а; нежилое помещение № 2 (спиртовое производство), расположенное на первом этаже в нежилом здании спиртоводочного завода, литер А, номера по плану комнат 36 (S=208,9 кв.м), 37 (S=67,3 кв.м)",
                    "RegionCode": "74"
                },
                "INN": "7413022993",
                "KPP": "741301001",
                "ClientRegId": "030000324794",
                "FullName": "Акционерное общество \\\"Озёрский спиртоводочный завод\\\"",
                "ShortName": "АО \\\"ОСВЗ\\\""
            }
        },
        "quantity": 28
    },
    {
        "price": "58.00",
        "FARegId": "FA-000000052391510",
        "F2RegId": "FB-000006564061602",
        "AlcCode": "0100000042540000020",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ФИНСКИЙ ЛЕД\\\"",
        "ShortName": null,
        "marks": [
            "197405643936901222001UHAQHFZHYDMSOVJETAQPI7ZIOAW5DOC4NWZLOSAINKT6IWAV5B44VYE45BLN4WVOUC4P6REOVOBHXI7C43XL5F5Q7RP4MF33YPDTAPY3AZVSYYBGLGOFS7OBUMXM7E5CQ",
            "197405643936951222001JGWDQCUW4VJ2WAAX5DV6KTLXDIPOSTERVGYL4QI3K77WVJKIQPVJVNNUXI7753PMST4LQPMZGNC7YNOWSTNWZ3A64DY56PSQVBRSECI3QQCQEQFCTMXVVEIIMW4T6XXTI",
            "197405643936971222001PMNDC3NXALQQXOHS2YZLCJPMNMEO6LSJM663NERVPLVMXEW3NMDSAEVV66E2GSOTPLVETBCXRUNPLSBHSQCWDERUV6U2KLLIJI56KJ2KPRS7Y7K2TW7V5TSBXSLD2FUWY",
            "197405643936991222001QZOZXI4OR3CSLAZQ7AMQZTFNGYJG6DYRN4WWYIMR6TK7IBCTUD4GTVBC53O7VJMTR56TAFEKRGLVQ7RLG7SKRSPKAAFR5LP4UALFU24ARAKNZTFE5RY4YQDZMQH2VEGRY",
            "197405643937001222001JQ7D4WSHL7LAD6VPZ2XLBKYO2ILDWPDQ2YE22YVXZ5C57RIIG4SXKXYJSWJX2N53ZSXZ7NEPHN527RQ6C73GKSPSF6TJY2UQXQOKU4JX7GE7ZOZJQYJN2BXBF6EPFN4PA",
            "197405643937031222001YV3GON4G7DLTDIKGZEWNVQZ6OIHDNJ7FTYSML4GHFAWY6DWUKBJTEAKIVRIDCRTNF72GMJIKEP4Q2VLDIS25DRS7MKA6J2WMVTQLUGWZPWER23RFOG33BRLPOO6IDK3BI",
            "197405643937051222001WZUHP67ANFEFQFX2Y2Q5FX5ZKAPVEME4M6WSVZJ5ROJKMSDP7YJKFPTGREGVDJIWSBMYSMP2ZDZXWC7J63VBSHXTART6P4UN7UMB5KYQFJJDAPTN3VVHDHYFO45IDDFSI",
            "197405643937061222001EFHDQNP436SCAVTOGBQ4Q6RGBULGLPIYECEO4PRUNZ5NK4QQXNDUXPRRNLFNFIRGDA2P7M2JMGWTTAENBXOCS53YVTRPGK6TW72REF5CWVUJSEKPV3NFCUPZ2HGIQ6J4I",
            "197405643937101222001YTKPRONIX5VAFY2HLIQMVOXHVIH4MS5MJ57XMVCNXBJEQR232TG4CFG7LTVBVO3G5TDW4CT2LAPQL6GDPBU6RAYOX3IKF6VGZGHYS3TA6SYUAPAH5M4Q7IQGVCUY36RIQ",
            "197405643937121222001GQ2SUBRD3XLJAGDFEXSIGI3NFE23TDV3ZBHLJ32TPZE4G7G7DROZHHQ72LDPBA2QGYWZ6BO5MQXGO47BTPQJTB2WPZIMIC76H7CIQYISZW7OZ4JZWVJJZLASEHTSKLFZA",
            "197405643937131222001PPZAKUE3J6S2MPFJTNIC2NJTSADVDWV47RM3G3BQTU3EMX4R3BUKGSSIDKZBHJZRGJUJYEDC7ZABW2WPQUP6FI3BKLSGC3D4QC6O7ZSUIP3SHMU6RY3DTD5NUJN4QCMVI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,Стерлитамак Город,,Аэродромная Улица,12 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "026832002",
                "ClientRegId": "010000004254",
                "FullName": "Стерлитамакский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 11
    },
    {
        "price": "73.50",
        "FARegId": "FA-000000052274363",
        "F2RegId": "FB-000006564061603",
        "AlcCode": "0100000042540000002",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "197405644242621222001PN7Y3RMRCQG5YFGQBD4IIA37XY3J3RL7ASWEEX5OVEUYDOJQ6D3BS64XKMOZCGIQC5XW4SBBZKCULI6KELZTHUA7QSXE5CQGQGHBWWNXUCTR5TBSQIIVY35W4FDESCM6I",
            "197405644242631222001N7YQURTJUWXUW3EKUW5UDJVKMIRV6O6AZHS5UWAFG3TTWWH56CAJL52RZYG42B4TYFOHGVR6UHZUBWNE5CMOCKFFPKA3HJX44ZFZSEJ4PBUU6SIYXAHWO52IXXIPXYVNA",
            "197405644242641222001BPOEBNM6DMNI2SSDZOZTPYZWGQF5HVWD4KJ4GUC2XEOLNH6YTCHYNIKV7XH7JDKGMBNNOZRIDG6ZKIPJK2PZCOI5RW2LHH7VGAIXD3ZVVURGB2SRY2LXQAX4OU5P5SUUA",
            "1974056442426512220014TKUJSCAW7TXSHR76SIZU2NC2EW5EJG23LNSUNKO5LJH6RB5AWVB5ILF4AJKWUBUZZLVBCWOD6PKFTPHOGTBKBH5AFRKR3ZEEEAPOA26P3KUXWHSAXOAVVU777SFSNJSQ",
            "1974056442427412220016MDQCEFATSEOBLFJNOVNC3K67QZKRK2S24AAQNQK435TZZ5JTDY44GVTXEBPIHAXTLFFTVIGCJHBKXXJSBIJOAA4WYE4HADEBZCA77VP3AIFPJSJ3J2PPRDZCUQDYMMUA",
            "1974056442427612220017YE5ACUEUWVZQWDPCWLRNKPNZYINVK4AIVANZ5XTJOF4QGO6QMEKZG25MR66MHE2C5QDMN6JCNZPDSUKS3GLU4WCYIDBGXJ6W4PDILJXGIWL73NOYOOIQPMNAMHXS36AQ",
            "197405644242771222001V7B3FJGOT44F4PTYBEUCA4BRGIMD4SD3FFXDWWG3EKT4JYINO256QAFBARJUFW443WP56VU2GJSR5RP4IJPPQF3DLAPXVUNPWVLT6DQLIS4J76KDH5745JOV6NMHQHLQQ",
            "197405644242841222001FG6I26MLPZFMTOCE7E66Z5OB4MKOE5XJRUKFFTKGXZI24YJLTOATEN4CE656UACLL3VF35S7P4KFZQPTJQWOA5YVJY2B2ILSLKAQOKVP5VIPE2NL62NVQNJWH7YK4PIYI",
            "197405644242861222001OYAOKTNB6JISQZPKN25FI7FVCEVYFLV3WNC2BYQ32O4OPALJDBZP6CF3SYLLGL5TZCPPWEOKSUE3O7ABRWW7M2RMZUDWOKZ3C3CPZSM6U2P2IYUUUSQ6SG2HXVUTQB4GQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,Стерлитамак Город,,Аэродромная Улица,12 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "026832002",
                "ClientRegId": "010000004254",
                "FullName": "Стерлитамакский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "158.00",
        "FARegId": "FA-000000052216953",
        "F2RegId": "FB-000006564061604",
        "AlcCode": "0100000005410000037",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"БЕЛЕБЕЕВСКАЯ КЛАССИЧЕСКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198411874567140223001VGOGLRDEE2SZYLIX2QSLEC6C6UDWCT7ZWIKJ34XT7JSM37TWA2LSGJZEJB2KMH7Z6POE3ABT3FOGUPAZ7CMY7KW6VIAAXXBR3TGLO334337RHEA36UOEGV4FGUGA6IPZQ",
            "198411874567160223001N5GVA3YUOUCSNMJ3GWAOBB5EJY3QJEKGZ4GZA4CDIH3QOSKBUXZDQKPPSACA3PF4HHQHG6KCDMBV6OSERIVFSHC2E4GENQEWBPHKXGFHNLRVIJ7ZG6D5GNB6ROPRIX75A",
            "198411874567200223001HX5QTHV4MNWI7P6WIWWCYAVCMY2SMS7Q56TJXU455M6YTGTR2TBRGYVVOKCYZLH3S7UAM3JOHZJ3ZHAI6BHY6WFOOJH5AJNOLTEZ2LYXQXDWMTT5CMOAFNT4TF2PZRE3Q",
            "1984118745672102230013M3BLPHA767VVOMPGTOHRVXQUQHZRYGW7BLTMONWJVOFXAVEYP5RKFLEJY3ANM5YVMKWKLXVWEARTODGK5GBQWX7W25GAV4VFW3YL4KIA5Q7QMX3LSBEQCUGXKOIEZDDA",
            "1984118745673202230012DDM6C3NVKY53AINFK5IYIVJ443NAHDDP4A5324VIEAISMHZQZS3PUDNXFZ46E7RSQ5HHW24NPIDHRLEF6TXJ2PS6QZMA6VRS5QGPW6IA57VDMIDPRPKHHKFZ7CQD2M7A",
            "198411874567330223001CEDA7S3PBS53A3QZEC5YVHLGGMKFLPAUGHGPFHSODH7KUAEFVTB3RNEAZOU3MK7AS7YETZRS3J53XDYRMPKP6MS5FCHUEAJKKG44YO6WX57GRX7RGIQA7UJ53WGL4B25I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "156.00",
        "FARegId": "FA-000000052272620",
        "F2RegId": "FB-000006564061605",
        "AlcCode": "0100000005450000008",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЧЕСТНАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198412528556200323001WTSOT5MJ237MLGWFUMZJWRGL3UDBUXOK7TWFHZOFOBF6MFXRNWIZRG5IV5HEX2SW7FPKVTLVSPYW6IAF5HST3XWIYBI45HDABAGB6U2CEP2PO2E6CLPK766BKNEOYOBBA",
            "198412528556220323001T4WWTIFK6LIQS5MMTLSN3S33HUTCTD2672NS2EFUX32XURJGSH3LXAHSOT5YFS75UGNQCNWFHZDSL6KRV6QBY4BGIGPEF7QWYBZGFBX7DUZ2LWHKT3CLG4SIWNJTQUZTA",
            "1984125285562303230014WGHQB2T2HJZT5ICRK2R6CQVLYPHBEI7CYNI37CJ2IDHW6UW5VD2HC3XGZBPSA3PHWJ3D3GNB3Z7MW6A7ECVBZ6JFB66EYC47N5DI3BZDCCLZTV5WIPW6767LPZTU6ECA",
            "198412528556240323001ML6TKI54SW2T7VYVDCWN3BJ5TMAPN5E52OP3LMYADQ7WNUUHT52F6XO7HH6BQVCHR4IYVMGIQJQZEJ5UVNVXZ7WCTAOGNYZCJ56AFV4VGHTRGNYMC5A7DS6FW7UFFN4BA",
            "198412528556250323001MHGXJAUVI2NGNBTSOR5AOXREEATQHKVPVXBETEZ4TVAK2653M5VKVD2SFXD5N37QWV6NHGDWZ36NZFG25SXXZFHNZFUBRPBYHYK2MPUNFFOFLFSIKENAY3FMCYPJMUWUA",
            "198412528556270323001YDRHACHORDA5JDWFZXN6PMQ43MQ4HDR3PPXPXMD5FPVOADXYHN3FLAZN2YKSIXORJOXUCUG2LVNGAOQIYLKDST6ROP3NEQICU4GBVKJKV6ZHM4AWY6S26NHN57XUM6ZII",
            "198412528556280323001UVVUJFJGSLIMR4WUXP2ANGUWEMHV2KEAO2TTIWU45ASIYWUOTUJUR4JGFKBEJN5P434WPY6VJPOF3HTCNBRQGDDCCUH4F3HEINZYWEXSSJET7FTCUP5PLGLA2UMTZXYIA",
            "198412528556290323001MPW2JUU6VOKZ6MAU2UMTUUHP7EOS7F53VR2THWX3LCPWW7SRY7U2J44RYK5AV26QK6POZAI7G6QYFDPHM6NGWQ7Z7OHK2X4AQPNSSJEITIXYKEM2ZRQUBBPQGNNE2PDZA",
            "198412528556300323001DLWDIMDJPCVQNHXFUNPOGQX7TEQKAVY44LBO4EQ6PW3ZJXJSWQUQEHLZH2TBSTK6PBKBMRROPAYN6WLZV3QKZKVDN2TCDDDFVGVMZ7ULPZXNSNSYMYF3NFHNNNPWUEXDY",
            "198412528556310323001APN4YNDBEG5RV5HXGNXPH2WKJUICHT6MLAG4ZPS3A3TEMQGCOU3BNCZCQCRGDP2STBSCMHP5VANNXI4GCYND7LZO3Z3TCUL6KZJEHYPQI5HSKZA6QGX3LGWYWYWVKB3EA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "158.00",
        "FARegId": "FA-000000051741666",
        "F2RegId": "FB-000006564061606",
        "AlcCode": "0100000005410000040",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"БЕЛЕБЕЕВСКАЯ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "1984108119856501230013Z3VANG774TCGDUSUL7RXO7TYEB2LHB5AMPCVROZUT5UT6GFQSH5TEZGCBNZP2OMVEMR3U2WLOMIPWGZ3BY2TCE2DSHTZOYBEDC3LWCFKXRWGFFTWFAU7RLLBV3XH34II",
            "198410811985660123001P2QA355FCVRPLFHLO4T5GW6Y54SIUNHGDZOBEQCDH3ABUUZ2WINMPAVQ37HLZ3I4WDXIKHVWJGCU3ICYIL3HTWY3RAQUSZXGBYHTEPU3SDXX5YZSOAZFRGVCQFR6NRKCY",
            "19841081198569012300136MSO5TFDIHPUGIECEZPU2IZHA6AFCT42I7MMM6QNNYTJSRZNDTSZROFPUCLD65S6K52VW23RT4XG7PL5NTFNJ6LATMFD6VPVKWKE7JGQMLBCTRUUBXHZ5JLCXRWKOSCA",
            "198410811985700123001IHKUI2AD6R47TSRKTMXP7RA3CEVK4B4SLUMA6SQVDLQMNKZPVKIZTMCCLXCJMDA6R7KGKVJ67M3LNDZTD5IEDUO376JWBUI43W4OHC2LDELPLEQTPEF7PYLUODPVOJWRI",
            "198410811985710123001QND6XXSTW4UDIQVVD7YK53UJPQ25C5QZMCY3FZWN6XEVJH46ECKVTZXMG2PAS26TU4IPFSXWYFSJLDUEIUJ3DHJIO476JLD2Y6HSBDEXDF3QWAQ4BU43TSO553J2L3PYA",
            "198410811985720123001QDEYYC7SKCFZYGX7L27PT3EEUAH5PONVQBR237OJHS6HJUU632V6DRBRHW4FGBHQVWSOPMMPA4CEYXIAH7NR5YERHLYAMEFCBQ5XFNKZAEUGU6735HPKMKMVQBSBZ55TQ",
            "198410811985760123001U56TI4FUKVI6N2WRDAK464WZPA5CWYNP25ZEKCJ2H5MYGICYXEBVXNWLBZGW7JZCK46XKLRBUH7LFWLYOVWFIPPSBTPE3FIDEYVOH4ESF7JFFKGMSNIF6FHRPNTKZAJ6A",
            "198410811985770123001Q34FG64Y6YJEZWUTKKKQV4OB2QSXAJPZK3OYQX3LBAXDZEC6HF2CKZPYYOYK73CQXJMYWOBW3RTLBM2CNRNDQQYE5CDFSAU6TBXF7LRSZGAXGSYWCH2THRJM2ZCWRAYNQ",
            "198410811985780123001JLPC4LKJJFK3JKTYBPWTKJJXBQOGAWBDXAMRRQXQLTCZHIEAJ7WPYDEL2LZH7RYRAGO56XMUXQJCGIYTY3O5J2UL4X7EZ3ES6Z6ZEVRJXMYI7EW6OR234D5ROAGM2CYXI",
            "198410811985820123001NPBBEBNFUI53W4ZGOIWW2G2O4YSXBIDHWPDULAKVKLMS57YYQR27V4QQNFZ5ARW6VTFVL5MMY3WDLB2ZJOFYE6UWEGCMGUSTHX37AK66NEID6OKCAR7JL6IZFA7MYIYCQ",
            "1984108119858301230013I6TYFPFAM72NJ2JDTBHO2CENU5243FT3VJRZAZFS2K2Y75JRZBWF3B52YAPK4JC4KIRDVL353FB4ZA7F4NSFFCOMKVMWQKHFP7FZE4O7FD3CX34NODQFXRMTXMTDHOQI",
            "198410811985950123001244DCDPBIUXZ2UZGCLX6TQ773IMJCYLX7IAN65T5M6YI3AG7S4ANMSTLE63XS5WFWM452GLTWILCXQAZCSUJ5UAGTG5ZZUNJHWSEKS56V5RHHHPBBUP4RS2VTDFJRVDMI",
            "198410811985990123001OZTODDUJ775TNUVSFPGSPU35LIMFG2MBTWKZIJMO6ZPGHCKMCD7VINFV34LJWRN6JYP4ZHY4KZ5D7MWLADR2P32O24H3O4PKICX67FHSF4CWL5SXL6FZL3J5NLBZUNIRY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 13
    },
    {
        "price": "161.00",
        "FARegId": "FA-000000051965568",
        "F2RegId": "FB-000006564061607",
        "AlcCode": "0300006342850000032",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "19841130376685022300164L24JIHFPJAJ4OE7ZFS2XPBVU4HVWMZSGR3YR4JCYAH35JS6RMYBB65M45FHRNVMJY6VLLP7PB2BX5VA3GXRSPM4NA7PX5NU2FOGI6WJ473C5IH5NCLVTGILZ3LMZYXQ",
            "198411303766860223001M7XBS7X7DN2RFS4I62VIQWLE4II2ZVXLLJWH2R2MN23CXOGPEE4BEHJWWHQZDHAUJ7J5G337G22KVTE5EK6BR7ILYYE7EBTBWQLEWACUBNYOBPG5KH753ZPOINWJDD5QY",
            "198411303766880223001FP6VXN3XNFXSQDDZA5I2PHUUT4GMUQQ4LVNUWQSYKP4DHSYXLZCKJW3ZLUJM2YBV3SZJKIUISFR5V67XI73NKNHJZVDFNC6G6WYIQI2R54SSA3QTK3PSFK6QQ73AATXPY",
            "198411303766890223001Q5ZGEJ2VGFQSC7NLK4LCWFCMJMD3AKQ7F4TQ5U62YMYA2FZ7QP6JZWW6WT55V3MUT2C47TSFQI3BXK4QSJINZN34N6KLJTXJBP6BGDKTRSAPDH3MK2P45RRA4ZBG4C33I",
            "198411303766910223001B22QQSWOHBT4AZBL2KIWZPIGEIZRYFRZSPSQ6RSUXHHI7A37OJGJY5SF7ISIWEK2WWA3D2YQKBDEC4UNJFB32LUKTUN52BPOSRBWXTKQYNKU67DWSFXZIDFKGYCPXT7HA",
            "198411303766940223001ESN6H2U6N7M7R2JHJ7UV5WOWNUR4WHKIM6VS5KX2WZ6QCVCWVW4XG6G7ZBVHFCMWBBXMRNNHBDOPQZIP4YJHMGSOONKQG3M2IQCKZAKWKYTZVPYEK7RXBZPIJI4LAL4OA",
            "198411303767010223001CBR4HH43W4LJJCL5NGEPMJDFMIZIHXB7OMU244GGWFHLOD42Q447VCDASQ3TGOHMIFK7PLCMDLRNOI3QEFDPDRRMIUEYMK42K2VOXNR3HH7EZ5DB2UQXPUFZFSAKKWUQA",
            "198411303767460223001VJYQNDQNUBW7ABP3NHFDJMHZBUXECYVB5LKQDPCJKEIIKFBH3LX3M75KMKFX7U4OXM4X3XQQW4DS3VX3KOELH5CGFPC4SJRR6UYZ4EWU4433I2IIQM5YBIT3AQC35ZQVY",
            "198411303767470223001FLXZC3JMO4MIF2JZV77MHXX5TQLXWPVT7BUBVPYGDN2GRUUADEO3ZDNQL5UQTPBQV6WUAXI4442QQKUDA2QDVCMKQYNVAJIWBDHVAG76X3K54MN4ERBPNCTTL7NWRC5KA",
            "198411303767480223001O5VKYIM3B5JCSJ5DHCARFCHIZQJKMCJDIMEJECENIBD324RZGWOSR5BB6CMJW574LDLYSHYS4UGDGJEWRLCDLHFEL5SKLUPHU5KGBKNG3CCGCCOV54FA6IWUFKATSF5TY",
            "198411303767710223001KUOYWZYE7OXRHRLN7MAUPWQZ543ZUPEJR7MKAR75FKDIXVGEN7URNAZSCO2RA2LPTNLNBRKBA6YLA4IFKBRPABJ5I2K63GRTHJZZT5GPCVUJWTRLNM7HONRHSKQOIWA6Y",
            "1984113040396602230017IISBGIUYXXBS5PILBIF4ZLTCQELNSBA53J5SC7YH2XTZWUY4DBEQLYNGN2BH2OLNVQIEEPUNR6N3YSQOFFXENSAJ4BA7DWRMWQD6IJXD6EBDTSI4XSFWVAM5D5LHCLVI",
            "198411304044260223001EAIGQUYRKRN7KGRBUW7DBUKEN42RV2EIW3RV6SJTK5XJHH7FLQMGGH2BTJ7QBFCZHJBVUFVD6YVUHBYDPSTNZEYUP4R3ODSKFAR4BBXIIZ644K4KX4LBYASPJGWDKTTFQ",
            "1984113040442902230017PDJMC6MT6JGZMYUAEA7XADHSUBDN5646SR2NFAX7ARFBVWENDLITCFMUAFUYCNLXAJELU5T7HZNU5H6CI37K4PTYTATUWCJZNQMWP6U2NY3KDMFD4YFSZZI5R6EFIYQY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 14
    },
    {
        "price": "161.00",
        "FARegId": "FA-000000051929800",
        "F2RegId": "FB-000006564061608",
        "AlcCode": "0100000005450000056",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\\"",
        "ShortName": null,
        "marks": [
            "198410690049450123001CXFVRQ6HMCMJKZI4E2D3KFDMBUKRKY3ADBN22CZZYQUH56UY5XI52UIKSAFQER6I7OXPLTWGF5IOFAVLKRINYRH2KB5PW6VTDXQPWGLIH2XFNIE57MN4FYT46VWUPUGPY",
            "198410690049560123001IOQI6XX542C6OUEY6WHDPFJR5QDYDGGI5IK6SOKJOU2W2QAVDOO6ULRELGJULBBGAEABMRY27ODT77O7Q6LIOKOAG2OMHZW3JFK7LLJETZT7OGAAMQZIP5UMYCAVIQZAQ",
            "198410690049580123001VE4ZQ4YAV6V45ZXPEXFUP23C7QUITZDHDFSWG2TXXPFZNH3FI75EMWPFQ4QODWOCZJVIYR43FMGBRLY4G5BDAG54I64LA2T2TK4HSSS52UERIYI4KDZFEQLGFRQCBVUDI",
            "198410690049650123001ZYCXO32W723SBE56HZ3XVIALZMIX7CAAYCQC74VCNRO5HCIHGXYZKG72OLIIKJUL2MCD5GLFN2SAZSBEBBIVUCCVSWHAEYX6X4ZUKCENCCEZOA7W5P2VOMDNUCNXXYCYI",
            "198410690049660123001RWZ6FZG5VLRUEQSLFIWHU5Y5FMO3IM3JPA2UMIGC2ZIXCX5K6CQFRLBHG24BLAQYKL4MS267DYTCKKEWKBA6V6OQLY6QN3TSZYS6434KY3SFULWJEZBKEELDZRAHTZHSQ",
            "198410690049000123001OBYYRGAPYJNHIY46XHHPMTAKFYSVHZTGJVLSZATGLMPDQDAHEP333I5M4TQAJWYG4IGHH6SIV7IPQUZTPBNMPKDDQEINR7QTFPFDH6WRO6S536REI5CJYKK5PHR2KLMXA",
            "198410690049070123001TCXTIPM4OXRN3EO6I3EGKMDITYXW3JHLQ2IZRVDHDGBQ2QVJ5PZM6PXSGWNCAOQMKFUPDUWBJWFTN4URXISSZMIEI55BUWDCBDBXSN65O6ABKB2O67FFEA4LARIDCFSNQ",
            "198410690049080123001HJBPOM6OHSNWEKEEVMGLF44XPYCNYUJFB6BZ7Y52PGOCRZ5IMF3W6V3R46ECXCKCTDBZUJ4CEMTQU5ZDDDCZOI4B3DLC2GDTGBBJX2IVGK4MBX2USWURPHYWE52UTD67Y",
            "198410690049150123001M6DYNVI4YEJMEFATQLWNJFATRM4M63EVWXZGGRUEAQXRQHX3VS536KHJUNIHMPMCQIH6O2YZNOISFTQJHLB7Y6AX5DZ3ILL4DZPXI3P3RX3YCMN5LP3FL6RUFN5VKODPY",
            "1984106900491701230012TRY3KU2NGDJI5MZUHF5F72LRQSGUF66SXXRERVMIVB3N4BBH5DVRFVE5T2GTJOTCBCYR47QCY3CLXQHXMGDPTSUZXCFIJHRCDVYDDOY3IPU2D3B6ZLNLOWYSHTC2UHSY",
            "198410690049250123001LVTN42DQJNPLJWZQSWGIUCI7WU5Q4Y7CYDZE63DTGHXJQHUEMSASISUCN5TFZTWWUYFR54OLZP7I2TBNITV6E2V4B7A7H2ATGLIAU2PHHHKRPAMKKPSGYS6AZUT4RZOYQ",
            "198410690049270123001BD7RBEVODQSQ5UKKEGPF6X4H4MMCEGH2FP6YQPV4QMKA52ESL7AJEYHMC4LTZWE7JUITBSZKQXOVBX355V3TBHSEJEYQYVLKNTQRBDEJCVUGYSIBWGOTVLGRMO35745JI",
            "1984106900493901230014JAHCYZBQPABMMEXBIIF7CVV54JUNELX2BD2VPQGIU7ZV4LQBQEJWQXCALR7YPVJ76RZP4QGHWBRYVDRFCAYOQ2QTWK6N44EAKMEWWI3J67QUDKJTP7O6CECQKUMQQC7I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 13
    },
    {
        "price": "158.00",
        "FARegId": "FA-000000052007156",
        "F2RegId": "FB-000006564061609",
        "AlcCode": "0100000005410000017",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"БЕЛЕБЕЕВСКАЯ ПЕРЦОВАЯ\\\"",
        "ShortName": null,
        "marks": [
            "198410831593120123001YW2C3B5NSISPQSB7PAMAQEZFQYBQUFAB5CAYLJ6P6GPETGPCCROHWPYFQYWFFIA7DZ77YW6BUWNQKXCATUR327PJDOENU4LGKJCSKAGAG7CPHDWT6YA7IZQS7L6RDB55Q",
            "198410831593130123001VCVJ35HZNOZKBCWSAHMBAPR3T4Z5KEKBUTFHZTRDL6X7OXM2FBTB6WXH4VN7ZHOYS7ASMSKWOKXXZRCFHS2ZVLAE6ZMH6EVVYCTSXEE2DHCZ7WPOOS6C2GBNY5EOUXSXA",
            "198410831593170123001VTEOX7YRV5PA5ES6C4QE4PJUGQ7ROZCEKMCUDZCNM5XEO2OBSG72ID2IFSKADQIGSC7W5ZSKW7HE3U57Q4NPF5UMQYMVMSRRFWJKZLXLIVQT4SHRGWGN7JJRIQBURXLCA",
            "198410831593180123001MHH74J2JKL3OLKLXFZM35E4TA4PCXDPVVQW4XPGTNMM6L3536QHIENOYW2OA7XK3FZSD7VJ6TDWHEZ5OKDVX2CLX3ULI75RXMBE656AGR3M73B6IWSNV5SKJHHDVCC3LQ",
            "1984108315931901230014VJ6FWH5FGH5XTPVOKI7JZPMJY56CNBXXRPYFAYWERDXZNQCVWDQW7CQB5TJCZERAEXXOWST4SFNTIVEHE3TRPO2FRQ3CY4KITQOHJ4OLIR43ATXCN54RWLO4X7XRCWYY",
            "198410831593200123001VBP5OWSMVIAUHK2PNXFM36Z5O4QD52RAKU73ERKH4DGSKFPETIQZMI5KT2UIO6O34HU6MV57XSRAGHQPSLJUJXLNOAIKFSUG4DWKZJ4SWU4JOI6VHIXK3K7FM2UBJOHRA",
            "198410831593350123001R4CQ7T4CAUZQF7CCOJ4NPHVOSYCMDZHBMCJGQ3VZJ4SN675ZYKW2F6R72RUWBEYZ22HCKVLBDRDW7LYB57G6E36QHV5MICCLFHZJAJK76U7P7DWCJX6J436SB4Z6JT7WQ",
            "198410831593390123001LH2SBTUTYKOZQT4EBV46A2QIU4VX5ET3OBSWCZVZLRPL65ROOUHF36GEJKPQOHTNARYDZQKK3IDKP3H5LKRL6EV2S5LTE6QSUYQOI3WHD76PGG3Y4HA2OTTKYFXRNGUMA",
            "198410831593430123001Z2H6GZPBJFBW635YAPW3HDIROEV6KQQOI57T4DVCS56ARCXVNGJJ4DCNRQYVXBULP3AE53M5FNH6OZNG4PY7FCS7TSQF2KY6WW7R5ZTJGGNBPBBJOEGOM2EPETBN532KA",
            "198410831593490123001AHKVWQ2GCOBQIEVKOCLBH5RRTQSYDIYR7HRZKN6I5S4233OSYUFGC7OYGFXM6JGGQPKLGXICAON6TNW3NYL47VBH6CGGSX6GHHPTDDKOAQMDCMK4MAFHVO6LKIHZ33HXA",
            "198410831593500123001OM37UCJH2TM43D2OACQTZIFXKMGHKD7IEDQKAIG6AETGI76YXN3Y3WSTF44JOQ3OSYTPGKJOZQF7RRN7ZVLCI7WVJUYMYTM6SUHCJEUBF2SUR3AP22YNDBCFOPQLLTM5I",
            "198410831593610123001TBFUYBVRJTULI3LD5NQGRFJNWYH5CUJEJ56H5VNEP2TXALI4U6XYSB4RBUPUWIGVINP7MHBT3JF34CMNQUJEC4HMWAT5CXTEHSSTDTDICS5FIPULR72ZXOI52YNJVW5NA",
            "198410831593620123001A7DQCSOCEA2V7N6LVP4HGMVPJYCO7M7PEURQFTAMSYMZP6ICZG6QMHHHBZPFPEUAK5IJ7YFV3Y3OMV7OIUSARHYT2WOMELCNJKUTAY677PEB6KMZBYED3RYWHHVC37OFQ",
            "198410831593660123001524M2HNNJ2JGUBZWIJR4KQ6CGQDKRGPJHMGUB4GSLGQJ7AJUNFV5U7JZUHC5UXOVH37TMD4XIC4OWRVPXN3XQI6TQY743PB2DDVDP6UHAEXCW7QFYUEV5G6Z2J6MVIO5A",
            "198410831593670123001XJYIHVF5N5JGHXQBHWAGDBV2LY2WK24RTVE7G7MJR34LXH5ZRB7GPMO6GHQXUCUKZ75MCLFDLEVNUGQTVJYTJRYCLAU5QKFIRN32VM2BUFCLPO33RDQ5ODMF2JPOVHHNY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 15
    },
    {
        "price": "229.00",
        "FARegId": "FA-000000051423235",
        "F2RegId": "FB-000006564061610",
        "AlcCode": "0100000005410000055",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\\"",
        "ShortName": null,
        "marks": [
            "187416257489901222001FOCJ4AY2NNRIUE37DMSOWZ33YUIDQDYSTHHMCMZVXNNZFEBMZOADURESWL5CJMSPLORNWTYLT7IYKIYGD2Q6SFM5TEIHBKELY6XYEGU2BBKVGG5OJUNM2U44BRBWILFHA",
            "187416257493281222001CZL6DBPLX76GDSHSYXWDX4KRVU4AHNQJKK6FOAJ3J4PG742RE5XQH5R7F4BB3LBFH4NL7GWE7QFB5RJ4FRTPNT7ZDSSTTH7FKJRHONOXGOC2HQ62WDXCU66WPJ62T2SYQ",
            "187416257493321222001TPIG3WW6XBHYML5JLFWQKBKTFM6L6TANNPQ3J7JSUIGJH6VMB3UV2YYY253M3H43ONOFTOXY3HQFVKSH2HFLLWUY7OHHHYUDJ42BKBBLFNCNACK2JGIDLDVY7W5B5Y7XY",
            "187416257493331222001FHDYUUZTZPYJ624BRFZZP2E74YJAQZKFGCNJNJCHO44GHTRQU74AHAGXFBCB44OQHHLSQMXJ2GGDY6J2I6EVMAZDDQHK3MYEYOSVO224NOTDG2KLB4IPWBMYZ5BQV3SQQ",
            "187416257493351222001P2BVM2KFH52W2XTM6E52QQF5JQE7DHYKKJ4FIWPW3SDWWEDLPRQYXNIO3H536OZJCNODWPOPUUY5HZNEVKG5HVBUNISQMR52RHZMJ4DKIX76NL5XDLFZ5GYQXU3RKKIVQ",
            "187416257493371222001RTCMWFDVVLVWSUCTTMDNG7XAP4WHJUH5BFVVBXZVO4MPUOPPQFERSHQ4V3ZBOSINDT5JB6DTJN6SBD62PYWPAWSDIZZFK75E2P37BS7GXZDKBZDW3MK7CS4R4CEAVTHPI",
            "187416257493431222001MPMX4RPW64NIN2SA7MDDXF5XH4KXVWF424VCAUS6JHSI54TFPG5T7VMD7LWQVQMKFFPZ4LA22K2HNEVPMWOXHDRHAN2TKBCNRLHKVOKCQXHQ52HOOSKAZQ45SV5IB4XAY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "307.00",
        "FARegId": "FA-000000052229157",
        "F2RegId": "FB-000006564061611",
        "AlcCode": "0300006342850000030",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "187422327017970823001KJYQNHP5SAU4ZKO3LWCGGYPKU44NVSSYGF6W24CRY63COSFC663OLAWWGKRFUVXVNJIMTB5HLUWC4XS3DC7WS4F6VPZQH5SUM6ILYD2MDJNRDNHFTR4TPSX5RCQLDQFCA",
            "187422327017980823001FJXD3O2YKC5YZJWULOGNNNSEN4AF3CM57LSRNRUTRY2YCUZCQH4E4I6ESJDXXEHXBKD2HJBT4EJ2PTHUG2JDRDAPUMWHVESHWPJVNLVA6CB4GYHKUMCMCEMXGSJWZDJSA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "307.00",
        "FARegId": "FA-000000051768113",
        "F2RegId": "FB-000006564061612",
        "AlcCode": "0100000005450000066",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ АЛЬФА\\\"",
        "ShortName": null,
        "marks": [
            "187420016917300223001WLVREZUKHR753Q5R7K4YSQH2WUY3MLNAYJQHC2ROWVFMHDXFSXCQJFMA3NWRD3PAC2MSRT3S23MHH2HCEOUUH5NQG7TQ2U6BOYH2ART3TBW2P42AINP6CXNWJV2HNHPEY",
            "1874200169184502230012SP6Y6GZFG777DZ2ENKIT6FA7YPEJWNMV5CYS3OWFDJWWX35RBNK2MNU7Y25OHGMPWZKYD373PMTB45VZOFMUXE5373PSA5HUDJBNGPJICJUC44HO7XNYLSNAACCSGQ5Y",
            "18742001691849022300166665V6V7OWFLLJBJSLNDEL5AAJHNW5IYCINAA5N6DOMTB5EBX6R4UCDPGEBWKPAFKYIULGHGMSFA6SD4X433YCKYR56TCBATL2OEW7JLF2M3DGMQYMCUUA32USZXKP3Q",
            "187420016918530223001ISHX7MUKYRYBQ3XLMKSBPOJKLAFZW6BZDLGFKIUGFROQLFK6Y3DVFSCK774HEMGRN2UIORNQ5UA3Y6NRSECESLUZDOHHEP3BZDWBSVE7CLKEFBPCVB2ZOXPT5JAYQMQYI",
            "1874200169185802230016Q4T446JFE6C35GO4US4OO5RKIDWVWXYVRHR7VDU63KJG6YS3TUMG6E7X7HDJIMA5LALRDBF7SOHHBWVAQKBMJBWCWN4B4KSPDPQ6Z6JGQRZVQ63CV2V5YVDOGXOVDKZQ",
            "187420016918590223001RXJCHPN32CIH4JXBSGITRCNDBY7D4DLPW3O6YPEWH4DVUWL6EEYHGIFX7LVQQ2R2MATFEWBRFB2XF5XXBERFQ2P2H77Q7LFDRT4SOO456YDK3VPPMBUL37XMDUNCJYN4I",
            "187420016918630223001EJ4QLT662BFK3PWR6SVQL3KCHEDSJ56ECQERHJT5UF4CYD6WXIJPIVGLEFY4E4IVSUM6VQJO7PCL5CWVBMDYNH5YMGCGUDOBJMHHBDZ56IGBDNEISM4FWTVII4MKTQU2Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Бирский Район,Бирск Город,,Мира Улица,33 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025745001",
                "ClientRegId": "010000000545",
                "FullName": "Бирский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "307.00",
        "FARegId": "FA-000000051988595",
        "F2RegId": "FB-000006564061613",
        "AlcCode": "0300006342850000034",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ КЛАССИЧЕСКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187421703088440823001TKBQ5FOOSAIM6MYNZVCD6ZHPLMNG5OSUKCPWCIOEJB7E5JRMYWZDHKJ5LY6ECAIDWUMEZEH75N5TZY3QDJ4PVPPG3GYVFS6YHGYCJH2C67IATS5OASWCLND4ARQYKHWMI",
            "1874217030884608230012SWNQGNXBSDSGXMVYRGSV3HNHI3ZGDEYT3I46XWICOKOORF4AQSJK5HMWMSVM3NDKO6M5GBT2RVZEAS2PIV4YJKXEJZABY3LDSHKSIGIH5JAST3XBXZ2VV2N55552I7FY",
            "187421703088620823001RHN2WQ3IOX6RVPCPOPTQYK3HHIPB37326SYGAMJTJXUC4HMRHBSRVRUILZNMOB25B5GE5NISZNWTDWP433LUWH4U6QZOLFVZ6RSJ3Q2KMNHUWEPHXVU57OMX5NHRNBMOQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "309.00",
        "FARegId": "FA-000000052265006",
        "F2RegId": "FB-000006564061614",
        "AlcCode": "0300006342850000056",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\\"",
        "ShortName": null,
        "marks": [
            "187422731404890923001P7XP53HKGKRDGGJSLFJMWARXTEJ6OGUU2PW66B4H7KA2P7HZPQKIUNEH5MOVD6QS2ZSBSPGRVR3N4SAVZG4GDNAXGGLT3O7JB72PW3LWWN55ZKDZM4AFZSZWXL3TQKQAQ",
            "1874227314049009230012YJ4ZODYVJO4CXLUVOVE5ZQVX4M6IBUVQSRMZE3VF7LPS6CK4UAGD72R6OIWAO55YHQEDZPMO66WB3Q4YEA7SCSRGUQ6KNU6TZNJC4IC6UNSDBJ6QQK67MW6HHLLEPAZY",
            "1874227314049109230013OZCJSPKJJNASVP54SDESSVBVAUM4ZLGIB4EPXRLR45ILLDXPOLXVBQZYFQIVELRIB4H6HBIPJYQQYUXUGEJ2S2CKCCCBO5KWTW3ARUD7RGGT3RNCBKBMNV5PLVTYMQPA",
            "1874227314049209230015B2VBEQMIFWHAO6HQ4OIYEK33YYF3XSYTGV2RJDLS5TBT4LRES3532FUWDJFVTKXXZRBIDHUNW3AN7RKTX7LJPU6SH37J2SEGSH4BF6WB4CU5HKILDSS7R32VEB7RWM6I",
            "187422731404970923001IN5ZBXHPVY452M65WPI5AYE7TYCQIC73ZC6W2PRZGZE3MIVQ537JE4XD5KRCGZDRNL2GZHJXUAKGL2EY4BH4PSXHXAAHQUOWYTPWBZXSS33Y3M4HNYGJONN7MM7WHS56A",
            "187422731404980923001TROXPIWNJH4VXLM65O3URC7MDQ7PAEHYGQKUDTVXEUET4VE4SWB2MK7FA4VSXGAJP2GKC2FNA427VLFGZPSZ6BH3AYEFCDPOAHKTQR53DKD3GHMA47FNVB2LLR4PL3RPQ",
            "1874227314049909230014JQIJLHPTRAEAHANCVFDRJOKDAKIPJQZAJUYDUXMXZVSFRAXGGLETOCNS3K7AP3FADPUYZAKSSYP63OLFJOOISSE4IC5FDYKPMIGMHVZOWIX6GNQYJBVIOJUOKB4XJ6KY",
            "187422731405000923001FCFLQGM5KIMVOUORVLZCXVQLVQQ7YYAKFR3U2UER3K64UND6N4ZMBENTKZWXEVLITELVBCXWZIBMMZB2QUUZ3ZT44PGBMPITPMPJRMLOINQ4SXR7X6JCKNOMIL4TI3MNQ",
            "187422731405010923001BZVAO3O72J4GBXRCQ6TFMYQZZ4CY2P4G7G7BHQSZEMZABXT4QGAU7FBPX4FPUBUCDTFJK7DF2M4JFF6TZ2NRZQ32KAZCLUAI4AMLIV4OGE576Q43LAPCFWLCPVZQQVCJQ",
            "187422731405060923001WCABNFZT7MR7EBERYB65WNWZXY4UFDKMTQW7W6RHX3AACRJ3IKZOX7O2KOQOT2CRDBM24X3BZSHQIKRWG6KCTCP3RBDTOK2PTYAYD6MW65Q2BTULNFUA6L6KWFICSHSRY",
            "187422731405090923001YUR6LVULIKXE27HJOM26XVMLEYPSETJASJJT2JXRMDLNTUPW22YJD2ODD57NGQLD7HHLLBT34YVTS7Q4WT3FME6DHJA64FLZXGNHIEHURJUW6DU7N7D4Z7XT2JXS6XNOY",
            "1874227314051009230016EFMPK2ZB2XKRTCGGKYNJBPNR4B5PHMTLFPOA5KVUNNJWWEEYNGTSIJEE633IBYRWUZHGKCMYJ34VKH554YN6NTBX5H3JZD3QONWX5LZUSCIIMP2Q4VLKNHPDP443P4FA",
            "187422731405110923001QONQXLWS5ZXT2KPZ3WAYR5NWLIALUJUZHYJRDMG4ESZ7CG2E7SCFSUBPVTJFEUJHJNH4JS7TKZC6N5SL64FEFAOKX3PLAD6JKYINISJFYNIMBAME6OZY6YF5VUJLWM4YA",
            "187422731405130923001NNXQCFOKKQMKXXHQ5H45VH2ZF42ETZAFWVKXBJ7B33WDDJV555C5ZWVEKN4BDNUXZJ3EW2LWHT4G6P2I2TS7VTD6M7EEQIXE4MGGL2LQXYRIOP4EZLMIUYO3P7J2XEU7I",
            "1874227314051409230014TOCNAFUZUFEG2V4VFAVWDTL6U6ZXPJZ3EGD3HQIETHTS3TLS7PJ7F7WRY2PCDDZBZJ5Y2JQVWIKG4RD42DQ47NEFST324DA226CWHU2SX7TU3PINPC633C3RMHEW3ZGA",
            "187422731405300923001UCTNJWTRJ7HVF66HGXRCRHMJGQLG42URZ34P7UJGZ3ORXJA7IYUZL3RAZVACDZMYMSVOF5VOCKCJNALYJFWE23P3JULHBHARTXHQN5HHZ52YDIXO6KOEFDXZPLVP5OKOA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 16
    },
    {
        "price": "314.00",
        "FARegId": "FA-000000052369779",
        "F2RegId": "FB-000006564061615",
        "AlcCode": "0100000005410000016",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"БЕЛЕБЕЕВСКАЯ ПЕРЦОВАЯ\\\"",
        "ShortName": null,
        "marks": [
            "1874233866666109230017E2NUJV24JMCD3HZPX6WFM2FRMKMQY5GPLWPBRJUIXEWAQJGB67TBYVRASDJ6NGDCL4PK6OIRTBBFEUR5QBKXJEF4P5JBUGY4GWQVZFGO7SBEFIDJGAIKITKHNO6V273Q",
            "187423386666620923001WGDIONJ42WKEUEOPUVDAPNTCMUMRDUBVVB4QHARPAR3CWX57L7P4YQFXTLAEG4VW2EBFIW5APP37QSJLUOM2DVBFZ2GKWR5SALQXIK43AIHTBKWJ3NZEVJ2LZXTRUTL6I",
            "1874233866666309230017IEV4DFRZZ4RQK2XNSMU4KOQWYTCBXWYRFAOPG6SEJ3PSCS7MGTIQ5KBBQBY27K3NZJOWJVDHKUKXRA2N3J4GVLW3LDHOV77PWXK3ELWXDYY5MAXEJCRXVNXKOKJMYBJQ",
            "187423386666640923001BDY773KTESMTKIJREOWT4VQFFYWFEDQF7IIJP4GB4COFF3EEQWT3QIR6U7NQZRYRHI7BPI5TJCY7T7UFQV6DYKGCZAM7XQVYHNCYFJ36BGAOKDHJV5GGC3F7732O2RHDA",
            "187423386666650923001JWUJQV3SCKSOW6JNOVKROSHN3MMZP24G4MBERFKNPLFA4FGDJ7Z4BFZ4JGBCZEAZWS3N2IY4ZMD62GWKNKAD2O6KRXEEDFNUQ4X5AD2CYCJM6FCWZ354XAMJFLORIASMA",
            "187423386666660923001EX2P27UXXYY6Y4FTY7TDCPBMXQN2TAKOVIVHRCBVHLX3JEZZ4A4KII4R7J6JXSKPAW7N4UCUTS3GD4VBOETYS52RVJDL4U2IFEEZSIZXQBVW4IILBC237B7DIJU3UZGEY",
            "187423386666670923001SSCWNQVQWNHCDIVPX6DNMLCN543CPI4TVDIFLSEKT5FGX3HI2W7Y6IHZIFRBXFB3OK32HBGH74P2QLSOKDFEJHFJULZXH4N5AW63I66TENW22D337J6FE3JEWVOSEARDI",
            "187423386666680923001IHV4EZTBEJCGXHR4TBXXOHUHUQWXUMHQNJRIBV3IYULHUTSOY5AKJKUDKQP7SV7JI4GEDNZM3PAFYU5YHGC7WEPSA4DE2OGZ73UXRSFALJ5KX3SZUHMTJDVMFVJW32IDY",
            "1874233866666909230015PG7SNT6QIB5LJ2BIZ5PEUGHIMRTZO2HDRTKYRG7J4WEO775ZHITA6KQM5WKPTOJS6R3HPCI6ZUAACELSUIC6FIOUQFWD3ZBO5V5WOZNXS4QPZAUD4T7VVCPHURE347JA",
            "187423386666700923001NJ6LHN4UAZJO2ZJXQGPZMRGNIMKW3YNIRE2V6UA62XPDBOCABJH4LAGTRNTRW6Z6VQAYYETGH3Z3JDDUBCCMKZ3KXGSXDRZC3FO4ZG6LDTE7XBJACOCHFEH5DFK3O4YNI",
            "1874233866667109230014QMUINAJVLQYIUPY76ZQCRMVLM2HJGXTSRMNZ4TF5HNWMVHWZ2LVRGFPWXTYG6AVO4RMCIPORP73RIUY5NLKWWD5DTQ5SCMXP3XGOGAPV73TXHMKH7POVMRV2HFASDG5Q",
            "187423386666720923001NTQRKCZ7ZIPNSQI2XIQVZEPEB4Q4VM4W6NMAJMDZPFPU2BEFM4YXVL4KOYJJ6MQMAROVTK2ZOSUDECXPM5US2WZGC24FL4POQQ42LE6ITHYK5WDAZR3PKJTSXMEVTHAKI",
            "187423386666730923001KYTS4L3GUTDXCWLFTRJ2IKR23EAYXRCLC5ABPHEWMQZ5DNSVB2NFMGELQBYSJ3WBQ4FCW66CUESBLQSLMTNIPCCXDCOIXGN5JM5NILMEDOKU27PHEL5663N6LJZUMIMBA",
            "187423386666740923001Q2M65DACTVKA5SCJBG3OXRIKAIFH6QQLX2C74KXARXUCB3T4IQV4YYEKJYLYZLWYKITP52OJY5E5QETM4QWQLK63RCT5U5B3NGW5OF724JLEOMW6M3M5EMPA43YUMJFDA",
            "187423386666750923001PR43L7VM4OSEILE6VW5FEQ7YUEUOUTUFX27VCX7HLLKTUCUBYPQNT7TDF57AEW3SMJ4VYA5RLUJDAP3BTN7O62M2RI3DNH25CXMUNLKS7U55FGQB4EAUXDDEJTPT5236I",
            "187423386666760923001DA6HZCZBF33WYZUKNC73JTODXYKQQWUJQLTWTCTLHKOR2JJV5KJZZ5YJXZNVO7GI2IGVDZ5RHRFP7DPUP2YD3R3YGGFHOYDCUFVUGO3DUVGQHZ2DR5VGTREHSPFT7AUZI",
            "1874233866667709230016B3CGPHL7XZ7Y4DLJZXCZFK7RISUFRJAZXSPS7H5QFU4TWXAQIEEGOF4V4EMVOYSHNU7UXRQCPEU3PFV7VHPZ33KKLR5UF4BZXYY2JC57M7VE44VBNICUFUCVVRZDXD2I",
            "187423386666780923001NI7TGBGQ6PVF2XRMW6HKMJES2I4QNLM4QDXZWUGLMXBJAA5WPMHZTEJP4OP3UF4PMYPJNKL2X755M36JNGN6XRAATGVD2ZKV367PEQNGDVXNSOWVR2QMUWJODBCNGMGDI",
            "187423386666790923001PPX2AKLL7VC7JJEB5CJB6SPGAYR7SAL4YNDFEISUCYKAYH2WZ5ZE7XGLE3TLMNWTNX7B5243JQ7OQQNDYUZDFASNW7VBJZO2SEHVAQRKU5XKAII46OWBDIPHYK47T6I6I",
            "187423386666800923001XBA3JJSWCQX22UKS75BITM37TIHTHRDF5YBWTEWXUO54KYUAX7IAUXEU2SBFL5J7V4ULDL436TJ77HFPNEWAXXX525VPCKTFEV6HLESFS3MR4LHAABEI6RPYORHUBSCYQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,Белебеевский Район,Белебей Город,,Чапаева Улица,36 Дом  ,",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "025545002",
                "ClientRegId": "010000000541",
                "FullName": "Белебеевский филиал АО \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 20
    },
    {
        "price": "130.00",
        "FARegId": "FA-000000052299521",
        "F2RegId": "FB-000006564061616",
        "AlcCode": "0100000010250000055",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «РОДНАЯ ДУБРАВА»",
        "ShortName": null,
        "marks": [
            "198412139693190323001Q5DKTVWVKBPP55SSXIKOSWY3LMHSKA7ENU56FRM5NXUDEFV7CBLDCEFA3UMXVY4X7ST3PW2HL7UEASR5WJPD56GBCJ5C7FW6Y3JJC3FNM6RMS5AVTDF2JDJUROTNRER2Q",
            "198412139693200323001WAFDWL7EFDOS3TCGVLIVCMFTAY2LIDH4WME5VDVRDAGPKL353KNETXROA3MKOEFPGJ4SZGY7T3WKV2GX7BZJFJTR3C73LTQHS4D573KOJMHLOYGUURODPJJLN6PO5GICA",
            "198412139693250323001FZBKNEMMSLNKI3N7GP6NAFLITYOZ4IKU3OUNQQR3EPII7NZTOIW5TZY7IK3OQYDA74MR2W2WDK4Z7SH34GCJBSBEXY47UA7UZAJW7WL6AZ6253JFABVUGARWIFBVSYOSQ",
            "198412139693270323001P3DY5PWH4NLPPSN4A5773R2AKEMQQX32IS7ECY555VJNUJJFGEYFXP7ZGTDVBLBA6EGPLHBXCVFZN3Z5WVRG56N3VUHTPHEBKP5XC3IUATOE7BASKRZDKJEMJZJPE4H5Y",
            "198412139693310323001ZRF47JOT5EIIA4PAGCWGXQ5QYMWHW6NGO4WFI3Q77L5PBHGFJTLP73T7FLHLTYF5ON47J2MDGWBRQRJFQXNB6F77VQEQWWJCQX2S5NKEHCGIQSDGJSYWWP3N4UXSBOO2A",
            "198412139693380323001FXGTSFW3S55FDOIQPV3YCYHXQ4UD7EFFQFM64RKS5VR24FGLHMHMPWY5N2Q7CJVZZV2Y7O4Z63GIHB3RNVVUJ4WDUGO45RLVFLAZJGD22FLWYASUQSEGN5676LATKHDRA",
            "1984121396933903230015MVKMSNAV2Y5DZYR6WBGYVWEDMYV75P2DHA45A2AYQTDMISJHLJYL3NDA7I2GQM24WFZMP6CNFEQQVEH6UKCJGE47IGNLQAG5DBQJ5IB7C3NEWMMZ2UNPY6YH2BUAWREA",
            "198412139693410323001YZAPP2RB4DZ74UINCKKHGTDXXAB3JG2OSY65ZOWXVIJK7FWUFYZOPJOKT2CZ5APNN2OVNHHOCSDZKVLPA75YTUKIZBTREGRQPZS7LGVZBEQBNBKOAIANGXRZBO2O3JSBY",
            "198412139693450323001AGRNORFXT6U6JCKLPV5RORMCMI4WLA5M5ESNKAAAZI6UPN3EAMYYLCBVGRED7PBXVGVVZ5HC766I32VK4OK4DHNTEWX7S5RIOCG2LTBZPLCGYCADLWGP7J42FWO7VM42Y",
            "198412139693460323001XCKQPLMDCACT737U5OX6WYKGHYD52PRA47YYPETWGD3D73WFCW4BRDJNFML3PM46ZR7VEJQ6K6BZVZ4PEAIYPQIFXJQYNR4T3B3KHXTAC6E7TTCOZX7BSN2ORXGZO4UHA",
            "1984121396935003230016QQQM5534KZ36GC7UKCC77AY7UJ6THDZK2TBJT7HOQIRXF74Y5ADEDCFN5XWAHJTNVVGXS2IKNGEHT56OGLUYQ4AHKLEAYEGGE6JRN6I7MYPJNRGOCWR3N5EQ2YPP2GSA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 11
    },
    {
        "price": "64.00",
        "FARegId": "FA-000000052332921",
        "F2RegId": "FB-000006564061618",
        "AlcCode": "0100000010250000030",
        "Capacity": "0.100",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"ПЕРЦОВАЯ С МЕДОМ\\\"",
        "ShortName": null,
        "marks": [
            "197405542500141222001ZSYCDUBGYJO4PE54BEJ5NHB6GYO2MBFH6CPNPAF6MQ4LTSOCY4LXPATORZ7N43MDQVYNKYE52RQUUM3R5OREZVU6HOKGRAQA3PNW6VAGYA5CCE4DBGMPI5BKFXKWC6WXI",
            "197405542500151222001SC2ZE6FQXZV64XZJHIB4GUBNAYSPQLCYMGUJWB6FFKSL7DRUX54PKYXRIBHLJKULFNDH3LQY45SDGRO7CUECHRKIJK5MONQUEKTOMVC6GV4E3LH5D4DXR7QQDSCJ5HKAI",
            "197405542500161222001PXVG4FCPRQBV3MWUV2UJ3GRO2EHLLDNRI4FJ22YIZ2CE2DECQQGWOR2G2GJF4LR3NLWK4VPA5LH2LV6NQIA5ZZSTZZLYNCTC42JDH6C62LE7SA3NXN7NWX3CGKFMZYD7I",
            "197405542513811222001DDBGBTPOE7EUV5QZEDWRGQOKHAOPY7BEVL4JPMFP4JJR2XCB2DSH352XG4N5AXCXENO2BYESS3OOMQVQQ6OGD3KX55OC7VZLWE62LTGFV4HU7AE4PQ5BSRROUVLXFQG2A",
            "197405542513821222001LKKAIQRF2KK5VBXEDNEAMXAX6QQTPI3BLEPGVFGKLZHGEPIX5BO7BCCE7MLXECQI5U3SISVGAP6EWIJTGMOJ3ZR3FFY2KD72OINXKRUZDWPUFBU2EHPFSP4EDIIO7IQ6I",
            "197405542513831222001UQMXELIGZW3DRWDAXFOBHDB4EATGYDRIXDEB7W2TOGYTCH7GEM43TWZWXQQXD2WYMEHXP2KHWLTSYRA4QNYDFXGI4IRP5ZPKM7EYOUHTBVDUVOD3PWNQFVFQUNRBB2KAY",
            "197405542513911222001TPPCFPGGKA53IQXP2XQDJDSIRULIWIC32R7QH4UAGHPH7ZVNYTXD766GBTIQ22UHL4HRLPMPELNGAB77FHBVUE3GWEXTU54KUBWSCYBSKDND54O3UI4ILPHL7DME5O2YY",
            "197405542513921222001MRPRWZJAEJMXAAPDR5MDSHXVY4WZEP5UCTUT7BC4WFRBIK3OQKEQHZ6BC65VZGG3YFPBUTNQMRVNBDXK6UA36TZWNDU4JW2H4AERRNKNG3QLFJCHVPPMQLZLMXKGTQQPQ",
            "197405542513931222001EXUJPOZEEJN2XP5P4DY56RQ36QVDJZKQKXFJMJBZVMWQEY7IOXWTFNRDPKX7DUDMWUCF4RYZYQG5UE6Q4DYOUM5AQAQMUBF6SIMEWWPEAVB72SKLSO655YT2SAFPOIA2A",
            "197405542513941222001CACCNMKDQHMTRBNPJ4KHGRPIJESKZDPLYFKSABFURCVHEJU62RHULKOSI6SVTB4R4Q7QE4YA3HWPF6W7KBAIW5C7UB4RQBRK34SZU6SPWYXVORSKZGRFOEJMC644UEHYQ",
            "197405542513961222001L3ZY4UQYWFYYZ6CJNPGYBMONGAU53RBYI5UZAF65CFS5TAJ5A4MQJRK3ZA6U4ICMJBGAJ5YFCR5BMEKQCLOVUWOQL6WVFUA23JMLTQNVOHD6ELAQZWOOTOMKDIVWKE6BQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 11
    },
    {
        "price": "133.00",
        "FARegId": "FA-000000052246328",
        "F2RegId": "FB-000006564061619",
        "AlcCode": "0100000010250000034",
        "Capacity": "0.250",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\\"ПЕРЦОВАЯ С МЕДОМ\\\"",
        "ShortName": null,
        "marks": [
            "198412151237860323001U2OAGZNI7PE2QQX2AOAVA7TV5E3IZ5MKAGBOGMW7QRARIFF5I53QRYBT4MJRCUC5G4AYQFCV6V4KH2J4DS6QCNTS7CEO4VBCX2APANTF7CXB575S52ZY4PSWHC3Y3J52I",
            "1984121512378703230013KHZBY6VR63TJJBSMJBMRI52UI4E4H3S46WA36H6ZYVH7R33YEAXRLJAZHZDSWX6KG2QXSBOG54PN36ZI4LO7VFVHZWHMN6OM2TYRNJ6FLG2JVYNNJMCE22HY477FZRAI",
            "198412151237910323001FAUBOH4J6XQZACYJJX2D4SBKQ4TIUVYGR7NNZVCMRUA7ULLNWWB5AEABL3EXTECXJ4PWYVADO5WT5ABUV4BMBNKRS32LT3QDJ3KM6CON2BDCERPXKN5QWRE3QHGK5JQZA",
            "198412151237930323001L5HP5K6OK4LWG5CGT3YYXACCOEWKCCOAW5BQH5J3P6JAQWIVQRMRFAYF63GAYAIN3N3K5DIDKSQFIPEM7D33Y4D3STOVO2NVTSTZ3PZZRV37F3ZTGZDRQ5ZZ6KQ233NVA",
            "1984121512379403230017MD57WGZ4ZJSCIOJ7JE3IDFFVUK2EXTKPVX7MYO62L7VU7SFJLHKEZ3EFTCKK5IL3KCJDKVL7FSHGWC6CNVKFOLI4FSMZVQMMP5MB6BCZVKKDTWP6DTX52OQQGI2LJYFQ",
            "198412151237960323001GAJO4KQDV5FQPE5NIGM2PWKRUMYDPVHVA3V6ZDZOG7XOJ5VC5USEBLQ3EWKDAIZ2C4IFLNVCQUNAQ5BU7KF5WH36CU5YNBRCFMSRQPSK3ZIQX3P4O6LA42D7H2UTBOJUY",
            "198412151238020323001X6OUAD7RZ23NMOAXHWR6L7LHPQX776QZAVMYVMPHOEHVZR2FAURR2RKOLU4HHAOBMRHQ6X6TAJRMGC43HJVL4EXPVGAW4EZVMVOO2GDCHTYQEFNDE3BMUZKDYTB2LRNSQ",
            "198412151238050323001TOWN6QC46MUFOFVV327WT2NZOETTY657LWK5MIKMW47QDCOVFI5GGJ6YOYPC65BU4TZKGGP2S7QRPRAGPWWSFOG44DGFIDCSJTYMPU57Q7Y4TP7ASAAFYOFWJPTBC6DVA",
            "1984121512380603230012OCHSWOYB4M7YY2W2WSUXHMDFQXLTH6Q3IFCT3546JLPMSBU5AGVYDLWZPTQ22OL7CLIPWN2MZO3KRZRRQU7PMP2UHK5UL6B5PVG4XN4QOYSHV3WRMUAFFK6EROJA7Q7Y",
            "198412151238080323001ZTM4ARBX4R2A6XUEZCF2QJ737MWUHBX6X42UHT33X6VYFHFLUKWJ2S7RX5467SZGEOZMDMQNRPO3QDVPJRAZK2DBTHUJLCMKVCCNUPDUQC6EAZ5KPOI5V52RNXUWNKHBA",
            "198412151238090323001PFK65MZQKUIOXYKXUPCFFHNC7MF7R2YAEDP2W6NLS4PGPBRR5TW7UFEIW7X56EGCGVG4VOLNGTGPGCHMRC7BWNDKSGWQIJ4DVVYWUGFCV4PNKP5ZV5MX3QYCQ26TOSW5A",
            "198412151238100323001QP3BXZYL4OGMA6RAJIKT6JU2PIUFOF6W43H5TBUW6JG3R6QFJEZ4NRVK3VYQWHU27H27FVKGIKTKKKM5FAUNJESASCQUQZH3MYR4LXOU6DES2DV6QJ4Z3IKXKBDYNTGKY",
            "198412151238110323001TVXRR5L2Q7QXQTZVH5FX6M6TFIQEPRBELN7JQ6SUPSWHDQA22XBDSHCNZ6QEZON63OYA3Q7ORBMDSZW2KQO4BJYER34WH6NEO54AYDLQ2M4ILQON44GD5R3BUKYPM63FI",
            "1984121512381203230017ZQYOOHRSDEXVWX35I4CI4YPDAPTVHKCNHYMPJQILMSMJNRQAX3ZSW2OV4R2VD3JWLIZTW7APIYABVBW6PMD66KXMTG7NNAVNGPVHQVXUUOJRERZWVH5JSZZIXQM26D6Y",
            "198412151238450323001KZ7RJ5SUAYUQKD4YGPAWAJQEHQKHU3WG2JE75XXL444ASZUM5NZDGHRHGFZHGEHBXBBRR4RYBU23JAUZKHUTBTYCWCVPCBRPE3UZUDD6RHU6HPEOY7UMVVYCILNCZ5S3A",
            "198412151238580323001JDT7EJ5O56OZ22IT7JA6FJ7AVUGSMP5IKRTPGNM6BSROXPYW7TQAQEPRRLOPESLYFRDHAYXWE2RPVBNR3ZBLJZNQS4ILHTMNIU4QRSZ756IBNNLWBJQ6N7SXTJITBK7GQ",
            "198412151238930323001U4IR7SEUVGVOZ5A2X2ROJBQO54DWSWIC4N2CU44MMIMFE2R6HYANLT524Y26STFW4GIELICNAKJLXJVJSTP4DVT2CVHDDXBUXXFAPWYZA4Z22ZRPNFEMFMBYPJ22YMBYQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Удмуртская Республика,,Сарапул Город,,Красный Проезд,,д. 1",
                    "RegionCode": "18"
                },
                "INN": "1827017683",
                "KPP": "183801001",
                "ClientRegId": "010000001025",
                "FullName": "Открытое акционерное общество \\\"Сарапульский ликеро-водочный завод\\\"",
                "ShortName": "ОАО \\\"Сарапульский ЛВЗ\\\""
            }
        },
        "quantity": 17
    },
    {
        "price": "93.38",
        "FARegId": "FA-000000052178634",
        "F2RegId": "FB-000006564061620",
        "AlcCode": "0100000002700000047",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Архангельская Северная выдержка\\\"",
        "ShortName": null,
        "marks": [
            "197303896804491222001WYJCMTHPEWO6DYGGBWODFY3KHY4FB5DHHZLLS6XTCIEDSNL5HBKA3JGYTAXJRZLNV7YRARP7BGGOOJ432CPZUGICV3HIKB2QZIELJIFHKDX5ABWQR63F5K4DD3GS6OH3Y",
            "1973038968045912220014NYUK6TD4A244UTCPD7CMME3PID3J6KAICQMW3IUZOZSNWEDU64Z4UN6Z6P2XFBFCVSHEIJKLBJYAYRNJMFQ5ZYI6LMXMMSGZ7HVMCSY2WATBAWKUYGIYGESHNT3DMESY",
            "197303896804611222001L23FHVAI6YTB3LS476XFIODXWANIXYNWUJGT5HCRKBXMS3LK2BK3FEZ22KSJZM7LWV3PGUZPUD7C3M53Y5YQ3ZCY7VZZT6OLM55NXFOH723FO5XTRKWME2ZSF3FECLVTQ",
            "197303896804891222001D3Z3AW4UZHRSE6TWBFJFYES5WY5X3GQZ22SODHBPERCKGBXRA5MKLYNECEOPR7ZI6OTMW5747INYL5F3BML5WBDOXQH26PTMT47USYZYZTSXPHIQDB5ONRHVPY4NOEHNQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,АРХАНГЕЛЬСКАЯ ОБЛ,,Архангельск,,наб. Северной Двины,д. 120,, | ; пр-кт Троицкий, д. 133, корп. 1, пом. 5-Н, пом. 6-Н",
                    "RegionCode": "29"
                },
                "INN": "2900000293",
                "KPP": "290101001",
                "ClientRegId": "010000000270",
                "FullName": "Акционерное общество \\\"Архангельский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"АЛВИЗ\\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "178.06",
        "FARegId": "FA-000000052173044",
        "F2RegId": "FB-000006564061621",
        "AlcCode": "0100000002700000030",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Архангельская Северная выдержка\\\"",
        "ShortName": null,
        "marks": [
            "198310217866700123001QMPT464YQGGIA7MRKZ2J7FN6UM43SJAN22CSE23YVEVMG5U4YWWGFFSXFHBVASNQAJW57MUJUBRJ2WN6SA675RNEO3KFKXYVJE4EP2YKORB7EJV7HGQRKHHGNPLLXASQQ",
            "198310217866750123001K2ZJDNCXRZVLUI7LZ5ST7IKPKYGOSQC35VES4AKPZUNV2JPUUVK5VDXSJ2EMWE7HZXMHWPKYQIW5JMSZ35EALG5GC66B3OF3LMJJ4I7PD3SAS6QXCXZHAZGYBHP7IB5YA",
            "198310217866760123001LTGJAKTJ5A3RV4DNRT2T6WSITQT7K5O6HKT7FYTRJR33GTCKSYWIK4MH2WHZJ2OWTXDOUINX6RQ74OZKUO6CLSY2F6DOMUGXZ5OZT2N2PX5OEM3IKHVBV4XPVZOBBCJCI",
            "198310217866780123001KGYGAYBHON5OIUR63OPH4WGFYQV7XPLPHHCFRUNWKBYCKCIIX73GHI6BO2OP2AQRGUP3NN2LNGEMDTNNGI3Z5CW5ZNFKAVJ5K5TERI53Y7G72VDWP756F4JLB5BVHUXZA",
            "198310217866790123001KI7PWXTDXUHXO5BPPRFDM2SIVEGRPDXTRX3GWCMYELM23KUTDV2QJI4YC42WM2YTQV3DPQ4QGBLDHQHU2PWCAAWKAHBWOOHSMIUGOOOJM4ND6A4R73I3AQT6PGVGZHX2Y",
            "198310217866820123001RZR33NXYI63EUQTROCJOZSHQUUJBWGCWNM3CJBISIIPRGNX2RJX5MBKWU2FPGZIWN5BGXT4IW2S5K7S2WQQ34IC6NDLVUBQUWYQWUES63INFP46NBXV2AIG6YDHO3X35I",
            "198310217866830123001G6XZOLNYGQOIAZ7QDCIIOFQHGAYTRE3TTVKUTAJTEOUIPY7U6TUQY7DMY5ILZGM5DYW6DZ5TA5PAN2RPVU3OCCKLYYXF7ADJIUYMIU5HALYNYTP4PWKOI32R32HPAAYHI",
            "198310217866960123001P5LPEPBTURJMNLGS2F6VLR4EEEUA3ZFDQUC6FOUUQPE47S5VJGKMNQGIDLGP3M23QCXLCVGHAMOOPUPWNQZED225UNPMIYRPKKAAMFQEHTYRLKCKWCPKYZ7WA74WSC7XA",
            "1983102178670001230014MVYXIWCFR2ROLAP3UWVT5OYI4356PCYAQJTCEDA2UR2BETFAACQOZGYE2PQC2Q4HCV7Y5NLKDLCNWSV6JQ4SDQOU2NPDCIKFV35FDAA5CM4ASQERKQPWGI5A6TXWN6MQ",
            "1983102178670501230014XBZNGLABDQBYWHDJDIIIYZRVAPGYGBOH33EYYK2PVO5JWCY73A2RWWDRBDT7JJCZNUREYCSTAHJJNMDTPCPCPUWS3I2W674NXPYQ3TO4T6AXV6SJ6YJXY6RRQEL43KEY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,АРХАНГЕЛЬСКАЯ ОБЛ,,Архангельск,,наб. Северной Двины,д. 120,, | ; пр-кт Троицкий, д. 133, корп. 1, пом. 5-Н, пом. 6-Н",
                    "RegionCode": "29"
                },
                "INN": "2900000293",
                "KPP": "290101001",
                "ClientRegId": "010000000270",
                "FullName": "Акционерное общество \\\"Архангельский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"АЛВИЗ\\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "167.00",
        "FARegId": "FA-000000052286804",
        "F2RegId": "FB-000006564061624",
        "AlcCode": "0300003173920000098",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ № 1\\\"",
        "ShortName": null,
        "marks": [
            "198412621321540323001GJXJIJNPBOKKR2KTHLCZ64JFNUNPNRWMZIGZB4ZNOPNPMGQDTJXF4T2IXUD4MQCJQHOVPW46T4AP3D3AFFOAFD4KOHPGHJNLCYPT4WHW6GCLKEBDUT5UO3ZKXEI5LGIHA",
            "1984126213215503230014Z6GLNPRBGS26GDUZW3E56JQVML5GF6U223IY6WJWZCD46M5EFDEWVBO3DNFIW3RNZRRGXR3NY5IW55CXNQOJQB2GZK267NHWINEH5GH27T2YYVERYEFCOITJCDKBEVLY",
            "198412621321560323001LJTGUCXPRTBV4R7XB2AKIMTKEUP5QVELUTBDDTWMEYFCTFN5BKV6KOJ6GYOM7FD6H3HPIYKL6S4IZKU4B7XY26MNEIIMEZTSTISVEEEFDMEEIPMVSHVH73JEQBJHGVVXA",
            "198412621321570323001JP4LTY2AYF6XJBXULP6IEIR5IUWQVGVCABD2HJIWOPQCKEFEIGR3TIBBTX3AOLUR4SWLANS4WMHAHXPUKDZUAX4SYJ4L6D7ABALQRZZO7GHP5U2SZS74YOXYB3CUXXP7Y",
            "198412621321610323001GUIHXE6SIUIGBZIDP3BXZE5GKIPKUZDTIVTZT7MSD2TNAIVBHUUDRANVGNCZ7VNTHLYETTM4IOZDC7XJZVJPMRWP4UDCCUNE6T22GSVS5RVPFHLOY4EMQPNT2JEEDD4LQ",
            "198412621321620323001JNNOGZR2ZWP7WVN23UVMVK7JDQ2LADOU5CKCJAC4ZJFJV5XRR3ET5SQTM7HONRNFHV7HAHOYZZZLCBA7S5SIIVADRU56RFUKR2BM6FCMOVELU6K246UO5BYKPLYX2RSCA",
            "198412621321630323001M5HLBR3FIXTDGBLW3R7GAA7GL4AHV3MJ3NYYHXNUQTBBNYVOO7A6RX27RWQLKYHGVE5HA7Z4TVRSCTNTGYTZZ4CBVXT7JZXUDMGAPN6GDYHH44KYWUP4L2XW4I3BBTNHY",
            "198412621321640323001FLXZNERIUXCM4DAHXNP2AXHDGYF7MUG7OEWTPMLT2TL6H6ITPGIDKZBENWCQVZDZW45FUOFGSLMMBPMB5PJ4Z3K6LPU5H2QY675NESLYYBTPWMEZQVKSWNY5EYLISYWTI",
            "19841262132170032300177G3BZXSTNFEXGO2F22K34IUEQOZTTZOO6JEBEENOL3TXP7ECXIWZ2TOB6ADNRIAO6OVJACMZHYPHYMJ4F36D5VCGVG45CT3WD4SN3366XUAEK5L5FSY3UHWB7HBT6V4I",
            "198412621321710323001C6NKP32G5KW54CU3T5J6NI54AQZRCZWJLZOMPBFWKF2QW4UHILRUMIKY3L7FOGCI6M5QP7TTANI6D3E3UVC4FRMPSXXMT4EMWCNF2CWGV2YE5JONZ7PRJMQJ43QTRN3JQ",
            "19841262132172032300173R7MVNGTXW24TSPOALJISDZFMFO33MU5PNFJ2DFXOA3ETA2POJOHWN5ZGKAWO4BKC2N75FOGPEKAZUQWDEY2TIIPD4E2PNUL7V7C4RU5LM6YYENNBO7VRPPMXJ5A4RGI",
            "198412621321730323001JBESLPJCSKCYZ7MAZQ5VUWQ2SQETDAHATJCPIVXRXP2MGD7KE5WQ7RKDPUJNC4TBUGJDIT6LR7YFQCRPCW52HVLAHHEC7CWUPVKFPRGJB5757LTAEQDD6FPWTRV43NWFY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КАЛУЖСКАЯ ОБЛ,,Обнинск г,,Коммунальный проезд,д. 23,, |  | АБК, нежилое здание, площадь 526,6 кв.м; очистной цех, нежилое здание, площадь 1003,2 кв.м; цех розлива ликеров-водочных изделий, нежилое здание, площадь 2690,6 кв.м; склад посуды, нежилое здание, площадь 854,5 кв.м; здание (спиртохранилище), нежилое здание, площадь 334,3 кв.м; здание (контрольно-пропускной пункт), нежилое здание, площадь 220,0 кв.м; склад, нежилое здание, площадь 1146,1 кв.м.; цех розлива ликеров-водочных изделий № 2 - нежилое здание, лит. стр. 2а, стр. 2б, кадастровый номер 40:27:040202:362, 1 этаж, помещение № 1 (S=130,5 кв.м), помещение № 2 (S=65,7 кв.м), помещение № 8а (S=78,8 кв.м)помещение № 10 (S=247,5 кв.м), помещение № 12 (S=188,8 кв.м), помещение № 12а (S=18,9 кв.м), помещение № 12б (S=21,9 кв.м)",
                    "RegionCode": "40"
                },
                "INN": "4025447648",
                "KPP": "402501001",
                "ClientRegId": "030000317392",
                "FullName": "Общество с ограниченной ответственностью \\\"Калужский ликеро-водочный завод кристалл\\\"",
                "ShortName": "ООО \\\"КЛВЗ КРИСТАЛЛ\\\""
            }
        },
        "quantity": 12
    },
    {
        "price": "307.00",
        "FARegId": "FA-000000052236532",
        "F2RegId": "FB-000006564061625",
        "AlcCode": "0300006342850000030",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ ЛЮКС\\\"",
        "ShortName": null,
        "marks": [
            "187422743142240923001CHMEXZHOCD4USNF3UGK6QUZTUYCHEG2TLFF5SL2R4GG4ZCDQZEN4WA3FFIOWCQ5XLN25HR7CRTIWJ562NCHYBR37LBNJ5WI2LHCHEWSK4Y67CWL4737INEU6VGGAFDYAY",
            "187422743142250923001TEQ6LAGMAMVAEJBOCP56HS26KEWZIASL22XRS5RHIXBPA3CMSOBQZIFIEK63ZMWYEPXGPP6X6TDY3T7NUEKZOR7LHCPVJC3AU2LBQVONXPVQEPVBGIKE4OJA723UE423Q",
            "187422743142300923001WI44WIU3P4SRRZ7S3SRQUYD7VIQOKUZ4TK3GKXCI5JQ5QXMZZ74SMZ2GFBDJRM5P7LTZSM7EZY46J37LTFASCF7YTVC7IHWWQXEFRMQW3FVFO6J47673BZMRPM43HXHQA",
            "187422743142310923001HP4H2ZUYSIPUTCLXTMHCQWXGZE2GFGGJKN4P2YQCK233J66I4XWS3OHARKI4TOP5COL6ITFNA6ASYUY7PILUVPP2ZUHHOSIBHWAGAPAC2GTV5QJ5RQT7NEJVH5JID2JXQ",
            "187422743142360923001MQ53NFG6RAN47GDKITK7XJQNCEPBN7QPQDVNTJIBL6J7XP226NFXWQ6XR6QH5LNYUKLBLJTLYOR4CO623CZAKW74XURU52EXPYRBHZIGMIAHQZZFKVSXVBM2TDXDYTWGQ",
            "187422743142370923001WOKFNHBGCFQLELRWJA2WRBMLXQR6ET7LVWVOCLG7KRI4K76CYWUQWUNS556RK7AV3LPU5OSYILZ6N67ER7DJ6FOWQVCOOMJHTBPCHGJJMCRM2PHHSOJPKOXLFXZEXBTJQ",
            "187422743142400923001LAG7M2OQQO3FXTTGF5QBTLQT4UFG6G4TWRORE2MY554P7EKF2PQF6KU7UWQFENSFU52AORGHVEGSH3L4LWLCH6IWL3BQSUQUBY6MVDN4EOGR2QWQYCEA5OTMCGJ3B4EQY",
            "187422743142410923001ELVM7HGS5J5QBLDKIZZLV6CEKEQBSSM2K5LKPRNOZFT7PQV6SQ6F54OD5MC2UWI7RAOAVONEPBKGRUDEPSJZYXZOAAVYRJHXGMQUYOIXPOWIQMFYQ3KWLAL5A66J2PUTI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "307.00",
        "FARegId": "FA-000000052248153",
        "F2RegId": "FB-000006564061626",
        "AlcCode": "0300006342850000034",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"ЗОЛОТО БАШКИРИИ КЛАССИЧЕСКАЯ\\\"",
        "ShortName": null,
        "marks": [
            "187422742661980923001WT4FLF2N3IZPDPYBIIMXLN2FVUWV65Q7Y2IJ4TMMIJMZYMIVQVHONWNBHFLDYLI57DOZKJRJKLKM6EPOHKDKEOK7JW3DORQNDPS346TKVM5KLBV6IX3RF77O6L5KPSYWA",
            "187422742662130923001FEHZIR6AO66TCXBQXFXLXMGQAEDRBCD3M4F35KH7DWKNB237SGFBPW2PPRSPN2SPXSWTHOCTIWNVCREVWADHFKWGC6LPQJNCQ324ZYRO7D5HSK5O6UHE6NTSKN6BGDKIY",
            "187422742662140923001KMSKB7WQ2QXYDO3YMISLQY6ZG4TGDW7L2K3HATOGX7P2VUTXYZECXULCGV2CZV4QPLL3WZXG5X2PKLOSBEG5EW4VWY2UADYIB5LCPIQCH7NZQP6EZRCPQI2ZK5ALE66ZI",
            "187422742662530923001ICBBK4GKREK6IRN25VXD5MU4BUSYXT5LLJ5F22PMKRZIAD4RUHSWFF4AYIKURMVCPMUDONPJVZMNPCYWM2PQWANFU5NCGIWUKUYHZ65VQ5I5H2Y4O2MNYV6MF4LHM7HBY",
            "1874227426625509230015XJTQSNJW2DDYCVJB7FETJ2NAMHZR5H65CWNPLF27RSTQKJUXURM34BSGLYJQCRCPYDJ6RX4JTNM2NMR2LB3BXYITRCVSAE474EH3HBICIJWWURFH6XPJWATLOYEQ4BZQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Башкортостан Республика,,,,,,,Уфимский муниципальный район, Сельское поселение Булгаковский сельсовет, село Булгаково, ул. Шоссейная |  | здания №№ 5/1, 5/2, 5/3, 5/4, 5/5, 5/6",
                    "RegionCode": "02"
                },
                "INN": "0276100884",
                "KPP": "024543001",
                "ClientRegId": "030000634285",
                "FullName": "Акционерное общество \\\"Башспирт\\\"",
                "ShortName": "АО \\\"Башспирт\\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "93.38",
        "FARegId": "FA-000000052089619",
        "F2RegId": "FB-000006564061627",
        "AlcCode": "0100000002700000047",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\\"Архангельская Северная выдержка\\\"",
        "ShortName": null,
        "marks": [
            "1973039183995912220013WK64EISMDHAOW5KE3UOSOHARA2SI4JHEEIVCW657MKO6IBG5WNSUQ45SG4SYF2HOL7BIJHALOB3OUZB75AJBHJWQ6LS3AU6XK7IGYNILLB7U4DF4NNGOPNAXGJU6LNYI",
            "197303918399771222001DIWDPJO7CQBSHMRQAED6HDRDHIT75BIAOOASWB746D3TOAIMBOALXHLYOHVKLMMEWQMXINLE6EGNCDKCGVX3JAZNKTWMED2UKPCGVRTGMBJF2FSSBRVUWUK4YGV4TA2KY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,АРХАНГЕЛЬСКАЯ ОБЛ,,Архангельск,,наб. Северной Двины,д. 120,, | ; пр-кт Троицкий, д. 133, корп. 1, пом. 5-Н, пом. 6-Н",
                    "RegionCode": "29"
                },
                "INN": "2900000293",
                "KPP": "290101001",
                "ClientRegId": "010000000270",
                "FullName": "Акционерное общество \\\"Архангельский ликеро-водочный завод\\\"",
                "ShortName": "АО \\\"АЛВИЗ\\\""
            }
        },
        "quantity": 2
    }
]'''
        params = json.loads(s)

        waybill_v4(utm_url, fsrar_id, shipper, consignee, transport, params, "21", 'Перемещение')


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
