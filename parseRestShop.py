import xml.etree.ElementTree as ET
from decimal import Decimal
from io import BytesIO, StringIO


def parse_rests_v2(xml):
    fn = 'ReplyRests_v2.xml'
    et = ET.parse(fn)
    #root = et.getroot()
    #et = ET.fromstring(xml)
    root = et


    my_namespaces = dict([
        node for _, node in ET.iterparse(
            # fn,
            StringIO(xml),
            events=['start-ns']
        )
    ])
    document = root.find('ns:Document', my_namespaces)
    products = document.find('ns:ReplyRests_v2/rst:Products', my_namespaces)
    # income = Income.objects.create(date='2022-05-06', reason_id=3, host_id=3, agent_id=1132, answer_id=None, sklad_id=sklad_id, total=0)
    # income.save()
    x = 0
    y = Decimal(0)
    for position in products.findall('rst:StockPosition', my_namespaces):
        quantity = position.find('rst:Quantity', my_namespaces).text
        inform_a_reg_id = position.find('rst:InformF1RegId', my_namespaces).text
        inform_b_reg_id = position.find('rst:InformF2RegId', my_namespaces).text
        product = position.find('rst:Product', my_namespaces)
        full_name = product.find("pref:FullName", my_namespaces).text
        short_name = product.find("pref:ShortName", my_namespaces)
        alco_code = product.find('pref:AlcCode', my_namespaces).text
        capacity = product.find('pref:Capacity', my_namespaces).text
        alc_volume = product.find('pref:AlcVolume', my_namespaces).text
        vcode = product.find('pref:ProductVCode', my_namespaces).text


        if vcode.startswith("2"):
            print(short_name.text if short_name else full_name)
            print("    Алкокод: " + alco_code)
            print("    Кол-во: " + quantity)
            print("    inform_a_reg_id: " + inform_a_reg_id)
            print("    inform_b_reg_id: " + inform_b_reg_id)
            x += 1
            y += Decimal(quantity)
            # IncomePosAlco

#        try:
#            tua = TuAlco.objects.get(extsource=3, extcode=alco_code)
#            tua.capacity = capacity
#        except TuAlco.DoesNotExist:
#            raise Exception("not found")
    print(x, y)


parse_rests_v2(None)