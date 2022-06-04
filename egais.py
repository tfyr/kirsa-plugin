import datetime
import xml
import xml.etree.ElementTree as ET
import requests

ns_namespace = "http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"
handmade = "Создано вручную, с любовью и вниманием к деталям."

class Doc:
    """Базовый документ ЕГАИС"""
    def __init__(self, fsrar_id):
        global ns_namespace
        ET.register_namespace('ns', ns_namespace)
        self.fsrar_id = fsrar_id
        documents_name = "{%s}Documents" % (ns_namespace,)
        self.documents = ET.Element(documents_name)
        self.owner = ET.SubElement(self.documents, "ns:Owner")
        el_fsrar_id = ET.SubElement(self.owner, "ns:FSRAR_ID")
        el_fsrar_id.text = self.fsrar_id
        self.document = ET.SubElement(self.documents, "ns:Document")
        # self.tree = ET.ElementTree(documents)

    @staticmethod
    def append_parameters(el):
        qp_namespace = "http://fsrar.ru/WEGAIS/QueryParameters"
        ET.register_namespace('qp', qp_namespace)
        return ET.SubElement(el, "{%s}Parameters" % (qp_namespace))

    @staticmethod
    def append_parameter(el, name, value):
        p = ET.SubElement(el, "qp:Parameter")
        ET.SubElement(p, "qp:Name").text = name
        ET.SubElement(p, "qp:Value").text = value


def get_fsrar_id(utm_url):
    q = requests.get("{}/diagnosis".format(utm_url),)
    assert q.status_code == 200
    root = ET.fromstring(q.text)
    return root.find("CN").text

def create_accept_act_v2(fsrar_id, act_number, act_date, wb_reg_id, note):
    doc = Doc(fsrar_id)

    wa_namespace = "http://fsrar.ru/WEGAIS/ActTTNSingle_v2"
    ET.register_namespace('wa', wa_namespace)

    waybill_act = ET.SubElement(doc.document, "ns:WayBillAct_v2")
    header = ET.SubElement(waybill_act, "{%s}Header" % wa_namespace)
    ET.SubElement(header, "wa:IsAccept").text = 'Accepted'
    ET.SubElement(header, "wa:ACTNUMBER").text = act_number
    ET.SubElement(header, "wa:ActDate").text = act_date
    ET.SubElement(header, "wa:WBRegId").text = wb_reg_id
    ET.SubElement(header, "wa:Note").text = note
    ET.SubElement(waybill_act, "wa:Content")
    tree = ET.ElementTree(doc.documents)
    return ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")


def create_accept_act_v3(fsrar_id, act_number, act_date, wb_reg_id, note):
    wa_namespace = "http://fsrar.ru/WEGAIS/ActTTNSingle_v3"
    ET.register_namespace('wa', wa_namespace)
    doc = Doc(fsrar_id)
    waybill_act = ET.SubElement(doc.document, "ns:WayBillAct_v3")
    header = ET.SubElement(waybill_act, "{%s}Header" % wa_namespace)
    ET.SubElement(header, "wa:IsAccept").text = 'Accepted'
    ET.SubElement(header, "wa:ACTNUMBER").text = act_number
    ET.SubElement(header, "wa:ActDate").text = act_date
    ET.SubElement(header, "wa:WBRegId").text = wb_reg_id
    ET.SubElement(header, "wa:Note").text = note
    ET.SubElement(waybill_act, "wa:Content")
    tree = ET.ElementTree(doc.documents)
    return ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")


def create_accept_act_v4(fsrar_id, act_number, act_date, wb_reg_id, note):
    doc = Doc(fsrar_id)

    wa_namespace = "http://fsrar.ru/WEGAIS/ActTTNSingle_v4"
    ET.register_namespace('wa', wa_namespace)

    waybill_act = ET.SubElement(doc.document, "ns:WayBillAct_v4")
    header = ET.SubElement(waybill_act, "{%s}Header" % wa_namespace)
    ET.SubElement(header, "wa:IsAccept").text = 'Accepted'
    ET.SubElement(header, "wa:ACTNUMBER").text = act_number
    ET.SubElement(header, "wa:ActDate").text = act_date
    ET.SubElement(header, "wa:WBRegId").text = wb_reg_id
    ET.SubElement(header, "wa:Note").text = note
    ET.SubElement(waybill_act, "wa:Content")
    transport = ET.SubElement(waybill_act, "wa:Transport")
    ET.SubElement(transport, "wa:ChangeOwnership").text="NotChange"
    tree = ET.ElementTree(doc.documents)
    return ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")


def create_query_resend_doc(fsrar_id, ttn):
    doc = Doc(fsrar_id)

    wa_namespace = "http://fsrar.ru/WEGAIS/ActTTNSingle_v4"
    ET.register_namespace('wa', wa_namespace)

    query_resend_doc = ET.SubElement(doc.document, "ns:QueryResendDoc")
    qps = doc.append_parameters(query_resend_doc)
    doc.append_parameter(qps, "WBREGID", ttn)

    tree = ET.ElementTree(doc.documents)
    #tree.write("./egais_cheques/{}-{}.xml".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), kassa), encoding="UTF-8", xml_declaration=True)
    return ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")


def create_query_nattn(fsrar_id,):
    doc = Doc(fsrar_id)
    query_nattn = ET.SubElement(doc.document, "ns:QueryNATTN")
    qps = doc.append_parameters(query_nattn)
    doc.append_parameter(qps, "КОД", fsrar_id)
    tree = ET.ElementTree(doc.documents)
    return ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")


'''
<?xml version="1.0" encoding="UTF-8"?>
<ns:Documents Version="1.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"
xmlns:qp="http://fsrar.ru/WEGAIS/QueryParameters">
84<ns:Owner>
<ns:FSRAR_ID>030000194005</ns:FSRAR_ID>
</ns:Owner>
<ns:Document>
<ns:QueryNATTN>
<qp:Parameters>
<qp:Parameter>
<qp:Name>КОД</qp:Name>
<qp:Value>030000194005</qp:Value>
</qp:Parameter>
</qp:Parameters>
</ns:QueryNATTN>
</ns:Document>
</ns:Documents>
'''

def create_query_request_rests(fsrar_id):
    doc = Doc(fsrar_id)
    ET.SubElement(doc.document, "ns:QueryRests_v2")
    tree = ET.ElementTree(doc.documents)
    return ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")


def send_query(str_xml, utm_url, service):
    files = dict()
    files['xml_file'] = ("query.xml", str_xml, 'text/xml')

    headers = {'Content-Disposition': 'attachment'}
    # headers = {'Content-Type': 'multipart/form-data',}
    params = [('title', 'xml_file'),]
    ret = requests.post("{}/opt/in/{}".format(utm_url, service),
                        files=files,
                        headers=headers,
                        params=params)
    return ret


def parse_simple_response(text):
    root = ET.fromstring(text)
    return root.find('url').text, root.find('sign').text


def resend_doc(utm_url, fsrar_id, ttn):
    xml_str = create_query_resend_doc(fsrar_id, ttn)
    return send_query(xml_str, utm_url, "QueryResendDoc")


def nattn(utm_url, fsrar_id,):
    xml_str = create_query_nattn(fsrar_id,)
    return send_query(xml_str, utm_url, "QueryNATTN")


def act3(utm_url, fsrar_id, ttn):
    global handmade
    xml_str = create_accept_act_v3(fsrar_id,
                                   "000017",
                                   datetime.datetime.now().strftime("%Y-%m-%d"),
                                   ttn,
                                   handmade)
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "WayBillAct_v3")


def act4(utm_url, fsrar_id, ttn):
    global handmade
    xml_str = create_accept_act_v4(fsrar_id,
                                   "000017",
                                   datetime.datetime.now().strftime("%Y-%m-%d"),
                                   ttn,
                                   handmade)
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "WayBillAct_v4")


def query_rests_v2(utm_url, fsrar_id,):
    global handmade
    xml_str = create_query_request_rests(fsrar_id)
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "QueryRests_v2")


def bcode(fsrar_id, fb):
    'FB-000004599103758'
    doc = Doc(fsrar_id)
    qr = ET.SubElement(doc.document, "ns:QueryRestBCode")

    qps = doc.append_parameters(qr)
    doc.append_parameter(qps, "ФОРМА2", fb)

    tree = ET.ElementTree(doc.documents)
    return ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")


def query_bcode(utm_url, fsrar_id, fb):
    global handmade
    xml_str = bcode(fsrar_id, fb)
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "QueryRestBCode")



def xxx():
    from kirsa.models import Income, TuAlco, IncomePosAlco
    # et = ET.parse(fn)
    root = ET.fromstring(xml)
    # root = et.getroot()
    my_namespaces = dict([
        node for _, node in ET.iterparse(
            BytesIO(xml), events=['start-ns']
        )
    ])
    document = root.find('ns:Document', my_namespaces)
    products = document.find('ns:ReplyRests_v2/rst:Products', my_namespaces)
    # income = Income.objects.create(date='2022-05-06', reason_id=3, host_id=3, agent_id=1132, answer_id=None, sklad_id=sklad_id, total=0)
    # income.save()
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

        print(short_name.text if short_name else full_name)
        print("    Алкокод: " + alco_code)
        print("    Кол-во: " + quantity)
        print("    inform_a_reg_id: " + inform_a_reg_id)
        print("    inform_b_reg_id: " + inform_b_reg_id)
        try:
            tua = TuAlco.objects.get(extsource=3, extcode=alco_code)
            tua.capacity = capacity
        except TuAlco.DoesNotExist:
            raise Exception("not found")
        #    tua = TuAlco(name=short_name.text if short_name else full_name, beauty_name=full_name, extsource=3,
        #                 extcode=alco_code, category_id=162, capacity=capacity,
        #                 volume=alc_volume)
        #    tua.save()
        # inc_pos_alco = IncomePosAlco(income=income, amount=quantity, price=tua.price if tua.price else 0, tu_id=tua.id, inform_a_reg=inform_a_reg_id, inform_b_reg=inform_b_reg_id)
        # inc_pos_alco.save()


