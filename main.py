import xml.etree.ElementTree as ET
import xml.dom.minidom
import argparse
import time

import requests

class Doc:

    """Базовый документ ЕГАИС"""
    def __init__(self, fsrar_id):
        self.fsrar_id = fsrar_id
        global ns_namespace
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


ns_namespace = "http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"
ET.register_namespace('ns', ns_namespace)

def create_accept_act_v2(fsrar_id, act_number, act_date, wb_reg_id, note):
    doc = Doc(fsrar_id)

    global ns_namespace
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
    #tree.write("./egais_cheques/{}-{}.xml".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), kassa), encoding="UTF-8", xml_declaration=True)
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
    #tree.write("./egais_cheques/{}-{}.xml".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), kassa), encoding="UTF-8", xml_declaration=True)
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


def send_accept_act_v4(fsrar_id, ttn):
    str_xml = create_accept_act_v4(fsrar_id, "0001004", "2022-05-15", ttn, "Создано вручную, с любовью и вниманием к деталям.")
    print(str_xml)

    files=dict()
    files['xml_file'] = ("WayBillAct_v4.xml", str_xml, 'text/xml')

    headers = {'Content-Disposition': 'attachment'}
    # headers = {'Content-Type': 'multipart/form-data',}
    params = [('title', 'xml_file'),]
    ret = requests.post("{}/opt/in/{}".format(utm_url, service),
                        files=files,
                        headers=headers,
                        params=params)
    return ret

# print(send_accept_act_v2())

def send_query(str_xml, utm_url, service):
    files=dict()
    files['xml_file'] = ("query.xml", str_xml, 'text/xml')

    headers = {'Content-Disposition': 'attachment'}
    # headers = {'Content-Type': 'multipart/form-data',}
    params = [('title', 'xml_file'),]
    ret = requests.post("{}/opt/in/{}".format(utm_url, service),
                        files=files,
                        headers=headers,
                        params=params)
    return ret


parser = argparse.ArgumentParser()
parser.add_argument('--fsrar-id', help='fsrar_id')
parser.add_argument('--ttn', help='ttn')
parser.add_argument('--utm-url', help='utm_url')
args = parser.parse_args()

#xml_str = create_query_resend_doc(args.fsrar_id, args.ttn)
xml_str = create_accept_act_v4(args.fsrar_id, "000017", "2022-05-15", args.ttn, "Создано вручную, с любовью и вниманием к деталям.")
print(xml.dom.minidom.parseString(xml_str).toprettyxml())

#q = send_query(xml_str, args.utm_url, "QueryResendDoc")
q = send_query(xml_str, args.utm_url, "WayBillAct_v4")
assert q.status_code == 200
print(q.text)

root = ET.fromstring(q.text)
guid = root.find('url').text

i = 0
exit = False
while (not exit):
    i += 1
    if i > 10:
        break
    time.sleep(5)
    print("attempt {}".format(i))
    q = requests.get("{}/opt/out".format(args.utm_url))
    assert q.status_code == 200
    root = ET.fromstring(q.text)
    for url in root.findall('url'):
        if url.attrib and 'replyId' in url.attrib and url.attrib['replyId'] == guid:
            print(url.text)
            q = requests.get(url.text)
            assert q.status_code == 200
            print(q.text)
            exit = True
            break



