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


ooo_dionis_tupak48 = {
        'ClientRegId': '030000575119',
        'INN': '0201014099',
        'KPP': '020145008',
        'FullName': 'Общество с ограниченной ответственностью "Дионис"',
        'ShortName': 'ООО "Дионис"',
        'address': {
            'Country': '643',
            'RegionCode': '02',
            'description': 'Башкортостан Республика, Абзелиловский Район, , Тупаково Деревня, Файзрахмана Хисматуллина Улица, 48,,  | 1 этаж, помещения № 1,3'
        }
    }

ooo_dionis_tupak55 = {
        'ClientRegId': '030000412016',
        'INN': '0201014099',
        'KPP': '020145005',
        'FullName': 'Общество с ограниченной ответственностью "Дионис"',
        'ShortName': 'ООО "Дионис"',
        'address': {
            'Country': '643',
            'RegionCode': '02',
            'description': 'Россия, 453622, Башкортостан Респ, Абзелиловский р-н, Тупаково д, Файзрахмана Хисматуллина ул, д. 55'
        }
    }


#

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
        utm_url = 'http://tasht:8080'
        fsrar_id = get_fsrar_id(utm_url)
        positions = [
            {
                'quantity': 3,
                'F2RegId': 'FB-000006259332159',
                'marks': [
                    '1933022854841004210016KUPSNVXZBAGLZSNOPFPYKO4IMBDO5OV4Z7BEGVGJN7FJT5JVLM6CTKU4UPSW3VM75AN6DHX5SYSCORUA2HDGYJH2DYDNAJSNBK7TFRWBXYNOUU3RQZTAEDQ25377EPWY',
                    '193302285484050421001HEYCDFXPBT5HGQ7PAC2YAY74OMAVDIKV57NHHWKZ5OES6WK73ZHNWF4UHSVVHLU2DZS72EJOCCOSDXAP2QRHRDHBNQZP7YKMQNSKOH7H425N55TLFXLL63N4TSPW22YQA',
                    '193302285484120421001EWDGHD3TNJIRTBNFXE2TB7GYOYLX5DCPTFGRRZY4Q5BSYEOFDEMDW4IP4JTGG2VQO3NQAA5HE26EVXXQCNWBIZKN6AECIJLSSNBHCCBJN4U5M7NWOUGGADAM6BP3SQACI',
                 ]
            },
            {'quantity': 1, 'F2RegId': 'FB-000006259332161', 'marks': ['1903008499310511200013AEGJVNFPMOTD6E7U3ODPVI6LMBW3FQPYSG6L2ZKXWC5QWYGLGJVTYB53KI2MA536AJIBCL3ULX6UF3JF6CSERQXT57MDPGSHHALTSO42BNQQSZGSB7F4SVILPXZCVUKI']},
        ]
        write_off_v3(utm_url, fsrar_id, positions, "13")



s="""
[
    {
        "price": "529.11",
        "FARegId": "FA-000000049332102",
        "F2RegId": "FB-000005738637159",
        "AlcCode": "0100000007020000107",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "233",
        "FullName": "Коньяк с защищенным географическим указанием \\\"Дагестан\\\" российский пятилетний \\\"Цитадель\\\"",
        "ShortName": null,
        "marks": [
            "187310041314810122001A6T4RW4FOSTPDS53ESKK26F5QEP5FF2AJVEHWQKSCJUSADW4HSIEIJ2BBWXRSKY5KEDCJQOPGSRS44SFUMES2VQRNGBWV36PZ7AGO2V52KDMHXC36WEZANCXTFPFQM6CA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Дагестан Республика,,Дербент Город,,Красноармейский Переулок,,56",
                    "RegionCode": "05"
                },
                "INN": "0542003065",
                "KPP": "054201001",
                "ClientRegId": "010000000702",
                "FullName": "Акционерное общество \\"Дербентский коньячный комбинат\\"",
                "ShortName": "АО \\"ДКК\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "491.84",
        "FARegId": "FA-000000049180310",
        "F2RegId": "FB-000005738637160",
        "AlcCode": "0100000007020000108",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "233",
        "FullName": "Коньяк с защищенным географическим указанием \\"Дагестан\\" российский трехлетний \\"Цитадель\\"",
        "ShortName": null,
        "marks": [
            "187310065932670122001IDLKJEK65T7S66M7KTQ7IEESTE3ZTLF6TKCOWXV3VRMQX5GW5NP4EZ4SARU6I6WNKPLQOWO6HYZQKGWU5Q5WS7OIF3YBVKMZGUHSF5LIYNQMVFPTVWJUCW42473YYA7CY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Дагестан Республика,,Дербент Город,,Красноармейский Переулок,,56",
                    "RegionCode": "05"
                },
                "INN": "0542003065",
                "KPP": "054201001",
                "ClientRegId": "010000000702",
                "FullName": "Акционерное общество \\"Дербентский коньячный комбинат\\"",
                "ShortName": "АО \\"ДКК\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "207.00",
        "FARegId": "FA-000000050482642",
        "F2RegId": "FB-000006018784475",
        "AlcCode": "0100000001740000280",
        "Capacity": "0.700",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое красное \\"Каберне\\"",
        "ShortName": null,
        "marks": [
            "192308221054330622001IDFM76CLMZKPITSVZFWSB3SVW43A54MYS7EBC5PS4YIEXE6ZTNF375YAHP236GGY3RTB6Q56X2JRT2QH56YWYPHJQIRERSEVTOLHMUFTF6S4MOHKHL5F3XLTQAJS2QSRI"
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
                "FullName": "Общество с ограниченной ответственность \\"Долина\\"",
                "ShortName": "ООО \\"Долина\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "169.00",
        "FARegId": "FA-000000051298494",
        "F2RegId": "FB-000006424019219",
        "AlcCode": "0100607004990000099",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "4213",
        "FullName": "Плодовая алкогольная продукция полусладкая \\"САНГРИЯ ФРУТ\\"",
        "ShortName": null,
        "marks": [
            "195301810439210421001TMPFPGYWBWXCZODIQTUC3DEO4QCJRIZR5FNCXEVCOOP5WPXCIM7OU4534V4QP2WSUZENSI7XGXJFJL7I4RP3XTLSGZHVNLZO6PFB55IVG72FHBMZUBOC6FXR52HVHVGLQ",
            "195301810439600421001V6K4CZLLZZCCIGOTCKGIB46VKAMKLRJAYSJEZ5OS3WO7CMN4QZX7M5XL42F5KIYH53IKB6KRT4TGNYO2O6G5LLTLMKWXBEVNIISIKGQZQAZEQP3OFLRVHUP3KJNZHZ6KQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Крым Республика,,Симферополь Город,,Московское шоссе 9 Километр,, | (за исключением: помещений №№ 8 - 19, 21, 21А, 21Б, 23 в нежилом здании цеха розлива 2, литер Ф, 1 этаж; помещений №№ 5, 6 в нежилом здании проходной № 1, Литера Щ; помещений №№ 1 - 21 нежилого здания заводоуправления, кадастровый № 90:22:010601:505 (литер А), 1 этаж)",
                    "RegionCode": "91"
                },
                "INN": "9102257636",
                "KPP": "910201001",
                "ClientRegId": "010060700499",
                "FullName": "Акционерное общество \\"Симферопольский винодельческий завод\\"",
                "ShortName": "АО \\"Симферопольский винзавод\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "282.50",
        "FARegId": "FA-000000052005741",
        "F2RegId": "FB-000006424118908",
        "AlcCode": "0300007181500000016",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк армянский ординарный трехлетний \\"Армянский коньяк\\"",
        "ShortName": null,
        "marks": [
            "198410280816150123001CKI6TFBC2I3C3I4545G2VCV4FAKUGBVGMXIO4JSRXVIXRLPUY2JW55TBPDNTHTLCSJFNEHN2CKOT5L5D62KBUM3PIMKOFF4HDONP24MRJ4H7MN7TWYAUWKY3ZUZVAOXMQ"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "Республика Армения, 2401, город Егвард, Ереванское шоссе, дом 7"
                },
                "ClientRegId": "050000049839",
                "FullName": "ООО \\"Винно - Коньячный Дом \\"Шахназарян\\"",
                "ShortName": "ООО \\"ВКД \\"Шахназарян\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "461.00",
        "FARegId": "FA-000000050339319",
        "F2RegId": "FB-000006633137405",
        "AlcCode": "0100606880350000023",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\"Армянский коньяк Трехлетний\\"",
        "ShortName": null,
        "marks": [
            "187414797025441022001PO2DTI6HFWWMV34JU6BIJI4U6M447PGY5RRJX32Q3IN4ZOA6LRA42OAOH4TNWTO2JBR2T2ZXVO2GVFCDNXRLPBHR7DUECQFF7LLBLYTREJKJDNDZRJSNFL7QFM7DZ2EHA"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\"Гетапский вино коньячный завод\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 1
    },
    {
        "price": "299.00",
        "FARegId": "FA-000000050177246",
        "F2RegId": "FB-000006772965738",
        "AlcCode": "0100606939440000049",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк армянский ординарный пятилетний \\"Армянский коньяк\\"",
        "ShortName": null,
        "marks": [
            "198406536951950622001QCX74EVGUZPI44VRHG6UJKTCFIWT47CMN6HRWLTJUUUIGUNGQXM3YF7W26ULRRYWQWVT3OTYLUZHJCXOZCBCDT65P6YOU7WNU2OZ4MAYYV23BFQAZEMOTHMX4CXZ2GXUI",
            "198406536951960622001N72MX55J6VMO3DNICFLUIS4PIIHKCUA4M3423Z2JI42JK2G5QHGTZTXIGZGV2BI6NBNEA3OU4GTDMZQ5ITWO4JSMTJOD4XTXYR3EWQYNWILFOEDNKDJKYDVQK3AKFUOLQ"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "Республика Армения, 2401, город Егвард, Ереванское шоссе, дом 7"
                },
                "ClientRegId": "050000049839",
                "FullName": "ООО \\"Винно - Коньячный Дом \\"Шахназарян\\"",
                "ShortName": "ООО \\"ВКД \\"Шахназарян\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "473.00",
        "FARegId": "FA-000000052724420",
        "F2RegId": "FB-000006772965740",
        "AlcCode": "0100606880350000021",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\"Армянский коньяк Трехлетний\\" (матовая бутылка)",
        "ShortName": null,
        "marks": [
            "187421325346220823001T5CUOMEEE2SCGGCEXOIMU6RAQYT5R5J7MOMU36YCC5T62HFQJODQCJLAEEEKSJCHOO3CBXIWLAKJ7GD53SCORW2QKUO5LZ73CL7WGAKHD27C27QMRY7ITV2EENFPQN4DA",
            "187421325352320823001V7NSHG5FQIXYD5T723W55C3NA42B5AXVCSSEKMKCA6ITPFE6CSDSPDKBV4QBSR2EJM3OPQNWM6KG7OCYSM2RP5XNBYSNLQLUL2QSIYIGJPDVB75SJAJNMNSSV5FS43WFQ",
            "187421325353610823001BVJKFROXNXNERVD2HDMI5UGY5EY2MLNRPARHEZKJCAOTW5XFTFIE6KFDJASNMMRUY3CSV6H2AGGCCOMJNSI4EY3XZZKJY3W4JWV7YAUFJTOOJY6SUBT6QVCNPKEJPRGGI"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\"Гетапский вино коньячный завод\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 3
    },
    {
        "price": "387.50",
        "FARegId": "FA-000000052848067",
        "F2RegId": "FB-000006822088939",
        "AlcCode": "0100000004970000163",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Царь»",
        "ShortName": null,
        "marks": [
            "188405017421301222001TDDIAOVXOCN2G4I74ROHR6DKL4AJ3FQPNCAV3LEISN5RELD742BY3CT2NPA4Z2SK3XAJ36YHPTFVXLIB6HQ46AOZVSU4NCBDWSHPL7AKTJCGJ3AC2Z5AWY2P6JK4PRM3Q"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "284.00",
        "FARegId": "FA-000000052101642",
        "F2RegId": "FB-000006866750444",
        "AlcCode": "0100000042540000049",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"БЕЛАЯ КРЕПОСТЬ ОСОБАЯ\\"",
        "ShortName": null,
        "marks": [
            "187421572562860823001EZF6UP34U7WQY4CYVXSHGLPXSUNYO22YUD6FXEV7NR3MUD3ZGKJAXSVSHD4X2CBEYQZDYUMY4JZPWSI6HPZSHDD5JR5YCBRWRTMS7L4PIN4HCZSDT6MNGXVTQFUB6I7YQ",
            "187421572563080823001OPOREL4GJUYN5BGXZRHEVQQ7GIU34RTWCR3KEW223RR23MM5COSHCRSXZJTRLZLAVRWIQNYUOSD3BLZKXOGF5XMJIG2X57GOOXTRJ2MCNRVED44G3ZAUT5ZAQYAXCHOWY",
            "187421572563110823001GIFM6KFS2TYHFDDIQFTKYAB6UYKARIEYRFZTBY5UB3POQCMMFSQWCOENX4GJRYFZJOBLP6MT3DQ43EJ4YB2DSMX7TFWVVQWETYKZ3NSSKHOCJKNNEMHRFMX7RI5LW4IEI"
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
                "FullName": "Стерлитамакский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "301.44",
        "FARegId": "FA-000000052967241",
        "F2RegId": "FB-000006907741972",
        "AlcCode": "0100000005360000123",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ГРАФ ЛЕДОФФ ЛИМОН\\"",
        "ShortName": null,
        "marks": [
            "187424804072421123001AB45DT6NTSUS75FRZFAYB2LT74XALBQBRI7Y2ENSX4KB6TVKMLSA4LIE44PTLA2SHDIBJSC2JCSI3ZHW44SKZC6FVGTD3GG2DYEPEBNDEXRMHKVTKSHL6SQQ75ZPAAZCQ",
            "1874248040759211230012JVIZSYICYDOURGI3A2KNB4SDA2RZNJWTUD4SD6UIP6KKO2GAQSBMTMRFW2NSRHPTLHP73QBP6KNSBOR3C3KV2B4NFKJWX7ALZ23DIUEU2KNJASMXMXQ4W4FV23QT5GJY"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000052857334",
        "F2RegId": "FB-000006907741974",
        "AlcCode": "0100489413240000075",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"РУССКАЯ ВАЛЮТА\\"",
        "ShortName": null,
        "marks": [
            "187424699313961123001AJVREVSARUZKHLMPP6RJ4RGIFMBIBW6ULYDTB7RKMYG2LG3XRD3LMJXYMP3TG6AYBSTDIYHMMO5ARTGI7HVRDW2MSMJVDFVRLKAPWOR5DQSS7T6R6NEUUKTEZEPJSZD4Q",
            "187424699314011123001KO5QHP4UG556ZT2FH7IRKXD6SA6UDVCW6P3NIDMSRKWR3MKU5APBFMQWCABKD5FTKPH4FBDRUVMAJ6VGUQAGGHJNUZXOTIN4ZGQA7HFKVAGUBQ7AOBWICHECE5BFZEHWQ",
            "187424699314021123001HLQOKFFRPTA342JMH5CG6YMDHQDYH4LGBQNZVOAYPHIDMC4RMJDZPGYJN6V5BJAH37B6WRRWSZ2M4DKTB7MRUWH7632E2UWIM74PQGO4NBJCPGGKSFY2UMLPOLDZVV7RI",
            "187424699314111123001K4YZZUKGZ6S4SMGA4IFJOWBTS4CIIKP6X72U2QRSRTV3ZVXQ3BOOT3FJAC2ZPMDCQC7WY5KRVM7FGUZDZ7EPLOFNZO6JXTZIRU6LALZZ37HYBXKLKOPHELTJREZLGKLDA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "238.00",
        "FARegId": "FA-000000052857334",
        "F2RegId": "FB-000006950462176",
        "AlcCode": "0100489413240000075",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"РУССКАЯ ВАЛЮТА\\"",
        "ShortName": null,
        "marks": [
            "187424699350151123001VVR7GZDDBT4LPQFR3AS5CHWLQI5H2B4PT7LHNFKO3LJK6XP5MSGOPLVLM5ZVPVCM5EONSUX5IUDEEPHANJEXZSBEL3YWRFAEXLEI2PPGX5TFEGOGJG3RAU5EK3FZBKTKI",
            "187424699350251123001G7DIR3ETCG4MLDZO6UWTFCGZOIICETDUDQOTUEHWTUJYGEE56MYUYMHFP2E5KMU6NY3C4BK6DAI7G6QGA76UYT3K5MMC3GUGJVWYFKNSSDVGWUXCPI6ES2HRZFYICII3A",
            "187424699350341123001V53LLM5E7HZXV3U3IOADAKVN6MOJBQCJDJX2Q76ZRJZCQJHRJFGBIDAAEPR3XN6EKD52OYZED25ZOK634VVY3Y5GPFGEV7GCPPKRZUFLBFDIJJ75JZI7FH64BUUPNMJBI",
            "187424699350361123001XDQIYYQBD2G7WR5UXYEWOXMPNUEBYBVUDJZI3OU2OTUE475EUTCZ5WORH2MSP6A6F75NDWG5C6EKBOPNPSW5OPWZ6ZREZO6GFWDZ6C47QWW6CPK3JVGKVDKGE45PY5L2Y",
            "1874246993504411230014G72SYGPHERHE2B2RCB4DA3Y2M2CI5WAHQBPDWRHXXGH6EGO6JBM76IUUERUPWJP5DNPEDGTR5PDGFIZULRCHTC7M5CUHDBTPBEN2WPD5PEHWHTPLNWKPJ3HDXG7VTQAQ",
            "187424699350471123001F7D2DQ6GZWCVEAIMIOVVVMBIV4XNC6XDT26RRSHZY2YP6Q2THUFFKFGYRDR2VNXI53QTC3UVPJHT63JHC3MWLAPXWZ3JMVXOSJVY72WCP4H5ZF7N2HG5M2XFJUCICL5CI",
            "1874246993504911230012TDLY5NGJ3H6M6DHEGATY6VYNYGUS4YISBMZE336WN6BDMDDNXC3ZYY7H5RO3HR3NDLVAHIK42XDUKMD6ONMC55LYOMRCPXIDGZZMM4HUDNHDYNKUTFJKG2XWBJQWTYAY",
            "187424699350511123001RAE2YBHMMC4KGFFYSO7J7Q6MBQPP2BZVZOYIHE6D3RDD2L2F4OLT2ZIKAR373NSBUK33S7STFVSUHJIHFWR7CMNJ47QIJOWDZ3UNCP3XGX3EM5FQ6FYJU2PWBWZBOQELI",
            "187424699350541123001EGDMBED2NIOTIPF6HNAFUYYAPAQ46BY426YIRP6CVJCHWNTICXS5WOV3HAINLKKYVWWB4XLR44OLMUHC2PKCFQBODP4DNQ5XQBME75OF2XI6OUHONOBUJ2FNW4PEHB3JQ",
            "187424699350581123001O6PHP7LSZJBWHJMKHQCWBYE3I4H5AX6Q4SGFWFWVCKSP3PDQQMYY65GG3ZU722D2E2LECNRKOLTBQ7GKUF3VQPIDSK6KEWNFZ3XWUFULJ2EZ7PDF4DRY5NKA2HEJKL44I",
            "187424699350611123001DHXQZ46MWAODLKFYBRBAT3LVFATOJBGEPTXUQDRT2DBB6TRL7KHSDU2Q3MLOFZHZX4KCQONJICYD3EESVJ3BPVQD6MMUUNXXLCXR5YWPTILKGCVGAVHRVMJHKFN3O4MNA",
            "187424699350651123001VU7P7Q5T23TME3FI2URH2SNTEMYI3ZCJB3ULFAQCZV6YG4TW2HQGL24NWOBWD7XWMXREABH4O6QZVR53OZNR7L2Z5IVQ5HONGDWS7NBO2KAMJ77WZPD4DJ3AJ2NZ6W4RY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 12
    },
    {
        "price": "387.50",
        "FARegId": "FA-000000053826590",
        "F2RegId": "FB-000007078378659",
        "AlcCode": "0100000004970000163",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Царь»",
        "ShortName": null,
        "marks": [
            "188303474065200623001SJVFZS6FKZQHD6WRPKC7PLSWXQPOUAMBXQQ7E332AYB5DU3YFHCUONHEJRKJ6Y2ZV7NHBHUJMV2G36HUXDV5PN7DS3DLIODRZIR3HHFBONSZNJ276NF4XLRTWXGR2I2XA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "450.00",
        "FARegId": "FA-000000053817205",
        "F2RegId": "FB-000007078378673",
        "AlcCode": "0100000005390000131",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк трехлетний \\"ТРИ ЗВЕЗДОЧКИ\\"",
        "ShortName": null,
        "marks": [
            "187426015858841223001LZK7P2DOH6I2DAX4473PIR3ZDE7ZBPVR2DEUM6BDEQZMZV7FSJA53IT7RNHIMDGJQWN26FECSG2VS5NYXIC2GOBTCKHPSKU2G6VCVP2MZOZY3F3A3K32WQT6HVTHPV55I"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "268.00",
        "FARegId": "FA-000000051415302",
        "F2RegId": "FB-000007078378674",
        "AlcCode": "0100376750480000198",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк трехлетний \\"ШУСТОВЪ\\"",
        "ShortName": null,
        "marks": [
            "1983089636564207220013M4R23FESSF5S7IRWY2XTSGFIMBAZZ3AGJNQ4MESG4E5Q5XM4XACUO4XC7ASRFEPSHKEA7BSSRAAH3BAE5L2R6OIGZHGO4KDKOBZQYZCRBGUBXHJFSV76QPLMWCFUKMMA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРЫМ РЕСПУБЛИКА,г. Феодосия,ул. Любы Самариной,19,,,, | лит. П, В, Х, И, АБ | литер АБ, Я, подвал литер \\"З\\"",
                    "RegionCode": "91"
                },
                "INN": "9108001581",
                "KPP": "910801001",
                "ClientRegId": "010037675048",
                "FullName": "Общество с ограниченной ответственностью \\"Крымский Винный Дом\\"",
                "ShortName": "ООО \\"Крымский Винный Дом\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "524.00",
        "FARegId": "FA-000000051032612",
        "F2RegId": "FB-000007078378675",
        "AlcCode": "0100000005560000272",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\"ШУСТОВЪ ЛЕГЕНДАРНАЯ КОЛЛЕКЦИЯ\\"",
        "ShortName": null,
        "marks": [
            "187416462251071222001OFKC4MMPSXM56OQB7G4X2GS36YWWDVKSTHEZSIGNHCJHRQNUMIVCURT2NXUDN2DEOVGMIKKR3P3YWIZRUYSNZ52WHIIZSPFUZIJVMVMH6DTB5BUVVDYEI553ST66K776Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,Мытищи Город,,,Силикатная Улица,,д. 17 | производственный цех № 2, кадастровый номер 50:12:0101301:103, литера Б1 (S=4570,9 кв.м); производственное здание, кадастровый номер 50:12:0000000:57094, литера Б, б2 (S=738,9 кв.м); административно-производственное здание (общей S=2658 кв.м), кадастровый номер 50:12:0101301:225, литера А, 1 этаж, пом. № 25 (S=52,6 кв.м), № 25а (S=18,0 кв.м); литера А6, 1 этаж, пом. 16 (S=14,0 кв.м), пом. № 17 (S=56,3 кв.м); литера А7, 1 этаж, пом. № 40 (S=116,8 кв.м), пом. № 42 (S=70,6 кв.м), пом. № 42а (S=2,6 кв.м), пом. № 42б (S=2,1 кв.м); литера А3, 1 этаж, пом. № 39 (S=215 кв.м), пом. № 33 (S=30,5 кв.м), пом. № 33б (S=8,8 кв. м); литера А8, 1 этаж, пом. № 32 (S=199,4 кв.м), пом. № 32а (S=64,8 кв.м)",
                    "RegionCode": "50"
                },
                "INN": "5029047184",
                "KPP": "502901001",
                "ClientRegId": "010000000556",
                "FullName": "Общество с ограниченной ответственностью \\"Родник и К\\"",
                "ShortName": "ООО \\"Родник и К\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "194.00",
        "FARegId": "FA-000000051105733",
        "F2RegId": "FB-000007078493626",
        "AlcCode": "0100376750480000185",
        "Capacity": "0.750",
        "AlcVolume": "10.500",
        "ProductVCode": "4011",
        "FullName": "Вино ординарное полусладкое красное \\"Шато де Весаль\\"",
        "ShortName": null,
        "marks": [
            "192309728242911222001F56HMWVRONEE5UZIVQV7DGTAAYFD2BTVAGMVHRC2N6Z6IJUH4PG6DHU5GO2BWO6RE2NYPREWY7FSHLE6MBK7KY4SOBWZ7PHTHTYOPLGLA3HH6E4Z3SGCMG35F5LCN2GOQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРЫМ РЕСПУБЛИКА,г. Феодосия,ул. Любы Самариной,19,,,, | лит. П, В, Х, И, АБ | литер АБ, Я, подвал литер \\"З\\"",
                    "RegionCode": "91"
                },
                "INN": "9108001581",
                "KPP": "910801001",
                "ClientRegId": "010037675048",
                "FullName": "Общество с ограниченной ответственностью \\"Крымский Винный Дом\\"",
                "ShortName": "ООО \\"Крымский Винный Дом\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "194.00",
        "FARegId": "FA-000000051103364",
        "F2RegId": "FB-000007078493663",
        "AlcCode": "0100376750480000179",
        "Capacity": "0.750",
        "AlcVolume": "10.500",
        "ProductVCode": "4011",
        "FullName": "Вино ординарное полусладкое белое \\"Шато де Весаль\\"",
        "ShortName": null,
        "marks": [
            "192309728208511222001PAZRF274WNKAHZ5YR42HQAMZC4AP3WQ4W6HFTXRSMXWD2TOYSWCPZK3U3H4PMUULGLUKEZNJQPP2GBOMVVJVH67HNAT2ZOI5QF2E6QVTO2GGOZXU6D3SEYUWVOB566XQQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРЫМ РЕСПУБЛИКА,г. Феодосия,ул. Любы Самариной,19,,,, | лит. П, В, Х, И, АБ | литер АБ, Я, подвал литер \\"З\\"",
                    "RegionCode": "91"
                },
                "INN": "9108001581",
                "KPP": "910801001",
                "ClientRegId": "010037675048",
                "FullName": "Общество с ограниченной ответственностью \\"Крымский Винный Дом\\"",
                "ShortName": "ООО \\"Крымский Винный Дом\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "311.00",
        "FARegId": "FA-000000054328060",
        "F2RegId": "FB-000007164527136",
        "AlcCode": "0100000005410000122",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"АКСАКОВСКАЯ МЯГКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187423838253271023001KWVFTC56EXYXISGQ6L2ZLBZKJEH7QUXAUEOCKR3UME5IQAD5BMGSW772VOLKGVRMLZTYTWFRCBCBADGD3MSMYE54ULNJYDCGF4GOUAF3OBRYILIYQW64MGVEJJMEKT26I",
            "187423838253951023001DJMV4WUSPCUB7DRT7VTIGJ577U54RGTYDGS7NXJXMAPA5PO47YECIWRXLERBKEYMTKWCJ7NQFJHKKDDAGB4N6CXZDLW6KMENII7672QDI3QXGM6P2LFJWR2K3NYEOULLI",
            "187423838254241023001HO5ODWHCBTJMJNFOSRMKCLJVXQKBE4BPUONNZMNIJTN5R5OQNLXRZFCEMMOMX56G3CEJR6LVIEOOCEKL6ZXSLO67AM7NW2I5XYG77LF2SHO3GSR3WRTAHPYLVTWK4IPEI"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "418.00",
        "FARegId": "FA-000000054299071",
        "F2RegId": "FB-000007164604993",
        "AlcCode": "0100000001400000078",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ПЕРЕПЁЛКА\\" ДЕРЕВЕНСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "1883036194736406230012MGB6VGDFCSHFTQ5RCXEBWK36MHHKGBRGUG7AW55JJMQMVN3GTBOWDUJO2MV73WA56WUFMY4TBJ4C6CKDQP3M32LO6YVZTHTEEPZWYQJWUXK6ARCCDT6W4MTWNA3AAAGA"
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
                "FullName": "Акционерное общество \\"Великоустюгский ликеро-водочный завод\\"",
                "ShortName": "АО \\"ВУЛВЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000053846179",
        "F2RegId": "FB-000007164605019",
        "AlcCode": "0100606942420000116",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "187427322801920224001JM5LOUS2UM7WKOKCFTAS5WMUWMRHLGRJC5SFFMCXXNBGKCNNXB6TQ54TUNG6QA5RI2DJLACRBN3BLHGF4UD24JQ5LO2DVPMZ5NMJ2GB2NL6X7E263GRINMIVMZOOAENNQ"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "90.00",
        "FARegId": "FA-000000053958694",
        "F2RegId": "FB-000007164605021",
        "AlcCode": "0100000005390000129",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк трехлетний \\"ТРИ ЗВЕЗДОЧКИ\\"",
        "ShortName": null,
        "marks": [
            "197406501329841222001AFL6DPCW7G4ZGQD266VDV5M7VAAPAH2ZB6CN4CQUYUCRUYZ6JTBRDHFMLCTES6PJX25BMO76P4E4PSURW3XXKX6YGUPEN2U3VGZAO5AXXXLGLZIKNP44NHAR2VEVYJ64I",
            "197406501330551222001UDARX6LZ23HREMNRGRGBC5C5JMIJPUFRPIPBKMMBQVBPJSDECYFBMC2T3MQXC6JEZDZUPLZKLADOUHWGP5PA7M75MS4LM7E7UEJMFG4JLXZYWEISEPWX6RFVRDKWV4HXY"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "327.00",
        "FARegId": "FA-000000054089318",
        "F2RegId": "FB-000007205567654",
        "AlcCode": "0300007181500000108",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Брестъ-Литовскъ классический рецептъ»",
        "ShortName": null,
        "marks": [
            "187423632925761023001UD5ZHCDSAPGRM2V4ADHXMSVYYMUF2PW2NS443HYLACSNAHCNFSR2D6Z2XVYFV6JMOXCRMHEJJUBCN6CP772NRQFCJDAHSJ5YSSFMCWXPK4CBBF7GQL5ZW2ZH3UQOQGQQY",
            "1874236329259510230014E4DMUSCAMZXJMM4FAKQI2NVT422ZAQS3AB7CXQRWPEABPIQK77WEHHXGV4HNB4NFYNXPNUZWMYAOOOIDADGAA5DCGJ7PG3KWSKUOM4CC22ME53E767XGPF4QOJ767SKY",
            "18742363292596102300136VIURRKP4FCAGV2MI3P727ITAUYSEUAS7IMO7HROQXPQKOWD3QJEOOMEKFPQETKWBH3M4NLTBF5EKX3TA2PGQBN7A5U7W33K3PGTELKRK2HHHCIGRPKQUU2EKZ77HIOY",
            "187423632926011023001PI6VBVV2EC435DNCBQIIGVXPCAC6J6CIBWWCJEQMX2VPLANKO4RZQUAY3EGE6W2J3MFZLGJ4AMC2S6CLGSFBIM6P2NOZMBPQFTHQXP5AUILGO47NTCTJKXPIZR22SBUNY"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "112",
                    "description": "Республика Беларусь, 224005, г. Брест, ул. Советская, 2/1"
                },
                "ClientRegId": "050000065686",
                "FullName": "ОАО \\"Брестский ликеро-водочный завод \\"Белалко\\"",
                "ShortName": "ОАО \\"Брестский ликеро-водочный завод \\"Белалко\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "301.00",
        "FARegId": "FA-000000053710624",
        "F2RegId": "FB-000007205567655",
        "AlcCode": "0300002891500000170",
        "Capacity": "0.450",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая «ХЛЕБНАЯ ПОЛОВИНКА» РЖАНАЯ МЯГКАЯ»",
        "ShortName": null,
        "marks": [
            "187320656859500623001M3KVWIXUJUWGNJ7CSRFFYIQLKMDRMCNPPURE2KXTT6SI4T6U4A5RID25Y4LDHTFQADW3N5UDDV6YEYXNQCO657GRI6TQBXKIE66BMIK2PZQNL72SHFHHVR4YZXH3FGECA"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "112",
                    "description": "Республика Беларусь, 246042, г. Гомель, ул. Севастопольская, 106"
                },
                "ClientRegId": "050000039845",
                "FullName": "Открытое акционерное общество \\"Гомельский ликеро-водочный завод \\"Радамир\\"",
                "ShortName": "ОАО \\"ГЛВЗ \\"Радамир\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "289.00",
        "FARegId": "FA-000000053950027",
        "F2RegId": "FB-000007205567656",
        "AlcCode": "0300002891500000114",
        "Capacity": "0.450",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ХЛЕБНАЯ ПОЛОВИНКА\\" МЯГКАЯ\\"",
        "ShortName": null,
        "marks": [
            "1874257833192612230013FGXEJQ5Z65SO4QBBPVALMLOAIBNKF3SOKW57K4KBEEZSJ252U35WYOIIHJHIFSPBFNIYXRRE5ZMBZMBMHXPUROERY7Q2LDZ36Q6Z4KJM26QZBZTUYFONJWZ2QZCHAO3A"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "112",
                    "description": "Республика Беларусь, 246042, г. Гомель, ул. Севастопольская, 106"
                },
                "ClientRegId": "050000039845",
                "FullName": "Открытое акционерное общество \\"Гомельский ликеро-водочный завод \\"Радамир\\"",
                "ShortName": "ОАО \\"ГЛВЗ \\"Радамир\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "200.00",
        "FARegId": "FA-000000052280898",
        "F2RegId": "FB-000007288686135",
        "AlcCode": "0100000003670000025",
        "Capacity": "1.350",
        "AlcVolume": "14.000",
        "ProductVCode": "4213",
        "FullName": "Плодовая алкогольная продукция полусладкая \\"КРАСНА ЯГОДА. РЯБИНА КРЕПКАЯ\\"",
        "ShortName": null,
        "marks": [
            "195302062024620421001UE4MOEW5CPGESS7Y3PWJHESZIABCZ2YINNHHEYEMIGOWSW6KAMWWIEPVYE5YJFB62LB3P4ZYA4MKTMTCXODPW7QK7P7776DLJI3ZC7JKLK2FXJFDD5FQO7SPK7IOV6TPY",
            "1953020620246504210015QVETMNLFWEAYISPCGJBK4FIYE43YSJFPE6K765F7JIYVZAQUBAGTED6AHNV2C37QQQFLDTMYHKSV6TD5HN5SMG6XIAF45PCR4F5YJTNX2VB6MX6UV4WW5O6FFWHBZ54I",
            "195302062024830421001O7HF56TX4CI6WWY4QSQR3IJWGYRLQOCTTECSRQFMHYDLN3PJL3WML3HE6WE5632C4JZWVUPVCOM2RKEBBV3HLQ4BSDPHPPG47F4Q4ZMMVKA3GJ4OMUAI7ZW4CHT7M7T5Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Кабардино-Балкарская Республика,Чегемский Район,Чегем Город,,Героя России Кярова А.С. Улица,34 Дом  , | (за исключением здания склада готовой продукции, нежилое, Литера И, помещение № 1 (S=1019,0 кв.м), Литера И1, помещение № 2 (S=429,7 кв.м)) | здание склада готовой продукции, нежилое, литера И, помещение № 1 (S=1019,0 кв. м), литера И1, помещение № 2 (S=429,7 кв. м); административное здание, литер А, этаж 1, помещение № 6 (ЕГАИС)",
                    "RegionCode": "07"
                },
                "INN": "0708009579",
                "KPP": "070801001",
                "ClientRegId": "010000000367",
                "FullName": "Общество с ограниченной ответственностью \\"Эльбрус Спиритс\\"",
                "ShortName": "ООО \\"Эльбрус Спиритс\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "301.00",
        "FARegId": "FA-000000053710624",
        "F2RegId": "FB-000007288686158",
        "AlcCode": "0300002891500000170",
        "Capacity": "0.450",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая «ХЛЕБНАЯ ПОЛОВИНКА» РЖАНАЯ МЯГКАЯ»",
        "ShortName": null,
        "marks": [
            "1873206568526106230015F2VV3YBOPQPE2RQUHV6FRAZJMB37P2KHU52JXNRLETHXB3UGTDZSIRLYIYSWT62KROWPLTXH4LD343E5FP32GVWKVNQ63UL3EZBLOTOJYJ5RN5PFL6LLGC7RVADMGHTA",
            "187320656852810623001MWZNIGOJEVZQXABU34KVHLV2A4V7GQVKDSCFRO22NXQEAAN2HKVP5KU3XI3IE3BGJO2UN4K2JZIOAWXI2PSE663LKCZB2IGYCXIALKXM7QGIVDU5SJDUKKZT7K3RHCHFA"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "112",
                    "description": "Республика Беларусь, 246042, г. Гомель, ул. Севастопольская, 106"
                },
                "ClientRegId": "050000039845",
                "FullName": "Открытое акционерное общество \\"Гомельский ликеро-водочный завод \\"Радамир\\"",
                "ShortName": "ОАО \\"ГЛВЗ \\"Радамир\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "289.00",
        "FARegId": "FA-000000053950027",
        "F2RegId": "FB-000007288686159",
        "AlcCode": "0300002891500000114",
        "Capacity": "0.450",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ХЛЕБНАЯ ПОЛОВИНКА\\" МЯГКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187425783319031223001C73OVRZKJAGHYK2QLGNMEWKCOA7OPZQIH6ZB324RKGR5GQ4PFS33BNVBWLWUZHZB5CNR3WMDHGU5LGZPIG24G2QDS3WQPHDG5WD5DIPGI5WQSM4P67DVA55VMD3KTAXDI",
            "187425783319061223001KUT6PZOQ3BN7IHZGFNE5RKRQ34PM6YDH457W6JHI5NNRJTIT7OVPSM7YFOSQPJRRV4MZCKV6NRKUQ3C27HLXB2LNIEGOCB7PQNTV3DECAOG66QNHBR2PKBCAI7QVAUUTA"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "112",
                    "description": "Республика Беларусь, 246042, г. Гомель, ул. Севастопольская, 106"
                },
                "ClientRegId": "050000039845",
                "FullName": "Открытое акционерное общество \\"Гомельский ликеро-водочный завод \\"Радамир\\"",
                "ShortName": "ОАО \\"ГЛВЗ \\"Радамир\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "221.00",
        "FARegId": "FA-000000052851271",
        "F2RegId": "FB-000007331199926",
        "AlcCode": "0100000005410000008",
        "Capacity": "0.250",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\"АГИДЕЛЬ\\"",
        "ShortName": null,
        "marks": [
            "198412742599210323001K6JAF4RNQUXB4CVJ44VHXQQ764QCKUXQWKZYTGJJAJZGYJKN54WUYTZESZMZT3V75QWQJDH4PJEDYC7DL5GJHQWQSEXVNNFNIKZCBIEBDP4SEW3K2GL3OEV2YH5VVO4DY"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "116.40",
        "FARegId": "FA-000000053218614",
        "F2RegId": "FB-000007331199928",
        "AlcCode": "0100606976440000104",
        "Capacity": "0.500",
        "AlcVolume": "14.000",
        "ProductVCode": "4213",
        "FullName": "Продукция плодовая алкогольная полусладкая «КРАСНА ЯГОДА. ВИШНЯ КРЕПКАЯ»",
        "ShortName": null,
        "marks": [
            "195302474263150622001JWSX7PWUS623NQ6UFTBTYYC3GQGMIEZPI6L2VMQIKZNEW7Q47YQDTMOTC4UBG766XD3EC7JJSL6EGW2FTIX667LTLIBZDIALAC4Y7VKRZOHNWSZDKTLLE6EO4KECYZS4Q"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Северная Осетия - Алания Республика,Правобережный Район,Беслан Город,,Первомайская Улица,224 Дом  , | нежилое здание Литер Д, общей площадью 14784,2 кв.м (за исключением помещений: № 2 (S=1301,3 кв.м), № 68 (S=698,8 кв.м)); нежилое здание литер Е, общей площадью 7884,4 кв.м, (за исключением помещений: № 1а (S=1198,7 кв.м), № 1б (S=1303,6 кв.м)); нежилое здание Литер Ж, общей площадью 2232,6 кв.м; нежилое здание (литер А), кадастровый № 15:03:0011023:722, общей площадью 9960,7 кв.м (за исключением помещений: № 1 (S=1351 кв. м), № 17 (S=10 кв.м), № 18 (S=44,7 кв.м), № 21 (S=37,8 кв.м), № 22 (S=39,1 кв.м) | нежилое здание Литер Е (за исключением помещений № 1а (S=1198,7 кв.м), № 1б (S=1303,6 кв.м), № 23 (S=863,6 кв.м)); нежилое здание Литер Ж; нежилое здание Литер Д, за исключением помещений № 2 (S=1301,3 кв.м), № 68 (S=698,8 кв.м) | нежилое здание Литер Е, кадастровый № 15:03:0011501:22, общей площадью 7884,4 кв.м (за исключением помещений № 1а (S=1198,7 кв.м), № 1б  (S=1303,6 кв.м); нежилое здание (литер А), кадастровый № 15:03:0011023:722, общей площадью 9960,7 кв.м (за исключением помещений: № 1 (S=1351 кв.м), № 17  (S=10 кв.м), № 18 (S=44,7 кв.м), № 21 (S=37,8 кв.м), № 22 (S=39,1 кв.м); земельный участок с кадастровым номером 15:03:0011103:54 площадью 6156 кв.м с вертикальными биметаллическими емкостями (зав. №№ 00220 - 00231 | нежилое здание Литер Е, кадастровый № 15:03:0011501:22, общей площадью 7884,4 кв.м (за исключением помещений № 1а (S=1198,7 кв.м), № 1б  (S=1303,6 кв.м); нежилое здание (литер А), кадастровый № 15:03:0011023:722, общей площадью 9960,7 кв.м; земельный участок с кадастровым номером 15:03:0011103:54 площадью 6156 кв.м с вертикальными биметаллическими емкостями (зав. №№ 00220 - 00231); Республика Северная Осетия-Алания, м.р-н Правобережный, г.п. Бесланское, г. Беслан, ул. Первомайская, д. 224 \\"б\\", нежилое здание строение А9, кадастровый № 15:03:0011501:27, площадь 34 кв.м; земельный участок с кадастровым № 15:03:0011103:185 площадью 1658 кв.м с резервуарами типа РВ (зав. №№ 201, 202, 203) | нежилое здание Литер Е, нежилое помещение № 1б (S=1303,6 кв.м)",
                    "RegionCode": "15"
                },
                "INN": "1511027798",
                "KPP": "151145001",
                "ClientRegId": "010060697644",
                "FullName": "Общество с ограниченной ответственностью \\"САЛЮТ АЛКО\\"",
                "ShortName": "ООО \\"САЛЮТ АЛКО\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "185.00",
        "FARegId": "FA-000000054309560",
        "F2RegId": "FB-000007331199930",
        "AlcCode": "0100606997860000425",
        "Capacity": "1.000",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое красное «Домашнее Кубанское»",
        "ShortName": null,
        "marks": [
            "192314375630381223001JIP4AFHVFJ2XGL5GS62OURR6EI5KCXOCAVEXBERNFRIEZGWNP6CRXJQGXEUFHYKPLTG7QNDVCEOVPO4VL2ESUEYJU24ZJ3EAWUMQEU65I3VREYX4U5OEUKI4KVLX33ZUA",
            "192314375630441223001VFQF2BUNELLGIPNV37OCAUPVFYECAU43V5SBZ7WZZOP4OSWTI2VDLT6MC7UP5SWEITAYDGYI5L2HUO3HSJPKJQUJITHEY3SJP2BUKBDBE6RNZX3BGTQJ6KJ5WWVLOMUCA",
            "192314375630501223001PB5HBRJAORJXQXJ5PN2TL6CN6EHSXXMXCNCFLOCV5IGPX656CJYPHNT46NEETTKBC6S7XLRC5F2WXN2XOXX7ZWLJWPSNAIO6Z4VE5EYKG6I6AFVQUF566LYBIJCVAE4TY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Краснодарский Край,,,,,,,городской округ город-курорт Анапа, с. Юровка, ул. Октябрьская | :д. 1, кадастровые номера: 23:37:0501001:3921, 23:37:0501001:4250; д. 1Б, кадастровый номер 23:37:0501001:4253; д. 1Б, строение 2, кадастровый номер 23:37:0501001:3603; д. 1Б, строение 3, кадастровый номер 23:37:0501001:3602, д. 1Б, строение 4, кадастровый номер 23:37:0501001:4248; д. 1Б, строение 5, кадастровый номер 23:37:0501001:4251; д. 1Б, строение 6, кадастровый номер 23:37:0501001:4254; д. 1Б, строение 7, кадастровый номер 23:37:0501001:4249, д. 1Б, строение 8, кадастровый номер 23:37:0501001:4246, д. 1Б, строение 9, кадастровый номер 23:37:0501001:4297; д. 1Б, строение 10, кадастровый номер 23:37:0501001:4252; д. 2Б, кадастровый номер 23:37:0501001:2337",
                    "RegionCode": "23"
                },
                "INN": "2301076247",
                "KPP": "230145001",
                "ClientRegId": "010060699786",
                "FullName": "Общество с ограниченной ответственностью \\"Винзавод Юровский\\"",
                "ShortName": "ООО \\"Винзавод Юровский\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "249.00",
        "FARegId": "FA-000000051579803",
        "F2RegId": "FB-000007331199931",
        "AlcCode": "0100607004990000022",
        "Capacity": "0.750",
        "AlcVolume": "12.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое красное «Бастардо»",
        "ShortName": null,
        "marks": [
            "19231122007738122200122A3DJCWCWLRNJHPNS2TLAR4XMLNAO33C33W5FECNWMALKSMKNGA7MXNF5A6SHK6ZK43KJMGJCRBKDP6JGJQMTY5GGXURFILF6L5A5HISBOO4OB7IRLLXKRN3P3MNT7KY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Крым Республика,,Симферополь Город,,Московское шоссе 9 Километр,, | (за исключением: помещений №№ 8 - 19, 21, 21А, 21Б, 23 в нежилом здании цеха розлива 2, литер Ф, 1 этаж; помещений №№ 5, 6 в нежилом здании проходной № 1, Литера Щ; помещений №№ 1 - 21 нежилого здания заводоуправления, кадастровый № 90:22:010601:505 (литер А), 1 этаж)",
                    "RegionCode": "91"
                },
                "INN": "9102257636",
                "KPP": "910201001",
                "ClientRegId": "010060700499",
                "FullName": "Акционерное общество \\"Симферопольский винодельческий завод\\"",
                "ShortName": "АО \\"Симферопольский винзавод\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "303.00",
        "FARegId": "FA-000000054418861",
        "F2RegId": "FB-000007331199948",
        "AlcCode": "0300006342850000048",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЛЕСНАЯ КРАСАВИЦА ЛЮКС\\"",
        "ShortName": null,
        "marks": [
            "1874279036728704240016J4SRL5FB44FHHN2O6ZLUKQ7KUCNKWYJOOQBLCI372YARTE4SC3TZ6CROEILHXWHNMVU2BSKHVXZQOSXWPFQAHCSDN27BVJWXXCU43FQXKAOMLDVACHGORGDE2A3EUMWA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "310.00",
        "FARegId": "FA-000000054644911",
        "F2RegId": "FB-000007331199961",
        "AlcCode": "0100000020360000163",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ №1\\"",
        "ShortName": null,
        "marks": [
            "187324122194660124001U6TO33LH7OWSYVZUZEJ5EUISJQYGI32YOKAZEX5OBKTXMMO3QYZE2SJZPZNR6OWQWAD3YGQTLWSR4YMYZTCX5FCY77PRWCK54MVNOTCLN72MSR7KI4SO255NWCFOI2QUY"
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
                "FullName": "Общество с ограниченной ответственностью \\"Русский Север\\"",
                "ShortName": "ООО \\"Русский Север\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "249.00",
        "FARegId": "FA-000000054340677",
        "F2RegId": "FB-000007331199970",
        "AlcCode": "0100607004990000022",
        "Capacity": "0.750",
        "AlcVolume": "12.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое красное «Бастардо»",
        "ShortName": null,
        "marks": [
            "192315661284101223001KZKYJPCIVYYJ7SHRUQHVJILJGQEIPOF2ND3VFIPZXVNJFSV3IJPO4C2PMPCYXDDD7EM5TNI45CCBADR62S5GDO6TELZMUEPCP4TKVUAQ4HJPRBLLEOCFUPWL4XTTH6V3Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Крым Республика,,Симферополь Город,,Московское шоссе 9 Километр,, | (за исключением: помещений №№ 8 - 19, 21, 21А, 21Б, 23 в нежилом здании цеха розлива 2, литер Ф, 1 этаж; помещений №№ 5, 6 в нежилом здании проходной № 1, Литера Щ; помещений №№ 1 - 21 нежилого здания заводоуправления, кадастровый № 90:22:010601:505 (литер А), 1 этаж)",
                    "RegionCode": "91"
                },
                "INN": "9102257636",
                "KPP": "910201001",
                "ClientRegId": "010060700499",
                "FullName": "Акционерное общество \\"Симферопольский винодельческий завод\\"",
                "ShortName": "АО \\"Симферопольский винзавод\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "169.00",
        "FARegId": "FA-000000055040506",
        "F2RegId": "FB-000007373996472",
        "AlcCode": "0300005907900000239",
        "Capacity": "1.000",
        "AlcVolume": "13.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\"Афоня 777\\"",
        "ShortName": null,
        "marks": [
            "192315519388281223001ENA6KJGRRWRSRL5GD4HVMMLZQ44R7LT75RDRD2U6YIJBW72LCEUTXNDZZXWWQFI7DVYLQCQABH4FCRHMG4Z42M3D4NOUXIHGUVQKV4ASCGUBEFLN56GWXJNUH7LNICUVQ",
            "192315519388471223001MWFU2KTE6ORVMJFIXUVR2WFDKY5AJOMIHCXZFCFL23XLTKTIXBJS7PNKUMHFTU4SS4DTOVJDBV4BCDS5PYSESJ3JRRTDBMY6OH7POAACQJJJD4MQGODHUGLBVZF52VM3A",
            "192315519388541223001DY4XNZLXPZQOGRPD7KEEBCECC4QY3AU2IQD4WQB3PGPCN6HJHGNRYGWT3UPPDZEOLUT6N43OGXZJOIJIPMLRQUBRDJHIBCQ4U3WNWD4ZUT27IYCSLSIZXHIAE6P6NAJTA",
            "192315519388821223001XQJADTOM5G7F3LTYKGQ57SCZOIIULEO2GWYWWK2NS7GR4JST26ML7MENBR7HCGXJ5T5VNY3SXE54KL72FG7ETZIVSWHCMUP4FI6FAN6MCBIBEKIWFXSCSPQTFRD7BYBKA"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ставропольский Край,,,,,,,Георгиевский городской округ, г. Георгиевск, ул. Чугурина |  | 9: строение 1, кадастровый № 26:26:000000:2072; строение 3, кадастровый № 26:26:010219:206; строение 4, кадастровый                                             № 26:26:000000:2063; строение 5, кадастровый № 26:26:000000:2064; строение 6, кадастровый № 26:26:000000:2066; ул. Чугурина, 11:  строение 1, кадастровый № 26:26:000000:2068; строение 2, кадастровый                                № 26:26:000000:2067; строение 3, кадастровый № 26:26:000000:2071;                 строение 4, кадастровый № 26:26:000000:2065; строение 5, кадастровый                      № 26:26:000000:2074; строение 6, кадастровый  № 26:26:010220:116 | 9: строение 1, кадастровый № 26:26:000000:2072; строение 3, кадастровый № 26:26:010219:206; строение 4, кадастровый № 26:26:000000:2063; строение 5, кадастровый № 26:26:000000:2064; строение 6, кадастровый № 26:26:000000:2066; ул. Чугурина, 11: строение 1, кадастровый № 26:26:000000:2068; строение 2, кадастровый № 26:26:000000:2067; строение 3, кадастровый № 26:26:000000:2071; строение 4, кадастровый № 26:26:000000:2065; строение 5, кадастровый № 26:26:000000:2074; строение 6, кадастровый № 26:26:010220:116 | здание 9: строение 1, кадастровый № 26:26:000000:2072; строение 3, кадастровый № 26:26:010219:206; строение 4, кадастровый № 26:26:000000:2063; строение 5, кадастровый № 26:26:000000:2064; строение 6, кадастровый № 26:26:000000:2066; ул. Чугурина, здание 11: строение 1, кадастровый № 26:26:000000:2068; строение 2, кадастровый № 26:26:000000:2067; с",
                    "RegionCode": "26"
                },
                "INN": "2635812087",
                "KPP": "262545001",
                "ClientRegId": "030000590790",
                "FullName": "Общество с ограниченной ответственностью \\"Лоза Ставрополья\\"",
                "ShortName": "ООО \\"Лоза Ставрополья\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "225.00",
        "FARegId": "FA-000000055045973",
        "F2RegId": "FB-000007373996473",
        "AlcCode": "0100000001740001178",
        "Capacity": "0.700",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое красное \\"Изабелла прекрасная\\"",
        "ShortName": null,
        "marks": [
            "192316083246820124001KSLWF3ZGCUBWSHDX7MBDJNBQGU4WMCA4Z5NHPFG45WWQ63NECVVTLDWEUTDRTWT3RDXOY4BCPNFVTFJU6FIA56UBTWVMESL46DP2KMKO7OK263LOC2JBXSN6PULMPEXFA"
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
                "FullName": "Общество с ограниченной ответственность \\"Долина\\"",
                "ShortName": "ООО \\"Долина\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "225.00",
        "FARegId": "FA-000000053749761",
        "F2RegId": "FB-000007373996474",
        "AlcCode": "0100606973030000507",
        "Capacity": "0.700",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\"ЛОЗА БОГИНИ\\"",
        "ShortName": null,
        "marks": [
            "192314022842810823001ZALC2LZE2OPOLU5CFPGOBQG7DA5CK2T3SUK7UVDQGHNSOUT6WRIEWTIYBIGRWCJLY5HJ6ZMSNTUUH5DTDTUI64F3JCYCXUS5LDJTNTUS6ZC4GG7LTKXU7QQESQ3F6LFII",
            "1923140228429008230017EWQUTFG4AXT24SSOBMYODFLJIACX7JDBP23AYETTWT23MBJQBJQKJTZM2UU2EGDQMXNNNAFP6J2Y7CS5LPLPKCK3EBB2VBWUKI46HRYV4RUNH4C6KZ7ZWAEPGGVU4GOY"
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
                "FullName": "Общество с ограниченной ответственностью \\"Прохлада\\"",
                "ShortName": "ООО \\"Прохлада\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "270.91",
        "FARegId": "FA-000000053724851",
        "F2RegId": "FB-000007373996476",
        "AlcCode": "0100000054580000047",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\"КЕДРОВИЦА НА КЕДРОВЫХ ОРЕХАХ\\"",
        "ShortName": null,
        "marks": [
            "187322488119030723001V6I4UZOFHCNEERV3L2YOYUTAZEJSAW2HQCS25QFDWY7RLF7NJMKPMHQH6LJDVG4AY22TCTM7NTJ2A7DQNNCIOOXMSSVLZOMGW6P32256O7KFGGZEDKC7MYDCIX5RE7WBY",
            "187322488119090723001ZLSNH5AVWJS3KCO4PIYJMJ7SRA6O53MAVOAEDWWYNU2ERNQATYK5TCRJFVF3EPGDCSXU6YXQGNXB35OQQTMPIO52JKMA4KZGHPFQJEJULR35IQJWNKCNFH3A3QEWPWLNQ",
            "1873224881191507230013EJXVEOH6AVZ5NLYXPIAJNEQJIY3G6LCNLUEGTASWJNPJHYNLV2BWTPYT5IU7GUS6JB7BLHP5UT7XTI3M3ITRL7UP5WZYVPARRVASPU3JBATU4RRQPAEJFBSABRHRBZ3I",
            "187322488119170723001KX2QGR4U4YT5NGTAQ5ZGW7GXBYFKE7IK2S7STSX3RI3RR6664QJINR75U6KTN4QEENRS4OG4QAVUXY5W3KXD3YRPN34GS32GR7ROMLROQR5ZNYZW3NU4GFB32SEKAVXYI",
            "187322488119190723001O3ZIVAF3VN3GNRRJDLYCJYSNSAJL36NN3D2OLIUSROTX6I3SAFP2R2MDSZ2ZKQTS2OMVKQACUJCSJEJYG5K6OS3MLPNFZCD77K7EXLUCGZSOLJH4QQPLVLNU4MQNHWEAY",
            "1873224881192507230013BRDLPY7LN7NGATUWJCEKH5DLQCYFS43C5X6IEMMGFZZNWAE4HGTMJH2BOEVJ7RLPN6GSVHY74SZSQ6G7QWLIJUD4UJAHDO3SJSBGB2SIIYZKELZSTA5R3OC43RYAYDZY",
            "1873224881192607230012HOLKAWKP7OWFV3MQQMA6VIN34BNUE7BP4WWRVPPV6D5FTM4JZ4U6QCAF2IB6XT5VVGTQ7ATSGAHNSXUS7UNCU33XMCQEBD756IJ47SOOIN2P7GJRPQDSVH7AG7H3UBRQ",
            "187322488119370723001PJ7HEZOR4U73HDIZ5A53LIR63AUMSAT6LLTUB7XVJWU56IYKPEU7POWMYVLESAEUPCIBZV2K3SCD4PDP4E2RLY2YZA4DEEKU6SKZCPXHSX565XTZXYB34L3BYRAXRXXPQ",
            "187322488119460723001MDGFKOGUFKN2O2AFDTHFA6ZGHAQGGB36IACVP4RHL2275BJRXG5QN5HMKVG3YSKAOCJXEFCNZWEPSEETO6M5IAK5OODZUMOKNLP5NK6G6GVXB4N7QU3DBIIRLK2CDWMSA",
            "1873224881195507230012NM7BCRX4EYIVNOFEKZQW6DGYQQW5OD534MLEV2UMICDMGTVDR7RD6ERLREVLHGC4TLBZKIFOSNOA5IPRZBWXBM6EGYEVCN22GUO3TCEWAWO42UYIZ5C7AUYAJ5XZHPDQ",
            "187322488119590723001IYX32IOSQRSRMLIZLRF3ZQS2SEFQKBGTJRUMZWS6225HPFL6Y4NSTY4SABUM6C5SQR4DT7VY2FNMMD2XBLBTMBXH7236EHVP4HEV562VZFR72MFWTH4M5C6Z5W45IE2EI",
            "187322488119610723001D4N5VJTG4PAGMXJVQ7MOOAQBQEK74DZZT25TAF7CIV62HYC2NJG3IFMT5GY7IEO32YGQDWLWQK3QCGUGDPH57LHLWWMY5NLT6XSUMYPP4ENKZMGCSPFYVQ64HJIEYUNMA",
            "187322488119640723001KNK6DUC2DD5LUTDMCOIV6ETFWQBGMBJBIK75NEJFCU6HUIAM2ZEM2I65NRSPIVGO3AZGU5TUSW646M2ULC2SJZLNLBH25UUJZ7SDFMIYLQQTCLNSVPUDW4724VULHPSKQ",
            "187322488119980723001ZXH55CII7XPKMI2HRW6DFBM5IAQA37RNFNMX6DJP4VAAPXSLGNPK5YGLLWK2LCFPOTWFAYNPCQQS66YPJNE2PMLGYRQ6T52MIG46SQDTABFEHYA6ZYVSVON4OU6KA7IPI",
            "187322488120000723001HJZWVCPVJT5XR2CXYVJCCYRXSUVWKLU6IK6HPPS4HFUT5I2CYN3REBPL7HGLA3RC2RYPFJXI5QFBFEMUM36ZGNM7TBHMBKPIRWJ7JUUS4Y2QWO2GBZBHJF65LEE5YVUGI",
            "187322488120120723001Y5BDL4CLCALZTTDCJXAV6AOKK4YJ6BLLLISMUZUPARKWTZKKALEWNQDKMC7E2OJZAUU36X6AEGNSPNJCS4L63KS4VVE2UKAE64ZEZORCQ2DTQLMUMDPFGBPDFQYHFTL2A"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 16
    },
    {
        "price": "285.33",
        "FARegId": "FA-000000054336997",
        "F2RegId": "FB-000007373996478",
        "AlcCode": "0100000054580000220",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ПЯТЬ ОЗЕР\\" СИБИРСКАЯ КЛЮКВА",
        "ShortName": null,
        "marks": [
            "187322980730160723001EB4A3F4S5GEQLM57OFOSMEIPZQJLXWRURHLIL7FKWER3HD3QP32W76BAQHBMTZSX4MD2R3UFIJEAJNCWMQU2GHBDNP5TH26TQG4KX5LNRINGYRTDY52VWQ7JDXLDMYVMI"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "285.33",
        "FARegId": "FA-000000053478668",
        "F2RegId": "FB-000007373996479",
        "AlcCode": "0100000054580000020",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ПЯТЬ ОЗЕР\\" СТУДЕНАЯ",
        "ShortName": null,
        "marks": [
            "187322149846210723001VU7XRAZ5E4W52G5NDCL6XFVDDA3CI67VWDWRVHCRG7ZDYPQAFLRASCTTUYP7KHJDSNO4CLO3JOIW3HG2NH637TFMW6UWAR45PXHMK4T2TN2CCIZQU6ITFV23HIKIGZMUA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "319.61",
        "FARegId": "FA-000000054111443",
        "F2RegId": "FB-000007373996481",
        "AlcCode": "0100606933430000077",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая «ХАСКИ СЕВЕРНАЯ СМОРОДИНА»",
        "ShortName": null,
        "marks": [
            "187323568798881223001TPQFGC44BH7ARUXQNGQZCEVWOQNW5URVB2MRQ3W3V5VRICC7U4YLBGWWOI762Q63WBY7CAJR4PPOHGIV5RJRU6XRW2XER6PASV3ITTDWQW5LOAYIUKFPEAR3IGWJAAMJI",
            "187323568798971223001KDNCUKAUKDS3Y7PWLZFWF2YIDYECS2S2S237S52SWNLESW4WFOMQNJ7CORT4QHHFAVXWFAFMBA7PH3QXW4BDDNMTWWDOMMRNC2WVELB2GKFIROBTVF7JA3WIPHFW5X5PY",
            "187323568799161223001CI4NS5EHOIJAJMWOX6MHP2MA7EPGRRBR26UAC32LQ5QYN2FZZPBC2YOQ3X3EHERVKRQFPCHJEY4PVU7PEN2RZNCI7CLARXKG6PSKZ3QX4G634SOEVEHROAXROQCPSKUOY"
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
                "FullName": "Общество с ограниченной ответственностью \\"Рузский Купажный завод\\"",
                "ShortName": "ООО \\"Рузский Купажный завод\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "166.37",
        "FARegId": "FA-000000054987678",
        "F2RegId": "FB-000007373996482",
        "AlcCode": "0100000054580000011",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ХАСКИ\\"",
        "ShortName": null,
        "marks": [
            "198313969488080324001TEJNS32VAGHMNOO5OFDUCPRSYA6KKYNK5NGPXQKZLLCTHCTNTOK4IQ5HMCO3L2PGQB6QWMYEK66ISUFDYQZTALNBMOC4IQIKQLWVSA4JNB2WTEO4HUHDM36BT6OJFLWDQ",
            "198313969488170324001QWZ326PFH6MFLSCF4FUWOJRIO4HFJFBMUIAWZIXMKJN6ZRYOQ7OAPNMN3TZX5H5OYPHJRKKVG3Q3O7C5V7KUSQ362MS75KUJEIH3BPY7NEM7RY5U3RF3TONHKYN4KSTYQ",
            "19831396948819032400166YOMGYDVOAKOWXWHFJCJR3BL43ZHEXKXUCLNZUOLKHM2LERJ464XDH7QAVEQTOXXRE4VE7QN7C2OG23A4UB7OATB7G4MKOR2R56L3INXOMMX634O24LEO7LKQXBSVRGA",
            "198313969488210324001VHIJA56UTAWQIYD7UH5RULXLTIZ6746YXVHRLVJ6AMSE4GCTU3FPRMGXFWNIILL4ITXPFOGEIZA7O3E4CJZAJJPKN2Q23EIXSCJNLZLMBHFCP7S73PJV3D45DXD3LMATI",
            "198313969488220324001JFRMTLOFES3PCQOD5A5XFIFXIIXDDJFRWBVB7J7PBO2PIX52KCROJPOM7HZQPQGXILO4EEMOAZ3QCGB7K3JLWCBOTVWN72LRMARPA6CGUZXPIIVDSJWHEMHTJT5BVCRDQ",
            "198313969488270324001NBHW4IYHZGDZLR4577KVT36UXIYOCGRSTCFZWDMLSRKSSTL3O6UUZ2SPTK3PRPK7UF43RHYBXVTMPRRNMRWYZY4CPKJG4IYYQBTDVZ3EVWP37QZBCU72NUNYC3ERBSA3Q",
            "198313969488290324001ILDDVKM3YQLHDEVPIRDYPPOZTA6VV5Q2AZOXZ2BI7HQJ6QAPKWTU2HSEMNURD6GLKDCVJKS74AMTE3QULYJGWLMNI3GZMFQXKPHNYCBV2TQQ4KEMWQNTTZCH6TZJ2MS4A",
            "1983139694883003240014QYUKRZRS3FFIPWU26HVULQHSUY6YZO7ZC3PHQN6RWJRTCFNPQIHICBIWBPVGHGOHEE6NTY6SF6PHKZVO6IU45ARJDVYJPG532ZXJZJIOY5DHROGQJ5VO34MVRFHOFAQQ"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "320.50",
        "FARegId": "FA-000000054826519",
        "F2RegId": "FB-000007373996483",
        "AlcCode": "0100000054580000013",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ХАСКИ\\"",
        "ShortName": null,
        "marks": [
            "187325021110630224001IGXFY33W6FFQ3CCGH4RIH7HUVQPCYHN65QBC7Z4JZXDZMO77UHFVLGPAP4VELAZYLMSABVZZZHMXG46PQFNJLFZ3IL6MHVBH4OIYXFYI23PKEDB72BDEBM6OKBWVZR4PA",
            "187325021110650224001IBVDIPUTR75V34WZUMQLQNTWAM6CXEMO4AIBGJKDGD7DQSENFGPOQODZHVU5HYUSVJ4VJDDQGZGSSZ4G2DWZYDQTYTJMTC5EDAPFGSCTO3RSGVLNJTYD2HNFIVFCEOVNI",
            "187325021110730224001EON3CFJVMGLSUG5HHPVB3BMAWEZICGKAJZBK4NWJAHUPEFM5YYYFQYADMBU4LG2OGRLJFC7TMVA72ZNW744ZAIZDWIYIBVGGYPRNGN6YBRMFXU7HYOH7W6S6XP7SUEAPY",
            "187325021110740224001BYLMTZVDH5U7UNNSJYZZPMWITYILIOC2HQ7CVTC5DDXRKIDUEOS7UV7BEBOMOROYPSK26NGCQ2NLDJYG6HIM5PXNR2CKTYC5VJP3V54PXUNJDI4FFEUEQNOAITQ6NMIOA",
            "187325021110890224001GFSRP6MYUOQP5R2GQBEGR6ENUYQBIP6WX4ZSGRSHGTXQOOEKNZTXAISKLQUHG5DNOTBT7VCJEUUOPFA2IMULHFWWC5OR7KRT63ONBQSUS4KQBVGY3566I27INM5YOP3QA",
            "187325021110910224001W2IPTLQQRT3H6KLZG7X7QNE4QU3CG4RG6AIYPNBNJPQ4VETZ64TNW5UN2IRX7O3DWZXR5N4BGEWACVYNNMHGWEHAH4ZPRGSVEGOAILO6TBCTAA3VLBZT27NP7UJ2SQXVI",
            "1873250211109202240016H62SQUKMPLWOZIPEOWIM2PMYAJSA5CA2MOG4KDX7SEOAFHFZ5B74IGZOEFG6OA3KYKA6XSS63R7R64KE4YPV6KZJ2ECHWZDESDL25OXI6YZAUUBG25V4CP3CJD6NCVWQ"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "140.00",
        "FARegId": "FA-000000054861268",
        "F2RegId": "FB-000007373996485",
        "AlcCode": "0300003247940000090",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Три Рюмки»",
        "ShortName": null,
        "marks": [
            "198417095594560724001HQ7I3DP4IJ5LZIXWN5QZHK7ZDAR2SEMNMVGOXN64ZDTAITUGJYVTQJSHHX3GCJVN6GMY5SZ3CQJLQSZUY5IHXZM4IRRPTZCKMHQVT5257T2IEW4QVRRPGESEUKLKEBJMI"
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
                "FullName": "Акционерное общество \\"Озёрский спиртоводочный завод\\"",
                "ShortName": "АО \\"ОСВЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000054585863",
        "F2RegId": "FB-000007374078854",
        "AlcCode": "0300006342850000054",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ФИНСКИЙ ЛЕД. ФРЕШ ЛАЙМ\\"",
        "ShortName": null,
        "marks": [
            "187428208697850424001BPVGJPD4Y6DRFOALMWWGAKT424JBGFHDJI25I5IUB5QPF2JJ6RINN3CA546KBXCBQEECZAKANTXB6L236TDIWCXPWBFB3OJOWMBRIUJHCFQK4MNJZN2G3NVWBVLKMOVLI",
            "1874282086979004240014ANGSRN7TB4PFDNDSYKU7STM34LTTKYGZABVQJFVHRY62DV67B7S6SPRH7627VHLXA76BXAULJDH77GXBSEFO7CABV35YAOEAK2HXDHYNK7AVWETRWXQUJQBOFKZ4LGAY",
            "187428208697960424001TVYJVLRNS3M4VITO6ZYCZPQ2LEU43QIZFTZVCEP7V4P722R4K7YO7WMX7F6RIBQTUVZOJLBN6NI7QHYKEOZVU3TGYIO7G6KSEMD7FKM5TONABZE5ADCV4QFMB7OR3J4VQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "418.00",
        "FARegId": "FA-000000054299071",
        "F2RegId": "FB-000007374078859",
        "AlcCode": "0100000001400000078",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ПЕРЕПЁЛКА\\" ДЕРЕВЕНСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "1883036194720006230017IX67AWBQ2SXWQEVUEWKFQCVMAEXVTUBPC6RAMSMLCL2PU6KSWWFI5T65IP3FF7N74KOKEZXUAYWKFIX7FFXPJKSEQBD5BYXFCLMNSFTJGNEZDPUJYGRCUEIPHII2WZOY",
            "188303619472260623001VGBHPLCHH4U7E4MA3ZLNRI4J6QCJTGM6SEKQX3RZCWRCIDXIBUOHTVYACWKZUMI5VVGUNWZQCI7UG66Y64LIV6LWD6ESAOMXQKQKPHKDYVQA2EWN3OO5W7X2C773A5YTI",
            "1883036194726606230012S6K6XMUXQJQGVX7TKLTY34KDMP4K6OHVQTQCIJOCPU2QGNTFLHBBHL3KGQYQOPFGIXTLM2FF57UR3DAVQS5NYQOWXRQZWCDZVBXO6MS5L7WIUN2TTGYIPZSNG2XSTDDI"
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
                "FullName": "Акционерное общество \\"Великоустюгский ликеро-водочный завод\\"",
                "ShortName": "АО \\"ВУЛВЗ\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "164.00",
        "FARegId": "FA-000000054499502",
        "F2RegId": "FB-000007374078861",
        "AlcCode": "0300007235710000098",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТУЖА АЙС АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "198313191823120224001WGFLKP2P2YH2QEZ23KO4FUDS74AQJ7LSLIPKCXDC5VN56AJFK2EZ3DPXS23JF3C5CYOI3MJZUEBAXQ2NV3GWT4I2M4GX6WDMGA3ISCJHJHOSZ7MQW3WN3CH26S3UFA5RQ",
            "198313191823130224001SQH53WKU2NPG7N4AWJOAFTKFDMJWHPGPXO5TTQVHMGJUHC57LBTMYFNGZP555Q4J3WIRLXHXXIBFG542WAOXFIF3KWZDOQVKFJ5HXPGC2VWDXIL2AXWLBFE4AQHORJMBY",
            "198313191823140224001NILRMOG2KLZ4PIJNUC2ENUXBIIMB7C66XYAL2VSCQ4Z2MCQ2CQ2BFLH3BVXDVE377Y2LKSYUAZZTSFJOVXCO4CHCRD5DZLYNS4C3E7M4FE6P5YKLK24PIOY3VIWH5ZUWA",
            "198313191823150224001BH4GJGWH23HJ6UQG456RYUSH4IMH5OEC4Z6V4U4VSNR2ICBYBT32VXKJZLZSX3ARG2PHO6UKM27SQA24G2FAKUCOEQH3MBDAWCID64Z6SYTUEQJFMJ66SAAQAQTB35VBQ",
            "198313191823160224001USSZ6JOK5W2KD73TWR3F2FGAZ4KX5EQVQB76UETRNPJDSRIWNAW5VQR4RLZ2M73C2Y6V6UG6HRRYBOCJTYWYCZPX3XO3YF2H2JLH4LYKHOAWTANEYJ6LE6WQEFCKYUVHA",
            "198313191823180224001ZYGJBYP4YC642IBPFD2KJ3LP44VMT3ZFYHBEW6GND2RXQNJ6GHNUVCLKCJRFAKHBAUHVBM5ZSBPQLLAZEXO6PP2ZJTFCGDSUUZSU3PMDICQQBC3AV3PN4GBUAVHIIPYDY",
            "198313191823190224001VNMHQ4WZON4NFWXXDGAANPGTZIDXPPFTKA4JWEOXKUL3B5QH7KLL754L5SP36RTNU77EUQQ7X6HC556HYWTSVSD5DMG33UZH6TAZCPD7ALSZFXDZR23A5MQPYE6IZOTAQ",
            "198313191823210224001EDO3JV6CGOABZXLBIX34ZL3DJ4T6CNTMRQFOROMJT337OSGAPZ3KL3UCAS6ZYFM3NOHHGDHEGOPQPL2SZUH3CAHI2XRAX7ZMY2DMEJWYZURNSPFAAZNI7ZKIDMNTJ54KI",
            "198313191823230224001KPJG6GWLBDTZXFZXZIOVBPIN7YQP3LIZFGJWM3WGHPFEXZZND46OUSHPGUROD5UFLA7LFYRR72C3NPI3D2XVPSZ2UVON7RZHMZYINEMQOI7UFSXB3YBXHMKRI6TI4DW4Q",
            "198313191823240224001SZWXBO2QKPR7YTNM22NIIVNN7AV6V4JSMENLAOMRZP5MFCU2FIB6DEVWSEHA3LMN3ZMV7ED6N6SN2IBPQ2BFAPHH57Z3MV7FQWYPET6L772UH57MACM6DK6GEHOPFKSDQ",
            "1983131918232502240016L2KTIYKXGG6LW3J4AS3XT7DSYUQO55TFCDN62WGI3KIK4GD65DLXFGNEX3S7XTA5GL75QC4ODG553U6TRPNXOUMIAOC45KHIOIIREGPQ5OWIP743AAEHM64UPWGW77CY",
            "198313191823260224001667AWPNCUK3M66NUFZ3KJYN7HUHY5FLRB4AVS2CWPBUCRU6ZIIEYI4RH5O2QJCFU232WAA5CZ7JG4G2LDW26F5JVEZORR4X5WTXY55K3BIP46QS7O3BYOMPYK24G5VV4Y",
            "198313191823270224001JCUAEIO2TBAZBJ5G4CNUEA624QL2K4Q4GMP3BFCCWIUWKPRAKCQEVL2C3XHT3YV43LUUBT45UKNYYATOPVL32PISYS4UDJLV7SYZUQK5TSQB3EIXFMPMDBFTSS3FZLFUI",
            "198313191823280224001WVVQTNTO3LABX4CG6YMTIRDI24EEUP4KA6JJAN33US6AEOENSQCGNWD2HTFDUR4HPMUZFPLAAVD556JHOF4NRPA2OHC2QEXNJ7XBVAVF4KSJFRDHE6F56BZPEG4AW2KJY",
            "198313191823300224001IBEKZ2TKCLU5HE6KFB74Y3FXXAGHNP2WWD2J7NO7AFYBH3MHZB5RZVSQL5DJ7O4GEOECTD5XQDRWT2MCNPG3LUIWJIKOQBHUXXZ36I2GNNNEE3WYERYNWRO5XC2Q3T4IQ",
            "198313191823310224001HZCQBPRQFJB6HBKPSMFRYZDFNQHI3L6ITYHVDLMTRGNT2GIODO3F4HL2RZCKCCU6EUQHXU64FZKOFWPRFFVGWNJSRZBW5CX3VSYS6SKEP3ZBENGQQMBCARSCB6MOZTGUI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,,,,,,г.о. Дмитровский, г. Дмитров, ул. Промышленная, д. 46 |  | строение № 1 (кадастровый номер 50:04:0000000:23453), здание офисно-складского комплекса - здание складского корпуса в производственно-складской комплекс для производства ликероводочной продукции, назначение: нежилое, этаж 1, № на плане 12, 13, 15 - 17, 21, 23-34, антресоль, № на плане 36 - 38, 40, 43; строение № 4, офисно-складской комплекс - здание административно-бытового комплекса, назначение: нежилое, этаж 1, № на плане 9, 10",
                    "RegionCode": "50"
                },
                "INN": "5007113108",
                "KPP": "500745001",
                "ClientRegId": "030000723571",
                "FullName": "Общество с ограниченной ответственностью \\"ММВЗ\\"",
                "ShortName": "ООО \\"ММВЗ\\""
            }
        },
        "quantity": 16
    },
    {
        "price": "314.50",
        "FARegId": "FA-000000054559310",
        "F2RegId": "FB-000007374078862",
        "AlcCode": "0300007235710000097",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТУЖА АЙС АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "187323271456721223001QQDHCNMJAWJEOXJFOA7HAINAOYBJGFBBAHNVGVGDDA6YZCJ6QCL6YFCZWEELIJPCFXZCM3CVFO564J3GKYIHBGWP5DAYKENJQVPYWEOBPHXAD34HR7UXQJGYAWHEQURVQ",
            "187323271456771223001ZGLXLLHQU43I3AMGOHNT6BZNDURVSOBRX4TK62F32J2PM5IJGLIA5JBWRPD4BKRBQ2HV4BO7LS37XGTP2KYK6RHUYHIWFJMHQVNUV34V4BU66CQPH5YLJ3MGL3D77OKDI",
            "187323271456841223001ATABVEE36ASGMKVGNPP6QT2D6QPQRJE7SM3T7PBONHDU2SH3GNJZYBQRLHEMGK4RQ2F7CTFIBWEM46TGWBOYFG45ZYZ7D5MFRGFQY4JEKBZ4OYHHTKLCNWBIOCE2B3JQQ",
            "187323271456851223001OXWMQK2655IKJELLGQXH3UUGIYFBSML74XHWPJ54PEEZHYKE5UWPGTCJKSLIARMDSGSZZJRETBJT5AH22YYZCEMAS7EC2B2X3RE73MJA2ITLH3VWIS46C25QJ2TALGRWA",
            "187323271456861223001FZYUL3J7CDNQPOZDUM4IGOCZUA7YNTAZD23K4JZPXSP4PSP5W4AXAAH4IRPISYKSYY4273CV4SFDLUWWV3TAYBQ55DAYUPAODUOMABRFYR22H27BQH4B7R5UQMOAJSZ2Y",
            "187323271456921223001N5BTZEKHZYHKJN5JYSHGFO47NQO5BYJXUI4X26YZ3JNSE6USDT7KMET5BORL74IYEBTTFSSYGY7HQDNCF4IIHE3CHFFBC7NVUX3KX2MJKRLHOOB3YD4CHNM3DFCMCJOMI",
            "1873232714569312230013ZXR6NOQ5GASHKTFNG6QH36J3M3WECDTGETOPOW23OUPW4DQ2SPAXMPQX7ZGKYXO3VGQJ73A5R4HQIAXHGZ75YUG6IRZH2NXYX7YCJPCNMEXCTMKUVMQ7KO3JGZMNGX3Y",
            "187323271456961223001LGK4OGJWXDNRZHYMDBGQJCJ6OEMJZZHHLLPGJO6XGTVKHVV36J47MIVIVZAIRDD4DNASUJH6K5QJZVUBNAQCJBXMI2L44EFLUOBKGUZW4NVIQGS6NQUA2TGOUKXHJZZQQ",
            "187323271456981223001DFPDVP4UUD2MYWO57XCR47WKIMRZ3ULN2DXCR3DGS3X7IROGNDGCRJQHSLEIBVZ2UAWNYZAJHY4URTING5QXG3DBQWMEY53ODWEW6GQAOA7GR6GMWXZXBLN4AGVZQRHTA",
            "187323271457031223001O7V5STJ7DVHSRNUFPXEW4NGLGICHVA6GLYWFTAY7MR4C2RIKTCNRMTBRNAQRLA7HPEH7QVNRKYVNM6QANUEXEF67WWHW3ZTJTLROWXJWJ5SFXXMGEAOC3S3SCU7XZV4KY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Московская Область,,,,,,,г.о. Дмитровский, г. Дмитров, ул. Промышленная, д. 46 |  | строение № 1 (кадастровый номер 50:04:0000000:23453), здание офисно-складского комплекса - здание складского корпуса в производственно-складской комплекс для производства ликероводочной продукции, назначение: нежилое, этаж 1, № на плане 12, 13, 15 - 17, 21, 23-34, антресоль, № на плане 36 - 38, 40, 43; строение № 4, офисно-складской комплекс - здание административно-бытового комплекса, назначение: нежилое, этаж 1, № на плане 9, 10",
                    "RegionCode": "50"
                },
                "INN": "5007113108",
                "KPP": "500745001",
                "ClientRegId": "030000723571",
                "FullName": "Общество с ограниченной ответственностью \\"ММВЗ\\"",
                "ShortName": "ООО \\"ММВЗ\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "330.50",
        "FARegId": "FA-000000050782507",
        "F2RegId": "FB-000007374078869",
        "AlcCode": "0100000003130000073",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"БЕЛЕНЬКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187417573982221222001KFPE6CCDYZEBXRGUFSPVQMAWAYLLNE4PKIBBOLLAV4BFEADVG63I7IE35JDRPGCMH236UXAEPC6U7R2WWWKUPVPSI7Y2VGJXMG4MGFAPIYGHN6XTHSCJKSLTPOL6XKAPY",
            "187417573982311222001NNM25I6RJNERM22CHHGIP7SE2MWWLWGPX6LB65UQ5UJEG3GSFFQ4UCQSJPH6LFDQR3IPUZ7BV4FM5Q2ZHWXTS7HXOS27CBXTYH4Q2Q3QDY3UYC26SVPQ7G7JEQV2BUGUA"
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
                "FullName": "Акционерное общество \\"Бастион осн. 1942 г.\\"",
                "ShortName": "АО \\"Бастион\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "310.00",
        "FARegId": "FA-000000054644911",
        "F2RegId": "FB-000007374078871",
        "AlcCode": "0100000020360000163",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ №1\\"",
        "ShortName": null,
        "marks": [
            "187324122287690124001RP6U4KJYM3HQYFOPY7PQMAMNPM7ZGFGIGMSG4ZUEEBWGUGP6X4KY5BVA3I4ZKMX22OM2Y6BDENN3GSO6XKZTKR6U2BTNNLIB4S77ZVVNTDPIMBW4FIYYNW2IUPEIECVLQ"
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
                "FullName": "Общество с ограниченной ответственностью \\"Русский Север\\"",
                "ShortName": "ООО \\"Русский Север\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "173.00",
        "FARegId": "FA-000000053042301",
        "F2RegId": "FB-000007374078872",
        "AlcCode": "0300004732090000355",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ №2\\"",
        "ShortName": null,
        "marks": [
            "198311829486690823001BLURG4X7FNMD2O63CCPI5JEJMI5VL2DP2FHITSFNYRIYU2YV6YEEKRPQM5QI2TXL3YVOTHOHAUYEJH4LABEZAG6MHSWPHUADPB4XWNFJ4OXA45BMBFWE6CU7I4LH7WFQQ",
            "198311829486980823001BV7G4U66RIATQ2MRY6O3AWV4JYWD5NLTABWLZYRLRP2SF3HHQWB6U5BZXWTHQDLRWUBOQOK2BS46LZ5LPBCBO36DKK7JA75XAX35HBWCJT45O4O2GHMQUFT2ISHSCEEMA",
            "198311829486990823001ICFZI4ZUEMD336EYGHGALLJK5MPP6CCL2LSIXPUMMNE37XJ7AWC3QXQUFBRGJIQPJG7TESYGIALER2ILCHKGAXOLTQBLYJO7C423FHC3UVG6YYOAQQ3U66AJXCEJWPLJA",
            "198311829487180823001NP4BROGCE5RVONYOMZRDZIPNTQ6V55WIRH3AXYKSBAOQZVONH4PYYEQZGBWPYCQ3GFQF4PTRXB74CJ5QUFZDKNMFNATKJRV4QVNNCHHUYKY76H3KPCDADHVXN7D4HCEKA",
            "198311829487320823001YE7HPONNU5I26GRN3C32IYIF3AUOMQJCA7TYEJKAJDTXNR6H2LACYCXU4IRLAJACQYJUGASWDQLJ26SP6WFYL422TFYWLQOI4Y6EU4NE44MQXA5VUKD2VIVT7VB4XDP2A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ярославская Область,,Ярославль Город,,Советская Улица,63 Дом  , |  | за исключением литер Э, А1",
                    "RegionCode": "76"
                },
                "INN": "7606118934",
                "KPP": "760601001",
                "ClientRegId": "030000473209",
                "FullName": "Общество с ограниченной ответственностью \\"Ярославский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЯЛВЗ\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "63.00",
        "FARegId": "FA-000000055144172",
        "F2RegId": "FB-000007374078877",
        "AlcCode": "0100606942420000119",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "1974076641027004240016SCHK2XMJ4IFUJSDVQJYZFYRUUW2MEB7OPHVWRMS5FQIX6P4AYRQRZN76S6FUTZDARJTQNZH3BHLOIQ52S5BXPQDO2BTE6KOD2LKRCWGLF4T6RBJAXNNLF5ZEH35YTCWI"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "460.00",
        "FARegId": "FA-000000052913868",
        "F2RegId": "FB-000007374078880",
        "AlcCode": "0100000005390000136",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\"ПЯТЬ ЗВЕЗДОЧЕК\\"",
        "ShortName": null,
        "marks": [
            "187424657528751123001UDQOSOMWRLBABOD2RGFFTEW7TYSLQPBFOZNXC4TDRHWYXVWIAVW2GGCZWUMGDBFC35CT7DJHS22C4N4ABMBB7323YEB4ZAHK726XSPAUQ3WLTXRYGLQODDQ4JV3ALFFTI",
            "187424657528781123001NEOIUQ7L65BRXTBFGIAIXBB3Z4DEYPFVFKBDYORT5LVQYX4GKPH6ZZOQAPXVXS7ASOCU2OOMCBJJ3LWF5P7XWBQHMPL7P3UFYQXJZFJWEQ7HKXRMZ6DSMSLOFU4AZHTZQ",
            "187424657529091123001K6YLYO6GQTENUZWN56NFMLMRZMOK7E5QHMQAR7YBA32OISWCPLIV4DTEOIS2HBG33FLULRBDHZYYNTABHN3RHF5B5V4C355EPA4JA2CIXKDWU4RO4EXIMU727UFQLOI4I"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "508.50",
        "FARegId": "FA-000000053065516",
        "F2RegId": "FB-000007374078884",
        "AlcCode": "0100000004970000298",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски купажированный \\"ФОКС ЭНД ДОГС СМОКИ БАРРЕЛ\\"",
        "ShortName": null,
        "marks": [
            "1874252594673311230012YWOBCGCR2FNCEDHEWCAFTAOPMRLNYH2Y6X7Y6J6ZTZE4OFSNGQFDHWQXD6Q444KSXWMI2VHB5VC2OCDIFUHWBI4HUMKJJEXUFRLASE33ISEJ4FLKJ7IBKK5K7RK2QPJQ"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "221.00",
        "FARegId": "FA-000000052851271",
        "F2RegId": "FB-000007460035818",
        "AlcCode": "0100000005410000008",
        "Capacity": "0.250",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\"АГИДЕЛЬ\\"",
        "ShortName": null,
        "marks": [
            "198412742595630323001556DIVN6PKI7VOH3TN7MDHVDXUBUQ2IAQQH23Q3LXKBHUFZIGSAR5XDDN7VIKQAKBC4MGS3WVXLMWY4FQIXQ2FIGLHLFILEOVNFWM52TY3NN2OYMJQYTGUFTLWICQPN3I"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "221.00",
        "FARegId": "FA-000000052016076",
        "F2RegId": "FB-000007460035819",
        "AlcCode": "0100000005410000014",
        "Capacity": "0.250",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\"БЕЛЕБЕЙ ЭЛИТНЫЙ\\"",
        "ShortName": null,
        "marks": [
            "1984113064634802230016JKCGJ374PWMKXTN4XTBB7UBPQVSS2ZL4U2FFAP7GE2E3NT3PGFYQ2H6CDEWTY3CGHOHEPLDMNEPMVEOGXZIRUK6VP7ANOSCLUNLADPW2XAS3RQYA5RDQSVLYP45AFSCY",
            "198411306463660223001KNEI4POKMB4AEEUTXTAUTUDTQMIJI5GNN7GYW7Q5LNPVTHVZAHHTSBSXQWLFSUE2OKV43ZOVZRZGAM4QA7FOUYHUABPGAPAPJQ5SXCZJC4DI5466JRW3IWXMRVB3IBWUQ"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "396.00",
        "FARegId": "FA-000000054840357",
        "F2RegId": "FB-000007460035820",
        "AlcCode": "0100000005410000013",
        "Capacity": "0.500",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\"БЕЛЕБЕЙ ЭЛИТНЫЙ\\"",
        "ShortName": null,
        "marks": [
            "187427374357580224001UQU5BIAVMOXXBQZ5HBPX22O2VM2QD5WJJRCPQQTAWLJGF2S3RM4SYGEH27XL7UNE4QCJ7ZQYYEM24BIJRP3ZAEVHRPG5YC2VTP27IUGX27O2J7OHNB6NFWFWC6OAB7ZJQ",
            "187427374362160224001IPVU6IWOTRXBC742NO45PI5644DEGWE2F7IZTPSYLBS4CTSTX36Q5ICVPLRCYPT7YIFPHX3SCZJTSWMWAE5MV6J2A5OF543QQNDPV3BDAFQDQAOEPXYRQAOANN3EMGO5Q",
            "187427374362170224001FTETJY3GMH33ZDQHO3C4XDHX34CFMIGBE6HXS3TINE2RZXGPXG7RZB2NJ73AOTSCGHFKW57P56TYMMXBX3EEJCD2NS3ROVQMRUV63Q5DVI2HSLBR6G4TYZYYJGQX5KP3I"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "381.00",
        "FARegId": "FA-000000053709412",
        "F2RegId": "FB-000007460035821",
        "AlcCode": "0100000005410000007",
        "Capacity": "0.500",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам \\"АГИДЕЛЬ\\"",
        "ShortName": null,
        "marks": [
            "1874268881197102240015KREYHTC6AUDI7VX3C2UZ4CXHYKUR2AXBDNZ3O7SJEPG4I76QO6QELKSONJIFB5424J467EIG3JQIFRQN7P22LTECGDER53WGLBBG3TNTIQ5OK7U4Y36B7ETPFMPHZMUY",
            "1874268881197402240013NXF3EZEE434F2QWGHVOQOROZEAJPYLFT44BE6SW57ZCP4RX34GVKCMKZPMHFXYAEAQAJUL5YEZIIFAWJXFI77FZ5ONC5UUBI7VVOGMWII5V2KWXYEO6VYMLAMJEY5E7A"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "116.40",
        "FARegId": "FA-000000053218614",
        "F2RegId": "FB-000007460035822",
        "AlcCode": "0100606976440000104",
        "Capacity": "0.500",
        "AlcVolume": "14.000",
        "ProductVCode": "4213",
        "FullName": "Продукция плодовая алкогольная полусладкая «КРАСНА ЯГОДА. ВИШНЯ КРЕПКАЯ»",
        "ShortName": null,
        "marks": [
            "195302492381410622001HWTJMV5Y45RWV2DSVZZTJNU25QXVRSVPGVECRPGZKSAGDNJC4EVC5V2IQEYHDFUD6ZYN3GAFCB2BFDOB7Q7UYWKEW7H45HLGXU5S7MZ2U2LBELPU6XWY5S2UQTOZYNSPY",
            "195302492381480622001ANOCM4QOOYLJRR2KPI5ZELRSCYKQKQH4KHBHI7XMMYZLUBIOK6HXM7HREEBZRCUJIQV5G7FKEMFCTOWZN6EJM3XXM73VSHT3PMTDK4HLONDXOBH73ZPQTAK4LF2DOT42Y",
            "195302492381500622001KJVSUXNVQPHTE34JTMAHI5YQB4YJSWBNOZ5ZW4CL54XW6WKCFXVLOHDL4S7L7K75XW4FUB5X77IXLDWO3CKVAQOBWUKW4GD3ILRRD5LKYBD7TZ4DIXLBDGBP5ZL6U4Y7A"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Северная Осетия - Алания Республика,Правобережный Район,Беслан Город,,Первомайская Улица,224 Дом  , | нежилое здание Литер Д, общей площадью 14784,2 кв.м (за исключением помещений: № 2 (S=1301,3 кв.м), № 68 (S=698,8 кв.м)); нежилое здание литер Е, общей площадью 7884,4 кв.м, (за исключением помещений: № 1а (S=1198,7 кв.м), № 1б (S=1303,6 кв.м)); нежилое здание Литер Ж, общей площадью 2232,6 кв.м; нежилое здание (литер А), кадастровый № 15:03:0011023:722, общей площадью 9960,7 кв.м (за исключением помещений: № 1 (S=1351 кв. м), № 17 (S=10 кв.м), № 18 (S=44,7 кв.м), № 21 (S=37,8 кв.м), № 22 (S=39,1 кв.м) | нежилое здание Литер Е (за исключением помещений № 1а (S=1198,7 кв.м), № 1б (S=1303,6 кв.м), № 23 (S=863,6 кв.м)); нежилое здание Литер Ж; нежилое здание Литер Д, за исключением помещений № 2 (S=1301,3 кв.м), № 68 (S=698,8 кв.м) | нежилое здание Литер Е, кадастровый № 15:03:0011501:22, общей площадью 7884,4 кв.м (за исключением помещений № 1а (S=1198,7 кв.м), № 1б  (S=1303,6 кв.м); нежилое здание (литер А), кадастровый № 15:03:0011023:722, общей площадью 9960,7 кв.м (за исключением помещений: № 1 (S=1351 кв.м), № 17  (S=10 кв.м), № 18 (S=44,7 кв.м), № 21 (S=37,8 кв.м), № 22 (S=39,1 кв.м); земельный участок с кадастровым номером 15:03:0011103:54 площадью 6156 кв.м с вертикальными биметаллическими емкостями (зав. №№ 00220 - 00231 | нежилое здание Литер Е, кадастровый № 15:03:0011501:22, общей площадью 7884,4 кв.м (за исключением помещений № 1а (S=1198,7 кв.м), № 1б  (S=1303,6 кв.м); нежилое здание (литер А), кадастровый № 15:03:0011023:722, общей площадью 9960,7 кв.м; земельный участок с кадастровым номером 15:03:0011103:54 площадью 6156 кв.м с вертикальными биметаллическими емкостями (зав. №№ 00220 - 00231); Республика Северная Осетия-Алания, м.р-н Правобережный, г.п. Бесланское, г. Беслан, ул. Первомайская, д. 224 \\"б\\", нежилое здание строение А9, кадастровый № 15:03:0011501:27, площадь 34 кв.м; земельный участок с кадастровым № 15:03:0011103:185 площадью 1658 кв.м с резервуарами типа РВ (зав. №№ 201, 202, 203) | нежилое здание Литер Е, нежилое помещение № 1б (S=1303,6 кв.м)",
                    "RegionCode": "15"
                },
                "INN": "1511027798",
                "KPP": "151145001",
                "ClientRegId": "010060697644",
                "FullName": "Общество с ограниченной ответственностью \\"САЛЮТ АЛКО\\"",
                "ShortName": "ООО \\"САЛЮТ АЛКО\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "225.00",
        "FARegId": "FA-000000054300156",
        "F2RegId": "FB-000007460035823",
        "AlcCode": "0100000001740000933",
        "Capacity": "0.700",
        "AlcVolume": "10.000",
        "ProductVCode": "4011",
        "FullName": "Вино сухое белое \\"Шардоне\\"",
        "ShortName": null,
        "marks": [
            "192314655970711223001V73FX3IUEZLFW2G6EMIRL3CB24E3NFQBOTVEBWQIHAI2LD3AF3TZ5B6XBQAWLWX4ABH5X26SC7CCEZX2I4I6D42WJD7BNJUV5IHOSJGPQSEDEB262GVI2ZL46OIUTKOVI",
            "192314655971071223001C2SJZPTQLXHQGKDIUQJAASGJVEGWG5KNRESSIZLGTM35O7IZIHEXZLMUPVHZUUTAOXYW4M2WZDJKBRZ7R6VPL7SBUOHQLI7PMRZ3R4KJDG6Y6CRXZRTVUH2LBSODQURHY"
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
                "FullName": "Общество с ограниченной ответственность \\"Долина\\"",
                "ShortName": "ООО \\"Долина\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "74.51",
        "FARegId": "FA-000000054767883",
        "F2RegId": "FB-000007460035825",
        "AlcCode": "0100000005450000099",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ПЯТЬ ОЗЕР\\"",
        "ShortName": null,
        "marks": [
            "197407438386350224001JSQTLFXA2X6SXHIX5RKQIVRFTEBJJQ3B2HB4ALKG7G4UZUCYS4O6GZ7NXTBCU3EUJUNIMZETP3USYJ5TYZPPJIKNDGGAAHMIRXK2OZYTCH54CPO4I7MNZKYEP3MITOX6A",
            "197407438386440224001DGW4BY37UWH2OUISB33GJW4C6APVAZHKQIQR5YNNPGPGIT2E5Q5CG4NOT6UOGAEMG7DGRAVJXQ4BPXP7HGXMKRLXC4T3NCTOPVZH2MPT74DJVMNAX5FBRDOORSKC6LDDY",
            "197407438388220224001TKDVUWHFGHOVA5FLZJ2VYBMR34W5MKNAVFQJYV46UTWWTTNE6OO53QRKFJT4LU4RLCY6X4W4BUY4M4GFLNPJBSQWXDQKIKNDQ3SNQY4VWXQTRO7DQ6QR3OPBSIPE7CJ7A",
            "197407438388230224001W2UZDLW3J4BU3GLPTX42V5WIE4PSWVQLZJU2HEQGSBAT5TKUTL2HD4NWS4ENZOPPSDPPINDP7L3INWJICOBT5XRSHYVNSAKBGDVDYPUR4V7HGK4Y4C5FI76MU6K27A7EY",
            "197407438388250224001JBZLIY573ORIDD74GN7EHUV4SEJTCFLJ2HFQI7UIJFUJACHGPKVD3IIYFM7SB7HSKIB6FTAJT2B5GDOSZKRCZXNMFZIE6RFGU7SMYDQG3ILMXYMEGRRIPCGQ5RRHGXYGQ",
            "197407438388310224001VDZUHGPT4A2B3GFLQZ4HJ5QQFE23MAUYPKFOZ2CAPHGNJWOLXWRFVDELPO6UKTVGI252CUJYNQI4S4B6ZC6P457ATHSESCYR6JJARNKRQCBUTTRQQABNX2ZVNRTJE4IIY",
            "197407438388430224001NTOIUF7RDLUS65INYXVEBFZFFAGSNCT5QCGJTSRBK7SCDQY2VVGZSRF3NSTG4YHJDSYINU3J3E2XEKVF5NCWMR3A3EI7NB7EHAJQJNXNF4NJZJM5QLMEXAG3UG7TRLBJY"
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
                "FullName": "Бирский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000054628158",
        "F2RegId": "FB-000007460035833",
        "AlcCode": "0300003247940000088",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Три Рюмки»",
        "ShortName": null,
        "marks": [
            "187324663503690224001QP5EPJTRAUEX5MHH5SCGLENDH4TWGNEH6J4K7MGWMRQG7CFHYGKXA743U4NE323ECWSIVSPWJFMV2FA3PD2U3UINNEVPRHFPS7XR62DLLILVLXEAKT3U42J2LLI66ULNA",
            "187324663503700224001MI2RWM7SNHLFESVTQKGNEWHJNQDVCUWTZ3OGMS67HKBFLF7Q4O7RATVMZ5WFP7MPR47KZA2FTQRIVPBKVYICOAASAKNUZF6OX54XO5BSVUKMEKDJKIGVUHYNFZGTFF46A",
            "1873246635037202240012NPBM4DZRHI6FWNH32J7N23DKEYK5MTSFKADWVQBXTM6D5VB2BELPLSPLGU45RXXV6OMTUEDCZBRYYYC7O5LDMKPHBYB5YHODRCEJVNQS743A4FOSN6ZTU3MDVKOMWKXQ",
            "187324663503760224001SJ3OOPAIEVSI3WGPYZXNTIWYNIRYBMS5J7G4IDDLNDEQMNXH2TNNFSUPK77IOFO7P227PO3M3M34VCOCEBLCPMGMKKAAHTJRQGXSVZ5EMVBIR2UJAMA56AU5SQIAVZGEQ",
            "1873246635038102240013USXR674YSRJCHLB3TJJQ66EFEYIRSB3ZN7RLCRQQFCR3HRWGIIVHSLLDE777GKONILL5JG77TSP6RO4LLM6FU6PQHHHOGZ2ZWGD7CZTEBQW6GFTK4B7PBN4NEJJ7CYHQ",
            "187324663503830224001T5JNTO2BSNDVN7NZSYMRPDCKDA5WRG5UDARTZEQBJGU4HMXZWKTY3K6TKMMSRHEK2LSZAYC4YPLIHAGXPDMQLJQZT7E2KZYLP5Q4XXDZMLMAL3YIBPHDKTOJIKTNF5VVI",
            "1873246635038402240013ZFWMMRT2BA3KX32F3LNEWE7YMLEDD5U5WNLZDXQBBAPQE7LQ75I7ZUXB3LRAXNJUELV6M32IJAU6J2YIDXMVMQB3OL5BR25KE77QQV3J4ENIQLTZLGWEAAW66V5UL3UA"
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
                "FullName": "Акционерное общество \\"Озёрский спиртоводочный завод\\"",
                "ShortName": "АО \\"ОСВЗ\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "65.00",
        "FARegId": "FA-000000054781012",
        "F2RegId": "FB-000007460035834",
        "AlcCode": "0100000042540000020",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ФИНСКИЙ ЛЕД\\"",
        "ShortName": null,
        "marks": [
            "197407122746781223001BESKICDWVW5HU6B75KJLOQKTZEFCHHF37S6GUIPOESEJPQKXARLR2JECGGEI4I3NAGONMYIEPOXE25DQ3Y3MNB6TPS6QF62XQRCY2O5DZEOINOQEHGN5SE7NP6O5BDZSI",
            "1974071227468012230012VVBUFD7VSMH6LO7PVQKYXEBMM67476HAOXNRD3SBX3AGX3CCAU6FDQEWT3QLVY25CCWX2BEAQP3MAT3SJONPVAN4EFSD5QGMOW2RFQLPUBTVRDF53OAJ4U3VPUUQMW7I",
            "197407122746951223001X4HZV7GTRCW3GZLRSDEEKB32CUTZH2BOTWADGSIBFV7ZEI2VRW5F6EVCPA7KDRLPIXKBU4V3FT7OPRSIDGOQBWDL66DXTFT2KXJTL3YN6W4GR223HVAX7XESP5E2WJYIQ",
            "197407122749731223001CFACZ2UHGBETEJWQCRZLMGBQXUPNCUSMOQUUYHK4FEBVWA2TKV2NKEDKLK7EP4XZVKZSYDK4D6DVV5J3BN3JCLBA65ZA45FURUOINGKFCBOLAFWMISK5GTGNA7NJRSFAY"
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
                "FullName": "Стерлитамакский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "140.00",
        "FARegId": "FA-000000055049468",
        "F2RegId": "FB-000007460035836",
        "AlcCode": "0300006342850000015",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ФИНСКИЙ ЛЕД\\"",
        "ShortName": null,
        "marks": [
            "198417253567420724001GR3F52CMQ6KDBQXXVJPYMKLSIQSNKMTC73Q7T2BUZXGOSQHYHB46MRHR7KUMVAKULJZOEZLDLXRXJAEBHIHWHDXE4WFRPUHV7UC5DOIF4LXOPEQM55TCZW4V2FJRW3R7A",
            "198417253567600724001L7KCHTQAEIKUBH3BEX4YJ3HWRYIQN3NQPNMAAJSFKYVKJEPDQJ5F64FKLYOLIYIQK5A36P2PJ3KJ3D6NUBWH5D4DNGNXGRKFDDTP3AHO76HGPS4GSNF2NNLCKJYPLM5DQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "229.00",
        "FARegId": "FA-000000055261144",
        "F2RegId": "FB-000007460035843",
        "AlcCode": "0100000005410000103",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\"",
        "ShortName": null,
        "marks": [
            "187431186341000824001FSYUHPB4LWY3B6DEMQQRTGDGCUEVGTOV5A3ARERO3KGYGV4KJDNW5ITM2J26TJUYM4YQK27H55BKJ73FPWUNJFPOTESRW7WPKIFGWJDYE2IZ76LAL3OB53LUPR47CNJBA",
            "187431186341030824001NILPNJZBLZGPCA7C32A3Y7WQPQ7TUTJZAX7TAY5SWQCVJUOU37XU7ZOTXHLE4KWFFIQKIEXIMDXWXB24RD43SZHSBLVMOPNENJ7TGM5PNWKFO4PVW4K2W73BJHA2V2Q3Y",
            "1874311863410508240014YUZSBGRL77NS6RJYNOC6MHDDUNUKXOCAHHOSBMADYJNHQ3AZXRIWQ5SDKM3GJ5PN33QVZJ5H264KXM5YUFM6E6C3MFW63FKI6FX5CXZQNJSMFZBFTRRPQGUOFM2CDK4Q",
            "18743118634136082400124IAAN6UMHBCZVBEGZWR4HBVUMNC5T3YBMZ5RERMZ52TSGFOUU5FQCLPS746LFN5VVFDR72SA4DRUSBC3KCBZY7H4OYXU4BAV3BWNOCOMLPG2KBSLLD7GWBHCB2Y4AQYA"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "240.00",
        "FARegId": "FA-000000054864779",
        "F2RegId": "FB-000007460035844",
        "AlcCode": "0300006342850000003",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЧЕСТНАЯ\\"",
        "ShortName": null,
        "marks": [
            "187429837168290724001SY6XSCB2BQNAPZOUZ2DMJBNGHQM4LMIAH6U32X2N3EFJ4M2FIWIXY4PTPR3IICPQRLNQ62NNLI2GLEHI5LT7TFJTTHAO2QLNPMJJG4OU7WURMLAK4SYVRUGML2FS3QI7Y",
            "187429837168310724001UTNARL5U655YUNEWDF7V3RFQ643VL5ZNUO3QU2FMWLILUAQETYTYXNAK6WQSWHJJC7RI3N5NQ3YWKKHTIVNLD7AJLCO4BZEBZTR6VIP3FAYYM3PFIXB7KF46WDCLRE6NQ",
            "187429837168390724001CIZAIZDCU3ZQPJBLIWR42TRRAEMY35VFBVWWR3VFOJ4KCD6TISROLFSVAB5HYDWLFFFI3TKCNFQW4EIUE5T3W7L4AXS4SYMJVHRCD6FCBKFSHULWSX72BVTH6KRJ6IADY"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "246.00",
        "FARegId": "FA-000000054073694",
        "F2RegId": "FB-000007460035845",
        "AlcCode": "0300006342850000007",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТАЛКОВСКАЯ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "1874237577332410230017MAFTHKBFEDKJ25TPK7K45IUHEW3ARWX5BGXZIJC4SU3TXMWO5JOXZNQ5LARWZG4L4NDPBZ5GVIKW5ID3LR3U74SOGHGHKZKTQY36Y6KDLL6DOIKRVVRJSQK2HFD7CRPY"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000055026772",
        "F2RegId": "FB-000007460035846",
        "AlcCode": "0300006342850000014",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ФИНСКИЙ ЛЕД\\"",
        "ShortName": null,
        "marks": [
            "1874295140541407240017MBONYRYI2IXL4K77CDWGZ7NTMHE35HCGROTJEUOAKAUOFEIR7LVDMGPCW3LWIQRMIA55RQ4UKYCNIO6YKV45PX7GJONZ5VHI6WZNT66NIUQIWHOPH52UMKSQCPJRRYRQ",
            "187429514054150724001VMHGSQKZ2NZMPM33TVW6Q3RS4IT5WZRVWNCX4M3B7I5RFIUOSDDJUFND6GHMDBON4EKPC2VNXU7YEUERFKU7XF3GYKROBDX7W5XRLNHARNNTJV5PANJ7QBN5W25FU4XUY",
            "1874295140543207240017RPCQCSKV3ECMTWJAJAZX5ZEQYLGOZP6DZRKKR6KDGMT56DNMNKUKMQ2SWINHGHW2IRTNFOBUNKLWN7QHSXZBK32LCHGEJWWCG2G6EMAWYGJWXBB4UEX55MI5NMCO2G2Y",
            "187429514054330724001PRWTWDDBB4HWCIJWQRVBFKGKIYA6GKSY7DNGXOKJBG27IHOFVZNCAEDKMGIIYP5PI7CP4U4BD4H5I2KEQQBRLYM5JNYSKMI7WAZ2XXNXPL7T45NNNTOKTISFIUZGRB3II",
            "187429514054400724001AMRADIZIR7HFSIJMBP3XWJNMZYXWP5VVB24ESMP4UKHLD4JMU5H2NZPEAN6S2RNDKQD7C5CARQXOJUJLNXZYX5RMJZTT45LA34Q27Q7N247XJEHFLCY6ECM7HI6OITLAI",
            "187429514054410724001GTOFU4AVYVMWDS43QJBAZ2N3YMXP2UMA6SNLFEZM4WFC2COD6B3D2TXHDZJBTVLLA2URFHSO2BK6XD2PLQYC6HYFUUMNE33ZMG7WCBAGSZ4WB27U6AQPDTJ3G6HNZELJI",
            "187429514054560724001HFEZGK53F5URJGJ6PJ76KW4YJ4QE44LMUHUCGAR7TIDKCDH5L7QL7TE6BE2ZZYEZGIZHZEVMFCUUQXNNCKRMG6PIK5PZSIZ3EIEMTT3F5ZCGPYXEPZZHZVKQDSPDGPUOY",
            "1874295140546107240016I66NHWGGIREYBIXBRZGQ62MXEBJFZOCE2DTIXQ5GQ7JUUV4WQ74HISMVJUHKR6VNUZJ3PKVPRJYUOHBTYVHSLS2C2BRCG4BRKU66WUBXJ4HNARIZ26VCJLOTHDWLQOHQ",
            "187429514054660724001KD5IY2NYVHRFNZ5VOVPYW7FJLYR24L5NUU4ZED3SL73CW3COYCLFX4MHVLZCZH4LRNSKKAZGEJ7W3IN6S77DCPFHNKGXXSPYUZUXVKNVCO24D3UAJPDGKZJGPAGL32Y6A",
            "187429514054690724001VAOJ6WFI5CYRERQYXMXI5PQF3IC4XRVON7UG7K2MPMAZAOI3HMSUXP6FNXSOV6GEIKWH52KKJQZJFJDQMJF33REQJ7EHIVHXTCMPSYNPZKIIL6KWGN5L5WSBZEVM7LPKI",
            "187429514054770724001KOOIPC3VHRSXVSK3LMKJYN5EIUIRUHQQBHYRE5TNUYCMOGAKD3UYUATZAQWC2V3M65GVJHD537ZIT2UY4CLA73UOY5YLI7BLHGPPYUGJGBSNYB2BBT54N6W23TAJGZHJY",
            "187429514054780724001DGCHHQOAMMPMP24JSSQPT5DM7YBQTGI74QFGZMHCEV3HS5DCRJLHFWAH5TXKKU7QXS7TUQF6GTMNNSZFBBRKD34674BCAXSBFAUHUQP4XHMVV67LVD2SCO3NQJH3PSOOY",
            "1874295140548007240017IUPY432YVCVJHZDSXM6WOOSUYEYTH2GUYIIZJ6H7LQZP45YZNZ4XFTFVZRLFORDCENP25DXTSSAKK4P7HDPRFC4QWFLZC6SHFBSYWQOMVH5KYUZC34EFAD5MRL3P7ESA",
            "187429514055160724001CGTTCQKB4C2HLSRU7JZCLYMJFQLYQD6GZAQHEA4XXLR22WZR7J2XT64P2RMA5FBW5MTVTTKIVMW7ACSUYOJNEEEUMGXEP56KR567MAJ4S7XE3SSXO7KCRKVUZQDB4S6XI"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 14
    },
    {
        "price": "307.00",
        "FARegId": "FA-000000054704437",
        "F2RegId": "FB-000007460035851",
        "AlcCode": "0300006342850000044",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЗОЛОТО БАШКИРИИ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "1874289080905905240013JA4PY4DKLCI6ZNQM6DPYLND6I4NYHNNOTNH6J57CDZB3F7IAN3RFELHCPFOC4VBVYDJ6LKZNZ2HE6USWRN5F5KCXHNOAZ52BZUIN2532BFQPQT55AT7TMGSPITFIAB5I",
            "187428908090790524001HM5UFA2L7HC2EKDZPCSOU4KWP4RAWBRASJHDOPCZ3EBLAVZUXLTVHBOP7EJUM6HKL7K64TQ6LJG2NEI7DNPB75TPW545L56HCEKJCYRAY7OGLQGBIQ6H3RZDBOIDWUEQA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000054935777",
        "F2RegId": "FB-000007460035856",
        "AlcCode": "0300006342850000055",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ФИНСКИЙ ЛЕД. СЕВЕРНЫЕ ЯГОДЫ/ФИНСКИЙ АЙС. НОРДИК БЕРИЗ\\"",
        "ShortName": null,
        "marks": [
            "187429256093690724001QPIT4MFAQ3GYZQR7Z5TTTCUJX4JZ2XI7LFHPZ7YNMMWQ4A76OA5EYZUNKLCZFTPYUFVV4AQNU7ZRRY3SYJTYWF4G64KQQAG76QZVQCYAC5QAX54USNAFLJSTH6UHFRGSI",
            "1874292560937807240013YCADFG2C2DLBIDDB7GM44JXZAEBEIIOEBJAVDOSRN4QJRHBEWP2W33XZJTOXBMIH7T3YNKWMEPQ2WZDJELI2AAEDQ2T3PJDJWPRWVOHIRMZQFG3TW44DBCRDDEPYZEEY",
            "1874292560938707240013FTJK4S4LXECKM6NM56X4DSJ6A6JKFTPJFCMPNCKPMOEDTUOJID7H7LW7PKSWKNDMI4PFTICXT4UYERLQJMQXW4FJ7J4TDN3TCHU4IEAVY7JJKQKWBOFBVBIKPITITVKQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000053229859",
        "F2RegId": "FB-000007460035857",
        "AlcCode": "0300006342850000054",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ФИНСКИЙ ЛЕД. ФРЕШ ЛАЙМ\\"",
        "ShortName": null,
        "marks": [
            "187425676323921223001WEZTT6DA5FEZTUG2D37E65XFQQZQLLIGI7HCCU3NRXYDDHXNUOATH7QSGDNPMSVJFBLMLKMBUY3RJLPBTC2DCX47WXYOLKZFD2MKMDEWE3EPQAV5HQ7AZH7GDY3K5KEWQ",
            "187425676325691223001HRO4SWO7ZYUWVZTMD744UHDZVMWI6ADCEOSADCV3B2Q4JA5YQ5RKODAFFVYBTKU7E4TUNZ7HANHGQZLTUPCVJLUNTFEFLUXZBCDBYAMUKQD7HMJHZLQZ2VQTZRR33DSJA",
            "1874256763260812230014PMQOXNBL33GOHLTWSKTLE6CHIV7GPMXUB4LXQHK7FKIWLQG2RRKU6ZGCEQDA2FNUDWN67AR7PYS3XAT7ALJ55W4DTMWFDUOJLVMUKF3YNIAG6F5DWKRGY5AVNS5LHOJY",
            "1874256763261712230013LX6XHCGRYVGQCQTZJ364YG36E2IOVUIF6AQILTDFQI3TQMLFV26QLWNKXFYXDPLJ4ISCEXDR2P36QPW3FP4ABEAXJI3PQQJNUI7H6YK6HID6CAI64MD4LIHRFWXK5ANI",
            "187425676326181223001FHA6C7SXPQMMRXLSIGQY2I3Z7Y5CRMLUW4IMKXNU35QVMN6IR55BGZXOFJHGE2EALPEBV5PUAO5JFC26ABAJ3OCVYQKOMSD6ITRO4UR3W3TCNLYRSCAHSI3RHSQYGLV7A",
            "18742567632653122300162RSAPPDB7RHUBRW2BUO2EVSQEQW5DXRR7BEU6JOGWFK54HBMZ2ARB2PFKPAQMPXOUYMYPF7POPS4UNUQLVJSBHESU6GCAPFI5LEID4QJZ4QTSK2W7JGJNALPTMI2SF7Y"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000054935777",
        "F2RegId": "FB-000007460035860",
        "AlcCode": "0300006342850000055",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ФИНСКИЙ ЛЕД. СЕВЕРНЫЕ ЯГОДЫ/ФИНСКИЙ АЙС. НОРДИК БЕРИЗ\\"",
        "ShortName": null,
        "marks": [
            "187429256184630724001HGMBYP7DJI4TZ5KVH7LX3Q7W7UZ2TJ6K5Z6DE2YDQZCYO7JXSEWKSJUJCR7Q43Z57ZI5NQKE4MDD6KDR3XZR3WFPQFOVHU4H3MUTI7JO75CQYNVEVTQLE3UZBCYJV4YXA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "101.50",
        "FARegId": "FA-000000054849813",
        "F2RegId": "FB-000007460035934",
        "AlcCode": "0100000002700000047",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Архангельская Северная выдержка\\"",
        "ShortName": null,
        "marks": [
            "197305166034610124001533TAPJ7KR5UY6ZHSSQ2LSGAUUSRQ3GZ5WNND755F2Z45RC74UWT2IB2CTOFQEHTT5O2Z6ZPH5JRAPHONTVSHYZIAEHZJI4LYQDD4ZE46EZ2PUBWVXX3MN6MQZCMFXIZA",
            "197305166034650124001NWIXT7MWK7OVLD2SLV7MYM3DAQAO5R6XSKLVG5EWWHNPDUNJXNRY3FY6RIE4L57REF24Z4NKK5WVD7L4MYBXNW6GSGUWDINOLNJU3WYR3OKOPJQRPZ7O5PUVXO36D3JFQ",
            "197305166034700124001OTOUURPP5K33F4XQANDPSF7UPEGTGUU6XR7DH22HPAWXB2UZZIVLWE74OKX5VW7PHRS67LKLQWTF34LBKYN2UXXJNZHJAMIBC4IWJUBSXGSYKVGOZV2624ECTCKKQOFWI",
            "197305166035040124001UNM34UECWHTLPM7BBHS54DBFCYSSHKLARHGW5DQV5ESMWQO5RV3AM7NX5ORH7R4U7YZQWDRADHUF7KAVDPRLL2RODBKMLLCMPUXZT5QP434VV7DPILTIYLNXBYWQXX6RY"
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
                "FullName": "Акционерное общество \\"Архангельский ликеро-водочный завод\\"",
                "ShortName": "АО \\"АЛВИЗ\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "307.80",
        "FARegId": "FA-000000055112089",
        "F2RegId": "FB-000007460035939",
        "AlcCode": "0100489413240000083",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"КУПАВА ЛЕСНАЯ\\"",
        "ShortName": null,
        "marks": [
            "18743000872543072400147AGPGVWMOVYVZJWDUIM4IVBPEUFY7WU3PWDBHHPCDM3F5YXUFRMFVTYYVO26NWOSXK2G2HP5TIBV44FQSA3BMY5PGW3WOMTTPMOAO22AI7LNHAZMBGURKQWIGGUZXYVI",
            "187430008725460724001DHRQHUNVITLT73ZUUNSNZQQ5ZYOV5TXDU7DAQJVL7N2VEI2IBHWIYGQW2HEMEQLPQQ232NDAIMETKARQCODYGGARZ2SWVN2RINIT4PJY7QFSOLO2YL2HQQKSMRCX264DI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "164.40",
        "FARegId": "FA-000000055183462",
        "F2RegId": "FB-000007460035941",
        "AlcCode": "0100489413240000153",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"КУПАВА МЯГКАЯ\\"",
        "ShortName": null,
        "marks": [
            "198417140090480724001JPQH6SDRPAEBK37O3XVSY3AEBQAIJARLYT5APXJM46JEMYEYOC3NXOEWVP7HWREXY2VUTN55TORCQJTVM7UZ3ZEKEHDPKA32XXMZL7KL3JU7PSGXGX3B4KKSAAGNNZFWQ",
            "198417140090500724001EHQQGEV2K37YT4KTBYXQXM4EOMKQ7Z7JRK3HGWZLKHVHFTAVLGPRTVIMJPGDXXQBYSPMTEYMRNLVJX33ILNOE5BMTMY3EW4L6FCJCTRSJ46NQUB5UJOXJAVKO5MHK5AFY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "307.80",
        "FARegId": "FA-000000055066403",
        "F2RegId": "FB-000007460035942",
        "AlcCode": "0100489413240000085",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"КУПАВА МЯГКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187430024935230724001GSWFHOOAZRYY2MLTAKK64BKB2EU3YVEUPTR6L4AJQEELLPTDCRQ2QKWVTSXUISEAVLSA4YXHHYVPQ3JHLZ6UNJSLBXFSGJAHNERNWMLIH7GPSXTU6U54QW3DR45K5MKNA",
            "187430024935270724001NYD37YN2C24N2OC4BAUVIZML5EWHDXVKV6G3BLQA7HCW4T7EG6SA7FIQPQKSWQAAXSI5SBSUORI2CPSPBRCNF7ZT47Z5LF2R7UCZO7LJYIBACMV6EOS5HXSYACVYXANJY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "210.00",
        "FARegId": "FA-000000054626501",
        "F2RegId": "FB-000007460035943",
        "AlcCode": "0300004732090000362",
        "Capacity": "0.350",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЛЁН НА МИНЕРАЛЬНОЙ ВОДЕ АЛТАЯ\\"",
        "ShortName": null,
        "marks": [
            "187425639096251223001AOAWLVOJSCB63AI6CN2AQXFLKEFUNT7EPJJHM5OK3AI72T3A5LWCZVB4QHGROYK3ZN3WU66T6RZDDN2VXUV7SAN3RE7672RTGDZERLXVGRKIIF3NHEMHLYX6QJOBGQXFQ",
            "187425639096601223001APEXPKRTQMCZJHNC23OENXQUOU2RAM6N5JSCTF3CR6RRYAB6XPFCGDK5J3RTVGHXIFQ7VTFPYASVIZMIPRSL52QLDJXXRQA6XAJ5DPR6HG2XO7SLYY2QKW36Q7BHZIFMQ",
            "187425639096671223001QW6IUXOOVN2YAIUO2JNZJJXXGMIPZWZ2N2NVHAQ5TNMILUUPBTSSZANJDTSSNLWPRFWBCCRYBWYLA4B2QVVYSZRQ2GIVC5I72XRLST55TCVI5UPVJYK7UOPOS3BRATGKA",
            "187425639096741223001VKNPVELHT6QK3NJKE6PX2ATMVEJGDB6WDWL6U3W6BYUCEANIBHPYCOG7GDBBMJIWQ7AR3SVKQ4LRCA42FXRPA5X33SN7VXDRXJEOBJEZ5PHKA42CHADTROV7XV55GJFHI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ярославская Область,,Ярославль Город,,Советская Улица,63 Дом  , |  | за исключением литер Э, А1",
                    "RegionCode": "76"
                },
                "INN": "7606118934",
                "KPP": "760601001",
                "ClientRegId": "030000473209",
                "FullName": "Общество с ограниченной ответственностью \\"Ярославский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЯЛВЗ\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "243.00",
        "FARegId": "FA-000000055007188",
        "F2RegId": "FB-000007460035944",
        "AlcCode": "0300004732090000321",
        "Capacity": "0.350",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"МОРОША НА МИНЕРАЛЬНОЙ ВОДЕ КАРЕЛИИ УРОВЕНЬ МЯГКОСТИ №1\\"",
        "ShortName": null,
        "marks": [
            "187321403762730623001ADFWPWNQP5VQHCNMJQRPJQ2SAIHHUOXS6BMIDIYRTVPKWSOD2Z6ESWE4F2XK7HBVRGRXLNZ67QBO4UHPGJOPOZPSFN6F73FCMKFHON5Y24U7Y2JI5LOYI36Z22OMP5EVI",
            "187321403762780623001IZGWMZQTTYQTPKZIUZQZEGIWFUZQYRN3V75DWRKKBD6FTTJM7EXFXAQ6MTHPI7HNRCLR53WFYR6HLJH7ESKJ3MYDKHX7DC3TC46JM7YQQWZCWLWM44URGFR4J2ZT7CRQA",
            "187321403762840623001O7VLEVGPHD4XXOG65MJENUKVCQXXX2JOJXJVQHAO65CNMILMC6CVJ4SCWPTZUM74NYTTPJGW7W554V3JCGZTAHCHCUGUXEISVLTQ3A4BU2RQGCYJEMVN4NQSO6Q3VLGAA",
            "187321403762850623001LZRBI4LQVUMT4722GF43U46TKUYIHUQIWQEV36MWTYMBPP2WADQLYXAHHWU6X6PJNOGZ6IS57DBUBFEHLMTY65XPVIYRZ55OOMRCKDNE64R4VO7ZF3E7OE3IAHDSLCVAI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ярославская Область,,Ярославль Город,,Советская Улица,63 Дом  , |  | за исключением литер Э, А1",
                    "RegionCode": "76"
                },
                "INN": "7606118934",
                "KPP": "760601001",
                "ClientRegId": "030000473209",
                "FullName": "Общество с ограниченной ответственностью \\"Ярославский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЯЛВЗ\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "299.50",
        "FARegId": "FA-000000055139782",
        "F2RegId": "FB-000007460035945",
        "AlcCode": "0300004732090000348",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЛЁН НА МИНЕРАЛЬНОЙ ВОДЕ АЛТАЯ\\"",
        "ShortName": null,
        "marks": [
            "187325309870600224001YPP23YK2NEQXKPSM5XFRQA2DVIKBR5RMKCDBRV3J3GQAMFG5J7EP5TGMB5BT52CNWJ6BRF2N7BXLLEMENMPR5TOOK573YPSA7JJFV754OJCO7R4CERMG566FDZMHAOHEQ",
            "187325309870720224001FDE7E6CUCKXVO7FNLYD5XNFJSARFG65CMF3D4HCP2GPLVEKF56KGNEUBIT3RLXUANUT7F7SPWWID7PLOZBUIAKIKH2W74K2FVIBE2X56MYG53KIRDMLLZQH66W6YOJF7A",
            "187325309870730224001H5MV5DYWRKXGKBJRNXXWH2UQK4S4IS7AC45QDQCPK34CDP66BORGO2GBR5MWP3VBPVSSKSHVXZDQRG4SB6WO7QENFQ7DLDCFWTVQD7TKS4WDEPIUAVC3E3VPG2QXITA2A",
            "187325309870880224001PMFVWYXBLP4VEXOQPA3PWVXF4Y5FTXR6IAHZBVZXGMYVMRRUAIA37HRQZRPYYIVTCQECTA75WUWAA6PZYAEGWEE2KIFO4G7SVGYOKKEGYZCUTOAWXYKBGP3YTT46OZB5I",
            "187325309871260224001ZY4K4AAEKWRHOGJNEZQZ4CYV5M3J4CPAWE7A2IJWBCBVPACEF7XNM7FS2VAO7VNBPEOPRQAUADJ4PK5WD42E46CT5FERAVFQP6WHHPTXTDFMZWZLJDIOS7CWY5AWUQGFQ",
            "187325309871340224001IMP5SMSLLJR6DNKSNMRQ4A6FBUGBDEII5GH7HROYNZIWGO4WNZXADGHOYZYC5AMC64R3LYG7VFG42NXLGJPTQY5BZVXPTETO3IHMDU3JVJ72YBQ2YJGNQMSFQFRZJY5EI"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ярославская Область,,Ярославль Город,,Советская Улица,63 Дом  , |  | за исключением литер Э, А1",
                    "RegionCode": "76"
                },
                "INN": "7606118934",
                "KPP": "760601001",
                "ClientRegId": "030000473209",
                "FullName": "Общество с ограниченной ответственностью \\"Ярославский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЯЛВЗ\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "63.00",
        "FARegId": "FA-000000055144172",
        "F2RegId": "FB-000007460035948",
        "AlcCode": "0100606942420000119",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "197407664107040424001OFFOKZWAA5AMXY2XFTXSYICMT4H63KPBLOCTQR4E7SNFSUCWLXY5XTCIHI2Y5UVEG3T3SXN57PJD62Q5UG5H4NOEWIVPVUT37OXJWPRE7EOZKI6VY67RPT5WTVQ5R3U6Q"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000055129160",
        "F2RegId": "FB-000007460035949",
        "AlcCode": "0100606942420000116",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "187431289429950924001YBBSK3VHZIEMHRP24FFFTXGJYYT7ILHVDPNFKTGGAKMDCXVNN4PU6Y24VBTGNANEO6ENMCGS2PATHP6VCCBS6FZ6I3VCFPO2JCQ3BYZOTUVYECW6D3PWJQ6GCMRSIL6JQ",
            "187431289429990924001OO5AHEID4JW6KDV6BPNV7QRFUQGD5PH2E2DDA33P5SHGGBHP5JISPOHZ4INSFWNQAYTHPH7SLW22NMFKI2PAJGNAAGSDCIKCFI7EFVSQZEFVQOWJGLMZGEF2BWHQ4AHAI",
            "187431289430030924001ASPT5JIIDJK3JFL7C4VKTFFLSIQ5ZCXDK32RXT4MBLQKCXW3FEC4XQ7NKFFU43B3WCN2XTWK6IIFVDLDANURVOIXJ35OJ5D5BT5RC2DVDGT2GNUZRQNHYA2WIUMWUX6QI",
            "187431289430070924001HTNIDURYL7RCW23WCO7NXAYWYIPU3LZXIU63HSUTZDTGBSK7OE5NIAFCKGBSAIBOHKQNYZYXLGQFJLX5VL5YWLGSV6MCP2TOQDA7ZPYTGBINWXEXNDQWG5ZWOWWAAWPLI",
            "18743128943008092400126FSWOBU7YU6CROBUFLPB42Y4MKRXPOFBH7TDSHQKGBBFBFXGGUHODF4XDGRPCTQQYCGAN4HVTP2JJXKL4SWTITC24TWTWQNL44NSD2BQY5O3HQBSER7R33BO3BEAEIGI",
            "187431289430100924001OO7BZJEQQGYNTRUGBZTAZI43RITU6CGYFPPTN42U22KNTV4QFQMZLMP6R7S3JEZHVYBANOWYQ3ZW4PLE4JAVHZBC7YQ4ABVOOTTLJO6D3DNAMNCXPCMSAJXQC5C3ZWGQI",
            "187431289430110924001Q4DQ5QZ7DDUPE7JPGHTDVBU2HENOZPQOEV774ZJXGUQOVDOPRZENVJLUYMCZZCF2KAJTYPXCHMYTI4B5NMAMLENUBU3KVWOQIICNJDZXPYCWFLOWQDQSFQ7GNKEPNZMUY",
            "187431289430120924001AYFY66HQVSRAZZE6YCTONOA33QJWYSBD6VRE7BLYDP5MSAMO7HRXDIE3TZLXEHXSA456BANCYIHXPUIERS6S3NND3DCXFC3AAU5IMJJILT5IPJV5IR3TUS65CJL6SKSZI",
            "1874312894301509240015XLPRNZVYTPG6J3CYGKKCLXVLUF3N26TYBYIZZK5Y2IDF57M5JELY6VQZC66UVJQRO4A7L7QHKA342Y7WBRNB2XAW6Z7EZ3VS7OIXQ26ZPN2EPO2REN3FRZXVPYZ3ESFA",
            "187431289430160924001MASMOCYWXQQL7Y4KTZ5IKB32CQD34TEI4ZLI3XJOTJGFD2UMDX4HJ7EKNZNLHMXZPIFWRIG5OZH77U2ZYIIBMY3IU2FOFBREGL2DATBAU7KUJ5ZI45I427X7A2N54V7RQ",
            "1874312894301809240014A6ASKM4FV7BCHO52SO3BUSCREQ32KW6XSJIEXIAW4LOCFDRO6AV5WWAKSOWBZW4RS6PIBVXT5YTA3WV3R2DGD66FWCOCENQZMKV5EJKFDCY5QRYEGAPYTXULTKWSLVLA",
            "187431289430190924001SL6OOU7T4XCGHYUXO6EHLCNSVUKLJRZSVFHTKDHRUJV2QBEOPQXZHTEWCULAHOCIXC63AR4N2YBXMYXZSBER2O3365YNTQUSZAAUVI2KOYDXLIE6OTITSVPLW52UHOYVI",
            "187431289430200924001LKUWWPHXGJYLRCJUXV5SGS3GZ4YU6SBEVTV4W6E4OAQI5BK7ZZQTTT463MXID3JDRIM65TTJI76NG2OT2IFCJGVHQBU5G5RCCNWWCVXLIBMLZRTQT2EH4PT7EFCUKJ7KY",
            "187431289430210924001OKHC343YKQ2BMKWVNCTNXCTQVEYVKLH2EJR45EXZ6E6DWWIKXDMB2IMTYTAFEPGZ7FKKIVXP3PRYRLB3C4YKUXRDFKTOYYYDATKDSFL4EMXYEONWY4HHL6HTLDAG4FTTA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 14
    },
    {
        "price": "192.00",
        "FARegId": "FA-000000054939217",
        "F2RegId": "FB-000007460035950",
        "AlcCode": "0100606942420000126",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ЭРЕХ»",
        "ShortName": null,
        "marks": [
            "187430394161800824001M3BFJP5VWUQSUUC2DAWHWV7EHMAW7WYW4WHWHEFVJ33L3HV4AYBJQEAFQHODN63YYLUOVXCNYZOZPTWD7FGV6DYRRZTHCTKP7YHHXGJ64VU2H65NLXRH7XVEVICM242RY",
            "1874303941618208240015N3KVW3QV5X33EAQUH6MXJOR2AMXERB5RDFJ2V6OYHS5JSV3YBQ2B72SR5HZYVZ3TSMQMSHOAOQNLCQL2TSAH3RGLZJAABQIQJRB37EWAQAS2WMAERUZ5K3225UDTBAUI",
            "1874303941618308240012V5AY6IMFYLGJXAZBCMGMX4BEUX3VAHL2BA2AMBNGMFT3EI22CYFZBOLVCNEKXHFQXN62GW3YX3BWWSQWTQFFVC4J7XGPB5N2ZGOWFBXI64J4VGQOHTASGMBGD5WORNSI",
            "187430394161840824001CN77IEJNPQFR3C2BNW33SMEOQ44PHOKJO2TNBBGVRHGS63IECUYO6IQT3KWYXRU6CLWUOCXTHJEYQI3OMGYHLJITF3CGV2ZO3F7MA4D7FGOS3DSY7XNHTS27AX32UGC4I",
            "187430394161860824001PPTK6ERE3T6BJZMPJUZUROZ7MYJ4XBQNZJZGWJE5LJOU4DSD5BKM7F3GTZAYPVQ35MSMRH7RBLNECIOZ4X5JTOSW4GQMWZ2TZR7NOTJEU6F7ZAD34EAQZMMXAU76YJZLA",
            "187430394161880824001FC3APBJS2TKAD6OWHM7PZWSZXIPR2VQYI4WPWBHXCTW24ASRGV7GSJKJJHR4T2BLAHOCPVCXOASIITTTCYIZ35OLETLX3PWCB6IB3NFMELL5P4LLAFWMFLKAHY4R7CQFY",
            "187430394161890824001CE7RA7ZZSZULBQ7TNE736QWGPEKDY353NWBADJQQHHJ35GKTKSESYM5SSHTNNMOB54T55K267NRLX24IBM5AVDF3KGJJVXZZWCGCP3ISAGT6Y3LEJRWPPJROOBV3PIFPI",
            "187430394161900824001PGPOY7CRCLVWNEJSABJRA5J2ZMP6RMN5UEIVY75FUSYDNWRIIDM7YBOZILJBNPVCP5TERR27XGD3XZJWMOYK4RI5MYCOJVCBUL7GHS5KFGBYJJOQSD4EFQZNCYBTN72NQ",
            "187430394161910824001NKGBY2A4HE6ORVWZIQMS2QOK4IJYBKWT4FG2ZGFITCDS6E6J62CVH6MLANVK7NJZGJAQZC3SBDN26562Y3HVZWRRG373TK5TGKX473XQJCPEYTWY6GUYUBG23JRWUJIYQ",
            "187430394161920824001RPGWOTQPQY6FW2L6QXSECI5QYY44SBAUIUNAXPWLL2FHOLDYDEMWJWOT4OG2QBLNVPMUW6RPA3X45QBVIIZQTYFRRRAEO3NFSRRDY5VMYBYUD37Z43Q5IJXSQCWSPJMTY",
            "187430394161930824001JYOW2FUV4775KBED4CELB6PLLMIUEUID6L636P4JCVSJK6DKFX7CB5GF7WREVLUCR34KAYMOLI3Q6SVNB53VXRJGMD7FCFDVINO6YNVAC3XQBF4IJAGNW64NPVXE6PMSQ",
            "187430394161940824001QRHEVUPCHW2BILJMMZ75H6A4IALBNQTAYSCMX3LKMW6NANI5FYZGKCJ64IXQKU47RLXKEROCAPMLXK3OUHOBNNTJLATVY7NMO7P3QT7FFBKFYTY3YHJFDFR3Q3FQZPYXA",
            "187430394161950824001WM7PCXFPHKIFHPGCMPEEZYKB2ATCVGVTGF2K37MLNFPXED455YK2EDSHPNCJO5S2CPGR3G66BL7MEQWH4QT7KCMCGBHXWUY2CNYRQ74AJMMUIMB3KPOVQ7JEHFI4N45NY",
            "187430394161960824001UWJE4T77HU3HKC47GGJID4GMLEXKVKX3SNJQRE5O2SBQC2L2TEOAJKJNR7PQGLZEVUKXJBJ3TGNLQTPLA2VIUFLY7FGRCUIJDYW2X52UHUYZMABYYITACRM3VUUGRY2AA",
            "187430394161970824001ZHSGGCUB2AVTKEKJG42ETZUTBMV6LF2CHPFAP5XJQTAJAC7KCSPPRL2KZXWTW6Z2ZFHLQJQHMX7ZP2UTLYCEKFFXS3CXBIYTJIBB53WZTQ7MQLHXVBP3L6ULQCPLIDGCA",
            "187430394162000824001EMF3LDV24YRTD4OOZHHINCTH5URNIK2W5V24M7VMVKLZ7TGIXHRQTNQN5UFYYXQMVVV7W7MG3YH2YGLBIUPL2YRSTOPVBOTO5SX4GXCTFB7LFEYKNHZC5LJRT57QLLEYY"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 16
    },
    {
        "price": "269.00",
        "FARegId": "FA-000000054352248",
        "F2RegId": "FB-000007460035951",
        "AlcCode": "0100606880350000010",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный \\"Армянский коньяк Виват Армения пятилетний\\"",
        "ShortName": null,
        "marks": [
            "198411597055320223001YOH435XYTCMC3BUUFTNBZEZNJYYRJH5IATDIUPSJC2ZHDWG6KVQ5CJG4Q4TQ3G5MTV4PDPTYREDDUYDLBV5LTEJEXTL6DSIEQAPCVAIWSEB6S6WWCJ6MHFROUFL7LOJSI",
            "198411597055420223001OHYUOBO7DWUIA6PF3CBDZTMRMAEHXLHZJSZW7OY3HDT6PHISD43ADZA3ZZDOYJO6UJCSY7YHXNO2IBH5TBEZB2EOE6ZXM3AMKLNFBKNKGS4D64IL2A3UWJY7QPBMJZNGA"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "051",
                    "description": "ул. Г. Макаряна, 1-ий переулок, дом 1,село Ванашен, марз Арарат, Республика Армения, 0622"
                },
                "ClientRegId": "050000053538",
                "FullName": "ООО \\"Гетапский вино коньячный завод\\"",
                "ShortName": "ОООГетапВиноКонЗав"
            }
        },
        "quantity": 2
    },
    {
        "price": "273.00",
        "FARegId": "FA-000000054862167",
        "F2RegId": "FB-000007460035952",
        "AlcCode": "0100000003130000135",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний «Золотой резерв»",
        "ShortName": null,
        "marks": [
            "198416572883070624001USIVW2CUIDFQCQH4ENSF24NAC47LHFEYNLFWT2IATOTP7CRPJHP3NJ6LGUSZGPUPJELHPKHN7FJMNN7SK3V3QXWDS6RHXOFD3KL4EWHPGU3TWDBHA4I6XC4UWKCQKUXUA"
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
                "FullName": "Акционерное общество \\"Бастион осн. 1942 г.\\"",
                "ShortName": "АО \\"Бастион\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "380.50",
        "FARegId": "FA-000000054873439",
        "F2RegId": "FB-000007460035953",
        "AlcCode": "0100606976140000407",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный трехлетний \\"НОЙ ТРАДИЦИОННЫЙ\\"",
        "ShortName": null,
        "marks": [
            "198312514151320224001RDBYKSQDABVFARFE777RZ6Q6BYNV5H35BV7AA2PPHYIACIHABCIXL7JYPLBWJUQ44T7P4FJZI4IFOIKYFF5SHLTSOUS6QNGQX6RHKFGUY32F5KZ2MPR33UC2RXUJYS2OI"
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
        "quantity": 1
    },
    {
        "price": "675.50",
        "FARegId": "FA-000000053970615",
        "F2RegId": "FB-000007460035954",
        "AlcCode": "0100606976140000233",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк ординарный трехлетний \\"НОЙ ТРАДИЦИОННЫЙ\\"",
        "ShortName": null,
        "marks": [
            "187426024167011223001ZJQ4DZEZH63OYTX6J3SCHYILYUIDKXRDA2PFSWLOJ5N6EFJMZRSUWRH6SEWEVB2WQSTIFTCRQCXM5U4BLKPMA3YM4N7MHMRNASU43NK3KYOE5XQXLGTTHLFBQRQSSHCQA"
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
        "quantity": 1
    },
    {
        "price": "235.00",
        "FARegId": "FA-000000055102977",
        "F2RegId": "FB-000007460035955",
        "AlcCode": "0100000005390000135",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\"ПЯТЬ ЗВЕЗДОЧЕК\\"",
        "ShortName": null,
        "marks": [
            "198417300925590724001AA4ONITDSREV6NYOX2HEL745HECJC32D2MYECWC33U6SBQRWFLZEKYACNXDN5QU7RLUERLJPG4S2EI6U3MOBKSPKI3DKFMYL4YGGFQT5JXZ5VECPJIJJWKVFU6VKIDIJI",
            "1984173009256307240016QX3ODVV4B3KCCVYQTH23ELH24SJFRMXFODV6QJHAALDDTCIMYNPDD2I2ZFV5SP3NOHVEFJAD6PTCXGUDAARS353AO3ZFQDOOEK6SWEQXGQOW4NKC4GOHQZ6NDCJOMA4Q"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "225.00",
        "FARegId": "FA-000000055073976",
        "F2RegId": "FB-000007460035956",
        "AlcCode": "0100000005390000130",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк трехлетний \\"ТРИ ЗВЕЗДОЧКИ\\"",
        "ShortName": null,
        "marks": [
            "198417307429790724001X36G6OUEGZGA4XBVPDUQMLSF3MWKAVSX5PZRJ6U46IGYBNEYB6LQMK63I6TKHVUQ5WQNQAQOHME33X5MBS7QA3NSQNNY2ZORFHJB5NSBKIIKRXMKB4XL4MAWI4S5G3GEI",
            "198417307430650724001OXASJOWNYA5Q7DJ7M6V3HIKAVUEYCVLSOTYEUKR5HRVMAQMOMXJC2TE5I5CTK773GKKNNVEWGMJWTL6QTK6NZDTRD4D2MGGSMTO5V7LPMHG24JRSERTJHPHOQTXLC32PA"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "199.01",
        "FARegId": "FA-000000052237335",
        "F2RegId": "FB-000007460035957",
        "AlcCode": "0100606966550000150",
        "Capacity": "0.750",
        "AlcVolume": "10.500",
        "ProductVCode": "440",
        "FullName": "Вино игристое брют белое «Российское золотое»",
        "ShortName": null,
        "marks": [
            "193306335442880723001QKDBJG4DUUSLW37EVUBUKADDKAAPWOLOLHR4L7BGIQCTFG77LVEFVM3WTSA53TEW723BG7YL2Y6NS7MZMPHS3YTA7QWQXMBLQMEEIRTNAIHCQYOW7LHLHEIUZDVBP4HEA",
            "193306335443130723001L2WPUZUVYNYUDQW3QEOPH37GHEW4EXB2DTO3MZTGSUTNSXD33ZBM2VBXW7P3IOXMIV6H3BEVR6L6TRFV24TCGZ3AMEAJH4Z4LIRPH3KF5XCZ4W6UWPFZGSF2KEWZH3OHQ"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ленинградская Область,,,,,,,Волховский р-н, Волхов г,,Вокзальная ул, д. 11 | : нежилое здание, кадастровый № 47:12:0201004:118 – административно-бытовой корпус (литер А), пом. 2, 3, 21, 22, 45-47 (общей площадью 93,4 кв.м); нежилое здание, кадастровый № 47:12:0201004:233 – реконструкция главного корпуса под производство алкогольной продукции (литер Б), пом. 5, 23, 24, 32, 33, 34, 35, 41, 48-53 (общей площадью 1193,2 кв.м); нежилое здание, кадастровый № 47:12:0201004:116 – автовесовая (литер Д), пом. 1, 2 (общей площадью 89,3 кв.м); нежилое здание, кадастровый № 47:12:0000000:2789 –склад готовой продукции вместимостью 50 тыс. дал (литер П), площадью 989,4 кв.м; нежилое здание, кадастровый № 47:12:0201004:226 –склад готовой продукции вместимостью 7,5 тыс. дал (литер Р), площадью 476,2 кв.м; нежилое здание, кадастровый № 47:12:0201004:225 –склад для хранения готовой продукции (литер С), площадью 939,8 кв.м | литер А пом. 2, 3, 21, 22, 45-47, кадастровый номер 47:12:0201004:118, Административно-бытовой корпус, общая площадь 93,4 кв.м; литер Б пом. 23, 30-35, 41, 47-51, кадастровый номер 47:12:0201004:233, Реконструкция главного корпуса под производство алкогольной продукции, назначение: нежилое, площадь помещений 2220,8 кв.м; литер Д пом. 1, 2, кадастровый номер 47:12:0201004:116, Автовесовая, площадь помещений 89,3 кв.м; литер П, кадастровый номер 47:12:0000000:2789, Склад готовой продукции вместимостью 50 тыс. дал, площадь помещений 989,4 кв.м; литер Р, кадастровый номер 47:12:0201004:226, Склад готовой продукции вместимостью 7,5 тыс. дал, площадь помещений 476,2 кв.м; литер С, кадастровый номер 47:12:0201004:225, Склад для хранения готовой продукции, площадь помещений 939,8 кв.м | литер А, литер Б, помещения №№ 21-25, 30-37, 40, 41, 45, 47-51,литер Д, помещения №№ 1, 2, литер П, литер Р, литер С | литер А, пом. 2, 3, 21, 22, 45-47, кадастровый номер 47:12:0201004:118, Административно-бытовой корпус, общая площадь 93,4 кв.м; литер Б, пом. 23, 30-33, 35, 37, 47-51, кадастровый номер 47:12:0201004:233, Реконструкция главного корпуса под производство алкогольной продукции, площадь помещений 2210,0 кв. м; литер Д, пом. 1, 2, кадастровый номер 47:12:0201004:116, Автовесовая, площадь помещений 89,3 кв. м; литер П, кадастровый номер 47:12:0000000:2789, Склад готовой продукции вместимостью 50 тыс. дал, площадь помещений 989,4 кв. м; литер Р, кадастровый номер 47:12:0201004:226, Склад готовой продукции вместимостью 7,5 тыс. дал, площадь помещений 476,2 кв. м; литер С, кадастровый номер 47:12:0201004:225, Склад для хранения готовой продукции, площадь помещений 939,8 кв. м) | литер А; литер Б, помещения №№ 1,4, 5, 7, 21-25, 30-37, 40, 41, 45, 47-53, литер Д, помещения №№ 1, 2, литер П, литер Р, литер С",
                    "RegionCode": "47"
                },
                "INN": "4702012163",
                "KPP": "470245002",
                "ClientRegId": "010060696655",
                "FullName": "Общество с ограниченной ответственностью \\"ВИЛАШ-Комбинат шампанских вин\\"",
                "ShortName": "ООО \\"ВИЛАШ-КШВ\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "248.00",
        "FARegId": "FA-000000050465843",
        "F2RegId": "FB-000007460035959",
        "AlcCode": "0100606924920000067",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "440",
        "FullName": "Игристое вино полусладкое белое \\"Московское\\"",
        "ShortName": null,
        "marks": [
            "193302807223471121001JGFK6EX4E6X3GFII4E37M2STBQEFAVUR3P5IIG5G66CBH5EA6KTGG7STQ3TYWBJUHBBE5M5QWKMOYIY6QIHGKK2KOB6BSX467SSJIGSQGOJ6ZZWWKWVDMPRGVGEFS2JKI",
            "193302807248641121001OWTXZ55HQQVDFF2DVI2U6LSJNU44Y72MAPLSXTYJLXVBXADFKJ7WLOYNJSIWQWYOLKENAP4ABHXZQ2YGAVEM6G42JG6UFFJ6F7DSPXOODXBSWSNDSGOI556YWATO7DHRY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "РОССИЯ,,КРАСНОДАРСКИЙ КРАЙ,Темрюкский р-н,Темрюк г,,Западная ул, 35,, | (за исключением здания склада с кадастровым номером 23:10:1101018:38) | (за исключением здания склада с кадастровым номером 23:30:1101018:38) | (склад готовой продукции, кадастровый номер 23:30:1101018:59; склад готовой продукции, кадастровый номер 23:30:1101018:373)",
                    "RegionCode": "23"
                },
                "INN": "2352034598",
                "KPP": "235245003",
                "ClientRegId": "010060692492",
                "FullName": "Общество с ограниченной ответственностью \\"Кубань-Вино\\"",
                "ShortName": "ООО \\"Кубань-Вино\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "307.80",
        "FARegId": "FA-000000055066403",
        "F2RegId": "FB-000007460035962",
        "AlcCode": "0100489413240000085",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"КУПАВА МЯГКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187430024936600724001G6HJYAYJDPVPOANK2NPXFYLXDIMWFOQMRXSORFRJFK6YZIACZTGUY34ADMOJRVKCYWNVOE4EA4PZQ4ONUZ66Q23IZ2ZVD3V4GADTTT7WHSLIRJMC6CPOKSQEJQ3H3CPRY",
            "187430024936620724001Z7M5DOX26NM6REYVJUX5V7FDI4VHLYBNH3IZVLDJCUSQKQY3ZL3PTQAEZA7NTQDJZGLU7EZCQS2Z6GNKTE2CFMGD6HT4WEDF5BEFDGW7QKG3GATZNMBVPMTEONSSBSY5Q",
            "187430024936650724001KVPPGGWJ5PN55BJYVBCTY35OWUAOK5CWGQ4TC2RV5VM5BLEDTCSTAOAWTYQTA5GX3YRBUOFIA7VJUNRMCN2H7XVSAHA2YL5IJ2IZS6QXZHQI5UBJ3HOTTURM5KUU7MHEI",
            "1874300249366807240014OHK2RWXBGGPFAH4TA5TM7PZVEU5CGQUTQDL4WWRFFV42NZG4PMDUK3LPFPRRLEZDGWMCQRQ5RABME25EIZGYBDMHPC5L4O3GDM7QXQZ3UM4BXJTRYIX4HNW2VBVO67PY"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "229.00",
        "FARegId": "FA-000000055261144",
        "F2RegId": "FB-000007503893727",
        "AlcCode": "0100000005410000103",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\"",
        "ShortName": null,
        "marks": [
            "187431186317820824001UXFXGBJPM35LZ2WH2QFG5SZR5MQM45RESCWI6CMZX7DK4W6PSFVSKYNH4QFMUD6PQHRNHMCMENKWEN2I2YERFFFGFEAZNO4AR7R2PUYWTANX3SZ3JIQCG4L26ANER6HPA",
            "1874311863178308240014BBZWP47TFGOP5KFUT5AHBG7Y43CBO7KH264FPDOJWRUSBT5EF6HSS4KXLZNVXAV3TDC2YOUBT4QCJWJBFMOOPMUV6FHOW6JTWVJGPPRIBQTSBVS4YTINZHNN3YJ7QQJQ",
            "1874311863178408240014VW2X4TESPDU3CZ5GKRX6RN7JM4IWWBJSFSEUA357YRB7ZGLDYWAJWALHROZ42TV7H6V3KARQVFHH4O53MARVQM4THK4XUAUSNHV6HO4P74NDCTUSWMT7CQU6A5CODURQ",
            "187431186317900824001USXTJJICFFHNRBJHVR7ZU22I243J6W2VHJGM7I447R6C6AV3KOCOFXKDNYJH4FLHYPUUXFEJW2EFBMWKDGYC4CXDMUHLLW32YBFM2D5HM5ZEYDBAS2I62VEHOVPMYDUVY",
            "187431186317910824001WEYBT62R6NHZXWA7YIMGK622EEEZE3ZOJ5QBRCDZ4QDB6WBVV2KP65XAFPDYD3BUQWO6BFJA56OJBNQ5QEWSJOZBO3I5OE7X2ZLF2KHZ72X6UVE2VFIJMBMZEJ3FFCUMA",
            "187431186317960824001PFA4PUNSFJ34WZUJM4DL6PDGWMBSK3D67VLLZMBLFCDE3CWNOWD56MJPD6FEA2RON5ILGFCYO4PGKDC3DATZDUEN4H4E5QDGQSUVKE35DCL3CYOL62TJKRZE2KVIWU3UI",
            "187431186317970824001KAG23Z2OAY5YHCDBC73BGKW75UWKYYKV3LXW52VDH4GZUF2HELTQKPETMNV6QOYW3Z5AI7OFOET6LKCNGJO6VS6NHDPW5OOKUBAJVNOBCNS7HMIS4MSG6UVJUAKXNRAXA",
            "187431186317980824001ZUX3XOAMFUMPD6IBFUPFB4LC34HWAKCQ54HSK76NEZLAOY4PGD6APX2CTHJGVUAHH26CVULMYT2AN5O2HKLYA7M5SV5JMIR2KJE255DUV4NCOPKTWZ3GKUZOMEOFCTIPA",
            "187431186318010824001Q2O2SVGMHFQSJMQVXPTO3EHC5UFAN3SYBFA4NXQDYJMVQ2HHTYK7KQKGCRKEJ6M32AZWTL6DQTDQUKEL5T2O3J7YA3LQT6GDT46CZEIABQAE74JKXGBS32N6HYOJL6ZSI"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "240.00",
        "FARegId": "FA-000000054864779",
        "F2RegId": "FB-000007503893728",
        "AlcCode": "0300006342850000003",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЧЕСТНАЯ\\"",
        "ShortName": null,
        "marks": [
            "187429837162980724001RKAXRFFXJGCA64BPRVF7HYCKPIAAOT5M2N23REUI7SNYXUXV4J2DGLUUXLLSH2X3MBZJ57P4HJMVYLO7LSTNIOUJNRO6FE7UFLLFTEYOSUH5DX4DN7WOG3A37XM7DXIQY",
            "18742983716308072400176KJQ243UEN2L6L3NFQLEA3CDU65YLNU2VTJ4CDF2AYYVUG7EBETG3E7N64RPBZBWC2E2ZSOJW45HLHM6OBQTOAH2ETOCB7U4XSIX462VHFZ7SZOAGXTUDIDSKV36FC6Q"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "246.00",
        "FARegId": "FA-000000055376859",
        "F2RegId": "FB-000007503893729",
        "AlcCode": "0300006342850000007",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТАЛКОВСКАЯ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "187431986501810924001HPQY7WINCPLJDOHGCOSHZVS2HQ6HYMC7QJHEN2EC6WKZ4N3NHVZJK2ATD3AWJZSMKAZCZ4FVLUUY3MPYL3PNMBZZ3JRTUEIOMNQ7LGNECYZ7AJNL4BNJ3KQ4CV5NTA2WY",
            "187431986502460924001JLH7D7WJQI4RF7OCPSZ3RSTNHAVCSXJDUOVQS765GM2C5EL6SRQZLLEIDNH4GDNKV5BEDBDTDAHUBTBDWBY7V4MOKHY7YU7IMXLWITBIETNNI6SNGSZT667LTOPZLYRVQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "307.00",
        "FARegId": "FA-000000054718781",
        "F2RegId": "FB-000007503893732",
        "AlcCode": "0300006342850000044",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЗОЛОТО БАШКИРИИ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "187428907462940524001KYF2LY2MWIPUFLNWTVAZ6F47JAO4XHOY23D5LG5BUBB7Q2ZKGEOH6HM3WXRBSFPATT65Y74NPZQFOO5ML3PFPOHDOQOAX3LMTGI35NFHGBB3GY6P3RCX6LW2XNN5R3MOI",
            "187428907463060524001GCKOXPK6UQ2TVIUBYAUZB56FRY4YXE5CPLMAX735PSVL2U7RODAVOTBY2NPHPCFLYYOJYQDQYCJQT5OQSBJPQIU4CE7KTHVX3OS7ADDOIOOROMG3LMERZLP73XGAHYQTQ",
            "187428907463360524001HSQDRSHRYGWLMYXS53MBLIR73QH2CDXP7666W2PGEXUNXFKIMTRV4DBFLT4LXZ6QYPNHQPFGU6UMR3VDONESRNEAQ7CK7TH3WYOECFSTP6EUSKWAWQISR6NUNCK5OTFJQ",
            "187428907463480524001ZOTJDZKVIYXYQW2GLJCEE5U5OID5AWPVPBQ5PQ2LVVBDR7XMT2DCSWV3XR3HGAXSG7UCSWF4UM7EGAGR5SHNZIHW44KRIM4DR2N7JFGPNWVSJNZCM4A27GDDMBJBKYZ6Q",
            "187428907463510524001FXL2JZG6TBVSMP2KBMHUUEGYGYXMLRRVKRDOJHWPH5LAGMH2VF6VI7M7LKMGCYXPSZQ5LPLTGBVMW4CKWOSUWF3YCJKSTKTX2V4MOSTIB4EVEDPQDR22SYO55KJVK4EMQ",
            "187428907463580524001O6XWWZG53DBGGYNHVJ3XN3DGJEYFFPZGL7S6BVJHSEKBCKC6X2PXKHL6XLZ545ODUQTFIFION7L4WWLL3A5S3X6UUNCIGIK77CEBIIHPVXZYC3SNBHCSOPNFBOV4TZ4UA",
            "187428907463660524001OVLAIJL5JQFEKAUTB6PH7W76ZI6JHPX5DXS3D5SPFVACXPI7PIJBIISB5MSL5HJG5G6DMNM6FHCQUK5JXZZFIFBOE444Y35YQU75F7SPNWYL4CENYB3FOGUEBX42GAVPY",
            "187428907463710524001B74HIUXS6BMMP7UNKSPXBEYEREYUVE2PG62SKDTPNNUO2XBNVUQERB7DT57B6MQ26T2KA4XQRZMKUHCDYOMRUX7LPA46NXBVKYHG5UQHSUWPKMGG5TEZK6QVR652GWWEQ",
            "187428907464230524001YZ5WIC2EL67EID5A7C24JFV6PQPX5NQ2BD3AUQEAJLPUEGV4YAA5UNZRUSKZVX4ST3RORPBHHGM265EZDAIWOLVMW5KOOPOZQ7OR5CBFICJF36VCSYMRBBKNUDOEQJALI",
            "187428907464330524001XVC6AQZAGEF7NGNWL6DWY34KGYUHYQM6RNEMFM3OZJQDU7ZQN454NKCGTCPLJBRNDPOWZAX5PGDLXBF6KG7A4FCSNNSHQKLICORPV7UMMRN4MN2B6P3CLJZ5XWZT3Z4LI"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "305.00",
        "FARegId": "FA-000000055276574",
        "F2RegId": "FB-000007503893737",
        "AlcCode": "0100000001400000077",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ПЕРЕПЁЛКА\\" ДЕРЕВЕНСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187326687171001024001IAF4GKVS5PT2VIZQA6C6APCR3IJWCTL5M747MU4VBCVRN2ZTASV3V6BSYWO2TIYF6LUBYY4EZXN7NF3MOUDLLBRNVA3AM3FXNOHMOPZMYGBQ5CRYQ4BLIDSJC4QHZ5Z3I",
            "187326687171091024001VLETV2544TRKCNRKLRIQUVBHHQONV3F5VIBK5RDYOWUZDVTE34WOHBNZDNATT3XHAA3I5QLVNFWDLKFKTFD25IMPYS5J7NJVUTL7KA654IAVKD6VJGRNAIRVN3EG577PY",
            "187326687171151024001HRK52KYB7ZQSAZTP73SJR7HX5UAXQMN7WOOW6QTK7SKEVBE6YV5BEYY433XOCIZO35A3MPLI4F6PK2EWVFHCGAFEHPUBQFEIY42AFKNPNEC53LRSWP5A3LSNLN3TWAXFQ",
            "187326687171161024001UEWAZBBBT7ALVFMC7LLEJQE5JUUXZW7JHOVSL45NZ657ZHVUIMF2N5OPNHKU7U7CCWYJX6TXZIW6HGYCKMLBJWX3W37RXNG2VFUWVLAULQV5ERFACROT55SN3PQ2ELTFY",
            "187326687171221024001HZUU3YAN4GUT6GCZTFJNQOYF5A4D4KTQ6NAQF6ZCKVOPBLMAVSMBHYPCFNWIFTYVY7TTX7CVZG4UNPIPMW22XN6OGK67HJI6U6XZJOJKGVH7XSGDIWLUCILYT7UR2S3GI"
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
                "FullName": "Акционерное общество \\"Великоустюгский ликеро-водочный завод\\"",
                "ShortName": "АО \\"ВУЛВЗ\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "128.00",
        "FARegId": "FA-000000055313969",
        "F2RegId": "FB-000007503893741",
        "AlcCode": "0100489413240000076",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"РУССКАЯ ВАЛЮТА\\"",
        "ShortName": null,
        "marks": [
            "198417782635080924001MHWTA5JDSLWXDMJIQ7IK6LUFI4OFUJN67U47TWATMBPJBPIHHS5ILCTYPX3WZENDL6EDMO42DD72RFNVSST6LLA5KQ2I2FI62X6XDVBIXQMXT5JI53LQFWLMPFEOV6AMY",
            "198417782635100924001YKBJAFARJLUONOCNDCDCKA3ZK4LKDVAIQWHMMP3PNL34YKJECEQYFHVNHK532QUCNPS3HCURTD7MEKFPQSWKVPAAYO4RGPP7L7WIQBIPNX2MCC66IPKPJKDNKH7MURCBA",
            "1984177826351109240015HUCGKOR676KUV5QEMK3EQENQQZKH5XPLOU5JL4WZYEPMYSYGHQHWSSDIY56ILG4SCFY2EGOXBBZR5HXE2EUM6VAGEZ5RRB55BO3I2CKI4IWK56HXTVO3JYGUWAAFLJPI",
            "198417782635120924001ILZKJMCJYLASLFZGLTINYANJV4764V3T2EKH3WZ54EYHHA5TCDJGU2S3FHQSRUICZQNXRVVRGA4O5VEITDNLHV7VPYBYDJ4F5NLEXJOJLXT5ASZKKEQDZCY5ZJKWFCXUY",
            "1984177826351309240015J6BMNAUBFGID5KH5HEWYAPRVM7HKGVECH7CEJ7T77UFJXS2PGEMWTFLGWPSPDCSRVTSVYRK5KUAB2PPRXYHRU25GZVNHKKIXW6F3J66FKHC4T2TYF2AXCTJN7ODQB2PY",
            "19841778263514092400175TT23RYEFUZPRDX6FDUPWEKKQUM2GYA4TMMBNKSR4ZFEQRAPKKKJZKRW3KXJSC3YBNJF67BOLT7O3MY55LAZZZ3VHLXP4BXGGKIVJVV35UTZO3YED3MDLFIT4XYKYWIA",
            "198417782635150924001V7INQXJ6NQTDVIDVAVKQ2A7CIAY7D3OOZ3TRU75T5UVENL7EK3ZDDIU5FIKCIGCNHICWC4NQLC6GEHNM3NU7QXKU4CCZKBDBN7T7JGEZW7LFFWURNJIWHXICK57AVDQKY",
            "198417782635180924001TRKCRWZDBFTDRGEOIQOMYDIGGI7RMA64NHHFV7EQNBYBV6MUFIN3IJKITGKSYVEZVBBSZRQLMK2DUOQQ2ACMEPAJV4QZ2FYUHGOSXCMH33DKDH7PV7R5FICB4EBPAHIKQ",
            "198417782635220924001NQLONECXULWYF7T56GMKR2Y4OAHE7RJLLHCPNQCXN3XYDJ6UGIARQ4RJI2TOX6IJMIVDQXFJEHW4T5G6HXCRMW76FBSZVUAUFJCI26AOIX7JRYG2IA55Y3CJITSVKIHTI",
            "1984177826352509240015O5LXH5AT42M7FIWTIFE3P3FQANGX4STASE6HICG3KQXAXYGN633YEKNAF435PQO3SPLVBADXRPPAVK6IRU2BX2D36KRR7VLTMZZ257CGXBYE4I52RAQM63LBYQML47PY",
            "198417782635260924001U2HSKDPZKC5WPIS73BNQK2Y3YMZXXB4LQJIXKXINPEV3QGYCLHG5BEAFWMUC3QKNPSTF5C4D4UG3BCS4UW564FVBVZXSVMGYXMVUVJHQY2BRVEIUFV4LSEJQDKU7BO4UI",
            "198417782635280924001XIRM3KSUNA6NUXELZULULO5DP4XMARCZHM3HJD63AO7P7N32FXCEUTVFANTWTO3XCYOWQM5LDGLBW6WUOHAY7C34NMSSNIQIZK2LB4GKANTTWGRXH5UJIOC2RM25BA2ZQ",
            "198417782635300924001VDYSLYLQAM254ZBTBZ2O4TBAHML3TW2LV7YSFH2GQU45EPV7HC73BENDRNX4VNREYKRKNC3K623HGOXVQRWJVLBGAVGWGQ4CV4UMZ6K6ZBUKEK3IDMELYZY4QNOQVFJQA",
            "198417782635310924001LZWQY7XZOT3L4RN27VEFKMPXEEJNCYJCRN7X63VN3QYFOIWDHAZXTDGGQZDUMRTVU4AZA22H2YVURRK4WWHZHLLBPRMHCYYHHZ3SXVOYAAWZW6MDMTSBOFFJYGNG2G45A",
            "198417782635320924001PNTX4PM4HQINOMLZ3CRKUHZOGAOR63PM57WNUR3XP6HACSXG2343EAGTCBPOHDELCV7OAPRVEWEEK27BJPOLWPLNYPOB7Y4U2PKSRTSJHA4AHJXFOBGKGANHTTPKY5L3I",
            "198417782635350924001ZD2HHSEZ6ACYDRCQNAJ4NIJ6AE73C6AVOTZPH5WORBFE5BC5ERIQSUR3NPYL7MB7ZV7G6ASJINXEU7CFZUAQLERFQQIUO4OTZ6RGFHP3HKGD77IFMGTXJCVL4QV2VW47Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 16
    },
    {
        "price": "256.00",
        "FARegId": "FA-000000054824367",
        "F2RegId": "FB-000007503893742",
        "AlcCode": "0100606942420000005",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПУЗЫРЁК» МЯГКАЯ",
        "ShortName": null,
        "marks": [
            "187429369728420724001WWUGEZ3GMKWNX2ZEE3P7KV2DTYKMXLTI23ROS3OXLHMPOTNLTCJ5VMK7Z7XTNNSPIYHCE5L7HZS6IGLPQ3YO3XGQRK5GSIALD2HIAUAC4EPUWVRZDX2P5WJI5T5JGYH6A",
            "1874293697284607240015QR54YML7OL3REXXAJWBCDMP3EJ5MFAEZVEMRWN24Z6TFXSIHZZHJRLLY7XGGNFAVSINAKL7ER2OQGUQFFFKPIEGTJKN3KN5RLGWQQEMWKYITXYEZG3MDZ75MTBDWHORY",
            "187429369728500724001W542WHKWG5647NAJP5JTUJB3UEABBMGMRS6X22JD3324T3KM75DSD5CVF6MSR7OARJHUZSXCMJGORCN2JLOCXSRYZNKFJD7CBNYU7UFDZO6AA7KUSCZSIFL2ZHZEO5NCY",
            "187429369728510724001OWTEAB63DA3LAQ6FF4EKBKS7KIYRMHMFJCXLWN6FJJ2Q3L76ICOLT4NCOWEOH44KXKUSPZU7YWBJR7RZS3GLY7J2RUVX43MWLJOSWMVZ2SHEQKZTRF6KJCZFKEAWGZVCA",
            "187429369728520724001EGITFZMCSPJ6WASCWHUDYF54DQZ5LXDFDIR7Y3U73XQ5D6MWEFVBEBL5BBW3MCBFEBR2IRZQJHFROY26EKRKU2W7GATWM2IHBNCWALACVYZX7APZ6D2IM4XIKAXQGLRQA",
            "18742936972856072400126E6A2GWTQAD6QVOQ6AOAGKV7UES7BY6ZWJUWPKCXL6MZGKCIWZGAGTNMUQU2ZMC7QCAE5UXRCJ74HCLJ62ZAZS6C7RKYIUN5YLHGQZV3AQQ64XI6LBLB4W2EGV4W3JHQ",
            "187429369728590724001PRIETL2PRG7YL5KYL7FBTCOTGQAITNSOEONLC5SWNPWKRCZEOZ5S7E2CCKEY37NNEZ3WJ2P2DDHREF7L72PCWT3CMKHDRSBYT3UY5RCQDH6F22RWWJAPAADCLRGOF4JJQ",
            "187429369728670724001OKSYIXJK727KGAJE36QAIQ3LNMF4IDXBRZU5CMDWH4BBQT4VMIOW4K45V7LLQ2XAOAOHCVOTQOVFTMRYDHOUH3FTCCLLMFKI5PHKBSSKE6P23MGPFYGCH2HYYWQ5YNB4A"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "235.00",
        "FARegId": "FA-000000055102977",
        "F2RegId": "FB-000007503893743",
        "AlcCode": "0100000005390000135",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк пятилетний \\"ПЯТЬ ЗВЕЗДОЧЕК\\"",
        "ShortName": null,
        "marks": [
            "198417300927830724001I6HSB2NMSOBAOF3YLTKOK7CHP4SSQKIKLSCCR7SWJHWKVNEVT7AEN6TG5IRMBB36CWI6IP6JRDIHMVEOLC2KZXTXEHAHCJWPGAKLLZDONCFELA2IGOIBL4MDENPYSHK2I"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "225.00",
        "FARegId": "FA-000000055073976",
        "F2RegId": "FB-000007503893744",
        "AlcCode": "0100000005390000130",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк трехлетний \\"ТРИ ЗВЕЗДОЧКИ\\"",
        "ShortName": null,
        "marks": [
            "198417307430110724001WRK3RAUCFW6UFYHUHRJ6SJ775UWUY5FGELSEBJLT2ZXMFKB7FHYS6N4ZZP36WRKT334I2AIBMPQM4GX5K37DU22WX6WYFZ7CP5EWMYKVOIINW2D4HM5ABLANGNIHGOLII",
            "1984173074301507240016C7WS6P4IZJW6KMKLVUU35JAMU76C6HVSQUUXHXXXJCBZE7YSQEZTQHLHUZ6FQV5SLZO5ULH3QLJOESK2EOMZZ2QSGI2BL2XPHZZ6YKAU7N2QTVNLGCYFSHQMPX6MMNDI",
            "198417307430170724001DFICIMWTPHUEXJI3TQ2AYK5F64PQUPNYPEZHVHK5WXPOZSO2CMKDMWKYQ53LO7YXLLG2DXLPC6XWHRG27S34CSWONX3RRMP5QCLDZGLOZCP74WT33XFMJQHW2AWCEMK4I",
            "198417307430220724001H7EP3RL353T7IM6FJ5GV6TOVOET23X6FC5S57SUWJXQAGQKS6UBU3EJUE6VOTOGNJRMNS6Z55LZO6TOV4O3VH22DY37UVRZBVJN5OPJQRZJZWKEAWURCVD4NFNXSX7O7Y"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "450.00",
        "FARegId": "FA-000000055191883",
        "F2RegId": "FB-000007503893745",
        "AlcCode": "0100000005390000131",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2291",
        "FullName": "Коньяк трехлетний \\"ТРИ ЗВЕЗДОЧКИ\\"",
        "ShortName": null,
        "marks": [
            "187430750432120824001ZQW6JQ7OGMFTC52GRLYBDK5OBEU6EHQVWLHLQ7RBR4GML5ZEH4PVZQNRBQJJBBAOIZVFOEQOTQ7GFN6TH3KKPO2WXOTSKQPW7IP3BAYWD4VUQYOQ7JGYZFLGO5G7AXOAQ",
            "1874307504375208240013VKJ7S6COQY4L34CEHSXHFXIBEIOXM7YBS44GWM7ACMJLNTP26CQCKUDDSUGADU3KFGSTFQUVEJF2HDZ3DWGIUB2Z47KOWFAAHB5QGPFEQ7NPHMNLWD7QEHHJMYWZF6YI"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "237.00",
        "FARegId": "FA-000000055174704",
        "F2RegId": "FB-000007503893746",
        "AlcCode": "0100607004990000259",
        "Capacity": "0.750",
        "AlcVolume": "11.000",
        "ProductVCode": "440",
        "FullName": "Вино игристое белое полусладкое «СОВЕТСКОЕ ШАМПАНСКОЕ»",
        "ShortName": null,
        "marks": [
            "193308830099541223001RJKPALJFQCLNTQTBQHUNMJ3EHAYUB6LE2XUSS2XUCQDSKHBQ4X4OYAHKOGMG2L3BN6WVJWYSXRE6QDQJ6BUIFDLR2S2NXGAGMSPON7FPSBSJTRHO5XO4JEGGVRFV64TZI",
            "193308830099591223001ESDFJSTRS34G24MVSPK7JBNRCA3RP4IKFDMSJFQBSQSFHTIVGUJEUXFSVGEKSTNQBCUZBRIFLG5FLXDKYWZEETOOXFYTKEQZYA3OLAEELOYU4PBHCCGLL6AX2ZAXIGL5Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Крым Республика,,Симферополь Город,,Московское шоссе 9 Километр,, | (за исключением: помещений №№ 8 - 19, 21, 21А, 21Б, 23 в нежилом здании цеха розлива 2, литер Ф, 1 этаж; помещений №№ 5, 6 в нежилом здании проходной № 1, Литера Щ; помещений №№ 1 - 21 нежилого здания заводоуправления, кадастровый № 90:22:010601:505 (литер А), 1 этаж)",
                    "RegionCode": "91"
                },
                "INN": "9102257636",
                "KPP": "910201001",
                "ClientRegId": "010060700499",
                "FullName": "Акционерное общество \\"Симферопольский винодельческий завод\\"",
                "ShortName": "АО \\"Симферопольский винзавод\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "352.64",
        "FARegId": "FA-000000055111799",
        "F2RegId": "FB-000007503893749",
        "AlcCode": "0100000004970000182",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски КУПАЖИРОВАННЫЙ «ФОКС ЭНД ДОГС»",
        "ShortName": null,
        "marks": [
            "198417418719130924001E7YNPNZEI2UQMOCBJQOKC5KSZYR4VYCEZHDBOL336ZPQJFG7NEPCK6AATVREX4CSNB74KWCTMU4EM7E2IWDMTSHHJNN6DYOT56JZEP6WRUMN4NXRMBW6IY42YB3LFWZGI"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "98.00",
        "FARegId": "FA-000000055115780",
        "F2RegId": "FB-000007570766760",
        "AlcCode": "0100606942420000046",
        "Capacity": "0.100",
        "AlcVolume": "45.000",
        "ProductVCode": "2125",
        "FullName": "Бальзам «ПАРНЕ»",
        "ShortName": null,
        "marks": [
            "197407663834300424001B2GLJVCLXKMI4KIW5I4YOQVZA4ZF7KR4YRNQIRSZ6AVTUXGBXEDZXP5XS7JBYOXZAVR5DXRO72MIN4L5472LNQQNMUDTZ4E6LCQ2RXFIVELE23WIY44GQGRE57FF3QBGI",
            "197407663834310424001JJYNUAFFVK2GZCJDBGX3MIEBKARAEJHP2IJCTO3MAVTWROVV55YHDETACBIU4FXJEILXA3R3SVF4XE4PHMHQPHZD22HQQ6CFBXDSSYFYKMIJPRPOJGBZ53VTGOBKQJN4A",
            "197407663834330424001JKI6BXH4VJEWZVQBCFBQSS2IXIUJIDWSHG6URG2EMYAHDCTFR3NMUB65YYAWYPPHILVUTZ6VC7TMFN2MLSWPA53YH2KF7GN3NEEELZPROIKYVYZK7MI47DXEBI2MPFBMQ",
            "197407663834370424001IZ4NHBKLTVIB3BOKXYUFN52LAIJCIYIFWVEOTCKNZJ2BEQCVKTGLAYJJ2QQK724ETX57QX6BPE3IKP744A42OJLEZVVGNOXY2YRZT3RG2QFNHNHOL4E2W4MN4CU4757JA",
            "197407663834380424001PPGMS55DCAORZVJJDZC5W3C35YRTJIXAENSMLJH37NCQYCTEKGZTC462NXTSCYMC56DJ5OPFNMEBOQ574CF62TLAS73PYYMSN45AATMCPL3B3DRHI2QTH6HRTV2STNYNY"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "170.62",
        "FARegId": "FA-000000055007142",
        "F2RegId": "FB-000007570766762",
        "AlcCode": "0100000054580000188",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ПЯТЬ ОЗЕР\\" МЯГКАЯ",
        "ShortName": null,
        "marks": [
            "198313747223550324001QJSMIB7EUAT6C5QQT5QTAQYR6Q5BGZSJA6QTDPAEJJ7RDT5AQWV7GWOI34IOVAHMZBCGCQ5ZEYKEPQCRCQW7EVECONIHGBCLT4QH6HET34BH4AN5FQDJDCW5KKFXMTBKQ",
            "198313747223730324001TTVG7NMSRGBIYL62O4UJFAWAUMD3CMCLNO47N2BX553G4RWDWAR2BZU7OEPHWSGERGLT3PIMHKV4WIYOZ4Y3N2TVWIDQUZHHK2E54JTBPMOCQA2MDEQMQT37JR5JJPIXQ",
            "198313747223760324001WBY7EJX4B4EA6MLDSQCBXE6WKQUZEUMDEPWSX23Z2NGM35KANAOOJRUP45UTQAIVE5767RAFGCYIXOCFXYCJMTRMJGIJ3VXBQOSTKNWI7DM5O2IKK4SN3NMVI4HU6XXHI",
            "198313747223850324001IE5AHJ64ZSNXEQSOZADJMHBXXIVX4QS2JY3QWKR3WAO4UUOSXURAUMOTVBUPNGDNXAXA7SPA5HJKVIDE4HL54K3V2RBSAJWXQFB5RQDPLE5F6GBNG4U5IB7COR7A252VI",
            "1983137472238603240015JU7VZY3QCMCQ2J5UUN6FSHN7EH7BDXHCR3WO3K3J2DQZVFW7VQWWZ454SGGTV2JTXKFA5GK5ZKCRSOH7X6P6DYFWVSKPO6VQ3OEPE3LKTN2UN5EQSGOVL4LIHDEBHGFQ",
            "1983137472239103240017LUUNAIFRYRQZBEDY45AMDJ3KINPBG36YZ6UK2DYZAR5NUKB767MZHSTIT5UBWA5CXGVNUT5ZAFIBN2GDYGNLVROMPMKIOGDKK2KECJQKODUVOOAEIGMMY3DMTZCZ3GCI",
            "198313747223920324001C6XUARQ3E6ZL55BPPMQFUV7GKMWIW4LHBSZNQOI3DMB3ZHWOS662HZBIOEW2CONFAS45BTT2P6TYLYRJPC2AGY5C7IWGFLX2VJWMH75X5QU3EBBR5TEBB5AOC3RIFD26I",
            "198313747223990324001TVC5MF554CK2MQTPLUZEPSLYAAGP3EHWARJE25EOQXDXRVSRWXYMB36ZBJZTCR3I6KSWLWNL75C5KGT3G37KLFJSVZBOXUCOED5HPRFTQPUCUO35H3TG3LFCXXNKIQYPA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 8
    },
    {
        "price": "318.06",
        "FARegId": "FA-000000054674008",
        "F2RegId": "FB-000007570766763",
        "AlcCode": "0100000054580000119",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ПЯТЬ ОЗЕР\\" МЯГКАЯ",
        "ShortName": null,
        "marks": [
            "187324581563940224001WQURD3BUJQITNDOWYW54ME5U4IHG2A7HRFNBO47X5YY7XAQ5WWV5VV2ZJFXIZXZEWJDNC5CAJDSOWNVME5LM26QKS5JCOMHZD2YC4OAF6Y2BNRBXFOP2BOTF2COZW5MEY",
            "187324581564100224001ODAMNJPTOJSJTNZXLCBBRWZD5MOKYYZTGMUKHVH2MLEGQYF3GHAVWKI3MGXDT6VEY66IENHSF7HJRWCVEZCQAJ2YDQMQUR2PKA2ZOHFZZLY4X6MKQM7GUIHWS7E4GRKYY",
            "187324581564130224001QWMYXQXNTW5PCS43SUQHEEEHJU3UGR6VW2Q7AKNT2LNZKUDHZ26A3XHO6LMWJCBENSVMU7HKOCPHKVHZACLWNHC2ARN4RBV3UM3WQQ2LCPD6K3AQDVESC6HK5JKWFZE3Q",
            "187324581564140224001WPZBDDE3VDO3ASXSYXO67O3IHE6QZVDC4Z2F6GBX632Z7HGDWXGB4GNMIGGEOYJWH5GS427JQAOV4UZ2KRN7SGAHI7SJMSBDP5MLKT56XVSUBFCUIBDWNFZF33UXPEQNY",
            "187324581564160224001Y7YI6MCBLQCSZCAYUCZCTPIINA6H6PTKRBPJAVUAPTZMI36ODFQO64IF34WZCCJ7PXHMCCTAM6QLNM7LCMGREYPGJNUGVKFSPLRJXLOTM7RCEZQ7SQOHX4XNI6BRWEFOI",
            "187324581564260224001ZHHAT5C7MDCGIOEZUGB35DR5RIWBTEWMQJ35DDP45PISPAIO4SZCRULQWBPXN73VFOXC5WR6CXNQGDKMH2PXORZVA3KO4CYYFB4UIIAEPGK2FRR7H2D53WERRAV3PXHMY",
            "187324581564290224001B3UQXDMNSKKWU64CJOAPRJRK2MDESHBS64Y35WEDDTKU6KUIBTFBBAD24N4YAZK625TYGGTMXCDOACXAKTJJ3QWNSCR3FGJKDJE5WSNB7HBOY2F4FK6ABVCYUX7AOQOHI",
            "187324581564330224001WQ4E6DNK4GI2KRB7QV2CLRUOXUPF4LZFFZJVNZTQW4I3JMYMP4BZXZUDOADRXHSMGIEQ7ZVFFPZEILOSJUAUJIU2FSFVU6ZDSEVCER6XR6LF6G44M4JZMWE25ZGS53KSA",
            "1873245815644102240015ONBDQKHNOVMPRF45PMTSLQSJAY3CZQZ7KQBF6BZ4QXPS6TZ4LZTWP36FR5N6MNTIQQM3NSSGIL6GHDTYX56DBN2S2IVXTFO2WBEUN4GOHDW774P32A3U5OAGEWCMFK4I"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "165.00",
        "FARegId": "FA-000000055374459",
        "F2RegId": "FB-000007570766765",
        "AlcCode": "0300003247940000055",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Берёзовый рай\\"",
        "ShortName": null,
        "marks": [
            "1983145473122603240014DCG5QRYTF6D3DG3S4T65X6XNQSCBJHYO3EKKBUK3AOFHB3UMVNUHDVOMJMZ4QXKZC4MJD75SPNPIZFF5UL743J7E5IZXGG4376NIFVEMOBS3UHLULHE4TQ7QNFYHNYFA",
            "198314547312340324001CJTWVNCCRHI2T4ILRTQSOSQ544NAKGESAOY2BIJQULHCZB54MST4N35ILA4LJYURWQMX23X32WCNN5ES4RVTY4PIKTBUALLSH2PVJLMLBTW7KXVVQPANXIFIBHZTNR6AA",
            "198314547312350324001AWRKHPMOYUD2DZMTV45I7TGYYEXK7Y2A3U5JSKLSBXYS56XDE252G2CLP7FR6EKFJEFFU3G2UV76OBHTCO7WUKAEY2J2TRDJ6UYQ4EH3AKRTGAO2MUINKHJ4WQXDGBIWQ",
            "198314547312370324001KJLPDF5UWBTYUMXSLNWGRVZWXIWAWW2WH6GMLMYKC5P5KH4ZEF6LA6PNU7JWJ7AGIN2XD5N4LGTNYHQZARTIET7RC4VAUUZAPKOK6UQNWFL5FOLTXWTU23KG5CBXUPMCI",
            "198314547312380324001IRIBNHILAJKKPRXXEEIPQ6JITAJM2W5SEVBTV36SEHTWCM4D772IMRHWHAUQ44JY77U6IKIH3QRFHIHY4RSVBIKSDWWSLZQVLONYV5C6ELXTYXEDAB4ELJCSE6OALVL2Q",
            "198314547312400324001MUFZDQ67ZUEC6SWYYGXP7TAUQI4BBLYO3QEWYB7ZCEBUECNRI2OUFWN56KRI47BEWT36AQRPXZGDKBINERK3SSTTAHPOWUUX65AMVMEZRLBGP7DE2Q6NCSHKZEGSW2RXI"
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
                "FullName": "Акционерное общество \\"Озёрский спиртоводочный завод\\"",
                "ShortName": "АО \\"ОСВЗ\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "165.00",
        "FARegId": "FA-000000055241778",
        "F2RegId": "FB-000007570766766",
        "AlcCode": "0300003247940000090",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Три Рюмки»",
        "ShortName": null,
        "marks": [
            "198417967405000924001DACDG3CHKEPFW7ZZW32SNVAFB4I5HQJW3DYQSUBTQ3RJNDO6EOZLXR2KUG5N5PZDHPFIDOQSTF2DWKSAFMBAX7J6MQI5UORVLPNL23OQAV3JMVWLM6T2O47BVJEVEGUDY",
            "198417967405010924001PLOMYIA7QBGTR7YUEXSIDJVSBQ3FUWNMMHSNWK6QQ4FP4TLCWIMK7IZIDO6CGJQJJLWOVFJZWYQSXEQFAUC2IBZCRWG5LY6O7JNHSEGGOXMWFJ4IYKVNVOFYVN6GCPBDQ",
            "198417967405100924001MEN5MHC7CE42TSLPRVBVGUZUVENEL6C674DBW2SWMYGJLF657X6NAPOIEE55XORFMWYDW57ETT6IUUU6YBUUL665CGZVQALMYMNV2CKFWBYWY7WSTVU3OZUHCCDV4FGUI",
            "198417967405110924001USQ5S4NG3YEAZ36HJ76RBLITJYAWP43BRDCAVN225CCX4XPBLR4VKQAWIH5NCEXMIB5YEMJ5LHJUNPEH56YJTBXNAXDJ4QVYSWYO4UVOX72TRRRAFOW6OACBEHULLVNFI",
            "198417967405120924001IEHRBEEK2AGDDQPPJJVA5KZLYEWDQXXU53FKWWTL3HRI7LGZ5XFR6C7YR6US43H3GPCQCUXGYODUKGQGSY42U3TAFUU7O4JU2YXN34VURM5UZ6QIMWZSTNIA4MX2HYVLA",
            "198417967405260924001SXUFDFDOMMLTHWA4GC3OMOORBU54URDSGBKKP4FPJK26F5HWLCHEVDVCFFOCY73JPASIRVINAYT4KDRTK2FLWA6YIECFCOSQUAZ7AOYFFEKLJCS4JTUQBHKDPAN2VL25A",
            "198417967405270924001LKCVKNZNDOLYTBMKPQXJW5SZOIHPDCTSPVOXT4JX3TZA5HYXPXRCWU5GCX4VRSFCSPUS4NJVARSGGRCTPDAMNPL37WI6QMLCWDFOS3XSXWY4W5GDTQA36U7RTAF2SHRMY"
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
                "FullName": "Акционерное общество \\"Озёрский спиртоводочный завод\\"",
                "ShortName": "АО \\"ОСВЗ\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "299.00",
        "FARegId": "FA-000000055366867",
        "F2RegId": "FB-000007570766767",
        "AlcCode": "0300003247940000052",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Берёзовый рай\\"",
        "ShortName": null,
        "marks": [
            "187326681022131024001LUHG34BY4GIF6GDGCP6WTZD7OIFQQ2SOBUBAMGYRT7QK7RJLZ2QSOFB7E7WTPZ3JL5MTZTRWZRXXYEPG7UCBO4EM5C7URTOGVPZ5N5PBY7DUIZO7EBCKZ4NXJWJS3GHDI",
            "187326681022141024001ZXXLFJOTD2MUTFHK5DESFPRW4A5HPMXRUJNPTH7JNN3HT2KOGPRPEZMGYEEMLCS4DKLOAUVWKHKMBTBRLYCASDAFUQDBWDCUFTN36DIKCQFG2GU66WAYR7VOTZGNT5VNY",
            "1873266810221510240017PJXOGX2Y7K7BSIYQBLOVYBUIEMWZNOPXBOBPTVECH34ALI6WCG3WN5L5FWNMEPPIUB3W2TDAO4XP6CPRYSBN47PDTBGIKBHSK635YTRGIQARCSBDUVYMAV2A4TPMKFRI",
            "187326681022181024001KBHU7WQTWBPXYAON657CNS7RHELCMDYWQWG34KF7GGV4Y7ENGE4WJWCANX5V7QGZJ776MHYCBIDX3KH6W3DFGP6MXFC47RZGOLF77D7IZWHR5LMUSEIC2ZD655YS7EUPI",
            "187326681022191024001O6YUAU2V5GDEWDU3ML6IY2EJDEAE23NQLXGEFVB7S7BFOXWFKLTROF6YFPIXGWIAPD7R7HHXREII7TJYEDXUSKSRMR7FFHP5AOJ32YV4EEUFF6XMQW2QCPDRHTXKNVW6Y",
            "187326681022241024001MFT7B2EESQYYFX3BMARXSJHVAAGHGRDGLTORRJUWX47OVFRXG4WD5NNNYNBCGEQ2EFKXMD3TMBKU7GHQAQHY4FPGHO3IKBGGJPRBHYTMFOFY2DTDK36PRWB3TC5FSMMUA",
            "187326681022261024001YXO2GNHOFKJ637ASH3PCNQY5S4QGFJ4T5Z2PMBDKR5NBNFJNIESRCH2ECASZZHNCZTQNNJ77IDJDRLAXPEJANMSP2GMWG3OULV7JTNC4H5TZICPUBSMU5SROT6WMDQIOQ",
            "187326681022271024001DII3L2KFFYVVD5JDJNXKVRSEQAMHOANYWMKV7DHYHEP3KGF4ZDFKATKOFW45TMRIL7XY2AT2IGMNOTALOPK2JFZYKN3746O2JP7OZNZQTLPXEF6KOMZDUWQT3KIPE75TY",
            "187326681022291024001YM722MW5SDFFVKIUKAZZ6UDWEQ4E67SZJM4J6MI6YGL4C6TTLFCSG6RPZ2L6ZHSRPE7Y46TTUVF3TIKORSTKO6ULWGUY6MWMWMA6LYUIYLEDUT2UICGME6GSX5N5YFALI"
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
                "FullName": "Акционерное общество \\"Озёрский спиртоводочный завод\\"",
                "ShortName": "АО \\"ОСВЗ\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "299.00",
        "FARegId": "FA-000000055403504",
        "F2RegId": "FB-000007570766768",
        "AlcCode": "0300003247940000088",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Три Рюмки»",
        "ShortName": null,
        "marks": [
            "18732668002680102400146FM5VBKXCBPDU52ZQPAMYZ2CUIA72Z4RFRA5GCV5HCIOTEF5RV2ZZ6Z5V652DGTMQKFQFPDUXF7DUGBZEZNJN4AQ3KXU2YVNXYSSYJXRTT3ROU32KGUWKUY6EZSU3DYI",
            "187326680026821024001YNCMUNJ6BDORRH6XOJTVSUHKLYWTJLK57JERV2JP7DJK2KNRHCH7BQVAMMGCK25Z63SKXO3CLNXPOMT76EWDOCZX44VUOFKYWL6PRCWGPISNAGKIVIIQSVB7NNODDSYIQ",
            "187326680026841024001DGBXN4D6ZKSGM6EO4FHHV3HRHASJQ3RPDQDBSMVEMZQUGT7V43VZY2UUPITO43MYVXT2MBT2BTZQAP7PDZQ56Q2DPKEMGIK4Z5QZLYRWA7CODQ7SXK6AWIQRT5EPBCBRY",
            "18732668002686102400145FJDCMMQFXAQV5C3FRTOKL6TQ7RXW562ZPKZQU3TIOKJYS74ADALTI62B7RYMMJ57Q6G2Z7RZPGHTCNLKTYVVMGEDIAO5XG36WVSM7TXAMXEH5R7HK55FJ4KAWWGWS4I",
            "187326680026911024001VT3LAF623FODC6HNJDQQTNM2B4EUZHEFTKLPMWZBVX45URXW7TJ6AKJQ3O7E72Y3PD3QPZP3FZZO4U2LC2D2NQ75MTQIQMHXO3HBVG3YD3P3Q2PF2TNMWNJXYCVNDBM2A",
            "187326680026921024001BOSYXTYPERH3ZGHIRQJWWQSE6Q6SWVJOV46XPEC6QPVLGNBDHVSMZWWUBBQAEGFGYIW5JLFTRW7ROERLQ3QUMG6EUNEKS6DA4L57JXFWMDETFHVFA2PIZNS7XF5GDC5QY",
            "187326680026951024001I3AEZEEXAWGMR2QJHHGWVZCHDUEIBQVSHIX64OOULLA7YX6OJM3BURXIJMWHB73K7GOSRVQMBGPNX5GLI247DLO6RUTHNNZVTBXBENO5HBY4JBTTTDZ6Y3O6UAZX5ZNCA",
            "187326680026971024001NGU4JVGU4VXQ3RMHYOBKX22QCME77VEJLB2Q7RLOX5LI2IWAME6DOVZDJP7XQ7JZI2XXRZBTPKSNEPWWNZ46GX47Z7JFNR6PII56LY6UQGF5Z4H6KTOWPGYQEZSDG7GDI",
            "187326680026981024001OWCDJ72MWPHMRX2QSZM525CC2UI4QW4JRPVRDXSJROXMREHHJTLAG3T7QHVNDWKUCNKFP2AXF2L35VVO447KP3WVPKMZRDRZVRWX53IMLFK4HYVRGC63YGKCTGFTNBH7Y"
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
                "FullName": "Акционерное общество \\"Озёрский спиртоводочный завод\\"",
                "ShortName": "АО \\"ОСВЗ\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "174.00",
        "FARegId": "FA-000000055205452",
        "F2RegId": "FB-000007570766769",
        "AlcCode": "0100000005410000037",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"БЕЛЕБЕЕВСКАЯ КЛАССИЧЕСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "198417316066340724001EL3XECMWTIZWMJZUGOBDZ4NOVQIG2DLVH2HL3HPSSSPQ54AEJQDVJULP5LGPBZ4P3EGEWHKFDD7ONFOAFPNBAPSTFHRJXAETEK4W5Y2D34LJHMMYX7DVBKQC5ZZCIMEAY"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "178.50",
        "FARegId": "FA-000000055468205",
        "F2RegId": "FB-000007570766771",
        "AlcCode": "0100000005450000008",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЧЕСТНАЯ\\"",
        "ShortName": null,
        "marks": [
            "198418203397320924001UH4GDIYFVS66CVU6CANJCHQ2OA22Y535JRJUS25JVLYLX4CFRZEFJ6SM7ASCZ4ST7SE7APSW377Y3Q2EQMIMFRSY5YSZPEUC74TTY2SJPG636QQSTKW2K2MIXABJD6WZI",
            "198418203397310924001NUTSKLRLOL4K3PCUOSXJ66C3QIEIQZ5HOAIK7B3QPLL5XQR45LGKVZNKL5RNPUJOHFKH4CVAHG3MACJAZB3W55AWT5CBMH66SVN7WE4EO7KDHWHTLROUN5TWS6I7LZ42I",
            "1984182033973009240012BS7ZAV4JM254RYFDSFJLCKWAEJ2RUTKWJ6GDD7TH23AI4HFFFYDBCBX4DYXKARE7NVGVCNKK77FVNEBHCUVXL77S6RS53MBHB7UAYSPWKWY4X4J65HEL4HBDLW5ZGBAY",
            "198418203397290924001QADBIRQC4SOT53MWH4YW63GSOYYFR3YCM3BPA44E4JYJA6KB6J3AGKR4RKKQCEW3WLIN2RIFVEZHKTE6NOR5EUY5CYNJ7EKUJUHGEB645QQ3UT547GRHNFMA2KCCSMIVA"
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
                "FullName": "Бирский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "174.00",
        "FARegId": "FA-000000054852443",
        "F2RegId": "FB-000007570766775",
        "AlcCode": "0300006342850000032",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЗОЛОТО БАШКИРИИ ЛЮКС\\"",
        "ShortName": null,
        "marks": [
            "198416858109430724001WIE6EAL4VJTINQ4XRDWGQTUYCQT6VYE2QKNMQJK7PAHAHIEQV764BRI7ACHMTSQGHIOO4IVFE77UPKJNF6SV2INARRFVAQCASITG62AQQY6NOFBUCORRARTJ6BMWRV3DA",
            "198416858109450724001RMKOBKRBKE4LOWSJTH72WDLARQMCBKFD4PJN4OZZRZ3BLGOROVZ5CFKYUVWKAEMGXRILNVZ47NDF6J5NGE4VK7QFC6YGNPKV2AOP2Z2DBPJLP5NYD4XREEKJ2I3M7773Q",
            "1984168581095107240017TZE22WDIT455D2ZUNGWD53FAACQ3RYBYFUNRMNKN4TFPHFJL27QMOP77SEUWE2GIMTZUYBDBTUGVOOVD52LAMHT45TUXLYACRBY46MMA3V6DYBGFSIMIUO4NWVFH2UWQ",
            "198416858109600724001AX4FEKZTUABLNZCVU45PAU6OVUQYYUQWF7JN3DQ5WOXZK34R2EN2QB4CB6LWUEIIFUEXAX7HEHRBKW2MQ7FDEV3C4I55SJ7DVHKTQ4TBPTE4DQXOCHOC3K2GP3QG6XWDY",
            "198416858109730724001CU5FWGC3ABKOZ2KPKB2AOKRDAMJXEFDVOJC2UMJ5UY7WB3AOETQN3LI7BYWK2RZHI4BLGMY7PWVM7OEJ7F3HAZ5TLALECQ7IBUKBIBBUVXLCSY3KU7TLQZZVSYBMMWSHQ",
            "198416858109740724001YBZWFZ2H65FJSIX2ORFO2BHHMUWCSYSCAKLI5X464XTPJFXT747WWWXTATAKSK4O3MPQVBPXWUVOIASQ3UOKIIB4426745UUGRC4B63DKUKTWTKUK3SXVTDWW447JDXEA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "199.30",
        "FARegId": "FA-000000055391822",
        "F2RegId": "FB-000007570766777",
        "AlcCode": "0100000005450000102",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\"",
        "ShortName": null,
        "marks": [
            "198418201407200924001Q4EP2O2MHP6IZVDH2YAHCEKNPIPU5BZB63ELEY3YCFH6TXWU5SZBQLG4OKQVFY7QSBJRKNRKNI3VWOTWBQVE7F7MGPYUTG7K7LONDS2WIMBW6J5RH2WUN3E2UMDPLYRYQ",
            "198418201408900924001FRIJGEKFY2W734I46GY2ZRE2IYLEV6WZ7J4WPOBQY552R6K5TVLG7WXQPNVE6KP6U3CHDFVZZJVQSD77JSWQO47Z24EGWGJLJYBQWJO3Y6LQZC5ITWS476QPMB6GOB75I",
            "198418201408930924001M3ZDEHQRRIZRSANPDOBQMVH3WMHXQ5THLGU2542VUR3G5J2OETOCPCTGP2O5UEUYEP3CPDR5DXSX345I4XCLEU42XJ7NI62URBYKJRFQZUH2QWT4YSK5XJ56WY7HDO3LI",
            "1984182014091109240012NZEGG5JZ4CM5UR6AT6OIUVY6MIRIKBCJIWDER7DLJ37Z2AXX3IS25LEDJLMZENEC4CHLJQMZDAC7DQP6XJ6C5HVOFTZAI22CZS3W75RONDEPJ5U6WT65YSAHXJG6AZZA",
            "198418201406980924001CCQVCJHPCWTWPQGL75DIU2SW7QWRUYZS5Z75CYHOCN5ATYXYLPHQYN34W6SHWJ6T55PSZDQWIK6M7IWPAFTG4KU5KAIJQQA7Z2CO7HGG2PS5PVIZ3NLTIKCELUOCB4LBQ",
            "1984182014069609240016LR4S3X5BJBJRSRCDLNRPV6N2A4UJBSOPKUPIR56IH5K5Q4SSWKBGO53S2OKZR7KLUWEZJG76BX2BY7TADAIHJ6VCD5MCEV54IPDRAUZODMZYK2HL2LXAPYKREJQNEZBA",
            "198418201406950924001SHHN2LZOYX6RTSDBOVX4BV73QA3KNJT26L4L4YDD4GPIU3QO2ISCYMF3ON44ILAGTEZIFOQAE33NK4LR6O7FJMDZUOFBA5BVSZ6ZEQ3QAZ3UABGB5A23TLK65MCSYAQLA"
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
                "FullName": "Бирский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "281.00",
        "FARegId": "FA-000000055376859",
        "F2RegId": "FB-000007570766779",
        "AlcCode": "0300006342850000007",
        "Capacity": "0.375",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТАЛКОВСКАЯ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "1874319864952409240013GGD425BEWU2BU4JUGDVI27FNA6VCRNMYH6GJWAW6YACHRGOKIGVJX5ZCBHCE3TEAB6Z7QWLUK3DILQKKUJ7PU2QJO2BFJLYZQNHA5SQHWJ5D3QHEJ43K4JZMM4FKWSRY",
            "187431986495310924001HS6CME36LOORZWHCODSKR7MBUYC52P5FYOGVS6QH5VDD23L6W6OM7INUOSGU4DXLAQ4KN5N4P4K4PVNY3AVFZZGIIYVRFQVPG2YU3LNN2WKFHTCTCZQWZES6UGLYUQOFY",
            "187431986495360924001SH2VCCFIGG5RKL4YZEXHVUAJUA72V55ULQNMW5V2PHRBDMBBCTL36MAIDEVSQ6BBTNP6VL7KLB52ODSGJ5M76QXQ6JMWDCRI76LHY6QDVN47HYCMSNNLZMIVQOWENHBBY",
            "187431986495420924001SNONALCFP7ECIHVLAHA5TQ2WWUNCZCW4YPEWQWNUHBFZZNJQDLJRFV2HMTG4BNTFNMQ5J5D525NP4QFDUGORG5I3XC7WZJBTGBZW7ELASXPKBTYS5GAQCQP4UOATHQFDA",
            "187431986495450924001ZMF3SNOGGL44IZC5A7TS24TIXYIOUW54UZNOVWIKEUTU2RAAVT2JHQ7MFK4Z2YNWBWRDLTW6MFVB2H7NL3BQKIRG4GPWV7HQYJYXSICSCV26EKCLGSAYGTFICAXR7XQTA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "348.00",
        "FARegId": "FA-000000055236848",
        "F2RegId": "FB-000007570766784",
        "AlcCode": "0300006342850000030",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЗОЛОТО БАШКИРИИ ЛЮКС\\"",
        "ShortName": null,
        "marks": [
            "187431445117640924001QTKGUOLYA4RT76LXJC5R4FTD2A5JCIAVFAKOIGK24GFNSLURFKLINYUYIQPBF43RYC7XHTEAWPQ7KJJSYLQSNNNA5WD6XLKW3K4UQN674UNV6SDJT736PKIHQJ2W6QILQ",
            "187431445117680924001MKPE4R6OWBNR3OIABBFI342YD4KY5LOQRTFQOITWCJCQFMY353VM6BQ7DQUTXZK6N2XHTWQVCHSMVTDBK5VQYEQZXSU2IIUYV27V3QMXZNGVUXVUV5SJSRXDX3TUNI22Q",
            "187431445117740924001OE67HZH7IJ45EYNR5VB7QJTLU4H2FAONSCFYTPEFLH6SFTVUBVLRSBJGSB2MWQLEC3QXFITIQPCV6WAPXUJD65UISHFRDN42EFGIY6PMILVKCK4ZMKFCLMP5JFSE5BIGQ",
            "187431445117770924001WADDKGAIRWDOATLR7OF3HJSX4AYIQRHVXFGFZQUNMO33KUIHZGN5KCZPZBZAN3SCHMAJLJIOQS7KGDNGCPBGGBJMFZ2VHZHNGB67X36TB2EFFIZQWCTTPJHAL353R6BUQ",
            "187431445117800924001IKRUVYOOAGZJW44KR4KNMJLBXUI4LTOUGKVE4LOYUDAGCVME6VJW3NAR2TWGHBJIAEOXSPPQHV4HI6XZL2N7AEQTCN7IOW67EFQW6Y7RQSDFWO73CRH4TJVALEA5H5X4A",
            "1874314451178409240017WHBXWBKB5I2Y63KR5EQAHTMHYJQ7KGDSQB7YKL45FT76C5ED635LNJNUTPFFQDFQY4MFVUPC5SC6CWTFWFFJ2KSJ4MQNSQLM3TWRFWQOZO262L4LLYTJTYU2OQCP3YVY",
            "1874314451179009240012HOIXHJOIKFNDLHO4YONQTC4UMRKUWIEHUHJR3GUFPONOFUGMUGVMICJZEFOC2JRL2TVVC4PUYZHF6WPIQEF67ZQ6WL3BSMYND4HWLBCWIEDR55AP6SDBJMYCCJJVALOA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "348.00",
        "FARegId": "FA-000000055307470",
        "F2RegId": "FB-000007570766786",
        "AlcCode": "0300006342850000001",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЧЕСТНАЯ\\"",
        "ShortName": null,
        "marks": [
            "187431544100150924001T62DHUIZ2MCPBHHOL3X7X6WWJQTJFGM4UU2LHPYMEEP33WP7QV5PGUEKCJ5YLXT5GWGSBWKV7PKGFGRMNSTQ4LTZQNO427SOI7QIB2CYDA5J65Z47SUJOVCKXG4B7S5NI",
            "187431544100210924001WKA4U5XCW2DZ5ZBVIOWNANUL5Y5DS7KRYUHOIGTIK3TM3KAOCIEYXGQD5E5JLWNXHXJWETO5KV5USZRHO66YMEQ4CII3LFYNXLISLD5LGMVO6CYNFZNTNM7VQFBCVX56Y",
            "187431544100230924001V4PIZV5NFOKBY2BWAU7CKI2PB4K53KHZL6RBZUFEVUA22KY4OIDTFYSXQEFWXP67UTRZDFZR2NSYD5PYUGYEKARWYZYR6RSDD2WB7EWJ6BEQ3T753EZM7PHSI753YFUAI"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "383.00",
        "FARegId": "FA-000000054913540",
        "F2RegId": "FB-000007570766787",
        "AlcCode": "0300006342850000013",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ДИКИЙ МЁД. КЛАССИКА\\"",
        "ShortName": null,
        "marks": [
            "1874292549535907240014XB63VNMY3FLH5T5AUUGAZ766QWBYT2R5IHWXIA2ZBLUOP3RFEBDTBZXBECUWRVB575TZUG56UFXONDQIRVBLBZHOGQHHJ2UBNNILVWVQ5RRLMNYBRJ4R26PULOSVPLYI",
            "18742925495360072400137LXBHKVIW6X2SK4WMGMAEYKIYRGBJOP64CV37UCQJ7XUGEIL2XGQFZEIHHL2STPZPCXJOORKC44YHLXXQ7E2XLU4XQSULG4CHEFECIEZXBJUDFX7UYQ4XZ44KRAVYDZI"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "383.00",
        "FARegId": "FA-000000055033765",
        "F2RegId": "FB-000007570766789",
        "AlcCode": "0300006342850000012",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ДИКИЙ МЁД. НА ЛИПОВОМ МЁДЕ\\"",
        "ShortName": null,
        "marks": [
            "1874308571195708240015PMFEG2KQ5TJSBJ4LH3ASI2VSEWGW6TFJRMDK6RNF6NFEZ6SXJQUOLKH6LPY3NFZSEZH2F2MHCQBQVMPJ6VM4L4A4NB2RCSNVCXBTW5TMYNVXZMPTJL5YJAGUGEMW4XDY"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "383.00",
        "FARegId": "FA-000000055020651",
        "F2RegId": "FB-000007570766791",
        "AlcCode": "0300006342850000011",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ДИКИЙ МЁД. НА ПРОПОЛИСЕ\\"",
        "ShortName": null,
        "marks": [
            "187430120218230724001SOU43F2N7XTLA37THDOU2AZWLERXGWNMN3SENZJFVWATV453OWNPPURIJSU4OTBZBD2V4HM34S6NIMYVX4QA64MRPAU5CPEFH526G3YHWZWLADBQNEVF3UBPW44VSVSKY",
            "187430120219290724001HIOMKPKRAVAMVBPCES4VKTYQ7YUHURFAEIL24YYUSGMMURPM2G6OIW2XZMSG2GD2E5CCOK25OYZKDVG7V5RODMB4OH3OPNCDM247NKBNJMNLGG3X7R65ZU4PB4IVAWLMQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "348.00",
        "FARegId": "FA-000000054787685",
        "F2RegId": "FB-000007570766793",
        "AlcCode": "0300006342850000034",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЗОЛОТО БАШКИРИИ КЛАССИЧЕСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187429709278040724001BNL3VEYW4SKQQ4PAEAEZOT4TDMIPZYF7AOGWNJRESVNFL7LTEIZSF6C32CNUZ7PI6UOZOAQR5Z6NPEZ2QKPVKSQZSNRBEKV3DDY4MUL3BDAUPF5T6PIPG35HIEZAQVKGI",
            "187429709278220724001B5AXC4CY4OS677F4NTLXYV74JEHUNFB6UPFFGQ6RM3F76XQMZMGKQQLK5PZFWBWVDLVZLBOEC52FVKILJW2OY67JSYCRPN2KBJ7UVMMMZMUFKND7UVUSFNQNBU62CKAOQ",
            "187429709278230724001OEXTYYT6F6C3OF7BZVIZ2NOA3M2I6VEQVBY5O43G4K76GJTTVBUPFAIU3RA67LHTDO63Q32FZLQN6VVM53BCYDESGVFW5QYF4PSWIJ7UUSKAOIM5HHROJU6S36MYZ7HQA",
            "187429709280230724001GHMIEONEEHNFYHHIXUXV7L2SEQTY3AGLT3JGJSKCEN4D7K4FSNAUPZTGHZA3O3NKB5TKAXP4QU6FELBHQZDGVXNGJMSUDS3MFHSWEMUHIB26XQORGKWSETDVERDKGRQBA",
            "187429709280260724001RAIWOZJDRVXHTIKXSR7RHJZK54WOYWWU4ETAJKTEO2PUEPQD2GS6MRIFHFNWMYKTCSSUPSTSO77QRHLXDPLHGFLIT272A53ZXEN7B63NPELBYPIGQIGWQG3WLOFFFSPQQ",
            "187429709280270724001CYT3TSQ6GRD6LCMOGOGWU7VGC4KJMB6JHUSU2WFYURNRTNF3L3JAE5SH2FW4NVDQHM62HEXLGYIU5S2WEF5R3RGAAC7HQVB7MPCULAIN4N5OFOT6DMH4CPPPVWK35G37Y",
            "187429709280470724001VCVFETEC3DYK4RFXWZQKUCL23A5T6T3LBROFEVFOMN5GM56UPPYGTGQUGVCXD2KKIV4GX4ZGLHUMFHZWJD6PGQOOH3MWDQ2R6WLYZ7HB52GQ56JEU4GOKM2LCICI5CUOI",
            "187429709280480724001RC25VEJWSHILYDXQEIZCVO6VQ4E7XZKKEUAFGWLB6NIR7FZIC6DRQDMLT7U4IATFG3P6XFXYYJ6O5REWNOJW2Y7DZWT2447AHG7H4WXD6M7VOX4TW2O6RTK3HPYS6DQ4I",
            "187429709280570724001AU4W4WYDS7RN6GTHKWL56MVDSAG26LT2NDTMH3I2IP5W6QLODLT4UQ2EYVRWVZ6QH3UAXMUHCGEJWLKR5N7IMWNO44HBG276TPL2FWHOMFCIXHEQIVWBBAHGGH6NMRV2Q"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "375.00",
        "FARegId": "FA-000000055329710",
        "F2RegId": "FB-000007570766796",
        "AlcCode": "0300006342850000056",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\"",
        "ShortName": null,
        "marks": [
            "187430320632610824001YV7IQNOQE5QBTQHDHFRIDBVXGI7HIO2CCP5MGRCVSZPMGG3RQSESJ4XRBW3VPVSGYTKRXNA5GT6KZ4J6TYKQJ6IE5VGO72752F5H246WMJEWEAYCSN5ISWQBR3QFQSYKQ",
            "187430320632680824001HXSI6AWBGR4GLC3BZRYLUBUOFIS7OGXGXJOZAQJJJLRGEXNS5H5QPJQKSHSOTBZKMH3XGOUI26C55RK2SCXP3BJM63D7DH6ZOHBZPVAJ56K4UOX3XYWKPVGL5V5EZ325I",
            "1874303206326908240013RJAA34EUQATYMDOA57A4MJPQASF73TIGUOWQC3XLVDVSXEMO3RFSGGGZ6GEQVAX2VTO6TWB6Y7G4S2DFBLXKH7TYH4CQ7N3J7ZTH4HBAGCVBJK5OUZPALMJEJJNRVT3Q",
            "187430320632710824001NHHPJMLE2EHHG7W45HQREYIYWAG53KU5ZG4NTXXVH4NEB7AHF3KFRN5XPHUHF5POYWZ3DNRVFCNZ4X7SQKLLLGXP36DCVTVLSMZGHIUBLAOSC3G3BRH6ZOUSC2SOXEDDY",
            "187430320632720824001YKTUTKJUK5H6OLZLKYPWQA55FQKRJO4PDABX2ZBUBREIWIZIZG2BF6ICMKYHJJRY64E74ONNRW5VK2AYWXLOPKDVN7RQ5FQZXHCTZEXLXLXX474Z2JV6OU76TVUTAHSHY",
            "187430320632750824001TS76CTWKTWZ4W557L62VPEBUXAJYIGRGBPGL3EOE6VJLAU27H5EMWETRCZWGNK33X263KFN3SSOSPM2WOARJWR5CT3NMVP72JYGICQFNRCDNHLLMNJLJY2FYQ3MX4ADGA",
            "1874303206327708240015H5BTJIHNT4MMFQPNP6K27GSW4BYK3I2YONWGKB42YKQQI3JJORQAVSW3MJSGMF3GWJCILRMIQFXS3A5AUVMLQB24BKVPHRNAXIC3SWJNISQU3NBD6UIRRA4HDFX3LOEQ",
            "187430320632780824001WDFJYR347TDFN3MJSBC7OXQ4CMJI6PJPWBWHNV2VZ6YHUWXUCPKEPFAKESNU4Z5AUKCMLGSYFBJQOX5IIOBTAXNOZDIQI4QPX3RLZCHAOBIHBUS6MGUTG27W76BJGIEIY",
            "187430320632790824001FHWFKZVSCREPDOUZI3QQGLZFGI2C26VKMHDMVYHUUEN73MGHKRRZTZZVS6HU2XLM6AUTSGE6QVBT2IXNATAJDMZX46QPMFBIUICZSOVPI5E3GOPC4UNMXT2VCBTYORG3Q",
            "1874303206328008240013IYR2LQCTHLIW2NDNLWDIUYUV423MSBCCHLKBDTB3ER2I7X2KIGCY2N7YAABW66DPKQPTDAVT4UF7IXW42QUW2CR3WXD4OWD7IQ6NW7HP2AL76YRHERIQNTX6M24HOK3Y",
            "187430320632870824001MDWLKMGBV7VXT4HW7OBMIRAQPA5SGOOB5RXSAQBTBKK2GDAGXHEOL4YU2SBZUPRENHKVBRLPYIUBZKMN74UGJRE5JU2TRUZ7AGTGXY3G5IF2LT3P4TE4W4F27AKTOYXZY",
            "187430320632930824001DSX4XH6WZCGKG2Y6D2IYLHPV544LM4VGRUFUSFGWYMEN6COXGJABV26SKYWJL3JX3BEGSYJMWB2MIZF5GDZ52ARSQKRMMO6TJECCRW3MAJ4CQDA3CHGOX4TSNCDZWQLVA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 12
    },
    {
        "price": "383.00",
        "FARegId": "FA-000000055228441",
        "F2RegId": "FB-000007570766798",
        "AlcCode": "0100000042540000013",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ДИКИЙ МЁД. НА ЦВЕТОЧНОМ МЁДЕ\\"",
        "ShortName": null,
        "marks": [
            "187431197107900824001WGYGVPLUJ2EVNBBZAFOBBORE3UXQVBQ3DGRU36WSHANKCBYOIXPQKKBECVRTGWZ35HS5IZWCHWMGYBY3U3CLRWPA52HREL3V7SZC5PVTXRELNQWY6BJQNS3G5DPWVRZ5A",
            "187431197107980824001OYZDV35EHDDS35QOI4RPH73SNUIM75V2JO4NFUQDAVYKWVL7GIVPQXVPOUIUUBWDQTRUDSBXDHWQ5NZ62VRK2P66NHFE5BOXFZ7FFDUAMVMKA3Z7W3OGVKOLG6VSLTGVQ",
            "187431197107990824001RS2EUTNIIJAX4RFNP36K2BW3345AEVBKN5W7WWW7HRV4RWG4DAG4HTJG2OBY473JSA4OHQYZQXR3ZIPUFA4LIBJZKMOBYMZ2Q5K77SNAF5IQDMJQMTZAB5ZURBD67W6LY",
            "187431197108020824001QZKXOECNGGNCMYMKFUOCU6JQ6EJ355R3GZNQCH5WFYVJG3NFS4ZXXLTXVMC3TMOSUGS7OGTWVK2GQGQROZRJCEAYTCXXGMDCPF3COJCL5THNFUQFUT5ZYRAATFBFFXFRQ"
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
                "FullName": "Стерлитамакский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "361.00",
        "FARegId": "FA-000000054719180",
        "F2RegId": "FB-000007570766800",
        "AlcCode": "0300006342850000006",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТАЛКОВСКАЯ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "187428910412720524001DDNFIGPTSLZYPJ2ICKORSWQHNYUDFXTO3IRGYL2S7QS4UVTORGH77BYKHWKJTGTLEFRILKE7UGE73HGZIRLFPB27QUVB4ET66W4RR3MMPU5Q5EYDLJYGNVS6RTUH7J4FQ",
            "187428910412730524001ZYMWWPS4TMTTP72KQ7CVKCOMEMOA32KIEO2ZGBQTI2ZXZX2Z3SKZ2YDOXOBCRLPKNQGQHA2CZJEH2PGAGORJZWKPVINKTMRXED27AEMF2BXFWJX4C7SJOWZPMY2X5CJYQ",
            "187428910413210524001NITZ6D2JWP55TWYNB343Z7YPMM575PYFPURA76WXL6VY2LTCBQBJ23CCHALVWCBYKXHI3IEBRJEMXJR7P5MR76NUSBGMJZARI7CI34YXAMQU5EGW4SIHSY7KVFRE2IAQQ",
            "1874289104132705240015CYWCVHUJBNOJUANOR7F26GT3UENRXFRHX4IWUGN4DXGBCBSBSOJLBM4DDIE3KEM3JMKNIS3I5LS2VEVB3EJ2RIX6KCFYFGM2PXLRP7S43VGEOBO2NJ5F24M6FCYGH2VY",
            "187428910413470524001XOQMFCUGQQGT5MIXKOKDRZ4TBU5BSLEBJOHHP5CGRNQO4R6WRCS6UQY6DDLMGBY4YTIFNXARIGZAISUYUOVT5QRJRIHFUSG4MTCODUYOIAUPOWUVYBP7UAR4EUNKNDVJQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "526.00",
        "FARegId": "FA-000000055164344",
        "F2RegId": "FB-000007570766802",
        "AlcCode": "0100000005410000105",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"НЕКТАР КОЛОСКА НА МОЛОКЕ\\"",
        "ShortName": null,
        "marks": [
            "1884065090619104240013GYRL2XRTD5I6CQAWU4ZP4SLCELJYNLBCNPPKVA5QDWTQC72DTAA62RRCKCLQWNWM2MJSR6DUWU7HKJFTEK54NLIIO2TPZDLBM5AKK7MCQG23RXFWVMENIIF3EVRJFEKA",
            "188406509062070424001X3XI7ZZOKU5QC2JDP53M7HTXX4COF2DRPCPLFTPTJJ4OYH5BIBIEBYUJV3BHRJJKJ7FC6JZW35UXH5KU6KWL44GL2UFPMNZZW7QIUFW7YMQ4IWSR7SIPULDAIJ5WWS75A",
            "188406509062370424001LP7V5Q7L5UGOBUON4MFJ3GF4ME6CJNJXHB6YR7WG2AARPYNWOUG36QEEEWJOF23QO3MHFQPENAYEVKXZWWTLNKHE6I3NAF252EGC6BXQJQFVS7DTUF27EH3S7CK2IRYFQ"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "531.50",
        "FARegId": "FA-000000055148635",
        "F2RegId": "FB-000007570766804",
        "AlcCode": "0300006342850000008",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТАЛКОВСКАЯ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "188406511076510424001BXCCXMA4KPVMUXHVNG6FQS7YL42JDBK2NLG67PVZ2Z6WGYMN44Z3YEOMQVCDG74WMIWOI2VJHQ2BR66YQOHJNZHCZH6SI5MPFPZXHDDBJKTY5AMDLAEHVZJYEAFENSMFQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "68.00",
        "FARegId": "FA-000000055062711",
        "F2RegId": "FB-000007570766805",
        "AlcCode": "0100000010250000073",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «РОДНАЯ ДУБРАВА»",
        "ShortName": null,
        "marks": [
            "1974073596271301240017GGHRM7LHINX4POR6UZFH2S42Q34GHHD2LT42ANQOTQ2D7RYF5DGEHAC5VGDTQLNH7UQCF2ZZTL75FBCRMK5VZKDZB7NPCBNCGP3UDXJ6R377EB46Z4V4YAJL3ETTWEAI",
            "197407359627140124001U63BTMHGKV4JZJIMAQX767GR3QGPHJSJGEIDME7EOVJ6K5N26ZFBZVBA67JMTFMRSAMCQLLBJ3T3HBRSCJZDWOZDNZ7CHCOIWZL75RO6JMJUZCKK5VSDUEVOQ7F4HN33A",
            "197407359629660124001BHVL47N6ZDSEAK4SFIUMYGXQLIPQRGIOT6MDKOQK2UNQGUNFPA5O6VVQMZGIIZJRK23IL4B5FZDJFDZQONXEE7FOPBXP63XNLIOJGZKN7UHQYL7BSL3QPDVNWOOEQJQVY"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "165.00",
        "FARegId": "FA-000000055134171",
        "F2RegId": "FB-000007570766807",
        "AlcCode": "0100000010250000055",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «РОДНАЯ ДУБРАВА»",
        "ShortName": null,
        "marks": [
            "1984174180303409240014G75BTSYDLJKDI5IIS4YUZWGY47CF36RXXSFXCB7GIZCBVAVUDW6RTUOZGGCQY2ZUWKOU6XHPI5IEE6BAOODDUG6TRUSA3RVM3NJTBWGYVM6CZ7XHIJE4GBHM675THNNA"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "165.00",
        "FARegId": "FA-000000055100228",
        "F2RegId": "FB-000007570766809",
        "AlcCode": "0100000010250000032",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ХЛЕБНЫЙ КОЛОС»",
        "ShortName": null,
        "marks": [
            "198417062030180724001T6Q5RHDLMBSXIFMRK4C4AJU7E4Y2PX6DSHO4NDAZHB4VDG4D6AI6QUNUIBS37VHQDIL5APINURRKVMY7VXWOE3MLHJX6ORE4RQLH6E7LVTC53YROW6NCIOJQKWCPKEBQI",
            "198417062030230724001CC2R26CPUCC3XS3UBECCNS2ODQVMWJL5GS5HILW6UNREJSOVR37QYTDZBIXAZTHWVE7YNG4RURNB457PBVI74GEJT6GFNQFRY3OFN3SY7W73MV7P7WDROVZ4LONVYMNSI",
            "198417062030270724001W62FY2S6JKQWMSW3WMPIKAXVNYZ6EZG5YA56BFXPZ5VXHL6NFVCBE6H6VDV44A5AKIF74JVDHUSKWIMWEYMZUAGVTRREQQRXZONZH2IO7H3ELCGSUKZ6LB4LH5T47WBVI",
            "1984170620302807240013XJMPRLVEAZVJB4ZNTCE6Q45WEFAB3V43FNGYUVL7SRFF5WQTAUBJBZNW7GMVEW5UT4VVLL77SLGVSFJJXOXZBUAEZDQCZM3H77QLF7LLGHASMHKOP4YOKL4ZMNM3C3EI",
            "198417062030750724001VLPNPCKW5CO6VZX2Q2RJEGTVFE4D5Y2MV3KIZMXADOYUKMYUARCEWLOIM7T3Q6DVK6OUJKW4MSZWGOTX772RXXK4QQTWNAUQCZVG7XFEIMYGVELNTEWCTKLC3V4C2IAII",
            "198417062030790724001R4S7IZYJKHDY7AGDFWZOTQJ3WUVEIU74TCCPSOXAFJQMF4MA4BX3A53YYCT6HUUDW6WXHSPV7B4ZYOL2BYEONCT4XS6PJIC5IE7P3LP7VRIPHIZE6OHZEJNKUNDREQJ7A",
            "198417062030910724001CBMZ5U5D556JIZJ6IIMMJIF5P4HHAUN67TWSET5OBULSMSAC3A37TKTJZFBNU2RCPNGR7XFUDLMFULFIZ4IAXPGH3MLIYPBJR7JHGCQMHC7NTSJQTNR3EAMLA4XXVPDQY"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "230.00",
        "FARegId": "FA-000000053542809",
        "F2RegId": "FB-000007570766813",
        "AlcCode": "0100000010250000010",
        "Capacity": "0.375",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\"ПЕРЦОВАЯ С МЕДОМ\\"",
        "ShortName": null,
        "marks": [
            "1874256666884012230016Y2TK34HRK4X4G74HSMR5BZPLI2T2QVYEQ7QY44MFLITC7HOWJ72G6INRVUN3LUPVQSPJ46WVOXUIDQIJRIC2ELMEGEJYS2T7UPH2W7PF2NIPIZJMGE2Y2ACYOK2O5HVQ",
            "187425666688411223001S3LVCVI4LGSCOK6DMWGBEVBM6M3T6TYUO6F7DQXJMHKFUHXRZ7YTJJNSCTHVIGMDJBVBK6AKZZIO3SXKRMPAVA4PUT6E4RHGHMSWVIVINTEGNIQFU6LD4UWZGAPKUXVFI"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "99.18",
        "FARegId": "FA-000000055123872",
        "F2RegId": "FB-000007570766815",
        "AlcCode": "0100000002700000047",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Архангельская Северная выдержка\\"",
        "ShortName": null,
        "marks": [
            "197305320580250124001QLPJMT7ZKKRY2LN3G4UVZBVV4YM6X6XCCADS6T5QWJ2QFGBGJAM7L7A2INSIAZY3LZ7IQR23TZ65SSMIFSP6K2EUWJDP6P4EKQSRVPUXIJZCKM3ENLTCPHMJN3BJP4MIQ",
            "197305320580270124001KUWOTUXEW5RZHIKGVS4OKMG4GIQ4LJW2YNGZCYMIGMA4JXHBOYGDKKBIFB242W4ULYNGAEHZAC6FMDMJETPG5F7KG5HIXLQUI42IMYIWQYI4LWVRKF7QZ5SGOBIZPHO3A",
            "197305320580320124001HATMMOZTZS6C6PCREPO2SXFUHUK6VK7YEXFUEBHS7SCHZSMKMUQRULBR3CVQ3IBYCPFEUVXKNGA7RVAR3WBEJGUCDT4LJZB4NFIQD2RQ5UCGDDJXVXNOIDQT3RHEAVCBI",
            "1973053205803501240014BX7WV4NR2GGD4TBH7TUJ2XIUAP32WGB46JQYS5W7PUEWCANUCCE3OWNYGTNGG5HT6AYO7POFPOIP4SH6ZHOXNUYDCSOBPXIZQGA46OXQHNT6P7WECUPQGXHGARNU6INY",
            "197305320580480124001OD7AY7B2TKHD7LEGDSPC6C4KHAICZUFA7S4DC55UABTYB7I4FFRIOW5BCZDENQK5SMFWTCET2OD522M235QWQYGDYTWE2JCWN4R4YJGJEXC6EGLGISIZFAL3PX5KGBGEI"
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
                "FullName": "Акционерное общество \\"Архангельский ликеро-водочный завод\\"",
                "ShortName": "АО \\"АЛВИЗ\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "170.00",
        "FARegId": "FA-000000055332936",
        "F2RegId": "FB-000007570766817",
        "AlcCode": "0100000004970000167",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Царь»",
        "ShortName": null,
        "marks": [
            "198417799036350924001V5H3SWZ2XDTX2MKZIOILUQLSPILYVR4VYYFC7JRLI7SBZBXTKNCUBU5UWVAK2BMJLZQDJRBTVC5E4IMZHWNSJIAX3UCQH52G7LIIBWQQC4FSL7DMWJE4RLETTTUIAYF4Y",
            "1984177990286009240012EMFZ22ESDMOCO5YVA5WMEEXGMGAS3TAEY6A5BDAXWRJXKQQRXWQWXCD3UZB64XOSSLD47IR62RZQGOJ3KFW42PZPAA6SEFHNQAXEAZMLIC5HOWC3YQPHCHBUNXHBSGFI",
            "198417799028910924001BSMABHQUHKHQPDGH5BIH2K4LRIWBLS4UHFCR5MENRZIGDERBVOHOLTV65LJCZ3GFXDVT7A46MZI5YH2VI5IQG3HZT3GWUDIRK36KIGAZUWDOPRKLOW2EU2KOJRJXJAVOI",
            "198417799029100924001LKKWWKGPDKSAKSZS45ZBA55O5UGUTQPIPM6PI2FT2DZ2XEBH5WVKO5FXK2BBFTA5OVP3LUIT6J5FCHKRB6ZE4CDHXI4VRMRGRWYM7HVJKT632U7UCXWP5DIGOIA7N2VQA",
            "198417799029200924001YUQBUTDKTIVLFBRZOZI4RBH2OIACCGVTALSDUNRNMFFLBF64Z6BAMMCJ7KWW6YJDFWULFEABM2R3URJKSI72Z7WAMUQLD7DBZCS3SJFHQPL3SK2R3GJIS76TD3VRE5C2Y",
            "1984177990294609240014UQZKG4YZA5AYZDJFDQCGS5C4MHQEVAORSJPGRQOZWYZFCEZU334WN75S2C73AOCPNW7IFQZ4UBECCFCSZ2DATHV5RWMNKQIZOHOXHKYT5YABGAF7ITAEY2BEBH4AVISQ",
            "198417799029470924001UM5SKFFPINJIXO7D3HFHFIZSGI2LXFXSBKRU4HFX2YVAIMBJO7I7CZ3GQXMRKOCQYKN4DURVKFE66FYECJQWCVHGZLCKTSGIO7STR7QSYEQMYWLBHUODYSDYFUR3I6GFA",
            "198417799029510924001T5IIGNHDBM3XL4NV2O5YAJPMRAFJBUJR4F6L25AM6A6AXAYKXTJCUKDT7LVT3QX3E5ZRFTOCKR6FNIK7J57UGZEKCIQOWTP4LHENMODHGNO24MBDLN2MV6XGZRCXFJQCY",
            "198417799035150924001J3RNQIVBIRG3OGEPLTEQO4KMRQBX4PC7A4UGMEHCPRBGYEGX65AW6HQX2JTTVOIANBCRW7DSYQIYZAYL5Q2WWKIMX5JJ47AVBLUJB6V36GKBJZZSTQ64VZ7NBU4IXMWZA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "199.52",
        "FARegId": "FA-000000055400664",
        "F2RegId": "FB-000007570766819",
        "AlcCode": "0100000002700000030",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Архангельская Северная выдержка\\"",
        "ShortName": null,
        "marks": [
            "198314229096270324001IMWSTHXTWGBU4TOJZXQO2AROUA4A3ZKTEZL3ANDWNMB4V5ZMOFAUMNX2GL6UTTBWOX5E4ON3ZYLSPOSNEUUPKULHM7HZJKJK3WZP4AIEDOIRKGQXYKZDPHVP5Z73RNPJY"
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
                "FullName": "Акционерное общество \\"Архангельский ликеро-водочный завод\\"",
                "ShortName": "АО \\"АЛВИЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "178.00",
        "FARegId": "FA-000000054857638",
        "F2RegId": "FB-000007570766821",
        "AlcCode": "0100000004970000154",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Беленькая Золотая на спирте «Альфа»",
        "ShortName": null,
        "marks": [
            "198313956376210324001H3PZNQ6UWAP2YTBFAFFUMCHVVQZUTH2G772Q2NVCCGIGBQWND7LZAB4DFPORNUZXHJPRY6CXLHXKOZ4OOHHMSATVOATO3WFZNNWESOKVHOETGCESSHHGTFIJOCNAQKWWY",
            "1983139563762903240016ZML4FT7BLDANLW4FFZZWC3H6MLA3B5K5JHCFXEGIOUONCBVFP5YS7EOA5C775AMKYIEC3TBKHRWBZLTUGIIUM2DNR7O3HWTQGXGJIFTBPZBDHQRVK3ED4D3FJBI6MGBY",
            "198313956376370324001HR2IFAPAYGGCP6OE6FIYNZCIO4MUWHWBFWQUA4FHKCTPFL2B7WJQ2SRRMK4D64SP3SZUJ5P2BLAZ5OFN3GS3ZA52GXSA6U65IQM6FJMGBWB4LYWXAVFAR6PAOWOUPW4BY",
            "198313956376730324001YZGJUY2LANJFDKXCBAECRTWSDMS5NMZZEP73QFC4BO3R7ZD36KSRSR65YKRCSJTAXXSKNZHKW4Y5XBDAMYN2HWSWCOPUNFHFVU5G6BIZCW2BW4KWBS5XC7VVSF3L7QAFY",
            "1983139563768103240016PV5YTMMNW7NKIDMNQ6LIWNZIYGXYD2KEGOY2OJNAZQGNIOG35UJSR522ITPW37RR54ALKFXFFICTLYXFKRT77UUX2DQT3KGQZIDLUHLA3BPNZKRAMJHSOZE5D4RZVDPQ",
            "198313956376860324001BFZ56TOBADUHJMPFMMBXYWPHOIH4LE2QUICAUHZA3T2M366473FXG2GR6COPTBUUQSFI5G32KLLXJQUNE5MAGRJ2AXAHMN7LYES35DNBT5ZA75E6SEOYWAXN7YU7D6OLA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "355.54",
        "FARegId": "FA-000000055361455",
        "F2RegId": "FB-000007570766823",
        "AlcCode": "0100000002700000031",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Архангельская Северная выдержка\\"",
        "ShortName": null,
        "marks": [
            "187326251342220724001YRTCJUPZJSVKWCU4T34L2V5L2UCYKTC2CUJCGOQJVJNLIDJRRGOAT7VR2NVPK2ROF6AY6VST4DRWZOGSFSWKIRIH3ZIFBGOABO4VIRCAQPSGASQXOQIWCL7NNOB53MDIY"
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
                "FullName": "Акционерное общество \\"Архангельский ликеро-водочный завод\\"",
                "ShortName": "АО \\"АЛВИЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "460.50",
        "FARegId": "FA-000000054876461",
        "F2RegId": "FB-000007570766828",
        "AlcCode": "0100000004970000161",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «Беленькая Люкс»",
        "ShortName": null,
        "marks": [
            "188406264545680124001RDGVZEPFQE7ENYNCY3CSCCQPRAHKOCFCB7AAGK33S7GHG6FDGJYX2GLISQBBTYYH44LL3QUAFZ4ZYEW4EAHL3GG24AL4GFST7ZCO5NPJ25OEGQ3ZAHNS6F4PDDV3XNUEQ",
            "188406264545720124001GT7K2LMN5MWBBFFEYIVLTCDK5ECDK22PFRRQ5LEOKKBL4YFF3USO5XUMWZ3LRLAT6IM25YGAUKECGC2U3JMDOWEDWNKVTE77R47KCNQFEVET7E3J3IC5RCJQ6MQL7IHHI",
            "1884062645457701240014BUQF4PAXUCJB5RYYVSJZS43ZMZEEYW6APEGBP6OZKGXLKM5R7LDPFDEO36NHIX34CKAX2KPAGZ25K3PGCAJUR5YLNCUPYWOPCLQYOYTTE22BJDIIWASA2O6DCVJF5UHA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "419.00",
        "FARegId": "FA-000000055425543",
        "F2RegId": "FB-000007570766830",
        "AlcCode": "0100489413240000078",
        "Capacity": "0.700",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"РУССКАЯ ВАЛЮТА\\"",
        "ShortName": null,
        "marks": [
            "188406641335380424001ATA44MBI34IGT3WNTRB4CPE4E4S7SCSY2DVT7W6LAIT6QD7DANSXL7I6JCI335BFJTXGAPAWCIOZ3HDBYXBT2K6FTRQOWEOPXPNJDLOQVTERLQDTELOLEY6LTYU4MQ3QQ",
            "188406641335490424001W5OOEE35BFB5P3CD3C4LN4GWWMEQNWLDJZOBV4GA3IELBI23BKJM7TCFNIK27UOVG73GSJTTRYRBHG6NLCPGTPEVXNYVLHFFYJOAZHXJW6NJRR3KS73BVIRZQU2D2X32I"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Татарстан Республика,,,,,,,Высокогорский муниципальный район, Усадское сельское поселение, д. Тимофеевка, ул. Профсоюзная, зд. 4 | корпусы 1, 2, 3 (за исключением помещений №№ 12, 13, 15, 15а, 16 (общая площадь 59,3 кв.м) в лит. Ж, этаж 1), 4, 5",
                    "RegionCode": "16"
                },
                "INN": "1681000049",
                "KPP": "161643003",
                "ClientRegId": "010048941324",
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО \\"Татспиртпром\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "598.00",
        "FARegId": "FA-000000055154870",
        "F2RegId": "FB-000007570766832",
        "AlcCode": "0100606942420000152",
        "Capacity": "1.000",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПУЗЫРЁК»",
        "ShortName": null,
        "marks": [
            "189401593222670622001WXTAVP7V2XMVKIVN2UZIMZ2HJY2PZGMXXPVBRCYTOHTBCHAZSBTZTKRKQLCFAKOMZIDV5NZBGA5QFNC6DIO3XNHAA4QDWA7WBUXCDUIUTFWTTWIGSVMB5TZ6GBXYXJZJA",
            "189401593222720622001H7IZOFFJRSX6XDHM2DNFTCXJHE46SPDAA6ECT5XAX4W7BP6EIW63JNP4TWWHIGACCMGVZHFDVBENO3XSV4O4BBFXUVPYUGNIFKPLJXRHHG6RBXKG2WJ6UDLLUXURCQTVA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "598.00",
        "FARegId": "FA-000000054871530",
        "F2RegId": "FB-000007570766833",
        "AlcCode": "0100606942420000118",
        "Capacity": "1.000",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "189401568711300322001OZDS2EZDX7PFUMFIR3DKZXYFGAWHTBWWLGQW26ACPVZUPIHXYGLYXY47JA6F6KYFIM563JYV6QNOKPJ3766FSTPSS4PEVGAV6WXZVRUBZLEROQ3OANZDLVIK4HC7PDHIA",
            "189401568711310322001DKDBKOMFNV5N6RSFRV3IA5QSPMC6G4Y47FBDPVUWKBWX3CCQYF5A7OJ6SJHANU26H25WENKMX65JEIOTDRKXARICTLY57CU3Q32KO33CMQPJMPKZKP7SXEMOPM3QIBJBI",
            "189401568711320322001KRE46LUMF3JXZ7ELKOIELNKXP46EM2GJHWOT3GBKMLTF7ZHOS22T2SJEOZXYXR6XTHIMIIAB3BMF52YEZ7E77UHLAKIWIIJYGBCQMIZJUDWIU6UZUGIC3PDAF6KPFZAKY"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "225.00",
        "FARegId": "FA-000000055308086",
        "F2RegId": "FB-000007604782365",
        "AlcCode": "0100000001740001189",
        "Capacity": "0.700",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\"Татьянин день\\"",
        "ShortName": null,
        "marks": [
            "192315456661711223001KOIL4KSZYXHMKRMGBVTSGNH5YYKA5A2LOLG5DYC6QWPSUCIILWRPY6652XVV5BEPJ6JGJSPTI34UDLZZVTA3MZ4FZAPPQ5GINDZ2VUBXPYMHBLROAUM6RO373D7Y2VDEI"
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
                "FullName": "Общество с ограниченной ответственность \\"Долина\\"",
                "ShortName": "ООО \\"Долина\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "154.48",
        "FARegId": "FA-000000055405008",
        "F2RegId": "FB-000007604782367",
        "AlcCode": "0100000054580000090",
        "Capacity": "0.250",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"КЕДРОВИЦА КЕДРОВАЯ МЯГКАЯ\\"",
        "ShortName": null,
        "marks": [
            "1983144997608603240012RTO64VXSQ7KKSA5V6CBKZRX7UCBVABS7DV3FC5WCL4EBCODCFD633MGCYPNPWSJRFOIPSGGTVRNPBC3E25PXB3VAPJ4FIHXONIJDUAAGTS6KUZNG2FJZ5K6BJR2R4SGQ"
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
                "FullName": "Общество с ограниченной ответственностью \\"Омсквинпром\\"",
                "ShortName": "ООО \\"Омсквинпром\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "165.00",
        "FARegId": "FA-000000055374459",
        "F2RegId": "FB-000007604782368",
        "AlcCode": "0300003247940000055",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Берёзовый рай\\"",
        "ShortName": null,
        "marks": [
            "198314547624520324001OYZIAZD7AGISUXX6E3DKDIXL44B44VLKBYDRKWPDUD2B555ZVWUY3XOA3JL5JE7HAYZKBTQGO5R4PMTX2G7NULNPCF3HDKWFYMTWTKHKZCX3YKQLHI7Q2IYX3I5XFZ4UY",
            "198314547624530324001ICQ43VPUVOPSG2NCW6LR5SJJ7IMN4CK5JABYW7A6ZUEPYTRW6YBDPTG3E5FBLMGVCQIBTCBJFNHXDSGDTINQIZ5YAMNFQDWVLPQ72LHTVDKTO272TAMSG55NAHCLYJBGY",
            "198314547624550324001W6YTD4ZZUQGGC3ROPRTWXWEO2AFXDXZ6TWP4ZIZHKEAP7VSL6R4VUGBU3DC5RIGPVROHZWKWBDSCYQWNK3CLSPINIYSCOVWRBRG7QM4FPU5QQFPLYPZPHTF4WACSW5XTA",
            "198314547624560324001K5ESM7VBDIMSPIF5HPSKJJBVHIHOHSE3NALBNSIH2MYWZUGCPJ4N6V5KPULTH6ELNIE2XBEPR72MJQTHFRZUVPMRR3FAZCVPTNFESVDCK2ULGB3MGPFMZQTJSTU6EQZDI",
            "198314547624700324001LV6QQSQ4WQQHEXR5GTOGJYSC5E6VNSPCQQXMN4QJAQRWAN2A5AVF6IQO2NIJRBYDOG5QU4NKPRQG3DDEMH6WXRLYBXP5DUBTUQJCM4DJVCOXQNERIB2XCPX5RRUMPRQQY",
            "198314547624730324001NL3R6HCR7BBZMOD3Y67NO5GEUISGIQ5THH2SZCHFG6KFQCRWG47HGWPAPNVEQOVTLVDFGYR4YNLU6YRFJBNZXZB35D7I2GVRFRSKNKVXLIKAF7PB34AG4R25AWYW4O5HQ",
            "198314547624750324001YDFGNVNTVUACCLNYR3HPBVSSTUU6EVFIBQ63HAAE2XOM7XMVAIS3WQREICFNU7MA22TSDH4JV36JWRQ5SVX4I5RPM74G6VVLUTEYEW7ZTYCJVV427GFKOPHWFAMQXUBBI",
            "198314547624770324001RN6UEDOITH24P3NF7VYVEQGOLMGL5CHB7NEJXLYVLZ3BTOKKF3KHZUGF5UYU4VVKQHIJ6GF7YY5GR7OL2MM7ZG5O6NYT6AT6KYXKPN3LWV2EWSUTPC7K3ZBS7ST2OOQ2A",
            "198314547624780324001SIFO6RIAXLG4MVDQRAUAVLRUSYKJ525V4665Z32F3BLV4725MB5PGY7QOM3VF3RJ7T7GHP2K6ATIXYLTOJQ6BYTUAXL7WX4FOSR6REQIHSXFWUXJTE2OJPKRTQTONMBSY",
            "1983145476247903240017WH6KE72DM2YNJ65OPYNLAPLHECDO7BJ3OORNTSYFABXAU7POT2QKRLT5R33XYZUGCIROXXHCSCELFUN6WRWOI6RRGT3L22BYVJ4JXGENYOJG4ZTWIM5QMGWRAUGXH5GA"
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
                "FullName": "Акционерное общество \\"Озёрский спиртоводочный завод\\"",
                "ShortName": "АО \\"ОСВЗ\\""
            }
        },
        "quantity": 10
    },
    {
        "price": "174.00",
        "FARegId": "FA-000000055398404",
        "F2RegId": "FB-000007604782369",
        "AlcCode": "0100000005410000037",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"БЕЛЕБЕЕВСКАЯ КЛАССИЧЕСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "198417716601390924001HOBTSUH7D2Z3EJRABEE54Y5QLYSV2QWTPI4QTDEH7W35U6MALN6WG4IRWDR63K2ZR4CQOTBDD5GXDWTTDVSVUSAYWO5AXYBWFFDYMTYAAOSSGUAF26O55ZUY4WGP2KKJI",
            "198417716601430924001HBX3UW4AWWNQLWEFNBZOQLAWGUCDTE7VTNGMEFRIM7ALDYHRJ63GQLCA5OGZHCQDRS3YCYZ2SGXNFWDVFXF2MAXT46ZY6TRRN6P5CYNSCR55B5XH2YWDRMBTC5DJCDKZQ",
            "198417716601440924001IWVGSLBG6ODUBOND3UPVKEAVXEZFSOAW34I7ILF4BFE6OP7YLVOFJHCU2RBPCX3H4PZVUVZANNXHRZX54S5W7AMHJL7CKCL6RYRUEIV3T5M4M3CDSZBZBVDB2ZGQ4DU7Y"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "165.00",
        "FARegId": "FA-000000055117321",
        "F2RegId": "FB-000007604782370",
        "AlcCode": "0300006342850000015",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ФИНСКИЙ ЛЕД\\"",
        "ShortName": null,
        "marks": [
            "198417312042610724001CA4DLORLUCMCYBGPYXLLT4JXVACP4IUWXIIXPSJNHDILEBKZQMPLZUDKWCFWX7UU3HI7PFR6G4NG563GCCBRVR6T2PFTQCNMUUSV5TSOCMI2YRUZTT3LPT7MNQGLLA7VI",
            "198417312046990724001XF7I4BKBJTLGIL7747T2EFBDIUAJD2HCWXFHID23AFUPA4UAH6I2MUZIMGV4BTQB42YQRJSEL5URO2UEAVUYPD6PD3KRWRLHZXZCVAXIOW4YYD3PBJVFKK4VBZKZJWJBQ",
            "1984173120470507240016DOXDWDKDGBD6GBNUSKWQ6MAWAZMXWJCC4K6JOUX3MI5Q247EUDGY4PSJD2AOVYNTBEYFBWT64NR5AUYET2DTGZ6YFKJRRTKQEDVNAZVMMQ3JULE6IP42GFUAE5CYFIYI",
            "198417312047130724001F23IYU6G3JKC46MEBDSCEBYCLIGX2JN67J7VHQYB6ARYLQ5J5OJ4LQLZ6PGYG7F3NFRVY3J3CWVLUV2RHCGJLB4AP2MP63OSSM5PO3I2KOSEWDKVYYLBSY6JADGQQMZPA",
            "198417312047140724001CVAV4XMXVQT5HJT4AB75XASRPETJV7ND4VL5EDGULS44OXSY6X4BI75SFFCGKKXXFND35SEUW7QI665RKFPBKKCLHNGEA7XSIEOJIEHXRXOH6XTGYQKHVXDYFYQHX6RRA",
            "198417312047150724001Z464EFZUTFPK7BMD2I3XJNRHIAIGNS6HK2F65BU77RSRPIDPNXA2F2KX7A3WIDRQBF46VOHSCMJP7X7IKDPSZAM63G4A6QZAKZJ2UZNJ2HXRMOA25SH5RCXBRSE2NWGEQ",
            "198417312047160724001BFQ7X5W5YZDIZ24O7ODD5RIDOIGOTGHMUBTQUGSI2Z6WDWDCJG474YPF7JEZNXCOQWZV35HABZZXZHR3ES6I6MA7NHKSS3KFPGW63EPIMB4CTEQPF2YWQHOZP5SDGPMWQ",
            "198417312047170724001BLL5QCM27FW6XC2TJZFLVWBEUY2APYZV3M74D2MGRSR2HCWPDYWUE2YGHWEP2PVCUWRVNMPV3KB26ZKKIUNISBJWNCJVABW4HLCPBEYM6V25XP25CDRWRNIKB4LNIB5KI",
            "198417312047180724001E6E5OSYACAAMRG6GYWB6AOIMDEWEIYSIZBTBMUL6UE53QYICFVRUZB2KU5BSHHOVGJMKHDKWVZ43JHC34WHGZMK53MK3ZOMDO3GKGZUK4QUX3EIHCY2TAC3OA3MVDQUYY",
            "198417312047210724001Z47XSQYAN23GXBJLJON4MBOJ3Q7VYQDH3SVNXVKFKBMJ2CHXHPFUGSNQKOGQMVZSH5M6BPWH4YGXBHZXDLXTDE6EK5M6JPBKIZTV6OGQMQ3BQGPV4VGIVM7CWAWKESNPY",
            "198417312047400724001P52XDHMOFEUG4DNMNUWHO67BFAXMXSRNDIQ674HPHOQSQWIAUFM4O4GTAWQOQ6KL4IRX6ZQCDOIORFTW7ZLRM6JCN5QWBFMIK3MZ5S44UBCE5JSEL6RRHEWUUSVIP63KY",
            "19841731204743072400174A3RP2EQYU2TV2TF4B4CEPHTAMCDTGBA5NPXXBAOGLF7UGQKABATEX6L7F7XJC2R7WJGJOI5CBIMC37N5RDHKH4VMANHRGQV3QLDFMU764RM7DYUUYQVSKTOLVYDZRVY"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 12
    },
    {
        "price": "174.00",
        "FARegId": "FA-000000054944295",
        "F2RegId": "FB-000007604782371",
        "AlcCode": "0100000005410000040",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"БЕЛЕБЕЕВСКАЯ ЛЮКС\\"",
        "ShortName": null,
        "marks": [
            "1984169076073807240014ZB2FHNVU7MDX62XNFD73DOGZUMNJ3XY7B5PTETAZBHBLEWIBFV5O7EIU3RGDFE4FPXX53YMU5HVBNZH7INLWSVH3O3SYXD44PPLBJ7TOQULWY6EZNTWRLXDPYJEXDSMQ",
            "198416907607440724001RFMXCYJEYKYZKBKZKLXILSXV3AORCGVFZWGV26SXKL2WV2JSWPVUQVGOCVNCDEPU4NX5EDMTBDAMXX6CRMXKTB7XW4CZ7DEGFC7IFJZCWTQWS6KZB2QCMAYSXNBMIOCIA",
            "198416907607460724001YH7VJJBEOVG4JQ7YTUUF2APR64MHWIGIZAPUUCEPSYOHVPZM6OCFXGA63LSFSIYD2CATBQP3YN52BLBWU5SM4JNJVD4UXCO5FUN7ZBVVCWGOW2YSXETVJHQ2IHQXT2SIY",
            "198416907607480724001SRSEAYUS6WQV4RSR3YTZLGISCU7DTMD7LTW7R3EJC2WLKXZ5OU27WQRN72YJGKVRXFSRVLBLUBSCEJ7SNVVVSJJZZIPTPSU7HFGWSRAZ4IGX5YIYE3FINPPZDYVUIF7TY"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "181.00",
        "FARegId": "FA-000000055226324",
        "F2RegId": "FB-000007604782372",
        "AlcCode": "0100000005410000017",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\"БЕЛЕБЕЕВСКАЯ ПЕРЦОВАЯ\\"",
        "ShortName": null,
        "marks": [
            "198417742347650924001G4PX7KUZHGKAGRL5LH3HFAGJ7U552EVSVNNSMWK6JTHTLCJVKDUT2YXKXAE2GECGMAE5R3YKUQP4GAUN6P6FVVTQV45PM4L5KNOOYBWLS7NU5UALJSBQX24NEU45HZOII",
            "198417742347660924001WMG5HRM5S3233TNY4FUKSTHEAU7GVXZBYV6YP2FLBPIHVLQZUSTYCKMTT7NSHHNR2FQLIPBOJJQEYHYU2DQSYQJETFUEMLBO2LI46XKII2PNKDWXKWUZR653XYEMPG4PQ",
            "198417742347670924001MRWBZ2F67VSTF4NEG5XM37G77QLCFG5PIUTLNS5XFPJCIWVN5C6VZUMCZGYR5HTDFYSRMDAWXQUDE2CSXQFJUXEFXE43XNSPCM7RRHUU53KO4BE22EUQF46QFTCSCIPOI",
            "198417742347760924001IS3JNPXRHMI6M6IF3LOBC73QQMQGNKIVUTOQJNLFB4PVQEX5PDLY34NTNTIG733TSC3L3A2HLWRU4B62MA2PZ7NIAI5GB6MZIIRFJO7XOU7OTMAQIRCT4WVNUXOFIJPLQ",
            "198417742347860924001GYLOQMKY5VDG4RFRUTWOTXYS5Q72XUAS4BY4YDKTURDGYP6O6H627BR3ULCRD3PBBTBVJQATT43XRM5PZ3WX67UYBWN6ME7IKCCB2FFLEZ2NQS27MO5DNODEYQ7DDKQQI",
            "198417742347870924001TOFUTZPOSBESBE3IM2PY4YVOMUEVEQU7FXNSJXUSHQYFAIXRBTCMOZCOQMWBFD6D5PYNRVNBO7GUNRQYUT7ALQVTXRJHJZLOA2KT6SHFOLM4S4CHZIM7LFCDQ2ZNVJSXQ",
            "198417742347910924001XX2GUEPPN2AU4BPNRDWIFRGVPULXVPXVXYYDGKEVR7KGXAY7W4UCVRHV2LZAG5HGHDMQWEFVU3PFW6RVZBP2W7W5GCQHU4MFV7HJSCEIVSHG53JDVE6DHEBK2DLZSXRPA"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "348.00",
        "FARegId": "FA-000000054834026",
        "F2RegId": "FB-000007604782373",
        "AlcCode": "0100000005410000036",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"БЕЛЕБЕЕВСКАЯ КЛАССИЧЕСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187429019503020524001I56VO2AZMA72CY4NI2GHWAY4YIMCPBGRSNWEFZ3PAIO3NOCO4QWODZXMOJY5UGCKR2MJHQWUTLWJL5QLEIO46TWOJIA3MPGUMYO6W67BXVDNVBFI2VPEFVQDSLWSKGJ5I",
            "187429019503030524001COH5SQ3XH26P4ZTO36EGMAZSUQYOKUQA3KYFU3MYBDWQPWXYOQXAXCSY4DKFIIUW3M2VAV3H4VZB2NOWT4LOKAQ5Z7B3BWTSQMFNXWGRNVFZIEXUTQTHPTCECCHNMIY7Y",
            "187429019503040524001VA6G6OWMQ6CLDCVBAPUEL5UCZQXIYNJ5DY6NORK3OSYQTOX2WUJ2ALP3LA2SCAOO4C7YOL4PCJ6P4PPXSIPJBHIOWILHKFNUD6QE5VUZQHA75K4CGXF2MZ7MCEVZIXVDQ",
            "187429019503080524001MO2DEG2SWDR6CQ6XRVFO6LBJLI4BPUOSXDWSLRWHH6RA5AYJS7WKQPTNR2KEBB7SAAVE47EUMO2D44YDJVRLB4GT7ERP53XIYZEN7XM2WLJEUV4YOUB2EUL573SSBFUII",
            "1874290195031205240016FKPAVH3MNRF2ARDLSOQD7HYL4X75UJERNXJGTFOFVGKTXCV23E62LPTE6AHA2RBDAVFZJYGABMQGVKC3AT6LBIT3W5PBFBL4MUCCZ6LSINBBOLFVR24RQX6OARTU3TZQ",
            "187429019503130524001DW4PCTUL3PACRTD7ZE55VLSISAV2YNGNBWQD56U744C7G4RCHPFCF6EDUNANTKGFU2NWYUAPESDWO2BCBYGTCNPK3UXJLHSUYF6TVG5Y6KYJJOGWJKWFEJHNII6NHRLJA",
            "187429019503180524001W6RDC7OBMV2P7Q4ZBMMQIPMS6QLMN3KW67P35E2S3MEC23JNFZ462DG2NXZ37AWZF6YV2B25RWK3X6MY6HICZRGIQMZVISSOISOFFMQ3ZGZORNYRN6L7XT2X5P3E6633Y"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "348.00",
        "FARegId": "FA-000000055292964",
        "F2RegId": "FB-000007604782374",
        "AlcCode": "0300006342850000001",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ЧЕСТНАЯ\\"",
        "ShortName": null,
        "marks": [
            "187431554918160924001FBWTVN7JW5TXELVO6I7C6KPCFEHHJQJQV2X27ZOTJZOCITXWEC7KITCF5KBCUYBAVBAHOTXHXTI6TWKZFABJPKCHSVCJRV7IOX7UFEKPWC7MLCYHFUMFJTUAA3YYDOAHQ",
            "187431554918170924001PIDBXUZ5G2Y445ENW4LCOLOWTIRLO2VLIQNAR3FYBC4ZMNLB4OGPHQ6IEGYNQ4TD33WGLNSF5GXWDGWWO4QPDGHQHBSFEICGEKJVH3UMBEKSYL2DPFILR24IZQZZFJUBA",
            "187431554918200924001VN5SPPRWHU2YUS75W24YV5ULT4B3SK7RQMPI7OK6N6PH3MXDE24POYKC7VIZXPV5AD6CGICTWMS4PEW6RUM6YOIABGW4ZQNI7JYU2NCSIZEUPUJWKNFJMI3TVRVOIBJXY",
            "187431554918210924001WPZONGG2YU5RFSVHRFGMOPRISQARYFSK2RUZFDFM7QKA6EROHNZ4ZZHELJODXK7IP5IVNB2SLITJQYGHHA3TSLIDH6LWBMIFA4MLUZKSZN3N4R4YUHHWJUHZQNKDHZAYI",
            "187431554918230924001IBH2EVZL5TR3I37DRP5N5DKTQMQCZOPNGG5NPBJQSOKOAERZC2YMHFYBPCANBKPBHAPSTOEKCTYL4MRLSG37FH54E5BEBCQFLD5RXTFW4AB4IZUUYN3KEWNKE57E3FFCA",
            "187431554918240924001UCNOEO3VBMCNREKAB42LPSGMYUIOQN66SZTXUXAGTNDI5LLUYOPUVG7EUWITNN2OQHPPB4C4QJLTRZ33QLIFSURSRQBPHREEI3OJVJVIEU2VHBYQWM6PBU6HQHIRUVM5I",
            "187431554918250924001PTXMTMZXDHTOHO3YBBZNBXFPCUEMUGND23LHDKKJ2H5TXDIL2ASJWYVCOTEYEULXCATZ7AZEXIX2HHOZ7AHCV2K55Y6EJ3K6F2MCXLSV5G3C556DQ5WJNJXEL7PSHH45I"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 7
    },
    {
        "price": "383.00",
        "FARegId": "FA-000000055026771",
        "F2RegId": "FB-000007604782375",
        "AlcCode": "0300006342850000013",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ДИКИЙ МЁД. КЛАССИКА\\"",
        "ShortName": null,
        "marks": [
            "187430757067040824001QR6CLFLDNPGXGWQPGSM5XCNYYIVBTPYN74GW6DHTY4DQPVVTRWQQ6AILXE4CKJXUMNJU5R4V6WYJME7SLKSXD6WAK3N4IXGW4ZLAV6TUJZBBTZ3NR7RPSKQHVEQHHIMIY",
            "1874307570670508240015OAVPXFI7HHYGVFTITXT5WBX5A3QFZSABN5MJWWPO6ZO4INHPBZRWQARHUN6MME4Q6KZEKNQG5MPYMRYSLNDWYFWBYATRI4JP3GNJWSIPBDBMIFU6QFQF7FU43EHFCEIQ",
            "187430757067090824001L36MBUCZ7ZSE65TCLZ6HYBB4KAZ3B34SJZQEZSYGGOS632I5MSRUYP7UQJO6LI6XG6ZRQXRTKSZQCFC7UXHFWWZ2EB23HX5CETYWAFHUDQYEWRR4X3HPTVQTNDZNSDOHA",
            "187430757067100824001ZPMNQHLHXJXTQMXO4ZBZG5QFNAMYQ5VALTIV3WNZIDXKKXXKDRJT7HR6WSO4C4N7K57PEM56PAHLFUVYDNUQSPKRZCMOPKO7NXYCXWGMCYKPAYKC3QGRRDFR7B7CYMIWI",
            "187430757067110824001O3DMXJD6X6Z373CJ2E3JNKEDUANFHE336INGYSTYGDFVGXYIDLGYT2RV7QA5HQJUUHNAINR2A62EVDHHE2VFB5XA3TL2CZQPGM6WSB2SCWAGVCLCFHS2KJMNO7Q2BP5EQ",
            "187430757067120824001OL2ZWWFMN45QWF3ZKZSPYPHO5ISFACFKWOHMPWUD2YA7TKE5HSKEUHC4RDUBCTADBPEX42I62EA7PAOVWSAZ2OVZL4QVFV4VNREXXMBR2V7R6ODCQDTZ6STENC5CCA65I",
            "187430757067140824001G5VEMHXVY2FAFJ2EADCME6HGLUNGZUU4QBZQKFPB6HIJQ3CZOYYWWDJM4WE5CNBSM2XHND3SWCQKGEJPV3FWD4EKPDQFY5RQI5OHFS27KBLPDQHATZYWS2JUPRDAMEQJI",
            "187430757067200824001E4NIJMOFJEVU2DK5PTQW4QZ6QQSNXT6F2MONNV3UY4H6SCWPELSN47I3LNQ7LYGNLGZXGU755E2TUPSQKJRJBH2X4VFXQ6UBVWZ7FGDN4LOJYBMKO7UMRXHXICQ3NRAWI",
            "187430757067210824001O4VERNNBOKW5MP7SNSSOXAENKIBKXIK3KRFVCZEGLA4NHKKN7DESNV4EZQKSPGUXYMZFWNK3J7BFUGXOXFRQPG4DRNJO2WIRPMFQY52IHZ7K24TWQTGGA7AAXKZ32I5MA",
            "187430757067220824001MNP6V2LVV6W2A7ENIFXZ7ZLUTIPVCSNNSSBDOEU7EIL7BULMFQM5WF2PST23NGVIA6KJ4FMXKXRCODEFX3ET4ALL2IR5ATLDKSINMGYJMAPNYSL7RBR7GC6YNHI2LV6CY",
            "187430757067230824001XVKYTWDJQSWGHGMYAPRJZXEDZE2JK2NNP64UWZJITCMOZXI63T5BG3KSCCNHT7IDAZJNVXVK2E2P6BIIJ4RE3DOYCSZYZ62QVDUGZLB7WCUMETIYENZMDIWG7LTSI3FSQ"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 11
    },
    {
        "price": "618.00",
        "FARegId": "FA-000000047126095",
        "F2RegId": "FB-000007604782376",
        "AlcCode": "0000000000038030343",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"КУРАЙ НА КУМЫСЕ\\"",
        "ShortName": null,
        "marks": [
            "1873021912161104210012MCMZ464QTUEMST5U6H7ZUAVIIKY2H2M2W6A7DUAIFNMMR6CSSHOBTHEE3MXEJX445EJAI2REM7PF3D56AHEJNU7557CS74KWC2YGTJKPHEUIIZJOTCACJNDSE5KPYJOY"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "618.00",
        "FARegId": "FA-000000047126095",
        "F2RegId": "FB-000007604782377",
        "AlcCode": "0000000000038030343",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"КУРАЙ НА КУМЫСЕ\\"",
        "ShortName": null,
        "marks": [
            "187302191216380421001TZI6EGQDOISYNVYZ5KXJ57AC54C6N7FVAK2UHJKG34YSD5TRXOM4PBTIQQIGFICVOPQBTWBLG3M4DYXPVU4AHH4NDAO7E5XHBRIDAPZBTXAEFQ5FQUHJYM3DGGSEVCWOY",
            "187302191216390421001Q2G27CILR5SHRRUXOGWARURLBQDGSQFLTEBR4AGF2OAFIYLGWBOELOU332VJSI7NBWPDIWYFN45FPLP5JF2BKV6VQ4GSDBAOK3KWN4WLYX3N7GE2UU4KGYZFUSZLFV6WI"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "348.00",
        "FARegId": "FA-000000052101642",
        "F2RegId": "FB-000007604782378",
        "AlcCode": "0100000042540000049",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"БЕЛАЯ КРЕПОСТЬ ОСОБАЯ\\"",
        "ShortName": null,
        "marks": [
            "187421572558810823001GL5POZX63A3UHTK5N3EZAKYX2YJIITYC7EQ2ANQFWNOR2NAJ3JK663FL2EPRILM5JOFEKKZULBNHYUW7ROFEBK55DLFGH3PAIOSWKTDNAOS47IDAFSLGSYTWYXVLS4CSQ",
            "187421572558830823001XCHE24LPLFL4AQU7IWD5ANDFAYNSLWD526657WUXOK53QKD5XAHHDLS6YN3YJL5UK757XZLGEKNEOZVTLWUMOSF7EZCVQZ7T4UUWYAUTWHNKIDSEQQEHB477DLLCB6DQQ",
            "1874215725588608230015KBCAP2NHNBFIYUSUTIDVRSPLQIHVIKKAHJGWGO3Y5FMTZCVCP5VICMM6ILRZZOGB2JWGQWIW7WIGECIGNIEQKJTTN2VCWX7AQAXQ3TTZKBAUY3QUOOXAPYFVDYSAIFNQ",
            "187421572558870823001WL5I2LEFDSRAP3HESY5U6VWWOUMVMNHC65LOIE73T56JJT2VTVFQDW5IJWBFBNC7JRS54WEBVMIEC47H2LQKTVVDUZEPXGYVLJNM2XMUONT7DHHXRYNZZUYNNZNCA7NBY",
            "187421572558880823001EEGUI4XBBWFT5JWPNZB2VQD3HYZ3OCGFDIYUWOS5KMPZNM27NSEA27V5IDT3W4OVJ3SO5TPU4JUJDTEUQ6D3O4LYA3J72BIBYFKOWIGG5KN6XXSXTWDQB24HT7QEXZBFA",
            "187421572558890823001SJMRKCGIHJ4GOMD45F332ILLRAJTWUK24UOTQ2T3UA6NS5WRD3CNV6JUVDT6PJLHPGW4E6BJGP62RTYNHH3ZMVRUPTDXGXF4TW7U6BDF3VPSHXBJTU6HUMEWPOK7VGHIA",
            "187421572558900823001SFMLSU5UIZKAWSPIXJ4LAMX2NYRLSVWBJSRTH2JZGI3MCNJC7VM74SCXZOC2IJXW7GHMI4DLCXUGW35RK2LI4GGW4X3ZEAMIWZJLKPMJ4Z3P6WHGEGLM72IGW3EXUEYHQ",
            "187421572558910823001A4XUUEDBQ67KB3HB6B3FEFGUO4D6KUN4GJSRPCCFVGP3ADELFPMDWX644RMQKK2UVGHXVEZJDMAQC5ZMCIGVQWE5WVQG4ONK6NTOOHV4ZTYKIEY6B2S76IY7FOPUS5MSA",
            "187421572558920823001EGWMGB2N6PVOV7MTSHQBWJWBXEW4RZPYJHHBABPYDKHZAR3QLEJTWGWLONABFSQZ4EHMADBULAXO5S77JJKGT654BR3S7TDDRBUOCEOEU3EW5B6RQ36DUAID7LQFGUWDI",
            "1874215725589308230012SOTR3XUROJ3GOOWF7AVYDRN547HO2UYTDI7IZY222MGNVGG5GWLOIMDRDWQ5Q4TAJ63D7H2JWVQ5RPSD3UESMOYR73ZPKDB7SY2OG4ZEWD6HPBXM552IIUASZESODCOA",
            "187421572558940823001UDOCSPNW3NP2HFYG33P3PCN6UA4RF5PHZW3LEY2B2BMENEPOMK3EN65O7LSQPWYNHJOQAFNW4AM7TLT3JC6R5ZUUSM7WTMPSZ4N5DOUSLELDLXDEUG6GURHQHCVYGCK4Y",
            "187421572558970823001VVDIP5TANTBUNF3EVBEOIDHRTAMRDMZRBJWRTC2PXQ6W7D3OQSUNZOBCR4PRD3HVNTVKRRP62T233NVV6V56N4W32W5IPYBCUJ3AKXEKLV24BF3C2XZGFGK3GNUYTDF2I",
            "187421572558980823001VCE3YIXFIEQMHJNULCCAMCPICY3AFEAWWDRR5V22S7SQUH5BLDLLZ6PTAOFYWM2HHY3OWENPDDUILXJSRUD5ASUCLPXHXYCN3HYOYAN7ZDO2O5MWYWUEYSEAG6KD7TQGA",
            "187421572559010823001SC53CHMGC4FTY5JCKEI3B4CZU4LSCIIL3TVKNZZOFPAIDGXLSQC3ICGWQZ5LWZ723EFLSVLQTNRMGJ76Y4NYWEMVCYBX4HB2LXWS3PTLFGFYIKYJXNRSTYHCYSSA2IGLQ",
            "187421572559040823001BTBJ6JGP5YGUMMFGCPABQQHW5Y5Q4FMEVAAAOPWGN6UJ7TCAOD6NQDICTHLSI46VULRAPD3CNPUBDTRWDMX67NY7CZFYNP2LLVDTWRM6WWL3RFQAKPZGRP2CKXWURRBFA",
            "187421572559050823001Y73ISUTDXLW5CIODY62C2M5QP4USRG2JFHBUJ5ZG2WWMBHAN5UFBBVM2X5YT3UKSJZUGMUU4LL63MY27J4DKANOH4WGNP5OJHXFKSIRMUADXLKMCE633ZHMDJMN5TSS6Q",
            "187421572559070823001KZGJ7KX3NHXMWXWEVV3OP7Q3UYAF6R4TN7GKJ3QOEB2OZTYNWXVLD2XKR5EHKZK4Z7L4YIS4SPIU77CYPDCW2BQVE5KWQBU53GD4PJKKJTOLAQPLK3U5TU3CPAYFXJ3LY",
            "187421572559080823001QT664CG2UW4DWFYJNMCJQZQZ2UOY2MMUW24YQM4PFORAA7R257UP7EVIXPLR5PKKUJTIRSNOGINRRWDBEM6ZKCOA4QKROI53XK7VVQBHJANKDBLGD4EQO2DLYA5C4PJSQ",
            "187421572559100823001CAGDUN2QI7EUQS7CUM3FQ2JC2ECSZYWCUT63UX4ED7V2ZL3B3EZMBETXX7PXZKSUB6PJLBXKWTE4TT6TAC25EMJDAFN75WSJG4NJJIPRZXSYPLRLLE4NRFTSJCIWQJRQI",
            "187421572559110823001B6G32UHPB3IUHX6JAXH663MXEACNBWKQ5YW3WOI7CXYCSUPRN3ZGSXHHUHLASDO3HWFGBAQ77NMWLLEOKMSG7PG5RKXFQXTHYOFDI4WFWETJJHZ72HH6B6WDUPU5SQZ4Y"
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
                "FullName": "Стерлитамакский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 20
    },
    {
        "price": "437.00",
        "FARegId": "FA-000000055269344",
        "F2RegId": "FB-000007604782379",
        "AlcCode": "0100000005410000092",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2002",
        "FullName": "Водка особая \\"ФЕНОМЕН\\"",
        "ShortName": null,
        "marks": [
            "187431184715330824001AGON7CKG2S2WMNGPT5XLW532JYX3WEEKHR5UYYEAPDQXB5JYYGR36C3JKY32UPSOE2FZIFAEL7BT3FNQDJJQTHSQITXBEAWYDW52Z5GFHB2T45RFQRCDOHNP6VUZOCOTA"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "361.00",
        "FARegId": "FA-000000055254350",
        "F2RegId": "FB-000007604782380",
        "AlcCode": "0300006342850000006",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТАЛКОВСКАЯ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "187431541401150924001CCMHPLB24TDOKIBTDMYRUXK26A7VEKO6RECOKU6C5AU36HJ7Z7HFOJY2UACMYFYPDXKL3TL4VQKVWCUMPPKVDDNPDZW6LVCLQGUEQP5G7M3YGMFLIOE74J63JG2EUAOTA",
            "187431541401370924001RD7BSZUXPH3GCO4DEI72JCOUCELJFU4Q4K5DWWBXJHN22V4RSVW2ZZY4BR6I3QLCKHDCJ3UPCPWKHZXAS6SZONKMIT3ZCR25RPKGFL3WJSPQUGT7EOR3X5LQUQVJOKB4Q",
            "1874315414014409240014VTHSFKRUN4RO6GQ6XIK34TTI422Y5XXHOT6PUGOYLJHYHFXPTKHM7G7LHGEUSGDPFLPKI5XTHU4LG2TQRAQBLP4PE3KJRMOHTWNJ6S37OX6Y3W775VPFKTZZPMXCVB5I",
            "187431541401450924001JCMKDMIJDB5YGA4FOCFJNZ35GMBZA2QCPR37JZGKHPQFP5JICOAVJU3SE2LAUR6B3HA35IPR6XHYBGFRZJMACO6BUA73C74B6WNWYRKCPNW244MUXD4S4UZBF4VJC2BGY",
            "187431541401470924001AMU2L3BAQ6ROCK2MSU74KRRLOUS6CGRHAGKINEKIGX6AEPHMRWPM5246FRBKXMOO2CJ4RZ7OA3ZALRCFYWWNMNTZ3ECCBTHLPVFEIXWSVG7PX5XBNP7ZBLZA4GWWTSMQY",
            "187431541401510924001NB73VTSXT6LAMCTVAKPSVOFEF4SAWXYUMT334RLB573JBSV5UTTRPPCQB5C3FX6PZ3SR7QL5XUF4DRUIUKKKHQRHSPA4SXPHLHZPAWX5SBEYP6QWXIKFI2LN4MKSDEFTY",
            "187431541401520924001L3S4GJ6SMAACYHNE7JH5YU4S7ATGUXBA3BXF4OPYDHUSFB6UELS6SJ725FDFISWJKECWFEO7ZE3DRMS7F2VUCCHQDWPFXZAARDHJTDLHY2CDYOO4L77DLCSNONNLTZEDA",
            "187431541401580924001WDC7P4ZTP7FIQPVZ3UGLFLCH2YDFKTPQHIFGE2HQBVMPVJDYYGBGR5NSWMPYPXBODTH7AJ6GEC6ZWKGDMA3MGR7BME6WZ475INSBTOVW23E2RLTRINMIGAP2KQOAU7JYA",
            "187431541401590924001ARUKG7EL3MJ3GXBX3EACZGJMAEN5PHWFZVY4XOVVR7YDXCWTWX7IM2CCR6VOJ2RKKZY7NZOU5KYRB3M7QYAKG2OP5XEHGGVLPELGYHQWWNLWSEYJEII6N3RCMDMXCEXFI",
            "187431541401620924001CCLZSOJSEVGBJC4AGO7XV6JJUAQ6KABU3TVFG53QFQFWUESEALY3RRWS7XJW4TZNS34OOGZHXRCLO6DO3KGRLQZ3IH7ODU4UGZEWOAH6QHA7N3I3EHV276KC4B4ORR4LI",
            "187431541401700924001IQLRCAVCCXGNHVHC5YSIXNJOYE56NVE7AW4UWZCOL4GAADJZRFMDCXXE2Z2LD2S7TDH6EB57KEYPQVACYBOR26VH7PYL5C2RYIQQLYXEKCC5NVRZMVNLCAGNK4OFYRYFY",
            "1874315414017409240016UVBCO24P5B2YJTWUJ5XCY3JMILQQBZJ7MQF2XVEHLPBY7AQMWVSFXICPAAQPA65YNSVZMWF4J2R6NRRIEBA7DROJSOYMTNBROV5YTXLZOULFFK24EXBBLIMT6USOUNJI"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 12
    },
    {
        "price": "353.00",
        "FARegId": "FA-000000055653807",
        "F2RegId": "FB-000007604782381",
        "AlcCode": "0100000005410000016",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\"БЕЛЕБЕЕВСКАЯ ПЕРЦОВАЯ\\"",
        "ShortName": null,
        "marks": [
            "187433195703991024001WVU7B2NPLZMUVLGYU43AHNWRPIFAPMIRVZUVNBDOVBPKQPTIGF245D5JOCND4OE3D2ASQIYM5VIAPLDVSPDVKQ7B3DPUMQESXXUHMHBMKQTS7HFFTXQTLS5YDXWIAUS3A",
            "187433195704001024001PSAUFGYFYEFOIPKPJLOD6L6LWY4NH6F3EN7DEI76GQCJJANCR2ZJPWZWQI7G4HOVHEUVGOHJTH3Y2BOAKAANVQDWGYF35XM5CYCYFATEGKRWSG6ILLA7CKIQ5QFBVT2NA",
            "187433195704031024001KTBAWVRJDPWHOHA7MKEBVB3TVYMLVMGTKKBO7CZBBT2FSCB6FM7OFUB2ZKESC4PDD6MO7LHT3SK7K6HQF57653LMD2XIKIHU6D7FB6WYSV65VSPXR6N54DJKSVLU6OPZI",
            "187433195704051024001PQDYELVKS44SCB6LHGT6F743BAGDDJANZPBGRSHANJU652KA5TL63DVYI35J64Q4J2XDPVCCZH3PFNAFK3HONKUUQGGDAZMRIFBRHVAMLTY4U3BXEXGY634PCQCS4KXSY",
            "187433195704071024001OKEJFLF4GAF3TSEGDSOABYM34MNSPOYVQFKRAJG4VISJ4K6LCXDAMGGJ2VH4CQTHZ5DZK7RMLQ5YGPTZGVPLD23GZS7WRAF37MRQOODB2LLFXHKJ5IPX7B73HNSPKU3DY",
            "187433195704081024001LAA4F3IO222ETVF2J33P5B6LAATYYGXPBWYTFN742K35NYDJ6QHJ6VEF4MVSQ5APBA4HNFJVG2OQSAYDSX4DGDQVXM5DOABODGKIYL35HCFI5E4INJHVIOJAI3A74RJVQ",
            "187433195704091024001B226JQ525AGP3T7NNKWVSXIYJYMSQG32CM7EMFYO34YBG4EAZ7WCM4LAFKNZYG5YWOLRUIAYYPYCF3O2WSBCCXUJX4VBA2ATIHX5KGXN64I65F7XNXUOKKAY7TNKBJCZQ",
            "187433195704101024001IWQMFMEKQKMV3MNLVLMLMJD6EAEPRYNN5CXZV3OO476HNWX6DBJXXRKNB5SU63L56LGXCLW2YNH62CXPYKHVRK4FMWFU6DTGFJOA4KNWPD4JKJHBJS22ENQJ5YBIP3PSA",
            "187433195704111024001DHXCPMSJLFPM5SEMGDEABHWD7IEAIMT7YN3G6JPUPM7XZXEU7A4HA6EPJYCXKEONADRWUALWOCK5HH5MTQNK3PJOOMQODOHFAYIXESZRU3CXU6CNO4EX5IVDK2DHWYUMQ",
            "187433195704121024001464PNX2EJUN3QLKYPWGRIY3BQ4OFJD3L5736ZV2Y3CKGATFGXJM543BOFEMVK2EIRXGZZGBBFAJQCLJBEGOJESLLHNXBVS3IJ4VIJA7B76QV6IYBDLJCHI2YB3UGRXB6Y",
            "187433195704141024001U7RKCCACAIJINZ2E5QVOJU7W2QM6WGTS5XPABML6ISS3HIMESZBS3557IHMNUBNBHULTAUC2LFTIJQIKI24BXBMK6RFWYPVYABF6XNJKU3D5J2EQILYZTA2MXHY66VY2I",
            "1874331957041510240014KARU2XBHBEEGG6ACPWFGHXGB46UD75QN7UTSH5PRDYGNWEU6Z5K5NFKQ4ZPRULTI4YVPSJRXAJRGKIJRE4I76OXNARMTHBMNDHKG4ULMTGGYZ4MUAI6UOGZMFJSRLHIY",
            "1874331957041710240017X4E7WTFZOWCWSYRMGL36L7GGQKOK45NRKQQSHBGOJTTVJ6LWEBOZUEJZ5G6KSQQLM6F45BZHUD6WB6XFQANEY3GSPRBWIGX22BWA77UPLBRNYVYLX4NPDHXWJQILRLXI",
            "187433195704181024001FARZRLMDHFBDYKZHHBSZ5LEHNAHNVI6EIJEPK7FHI6M3TU4CO7JV4LBIFO2H76AFBLMDNYAFOQPUK6SSMTOKHVITOQNMHQB7KELDDKIBVNTUOQAJ7AVVCPX4JXNZUTNXI",
            "187433195704221024001EBFFG54RK7FTRFTG6QXBDC26PAI5R2QG5WZCTIJIFBGCMRZ2AD6XPS54N3RKVU456O2VVQUALZ342T5NLPODNCRPRJ36Q5FWOODVHKSJB3VPVHFXUE6WTCG4XSGKGYZ5Y",
            "187433195704261024001MZSBNO5EUT5EZE4VDOHDSYCRI43A6SQO3UDJWTMO6GZ3QW6VIW2GYNAGOM5LD3VYGJPNIVDXMKYM7IHOJSURDDYL2YYMBNEQECDSHNO3C5KSEYKU6R2MIE2ZKBIDBC2JQ"
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
                "FullName": "Белебеевский филиал АО \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 16
    },
    {
        "price": "531.50",
        "FARegId": "FA-000000055148635",
        "F2RegId": "FB-000007604782382",
        "AlcCode": "0300006342850000008",
        "Capacity": "0.700",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"СТАЛКОВСКАЯ АЛЬФА\\"",
        "ShortName": null,
        "marks": [
            "188406511076570424001MXOJQBZDDWQL3CHNX7LZGGWFXUBJUXHKDHFSJXS6GCODIUFBOP3FQVPAOSQJOEQR73HETLW3V2JXLVJ54RKRYDPVW27KBNPG737ZF6JUTYOIKLIHTLN2YXOM7XQYQJGIQ",
            "1884065110765804240012TFGOOEJHLA6WC2HQRLH6XH73Y6XGMVFDV35XHLJA6LUKU3AEKFERUMSIFHCYTBUKKBU6DGBLE5JF2XHPHNCH4NXYSQJNNTJXPALFDXXQHM7B77IR7KTGKPYVUJIL6NBQ",
            "188406511076710424001J73EZXKK7DHHWSVRP6CZ7UEM4AX64YB3XOMIXJCJSJPZR45VI63VK4AUSTVDHCQ2FH7UKZ3KCUQA3OIWO32SPT4E7526NIC6QA47G4VK3R76PL7RCGSTILBTSZXLJLQGA"
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
                "FullName": "Акционерное общество \\"Башспирт\\"",
                "ShortName": "АО \\"Башспирт\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "248.00",
        "FARegId": "FA-000000055287990",
        "F2RegId": "FB-000007604782383",
        "AlcCode": "0300002891500000161",
        "Capacity": "0.350",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ПЕРЕПЁЛКА\\" ДЕРЕВЕНСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "187428962790360524001SYXCADOCLTZSWRHS64PHOTNJJYPBD3XA2EMCA7AIK5B6UHNJZKJXUR4QEK5Y5MYVIBYYJEKJGOC6RQUYIMSEEMBPS3HK6Y4NQ4NQUOCHNU53NPDJGD5RLUML3CBWCQKUA"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "112",
                    "description": "Республика Беларусь, 213633, Могилевская область, г. Климовичи, улица Набережная, дом 10"
                },
                "ClientRegId": "050000036917",
                "FullName": "Открытое акционерное общество \\"Климовичский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"КЛВЗ\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "153.00",
        "FARegId": "FA-000000055300152",
        "F2RegId": "FB-000007604782384",
        "AlcCode": "0300002891500000012",
        "Capacity": "0.200",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"ПЕРЕПЁЛКА\\" ДЕРЕВЕНСКАЯ\\"",
        "ShortName": null,
        "marks": [
            "1984169710106607240016A54MMN2IATWSOMNT45JZFRVMIKJLKIXBCM63LKPGKKGCH5R4BUPCGVLH2CTQUQYGXTZTVIC26PXTPWGIJT6AAQAUTDRQPZ24NS6DHANH2JXK6IMBNUM6XH4TL25ZBP7A",
            "198416971010760724001NS6YPAMMHLEOKT4NOMC64CLEJ4TZO5QTBI2TTQ2BOO6DDEPHY4OWULXTBSU563Y6S7G27LYPQ5JKE67OPCOPBART4SG2B3DCR3Y43RBFUT4EFD276S7W7Q6XMUTP5COAI",
            "198416971010810724001TFTWKMWYZQXMGVHJKBLNEU6QEIHDCNNNLIIDCY74FSG5IVGFGP43QWAZJUXUEFWCTVXZFGDEEOOVJW2SYHGUMJP5WUFEDXGERPKCFAD64KBVXZ5KC6ULCULH3Q6CLVUAQ",
            "198416971010860724001OOE33LVTQY3RR67ZB7K2ZRV22ISQHYILJLYJZUHY2EU2VZ7DD7QVECL2GLAWSG4QQJLACPDQ7YTC5UFXIHBLBYK3OJ4TNJB2PRCFF3N4YOPSWWN2RWDLK537PSXTNBYUY"
        ],
        "Producer": {
            "TS": {
                "address": {
                    "Country": "112",
                    "description": "Республика Беларусь, 213633, Могилевская область, г. Климовичи, улица Набережная, дом 10"
                },
                "ClientRegId": "050000036917",
                "FullName": "Открытое акционерное общество \\"Климовичский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"КЛВЗ\\""
            }
        },
        "quantity": 4
    },
    {
        "price": "68.00",
        "FARegId": "FA-000000055062711",
        "F2RegId": "FB-000007604782385",
        "AlcCode": "0100000010250000073",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «РОДНАЯ ДУБРАВА»",
        "ShortName": null,
        "marks": [
            "197407359612320124001VSZYRA5ZKVLRGH2GE4QVWXOLRUW2EKS57IFSFBYGBTMSYTCGHHYIURFZODBWTCMNPWXHAZEUPTXOMCJBU34XIOAAHHATP64RIBMSDKIOATKDW7VIB32MBBEZK7BYVWVMQ",
            "197407359612690124001Y24LJSIFIKHJTXTBNINAPHVMQQJ57AUVVPGIFO6IMTXGXIMY3DX35D3T72S6CLNDTJSHPJXFQTIUSAFXCNCFSJFAXOSJ2BOL2XS4CMY54I2ZVB5XOBLFDIYX32AZHDRAY"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "230.00",
        "FARegId": "FA-000000053542809",
        "F2RegId": "FB-000007604782388",
        "AlcCode": "0100000010250000010",
        "Capacity": "0.375",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\"ПЕРЦОВАЯ С МЕДОМ\\"",
        "ShortName": null,
        "marks": [
            "1874256667467112230012RWU7DJIFTV4SWF4QF4SRB3G4E6ME2JY6CH3GMPW6TLCCYFBELNU2CXF4DJA3LGQDSQPPHBMYNDKD5HHZAQW3VIOAXN6XUF3LVC4YCV7EYYBNTZXZ5N5F6HK7I6IXHRGY",
            "187425666746771223001VC6TUS7XZCSLXMRATTTAUFMUWMRKPWENGH5VTSZB6TLSDETET34YCJSAVXB5YWKXZJ4L57D6YK5PRG7SOLXLJJ262S2Z5IGEVYRLBF3SOI4P6CZJOOUZUOW3VHCI4ZC6Q",
            "187425666746781223001IQEKJV3SU7OU65G3LF5SGYQ5ZYYCNOGDTNJL5YWXIESJNNQ7A3B7A5OYKXZNS7QMPP452AESKZWGDXJIQGVGI5X6YTCBBVDWGLNZO6EJBWGT33UF7SD24PKLEBLFD6F2A",
            "187425666746821223001QVH6VBMWDNJU7BK4ZEYG3G72HQJXL2RQSLIVOWUGXXDNVFKJJNQX5TR6IB4XRZBCO64VSN7AP6QFUUNQUPXO2FOWXIFHXM24FDZIMMKRVTE6ZSNUWSGQIW634WBP4ID2Q",
            "187425666747071223001EQDSYSY57YMDWI254BEYEHKZDERP7UAG3ZFBSDCCESWMEAU3BIGY7UK2CZWECJWXQDHCOA6WVSBHKVNYBIHAYF6VQNO652TIT46RAXLBYMAUMWG6F2QZODBH6XWJNUDSQ",
            "187425666747111223001YNKVIZ6HGT7OMZN3NNJWHAFM3E4NJMKQY2DE4AO2DZ3KAFHEB3J4XSYMCEDLOHL5VJVQUXSDE2ICCCNX7FZEOAQYO4S47PWTFER76SVZQ5YWLXV6NZVMXEN76EPPT2AVI"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "269.00",
        "FARegId": "FA-000000053845367",
        "F2RegId": "FB-000007604782389",
        "AlcCode": "0100000010250000009",
        "Capacity": "0.500",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\"ПЕРЦОВАЯ С МЕДОМ\\"",
        "ShortName": null,
        "marks": [
            "187426326353050124001BV7UTJSQDWVHSZ5SFD2QKW2OYMJYYVIIYL27MV3G3PMIG6SYIV6HLMDRZU37EFREHMF7P4FUHHAVSQICMJUNZYWXVLYKDD63WSY2JJE6DPC4B7SYL5K7EDGDA4GLMCOEQ",
            "1874263263530601240014H4H4WUVZKENXYQCCHH6ZVD6EUYKJ5J6GKZPTWBSXYQO2JEICNWH4MEBJXAC4VRRYIGUCWMSV7K7IIOKMVGAMCYOLXTTWKC2WDOVESQBRQHRZ5VY2FMQXHWCX3POWVLOQ",
            "187426326353070124001EEKUUTHAQSTLBOLSFCHPEIE6WABGIBMO7VT5CR7ZTYPBZ6QFAINIO5ZXWX3BSFPKMHRQ6ZMKEQGMJB7KMSVN6OL4IYOK4A4T66LOVDM4EN2NRY56PDYVDX2BPD3VSDWUA",
            "1874263263531001240013CLG7T6G7OOJZ2CMJCXOQSYEDAQVGMYKTIK2IR7FH5IVTTEKVFVZQOU5M7XEEMAARANBA7E4SKCPLTQQQCQIV4VZCVYRYJ6BEOOSRP2ESZ4V2CXYBPDM6IZJYSYT7D27A",
            "187426326353110124001EZ2QQD2YGVMMCONFOFKBXZXFLYT7QXKUKEZQCSCRJMABYJHWF23LNSES727M57MS3J7KBSVIOGFOVFD5NKA6JIYTFUAM4QVF4SRWVRCICFXQFOVQOH3V7B6PAY2XV76FY",
            "1874263263531201240016ZY6JLM3XQPPXVSXPXVLJZ2LSEEX3XEFN4SBZSCA2LW5E63SQHXCWETJ76ROGZT4JKGVM2BBZ3NQQI7ZHZ3PAQOKRJDXEFV2MJVOV6JCU55PWYQGG5T3TRSH5UPVYXYZY"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "310.00",
        "FARegId": "FA-000000053690883",
        "F2RegId": "FB-000007604782390",
        "AlcCode": "0100000010250000009",
        "Capacity": "0.500",
        "AlcVolume": "35.000",
        "ProductVCode": "2128",
        "FullName": "Настойка горькая \\"ПЕРЦОВАЯ С МЕДОМ\\"",
        "ShortName": null,
        "marks": [
            "187425442634161123001CB57C4CA4J4RFE26KBXZ4UXREIZ3WGXVH7UY754FDZLJHOL7S7QURCUG4X7KOITDEYJU6SVHSD3XLWMCM2K5755G4GS4Y2RYYHZG6XRFNZBKIQSJNUKJ2QJVRDBZRADPY",
            "18742632545980012400157PNFAZKFIWZT6DXSP3DJHC46MSG655IHOUSGXNLK35QZXHD2YKIYCZBD3WG4VRFA224ML3FLOZS5WSPGFZMTIX3XFRCTYVL6VUKJJR62P75YJ3R7KOLSD64ZFRX6CTOI",
            "187426325459830124001KNMN55FL4WJGPAK55OXOZ2ZBGA3XQT2XIRFQBRKHMF4R6CUECV4VTP3CZFIHVYFCRYM3C7DUGBHKF6ERUB2AQIJ7XAPCZFLGDEE4F4TJKPXS3JIMZT33ITEZ67DJERZ5Y",
            "187426325459850124001NWHRG7OR3EESYKTDALFVDOX6PY33GUGMDOCEGRIJJNIW4XWYYFD6CF3ABUPGZBJCJLTR3WLPUGK5QYUJE2T2X7GMT2DDISJU3AIJQA62YT3CIZWM4D2ZSVLPSGIH7VC6A",
            "187426325459890124001O5RVX4GJQVECZ6XS3K2EG2LSTUXLJVOJM6DTV3GSTGMWQCOWOWXBN7FZKPJ2C6MQOOHOKZWDFBBKLNHTG6ZTK6FE7I6RUOKA774YDXUZ5FWDCPH26R4OLGASCMOYRRPRI"
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
                "FullName": "Открытое акционерное общество \\"Сарапульский ликеро-водочный завод\\"",
                "ShortName": "ОАО \\"Сарапульский ЛВЗ\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "199.52",
        "FARegId": "FA-000000055400664",
        "F2RegId": "FB-000007604782391",
        "AlcCode": "0100000002700000030",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Архангельская Северная выдержка\\"",
        "ShortName": null,
        "marks": [
            "198314229091140324001QJY4CEYPP3KG23LY6UE6VBMCUY3CLFKLUKJ6DQYPBEM2EYOIZLD2ML5JQVH65GJQ52PIYRUV7RCGKKD3OCQEBHHTUUE2Q6M3ZNUMYHGSQSJF5SRHMN2K5GKNKFMWI5L2I",
            "198314229091180324001QSMSRGY64MKAOCHN2PHNAYC26A5YE5XH6PKPZWXDKWVPHG55KR2RV6H6TGHOGVYONXADRNOYSLCDOAUSZNPGU2YQPYF2P5D4NRDD2T4W42DDGON5XBHRLT3TTB24XHVDA",
            "198314229091220324001SKAG354KM5DE6G2YPG5B7V5YLMKFSAOZO6EATXYMCALTVDM44CI3YLHCV4RGDUVQQBBHCRFXHKKVDCKIJKSXHJBEW5LKRQIFDYHGIM4JPUMMUKCECL7WQKLZKXAJLYI5Y",
            "198314229091230324001AEDOYENO26LDXMBUMRD75RSHJAGVPRGZJJHHIABFWTPGJSRKI3WFN6PM6KL6KMGEBZIP2TYAEN4UWWGY2732OXA2ZHGVLA2LWJZDMPWI4H5PSUAJ7CB47ZQJAGPSF75XI",
            "198314229091260324001EDEDNXGZIEEJFIFR356232JZPQ7CLUZ6WZA3GMIFY3WYBG4GSEDRDLQM6RHVMMMHQQPJILC7M6TQUZIHYAXEPRY2VMXPOV6Z2WSKVPEUSI5LX7PBFERF4KYGNRGKIMEWI",
            "1983142290913003240017JKMEJW4MKWZU7T5GJ2YI64OQQJ74GIBAZ2LUGL73YTHVWSYS6SRGFBAKKZY456KO4FH2CZM25EIY7MSIMRF7BA5PKI6EN3KC3KY2UEWSW7EX55ERDLUEMDFDVL3MWHGQ",
            "198314229091310324001XSARWJUXTVB576YJ57ZCBB4O2YSW3JPC7SH2NSVVW3ZIEJRPSROQPY3JNCX2DSSABNPBZUEQYKMT66KCY3XHLXNZB43WUUNIAT7A22KV5RQNVTNBUNQGCT6WGGXFIDJQQ",
            "198314229091350324001CGQ7N6HHYQ2UO7UJKRENDGDSEMTGX4M2KKJK4ZVFNNBIZVPNBZXNLUO6JR4TR656GITM2KFQSIDRMASDXNEAIFGLMOPEOPIEPHEK3ULQCNNOTWNQG2SFWOW5AR3J2EWAI",
            "1983142290913803240012DQEZYWMGPK3Y6V7RW26FZCNWIQM5Z4Z4WUIUU2ZBXCFK2AIHMJQHJU7XY2DY2JVABXRT7XUE3B5ZSOQVFC53BGCIHNAHO3LXUDTJZC4N3NSTC4QIXE7G5PGHAMDSBGYI",
            "198314229091480324001OUMOAD7BI374PY2CMF6XV6H6ZYHC5X4CHZYQGJPILBHH66TMWD2ZG2GND5QHWRI574TWD7MAPT357ZAL4U3JBQO5IT3UY7WHURQHXSYHMEXOAODUINQL523RZKAABLEHY",
            "198314229091510324001BNOYYUCICNK73JZHKRILOIS7II3C6ZV2ZWEQXHM5DGZ2QTE2JA744DR4CACRPPF2NFOYA5BTGW7J4Z4S4G3CRQTVWAGRFQOSRO4BA6GWG5C5UIXAPLMXTMB62XCWJVNWI",
            "198314229091560324001TWH643HY6F3GUCUCPKBYTBBQGIDW4WW5JZBLWJTYHJLWJGQII6Q5XPW2YDNJESNR6Z2IFGA5SHT3ANPQ2ZGVEFJLIE6DZNS6NYGBLELDI3YRU6Q3VEHZA5DXNIWWQ3NFQ",
            "198314229091570324001OYGSSXTHACWFOQPR46QKX6ADQEGAK5N3HCHZWD22FENA5BAFK7BRMD3HTRYEFGGNIGQTR3IHMVLZETJ2OOOTUCR5CK3KI4ZXG7XOANN3QTKLKABFX6R47Q3V77H4ELB5Q"
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
                "FullName": "Акционерное общество \\"Архангельский ликеро-водочный завод\\"",
                "ShortName": "АО \\"АЛВИЗ\\""
            }
        },
        "quantity": 13
    },
    {
        "price": "355.54",
        "FARegId": "FA-000000055361455",
        "F2RegId": "FB-000007604782392",
        "AlcCode": "0100000002700000031",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"Архангельская Северная выдержка\\"",
        "ShortName": null,
        "marks": [
            "18732625134181072400166VBBH6KXHPBBSNW5QNDFEOUZU2JAAYHVLYDABDJGSCX3LT2FJYBIMX55NTSQ7YEYAKIYGSUKXN6TXJ63VFYT47IKL6TQG4Z6W5CZUAY5JDXHMOL6MMLR7CGTKASZOG4Y",
            "187326251341820724001THHHITO3RO4DK34EQD2JCYIR64QCX6R6B34GDI7CRQZ7P6C4YJJ7IVV72UJRE7WSA3PVWTVTYMZRHYT6HOK3DVKKVGXQII6TN3E3SFSU7DV3KPQYYU3Y22TJYXHHFGZJY",
            "187326251341840724001WMSQ7UZSMDQLVKWRCIE35XZKYI2GSKHB7QZSHHH35RQKWREHDTTE5F2WSHH4BI2DHXHNKEWBF3VAMXKRJLMP54CYN7QSLPDEV6M7K2GWXYMZ53LIB4U6GBTARDTLM7BBY",
            "187326251341880724001WDZ76FSZL6JEDR6PP2I3NTXQMQ2M3PJWTRNC6CUWYELZYTXIE3IEJZ66ZQ5LSDMZ7CH2VQ3OBY2B7AKY44ZTG76FSSQUBPVMOPUZIETFW7KF6VUM6MQHAAQNSFNKQOH5A",
            "1873262513419107240016P55KGIMAXZDAY64XKEOCBZPIUU6YIZR5OQM2CTESEFPQBX3AQTN5OZLDHVB4PZZDBZSB2WHZIU22FET6MRTFYZ76A2LJC4XV3CYVGXFGK5HJ6DRUV3SCMWSZ4NKMIXLA",
            "187326251341920724001OMFPE64VKG6M3BUBOLF2WNGHIYCIJ2OAQOWGGEGMJ7TMUSFBTGB3MSZKXXH7WZED5R2F55S7DLS2NR254M4ZQR7J4V54JNWJ2TYW4GEH3D67TKAY2Y3NCOLSM7A472XVA",
            "187326251341940724001VCKCJS6IQTYBSUAYZEYGOZFCHAIDO6VXCEZOKFUCUWDJU2DYAYD3KIPXNH2UZ5LCOAPAS5OIO52DRRQ2XS2M3MOSX7VB3Z4ULILEOPGEAXF447CO3ENLFBQFHHUF7MQ4A",
            "187326251341950724001ZOHHLHVLZDZK6LSHULZHLQDDXI4M3WI6HHZFCTWY6HY3M7CZOCCPH2GAZCMWUY34GLZYPM7XWQAWKZKGLZQLHEH7ATVCJXLML4LFQUAYJXVCVAMKRIQKJIOTZ5GSK3TYI",
            "187326251341970724001CJHMSGAYM6MLF7KOGNYLT7NKRE6OQMFFSMARPQON7DLA6KWE7VFODMEBPQQVQY5JIEFZ62NFK7J7CKQFEAHHDYNGRQZO6AMFI3UXVDHY5QG4FPMGTVRCGX67MOXQLWDPY"
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
                "FullName": "Акционерное общество \\"Архангельский ликеро-водочный завод\\"",
                "ShortName": "АО \\"АЛВИЗ\\""
            }
        },
        "quantity": 9
    },
    {
        "price": "330.50",
        "FARegId": "FA-000000054655271",
        "F2RegId": "FB-000007604782393",
        "AlcCode": "0100000003130000173",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка \\"БЕЛЕНЬКАЯ ЛЮКС\\"",
        "ShortName": null,
        "marks": [
            "187421360949740823001KWH7BOVSTITKBNAXI3V3ADF364AWUQUTXCK63YWRG7AOVKF4C3PQQU6XDNIHUJHHP2ONWW2L5PAOCIQ3BDONAHP46THYU23YCARAKAV5DKFZM2LPWLTGP2EFQGM7APSBY",
            "187421360949760823001EHWBXKF5RDIHG5TRS6ZU5B5BOYPR37OHD27JEHQCKDR63N5ACP5SRCMXUJSAIW4XSOQM4XCOSR7VOBXZKN5ZHW5REMMD2MXJDJMIVIWPXNQLKGB4UOUB6HILTHSSBUK6Q",
            "1874213692596308230015ZAK4DNVW6I43RVQCULALGMQWEWMZTOFN6JPRLYZOIXGQV3G6OXWOVVAGWRSFQ3F5MO3FMPOV6XYYVICL34SCUR5ATVLUC7MTYYR6JYFNY3PYRMVSTWNMSW2DJMCK5YRQ",
            "187421369259680823001YR2RA2TIQO5RUSL65NVYEOAXGE2355ZKKGJGVU5YV4UQWXPHIQE4LJIBEIVFT2DDASJJBD5YTISNQT3XE5P7USHJYOOZ7LIYVYZNLGVMCSGLNVXPFGK3DVPL3JAGO5NDA",
            "187421369259690823001VDP2TKAO3IQCI72L2DVUKXQ4MUPUVAPQ4IHFGHHSDK4LSJQTNXKMOVPDZYZJPW3GQ7IMYEGWVPAXZNJPMUJZX7XI5HQBKWGR4KWNKYNYPOVZXBKC3LF2A7KFBVTHMHOZY"
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
                "FullName": "Акционерное общество \\"Бастион осн. 1942 г.\\"",
                "ShortName": "АО \\"Бастион\\""
            }
        },
        "quantity": 5
    },
    {
        "price": "299.00",
        "FARegId": "FA-000000054824367",
        "F2RegId": "FB-000007604782394",
        "AlcCode": "0100606942420000005",
        "Capacity": "0.500",
        "AlcVolume": "38.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПУЗЫРЁК» МЯГКАЯ",
        "ShortName": null,
        "marks": [
            "187429369744550724001AGYM3ZTZKDSRGHHM67QUH6TGSYOUNC5HBSZOEOHVOGJT4AT4SVATMN6SJFBRSBYR7DX65BJWQU455OXHONPN4ZWDPQO5VHKZGDVVKTQ5TNMVDG5SAZXAD2YPOSPFCVPAA",
            "187429369744610724001AO5W5W7M6OTB7HYQ7Y7G7NJI6YSQEKGV2KSHU4BMJFKHQQRXRIU2WK7E4TZFIC4BWPU2EVG5RSBY6OBUZ3ZCKYC7FVPDPOINOQJ44TBYRVSHPQDVKPZ5JQNIML4KGN4NI",
            "187429369744630724001GCSZPADQU5F4JESL57H77NHEOARL3UW5ATJW5JPNYPPLRR2XLQAOMNEV4GCKIRMRJU2TS24B5DVAAKOKOQMXDPHWVTDVUT7ZDPA3ZYDTQMQZUBHFE2OCFRXWPN4IULWSY",
            "187429369744640724001HH5AHY4MOI3YNAPNC54GNXF7DAW3XY7DFDEDEY733JG4L2PJHDGC7CBZUYQU5HVCXXL7CDVYCUSRPWHAWYBSG25HXX5APNBGIM6MYTBBBLYKVVQW6UN47KH27LKUZJM2Y",
            "187429369744650724001SXOCZYJG4OFEPUATS4NLWGBYQEOEMJFE3GBA4ISHWSGMXE45FY5SZE3RREYSCVA5GAQRB4NUUHNMTQHOKUTULYHV5MHEV7W7KPYWBC5D35TY5NFLMGAFUDYZPJN5VJORY",
            "187429369744660724001NP24RS6DRLXFZTQHQPF2JJXT3YZCPLMDH2MNSTHG7SLTCSVKNERNYXLOOHUPXF7CKZHXGIKEZE6W5SKGRE4FQIUH2VEJ4NLB56VFHQQAV2UYMPGSVPXLFQDTISEGFVBRA",
            "187429369744670724001XYLSZZA5WCTI7LCRF7WDEQSPZMT2LQR6UWHTISQQYAS7NJGFQ6X36U3DMIXTLZXCFCC3YGM4E44BIGBMQ6HDUFPDMM35YEMSFZS4HXYTCMDXWVJYBEWCJUIASJFEPQPIY",
            "187429369744680724001TFYAGBIUKH7BIXFNJ7CW6HHSNQDP6NYQTXPCPHSV32SL45ZFJXZJBZ2OPGTLVSSUYC3ECP7PLFDPTIQRUQKEFIZYQSIUKLFBFIOCBQ54JPHOVBVIRX5CHSWHBMWPIW5EA",
            "187429369744700724001HJBR4ZLYU6RV3C2R6CMNWWSN4E6PGLRWKZQKPKY4OJ4MAQAZWR4NHM77M4GII3ZVEAOKFLVDTTJURK4T34P3X7NQP7KV3V5YBZ2VLDCAEA53A3KPVXS47SSR5FFI7XA7I",
            "187429369744710724001C57GWJ4DN7WCUA4M4OHD5H7CDQCPQSOO7XGUQ2OG5U57TGUYLLKMSOJCPYGRINQV6RSIOSOFKOUPPLMJHLVZFLVLQUF6K3S56JOYGCNRDM6GHCMIMPJZ34M42YYDN2TEY",
            "187429369744720724001LNBXKX53DXBFA6SLQXBRXTSTQAZOYQ5BVZGTRFBZNWWHBEUZTIKAJUXLKNI4T34BTG47NB4457HKU2OHQEMMKINWAVM22GBJXSGG26WPTOJXKBBTPSVSVSBSDQJPNJY2I",
            "187429369744730724001HSO6UQ4G246ELAAJ2UA2JC7DDELGPBKHAFZZ3MLJMYAKU4U2BLTT4CBHMOICSISZCYBWF3TDVT2K2VZSQJXVRD6OID57Y2A3BGGYRDGCRNPXCULUBK36VNXBEDQ2BN5AY",
            "187429369744740724001HZTON5YRBB4VRF4RTGJPWGTYJ4T3UQNBXSJQIQGGELFEDGIXYPPHJDDKT22PBC5R5IECW33Y7D3DZ4JW4PUE6YUDXSRZHBOPP36JEBDXF6WAJF7IY2ECUQEHYVGEPTK3I",
            "187429369744770724001TH3W7T4KDQ5SENYTPO3OLZN7YQHOHLCH4RGUXER5IOYDBX6P45SORTQFICV754U6754ZEO5Y7OFGL4VXQWJRGFMUFOEW5NN2I2KHROAZW5OARIANVURMWIIMPPPCUHVDI",
            "187429369744810724001L6E246GPZPXAJFLQ7JLAPNUE3Y3XUGWYJHWAOSRP7F7OJAJZWUGYFGKIHEHOLQIO4HB4GCN36RDNUXYD4HKUWBHUOT4OL6R5QU5HYHOXTJOKW3F2G5IXQ3VGRZGJVIXCY",
            "187429369744820724001HCNBZAF3C44UCBMOUR5YXYDJVAHWXTSZ66EP3GHOZI4XWBQAJPMDFZNLGWU37UBT5Z3RSMLVXZUYSQBCO25V35SXCLYZHG3TUBD4YKVVBAVXPFJJLWIQBQEOALC75MAJI",
            "187429369744840724001L4SAOP3NSEL2JXYKQPMW4M4R3AQ5OSS356NSTTYXPWEOJK6SWIAUFGHUL5OK7YXTLUNBMUBUGLE6OFPQX4P5GV74OG5GDBYIKQNVHP5GTPWTNCKH6GEZXWUCKTNE2XSFI"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 17
    },
    {
        "price": "68.00",
        "FARegId": "FA-000000055144172",
        "F2RegId": "FB-000007604782395",
        "AlcCode": "0100606942420000119",
        "Capacity": "0.100",
        "AlcVolume": "40.000",
        "ProductVCode": "200",
        "FullName": "Водка «ПШЕНИЧНАЯ»",
        "ShortName": null,
        "marks": [
            "197407664091610424001NSC4564DMPWJDTQI6ZPRTEMIQEWK3QDXOR6XOLQ6QPURFWZYZ6G4ENEI7GQ5XEBKAFHHXADEUT6QFSBWNQJPM2UEI2UHMTR4OW2EPWHT2IWJLOQVICVKFF5MXKDUQIR5Q",
            "197407664091620424001ZFHJ5CWYRMLXX7JAWPYNNDEPEQVEQMJZPYLERXIKP3DHWZDJXLXLWHEVNDU4PA5DM44X2NY3GCDRPH36AIHLHO2P56CTP7PAD2KH6Q4MQLYA4C46TCPQFXRHA2TGS3SGI",
            "197407664091630424001MT2WQEJZ7ED63KXV4ICX2L2WVYZZSK2ABBI7EZGI44QR3HH3JPUSBGSHFTSSFJDE2F43DKXGJ4OG3FLAVYPBLKVTSYQQQ73JHY76EVIQP7HRD4SBAJIGLOSWCBXHWRN4Q",
            "197407664091660424001XZUMFUHGXAGZPJ7TMMHYYFKZOQ4ND63DMG4EUEIM4B4F5TL7W3R6UMCB7CDQF2Y44XKONEMSX4FVQ3JRBLSFVRYYVQMWXAXPQFBEYY27VRDA5OFFT24GBZWLMUJDDPORY",
            "197407664091680424001AZFZVTFBOVSTLY7DK6D62GMZO4X3LDIZJN3WQVGAD6FMGXCPQ4OQEM4BAHHR3Y2IDSHY7Y4PW6CKW45BMXU6KSZOOMEJIUUSBVGUTLNKOKPOJF7MKQ5BBQRXCDVJHC4IA",
            "1974076640916904240012VLE4N2Q2BXEH7FW5XVFH3OC74JQT4ON2YYCXJYQMH4XQ5DFM35JTXZFPKZHYUPOY6HPAJ3LG5I7HOWA74M2DGUIVOPYPAWH3ZPG5UCVEARV6IWYTKLJZA4ONRH7W5XVY",
            "1974076640917004240014ELBPYSI7NNUDSKZTOH72FA23MZKVI6N5QUCYAF7LFKWY4JPHVGC7JS6SVP35TQ7MTHKLGBWX56LNKJSACNNCYWOBXOI5U6XF4DAJYWG6WN6ZDVBE6SMHIJA4XR2RO2EY",
            "197407664091710424001GMMS4TI7Q6KUT2VFGN5FRHIFL4W3P3DPPGU45OTE6XVS4F5LRQYDMOBGZ2RSVKGHUCBFVXQTZXRCELILKD56I4NYLQOOZJKVAORN74HQLLQQQOMTWT5Q6AC6BIALYTWYI",
            "197407664091720424001XDSP62G6REMW72B4H7XKAGFGGYYCPPUFISXSNM3RG5MMSYDTE23MHOCRUPNGMDYKD7FP5H2VEL2T5YI5KGBPSWWJATB4EAIONK6EUP3GJQGXC2PKQ6EB4LK5B6KJWRQMQ",
            "197407664091730424001IGOC63652VEQIZRICPHGXE4JGU22IK77AKDIXMN7L34G6DYL3XKWFZAWQ3MH6VYH2YWO4336EPFKPEDQLAE2WTZFZDBS5ZGO5RQF7HABKWAAPLUP43C4MXT3MF4F6IMVQ",
            "197407664091740424001OICW55ATSFWGBPNI7UDS6MU4YUPFN2DN45VTNEBRWWXQY7LWRA24XU6B6F33OH253O2ZJOZFWSSCZKGQWJV3NNJU6KNLRJLRJWZEZWNOY7ZLXIMZSHRXSCDNR7VOSZZMQ",
            "197407664091750424001JKHWGPX7CQHDLYJYYP7PQO24BITQQGLAEK5P3GPP67DLKOFYCZGKXF4WWNDJFVQ34COFQTIWXPGHTUGIR3P5PZUK6M4TFIYQHHS2ZPZ5H5P3MBSVTKCQ32OAZT7Y7LNJQ",
            "197407664091760424001UMMZEP2LZQZT4CWJK5VFYDM6LYCOY4463TY7JCVQYH423QJFKAUDO77HG2WEL42BHS6W73LIFV57LX64TV3LTOMG3PBI4SSJVHQCZTPQDOMNABPD3GJUMD3SPTIXBEQCY",
            "197407664091770424001PFNYSZXXHDYIJILCPM3ON4OUBQ66YBEH3GJ54ES7JSZUDBTVWOOTXAC43XHZUDUVTAE6LFTHBBTQ62HU3Y2YJ4I5MPUXYKBUWWPOFGSKKOIQ5SN7XEW4DKZ3JBV6VIR5A",
            "197407664091780424001CNHQECKHPIZOGK52SOTEFMVK3UM2PQIF56SOOQXCZ3IC4PSWGHK6YNODF5FZLODMQATIYQJDDKNEXRUJ3DXBZHI53NBAJP3BU54N75QI3RMSAVDWV4523XTIJ3A462RAI",
            "197407664091790424001YPP4S64RV5MUISFA2L4AEK7SQE7N5FOP3WBHRCIVNVFCMVHSPNESGJWKR6D4X5GVPNPOEI2373ZR34W5EJG7WYTGOW6ED4X6ZVG6HGI7VKZ7XNLRLHVB2EIYL4HIMM7JQ",
            "197407664091800424001Z7BRBMINX7M7746PWAB5CHVZGYVDKG2RVJYQS3GRCC7BVIDNSWVW43ZU2EBJDG4OPGC2CJEGKH3GUMNPZCXBGIC77H73TCT2MPV6RFHHUGBW4A3DNAN22P3IF57VZ7QBI",
            "197407664091810424001W4TMIPS6CKZ3LU4YXE54EKA63IR4G3MCCO5AJCPBUCEEUVTFVMT3XEHXMZDIILTZZ3H6Y6TKKIK63NTWMSDOJ7W7V4EYAZHYI4SHZGPFRP4OWJHQC5ZSABWBVVUQRQECQ"
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
                "FullName": "Общество с ограниченной ответственностью \\"Чебоксарский ликеро-водочный завод\\"",
                "ShortName": "ООО \\"ЧЛВЗ\\""
            }
        },
        "quantity": 18
    },
    {
        "price": "439.00",
        "FARegId": "FA-000000055093922",
        "F2RegId": "FB-000007604782396",
        "AlcCode": "0100000004440000136",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски пятилетний зерновой \\"Макинтош\\"",
        "ShortName": null,
        "marks": [
            "187325073415990224001IFEAWXQBO5XXP3OHDSPUFSB7SIECBTLH3LFL6QJJPA4DELC553D7RSJ6ZFILKT75P27SROPMX4R735NE7UHFSQAQJRHUDSVJR4KSNPRJUDDZEGV4BIXGBYY6ZBOFDLTYY",
            "187325073416000224001YGVOPLNODJ3OXN56F7M3NIAY4AMCRP5UMXWFT5YIVSJ46433B237LRUO2IKFRHSGRSKTZH5LO77VN44EOYEFZ25CUYZWYVRHQWMJDCE5ENUWDPSWHUA3APOFE2563FX6A",
            "187325073416040224001ALEBQMIAIMODJVWAICQVEEM2IADYIRBQOTWGL4ENEF43QV7ZM2WYOVIKGHPGIJ2MCCYSPZVWECWHKDPWQSX6J3FMXY4K2XPHNWYNSFK4QSJRDXMCNDVM3PA3DNNLURUKY",
            "187325073416050224001AMBIODMHJOGXBVIHFIQNYOVRWEREXDK7AHZYB23VQELUQGMCPE6SQMPE7Q5E4RPGZKJEJDUJLFPW2ABX4GSNQHZ7N4JKLURLQAU5AWHQURYDTKTQLXIMIBBQJ7IXIHVOQ",
            "1873250734160602240017K3DDUS2J57METQT55XFNOZ7BECUSQP4SQGCHR4K6EYCXR5A44FKIR5KTDOZJPCRMIF3CLGUAG6G7HKZV5EEBRJJ7ISKM2YG42LVCNI2MWSLWPVSK6UZWOEKID3GIWYMI",
            "187325073416070224001YV56P2BUXRTSRK7CXFZ47MTP5UEQUURPMLNLL4KFSZ5E6GOH2XOJDCBUZWSST3U5Q7UVROMNOWRLDAFRAFZBQKNSYTAW6654O6Z6CIV7VVAEMMGC3BYQ3QVT76DGD3O4Y"
        ],
        "Producer": {
            "UL": {
                "address": {
                    "Country": "643",
                    "description": "Россия,,Ставропольский Край,Буденновский Район,,Красный Октябрь Село,Победы Улица,,9 | в том числе: винохранилище № 5 (S=1419,0 кв.м, кадастровый № 26:20:000000:2829); винохранилище № 6 (секции выдержки дистиллятов) (S=390,3 кв.м, кадастровый № 26:20:000000:2825) | в том числе: склад готовой продукции (S=667,9 кв.м,кадастровый номер 26:20:180203:139); склад готовой продукции № 2 (S=1438,8 кв.м, кадастровый номер 26:20:180203:148); винохранилище № 5 (S=1419,0 кв.м, кадастровый № 26:20:000000:2829)",
                    "RegionCode": "26"
                },
                "INN": "2624022986",
                "KPP": "262401001",
                "ClientRegId": "010000000444",
                "FullName": "Открытое акционерное общество Агрофирма \\"Жемчужина Ставрополья\\"",
                "ShortName": "ОАО АФ \\"Жемчужина Ставрополья\\""
            }
        },
        "quantity": 6
    },
    {
        "price": "352.64",
        "FARegId": "FA-000000055111799",
        "F2RegId": "FB-000007604782397",
        "AlcCode": "0100000004970000182",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски КУПАЖИРОВАННЫЙ «ФОКС ЭНД ДОГС»",
        "ShortName": null,
        "marks": [
            "198417418710520924001XXXNH6TYX3POXE37VZ4VBTGIEIQVHM36BOKHPHBF3JZGTGY5PWPSMEOKX7IGABZAUXZVCGZGZSTIVORO7LEXTCL3FPUAXBOPSDJDZOKTEXZGPJWZ3NSELJL7SQUMWB55Y",
            "19841741871053092400157GLXXGNHNEY3XM3QNK6VKMQGUJ6S6F3G757KRKFNUYL6YEUJLPMACAZGDSWEE5UUZ5XRHNBAT2KEBYZTSV7EGNPOMRNA644SJC7O6RXFEKCFTBHSG4SBQHMWQNQ3KYCA"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "508.50",
        "FARegId": "FA-000000053065516",
        "F2RegId": "FB-000007604782398",
        "AlcCode": "0100000004970000298",
        "Capacity": "0.500",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски купажированный \\"ФОКС ЭНД ДОГС СМОКИ БАРРЕЛ\\"",
        "ShortName": null,
        "marks": [
            "187425259476541123001HJCPBHQEH3P4JTKFSVXLSMPF6Y642OORPWHPVGZTGYUWKPDE3UVWPEQGGYP4KOESEL5HICGU4WBYL3ZPXETKQS6PAJTQRN7FGBVBV3CSLS5NENIZ7W3FMX4KIFRUT3CLI",
            "187425259476561123001BCDQMXTOVGFLFYAXRLFPRK6RV4DLRJZB3LDPU3IRSXOFCGSSB7Y5HH7UNAGH6IYAH5Z73ZGEGEHP3QI2EEAEAOSRJFGTHE4I72MUW6KOXP2NLFSJQLJMI4NFOQPCHRD5A"
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
                "FullName": "Общество с ограниченной ответственностью \\"Завод Георгиевский. Традиции качества\\"",
                "ShortName": "ООО \\"Георгиевский\\""
            }
        },
        "quantity": 2
    },
    {
        "price": "228.00",
        "FARegId": "FA-000000055028288",
        "F2RegId": "FB-000007604782399",
        "AlcCode": "0100000005390000208",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски российский купажированный ординарный «ФАЭР ЭНД ВУД»",
        "ShortName": null,
        "marks": [
            "198414413139550124001YDIEYGGEUCC3F423RN3ML2XBRQWBKSNC2O4PSMUCSVP5GS367GMBCXFGL3O6EYKOYLD3TQ2GYA57P5D7AMUH6IPKFNWSVDS2KUMZ55T35PBJVHIC3BVJT4PKFVJJDUM5I",
            "198414413139580124001ODSE7TQJYLCVWJIM7RKDRFCVPQ6FTTF32Y5S4BX2IKFZABTYJQEPXUCCTPD3UMHQGSQZOPLGXEKRFTPILXNMXQAGRQU3FFH7VGPRECBXBQQB6COHVLEAXA4NE7CJRDRQY",
            "198414413139610124001CLP3ARCIBKHBNISCOL3XQCALCI5ZWQWZXEF4TTQIMQ6OUTFKX7W27L2HU7BDNVXXKI652BOEY7T267OWRYFX6SQ6VYOLUR66T7XGDX6DW5B5MC2FTSQQ6I4OWQ2EOLG5Y"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 3
    },
    {
        "price": "225.00",
        "FARegId": "FA-000000055153434",
        "F2RegId": "FB-000007604782400",
        "AlcCode": "0100000001740001189",
        "Capacity": "0.700",
        "AlcVolume": "9.000",
        "ProductVCode": "4011",
        "FullName": "Вино полусладкое белое \\"Татьянин день\\"",
        "ShortName": null,
        "marks": [
            "192316095542470124001J3GBFREWTFOEHYUVCZSRMJH36ALFXY5KM2A7QIM6IDALOQBJ4WVMISUBC24IRZJG2OPFXFJPHSXIIODLHL74S6LESCJG6BPRKQ5RHQXBLIESMOIEGYUCSWIZ2HSR67UFA"
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
                "FullName": "Общество с ограниченной ответственность \\"Долина\\"",
                "ShortName": "ООО \\"Долина\\""
            }
        },
        "quantity": 1
    },
    {
        "price": "228.00",
        "FARegId": "FA-000000055028288",
        "F2RegId": "FB-000007604782401",
        "AlcCode": "0100000005390000208",
        "Capacity": "0.250",
        "AlcVolume": "40.000",
        "ProductVCode": "237",
        "FullName": "Виски российский купажированный ординарный «ФАЭР ЭНД ВУД»",
        "ShortName": null,
        "marks": [
            "198414413182780124001Q323XHFCB4ZMP2RZ7BNZUHRKQ4BXF6ZE6ZDHZGZH2SVYLNWSYUKKPUXKW3UA2LGPZSR3JXXCMVAGM6INBYKNPICKML2AX3BF23ZP2NPDKN7ZY2CBS37VSACX3YNNQCRAQ",
            "198414413182800124001A3G2MZDOV3HF6G4W2WKWNTMJHIH7GB4DNXMUZ2IXGFIPNVMVUSVLBZEIKQ622RV4I3RIDXEQITNJTFAGXGLMG5NTO4C5KYUAXPTBAXZFDZGX6VIRUM5YBWHG5AGVF6VRI"
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
                "FullName": "Акционерное общество \\"Татспиртпром\\"",
                "ShortName": "АО филиал АО \\"Татспиртпром\\" \\"Vigrosso\\""
            }
        },
        "quantity": 2
    }
]"""

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
        positions = []
        positions = json.loads(s)

        shipper = ooo_dionis_tupak48
        consignee = ooo_dionis_tupak55

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

        waybill_v4('http://tupak48:8080', '030000575119', shipper, consignee, transport, positions, "19", 'Договор №103 от 16.07.2024')


class TestEgaisAction(unittest.TestCase):
    def __test_send_rest_bcode(self, ):
        get_actions(fsrar_id='030000543922', url="http://localhost:8015/file/", utm_url='http://localhost:8082')

    def __test_x(self):
        params = {'fsrar_id': '030000543922', 'action': 'store_sign', 'id': 1, 'transport_id': '90813081-144c-4512-aa28-972f61f8a90d', 'sign': '4DC19C9C13A67E277BB81EBA3577629244522657CC89A171EB2AC85F2B84753B05C7BA2BF0E84C40EA3B7FD145F2B9B2612BEFC3249C70CEB70993D6C97293C2'}
        q = requests.post("http://localhost:8015/file/", params=params)

class TestAct4(unittest.TestCase):
    def __test_act4(self,):
        utm_url = 'http://localhost:8088'
        fsrar_id = get_fsrar_id(utm_url)
        act4(utm_url, fsrar_id, 'TTN-0780899048', False)

# params = {'fsrar_id': fsrar_id, 'action': 'get_actions'}
# q = requests.post("https://kirsa.9733.ru/file/", params=params)
# assert q.status_code == 200

class TestQueryBCode(unittest.TestCase):
    def __test_query_bcode(self,):
        utm_url = 'http://oct2:8080'
        query_bcode(utm_url, fsrar_id=get_fsrar_id(utm_url), fb='FB-000005196978883')

if __name__ == "__main__":
    unittest.main()
