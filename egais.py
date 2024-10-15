import datetime
import json
import xml
import xml.dom.minidom
import xml.etree.ElementTree as ET
import requests
from lxml import etree

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
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


def create_waybill_act_v4(fsrar_id, act_number, act_date, wb_reg_id, note, missed_amc=None, rejected=False):
    doc = Doc(fsrar_id)

    wa_namespace = "http://fsrar.ru/WEGAIS/ActTTNSingle_v4"
    ce_namespace = "http://fsrar.ru/WEGAIS/CommonV3"
    ET.register_namespace('wa', wa_namespace)
    ET.register_namespace('ce', ce_namespace)

    waybill_act = ET.SubElement(doc.document, "ns:WayBillAct_v4")
    header = ET.SubElement(waybill_act, "{%s}Header" % wa_namespace)
    if rejected:
        ET.SubElement(header, "wa:IsAccept").text = 'Rejected'
    else:
        ET.SubElement(header, "wa:IsAccept").text = 'Accepted' if missed_amc is None else 'Differences'
    ET.SubElement(header, "wa:ACTNUMBER").text = act_number
    ET.SubElement(header, "wa:ActDate").text = act_date
    ET.SubElement(header, "wa:WBRegId").text = wb_reg_id
    ET.SubElement(header, "wa:Note").text = note
    content = ET.SubElement(waybill_act, "wa:Content")
    if missed_amc is not None:
        for missed in missed_amc:
            position = ET.SubElement(content, "wa:Position")
            ET.SubElement(position, "wa:Identity").text = str(missed['identity'])
            ET.SubElement(position, "wa:InformF2RegId").text = missed['inform_f2_reg_id']
            ET.SubElement(position, "wa:RealQuantity").text = str(missed['real_quantity'])
            if 'amc' in missed:
                mark_info = ET.SubElement(position, "wa:MarkInfo")
                for mark in missed['amc']:
                    ET.SubElement(mark_info, "{%s}amc" % ce_namespace).text = mark
    transport = ET.SubElement(waybill_act, "wa:Transport")
    ET.SubElement(transport, "wa:ChangeOwnership").text="NotChange"
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


def add_shipper(header, shipper):
    oref_namespace = "http://fsrar.ru/WEGAIS/ClientRef_v2"
    ET.register_namespace("oref", oref_namespace)
    c = ET.SubElement(header, "wb:Shipper")
    ul = ET.SubElement(c, "{%s}UL" % oref_namespace)
    ET.SubElement(ul, "oref:ClientRegId").text = shipper['ClientRegId']
    ET.SubElement(ul, "oref:INN").text = shipper['INN']
    ET.SubElement(ul, "oref:KPP").text = shipper['KPP']
    ET.SubElement(ul, "oref:FullName").text = shipper['FullName']
    ET.SubElement(ul, "oref:ShortName").text = shipper['ShortName']
    address = ET.SubElement(ul, "oref:address")
    ET.SubElement(address, "oref:Country").text = shipper['address']['Country']
    ET.SubElement(address, "oref:RegionCode").text = shipper['address']['RegionCode']
    ET.SubElement(address, "oref:description").text = shipper['address']['description']


def add_consignee_ul(header, consignee):
    oref_namespace = "http://fsrar.ru/WEGAIS/ClientRef_v2"
    ET.register_namespace("oref", oref_namespace)
    c = ET.SubElement(header, "wb:Consignee")
    ul = ET.SubElement(c, "{%s}UL" % oref_namespace)
    ET.SubElement(ul, "oref:ClientRegId").text = consignee['ClientRegId']
    ET.SubElement(ul, "oref:INN").text = consignee['INN']
    ET.SubElement(ul, "oref:KPP").text = consignee['KPP']
    ET.SubElement(ul, "oref:FullName").text = consignee['FullName']
    ET.SubElement(ul, "oref:ShortName").text = consignee['ShortName']
    address = ET.SubElement(ul, "oref:address")
    ET.SubElement(address, "oref:Country").text = consignee['address']['Country']
    ET.SubElement(address, "oref:RegionCode").text = consignee['address']['RegionCode']
    ET.SubElement(address, "oref:description").text = consignee['address']['description']


def add_consignee_fl(header, consignee):
    oref_namespace = "http://fsrar.ru/WEGAIS/ClientRef_v2"
    ET.register_namespace("oref", oref_namespace)
    c = ET.SubElement(header, "wb:Consignee")
    ul = ET.SubElement(c, "{%s}FL" % oref_namespace)
    ET.SubElement(ul, "oref:ClientRegId").text = consignee['ClientRegId']
    ET.SubElement(ul, "oref:INN").text = consignee['INN']
    ET.SubElement(ul, "oref:FullName").text = consignee['FullName']
    ET.SubElement(ul, "oref:ShortName").text = consignee['ShortName']
    address = ET.SubElement(ul, "oref:address")
    ET.SubElement(address, "oref:Country").text = consignee['address']['Country']
    ET.SubElement(address, "oref:RegionCode").text = consignee['address']['RegionCode']
    ET.SubElement(address, "oref:description").text = consignee['address']['description']


def add_transport(header, transport):
    oref_namespace = "http://fsrar.ru/WEGAIS/ClientRef_v2"
    ET.register_namespace("oref", oref_namespace)
    tran = ET.SubElement(header, "wb:Transport")
    ET.SubElement(tran, "wb:ChangeOwnership").text = 'NotChange'
    ET.SubElement(tran, "wb:TRAN_TYPE").text = transport['TRAN_TYPE']
    ET.SubElement(tran, "wb:TRANSPORT_TYPE").text = transport['TRANSPORT_TYPE']
    ET.SubElement(tran, "wb:TRAN_COMPANY").text = transport['TRAN_COMPANY']
    ET.SubElement(tran, "wb:TRANSPORT_REGNUMBER").text = transport['TRANSPORT_REGNUMBER']
    ET.SubElement(tran, "wb:TRAN_CUSTOMER").text = transport['TRAN_CUSTOMER']
    ET.SubElement(tran, "wb:TRAN_DRIVER").text = transport['TRAN_DRIVER']
    ET.SubElement(tran, "wb:TRAN_LOADPOINT").text = transport['TRAN_LOADPOINT']
    ET.SubElement(tran, "wb:TRAN_UNLOADPOINT").text = transport['TRAN_UNLOADPOINT']
    ET.SubElement(tran, "wb:TRAN_FORWARDER").text = transport['TRAN_FORWARDER']


def add_producer(product, data):
    producer = ET.SubElement(product, "pref:Producer")  # pos['Producer']
    if 'UL' in data:
        xl = ET.SubElement(producer, "oref:UL")
        data_xl = data['UL']
        ET.SubElement(xl, "oref:INN").text = data_xl['INN']
        ET.SubElement(xl, "oref:KPP").text = data_xl['KPP']
    elif 'FO' in data:
        xl = ET.SubElement(producer, "oref:FO")
        data_xl = data['FO']
    elif 'TS' in data:
        xl = ET.SubElement(producer, "oref:TS")
        data_xl = data['TS']
    else:
        raise Exception("unknown producer type")
    ET.SubElement(xl, "oref:ClientRegId").text = data_xl['ClientRegId']
    ET.SubElement(xl, "oref:FullName").text = data_xl['FullName']
    ET.SubElement(xl, "oref:ShortName").text = data_xl['ShortName']
    address = ET.SubElement(xl, "oref:address")
    ET.SubElement(address, "oref:Country").text = data_xl['address']['Country']
    if 'UL' in data:
        ET.SubElement(address, "oref:RegionCode").text = data_xl['address']['RegionCode']
    ET.SubElement(address, "oref:description").text = data_xl['address']['description']


def create_waybill_v4(fsrar_id, number, identity, date, note, shipper, consignee, transport, positions, base):
    doc = Doc(fsrar_id)

    wb_namespace = "http://fsrar.ru/WEGAIS/TTNSingle_v4"
    ce_namespace = "http://fsrar.ru/WEGAIS/CommonV3"
    pref_namespace = "http://fsrar.ru/WEGAIS/ProductRef_v2"
    ET.register_namespace('pref', pref_namespace)
    ET.register_namespace('wb', wb_namespace)
    ET.register_namespace('ce', ce_namespace)

    waybill = ET.SubElement(doc.document, "ns:WayBill_v4")
    ET.SubElement(waybill, "{%s}Identity" % wb_namespace).text = identity
    header = ET.SubElement(waybill, "wb:Header")
    ET.SubElement(header, "wb:NUMBER").text = number
    ET.SubElement(header, "wb:Date").text = date
    ET.SubElement(header, "wb:ShippingDate").text = date
    ET.SubElement(header, "wb:Type").text = "WBInvoiceFromMe"
    ET.SubElement(header, "wb:Note").text = note
    ET.SubElement(header, "wb:Base").text = base
    add_shipper(header, shipper)
    add_consignee_ul(header, consignee)
    add_transport(header, transport)
    content = ET.SubElement(waybill, "wb:Content")
    i = 1
    for pos in positions:
        position = ET.SubElement(content, "wb:Position")
        ET.SubElement(position, "wb:Identity").text = str(i)
        ET.SubElement(position, "wb:Quantity").text = str(pos['quantity'])
        ET.SubElement(position, "wb:Price").text = str(pos['price'])
        #ET.SubElement(position, "wb:Pack_ID").text = pos['pack_id']
        #ET.SubElement(position, "wb:Party").text = pos['party']
        ET.SubElement(position, "wb:FARegId").text = pos['FARegId']
        inform_f2 = ET.SubElement(position, "wb:InformF2")
        ET.SubElement(inform_f2, "{%s}F2RegId" % ce_namespace).text = pos["F2RegId"]
        mark_info = ET.SubElement(inform_f2, "ce:MarkInfo")
        boxpos = ET.SubElement(mark_info, "ce:boxpos")
        amclist = ET.SubElement(boxpos, "ce:amclist")
        for m in pos['marks']:
            ET.SubElement(amclist, "ce:amc").text = m

        i += 1
        product = ET.SubElement(position, "wb:Product")
        ET.SubElement(product, "{%s}AlcCode" % pref_namespace).text = pos['AlcCode']
        ET.SubElement(product, "pref:UnitType").text = 'Packed'
        ET.SubElement(product, "pref:Type").text = 'АП'
        ET.SubElement(product, "pref:Capacity").text = pos['Capacity']
        ET.SubElement(product, "pref:AlcVolume").text = pos['AlcVolume']
        ET.SubElement(product, "pref:FullName").text = pos['FullName']
        ET.SubElement(product, "pref:ShortName").text = pos['ShortName']
        add_producer(product, pos['Producer'])
        ET.SubElement(product, "pref:ProductVCode").text = pos['ProductVCode']

    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


def validate_xml(xml_str):
    xmlschema = etree.XMLSchema(etree.parse("./xsd/WB_DOC_SINGLE_01.xsd"))

    try:
        xmlschema.assertValid(etree.fromstring(xml_str))
    except etree.DocumentInvalid as e:
        print("Validation error(s):")
        for error in xmlschema.error_log:
            print("  Line {}: {}".format(error.line, error.message))
        raise e


def create_act_write_off_v3(fsrar_id, act_number, act_date, wb_reg_id, note, missed_amc=None):
    doc = Doc(fsrar_id)

    wa_namespace = "http://fsrar.ru/WEGAIS/ActTTNSingle_v4"
    ce_namespace = "http://fsrar.ru/WEGAIS/CommonV3"
    awr_namespace = "http://fsrar.ru/WEGAIS/ActWriteOff_v3"
    ET.register_namespace('wa', wa_namespace)
    ET.register_namespace('ce', ce_namespace)
    ET.register_namespace('awr', awr_namespace)

    act_wroiteoff = ET.SubElement(doc.document, "ns:ActWriteOff_v3")
    ET.SubElement(act_wroiteoff, "{%s}Identity" % awr_namespace).text = '1'
    header = ET.SubElement(act_wroiteoff, "{%s}Header" % wa_namespace)
    ET.SubElement(header, "awr:ActNumber").text = act_number
    ET.SubElement(header, "awr:ActDate").text = act_date
    ET.SubElement(header, "awr:TypeWriteOff").text = 'Недостача'
    ET.SubElement(header, "awr:Note").text = note
    content = ET.SubElement(act_wroiteoff, "wa:Content")
    if missed_amc is not None:
        for missed in missed_amc:
            position = ET.SubElement(content, "wa:Position")
            ET.SubElement(position, "wa:Identity").text = str(missed['identity'])
            ET.SubElement(position, "wa:InformF2RegId").text = missed['inform_f2_reg_id']
            ET.SubElement(position, "wa:RealQuantity").text = str(missed['real_quantity'])
            if 'amc' in missed:
                mark_info = ET.SubElement(position, "wa:MarkInfo")
                for mark in missed['amc']:
                    ET.SubElement(mark_info, "{%s}amc" % ce_namespace).text = mark
    transport = ET.SubElement(act_wroiteoff, "wa:Transport")
    ET.SubElement(transport, "wa:ChangeOwnership").text="NotChange"
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")

'''
<?xml version="1.0" encoding="UTF-8"?>
<ns:Documents Version="1.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:ns= "http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"
	xmlns:pref="http://fsrar.ru/WEGAIS/ProductRef_v2"
	xmlns:awr="http://fsrar.ru/WEGAIS/ActWriteOff_v3"
	xmlns:ce="http://fsrar.ru/WEGAIS/CommonV3"
>
	<ns:Owner>
		<ns:FSRAR_ID>010000000435</ns:FSRAR_ID>
	</ns:Owner>
	<ns:Document>
		<ns:ActWriteOff_v3>
			<awr:Identity>456</awr:Identity>
			<awr:Header>
				<awr:ActNumber>10</awr:ActNumber>
				<awr:ActDate>2015-10-08</awr:ActDate>
				<awr:TypeWriteOff>Недостача</awr:TypeWriteOff>
				<awr:Note>текст комментария</awr:Note>
			</awr:Header>
			<awr:Content>
				<awr:Position>
					<awr:Identity>1</awr:Identity>
					<awr:Quantity>4</awr:Quantity>
					<awr:InformF1F2>
						<awr:InformF2>
							<pref:F2RegId>FB-000000000000304</pref:F2RegId>
						</awr:InformF2>
					</awr:InformF1F2>
					<awr:MarkCodeInfo>
						<ce:amc>09001785400000118984310PX8051522100000476712617218613594213116182124151</ce:amc>
						<ce:amc>09001785400000118984310PX8051522100000476712617218613594213116182124152</ce:amc>
						<ce:amc>09001785400000118984310PX8051522100000476712617218613594213116182124153</ce:amc>
						<ce:amc>09001785400000118984310PX8051522100000476712617218613594213116182124154</ce:amc>
					</awr:MarkCodeInfo>
				</awr:Position>
				<awr:Position>
					<awr:Identity>2</awr:Identity>
					<awr:Quantity>1</awr:Quantity>
					<awr:InformF1F2>
						<awr:InformF2>
							<pref:F2RegId>FB-000000000000305</pref:F2RegId>
						</awr:InformF2>
					</awr:InformF1F2>
					<awr:MarkCodeInfo>
						<ce:amc>09001785400000118984310PX8051522100000476712617218613594213116182124155</ce:amc>
					</awr:MarkCodeInfo>
				</awr:Position>
			</awr:Content>
		</ns:ActWriteOff_v3>
	</ns:Document>
</ns:Documents>
'''


def create_write_off_shop_v2(fsrar_id, identity, act_number, act_date, note, xtype, positions=None,):
    doc = Doc(fsrar_id)

    awr_namespace = "http://fsrar.ru/WEGAIS/ActWriteOffShop_v2"
    ce_namespace = "http://fsrar.ru/WEGAIS/CommonV3"
    pref_namespace = "http://fsrar.ru/WEGAIS/ProductRef_v2"

    ET.register_namespace('awr', awr_namespace)
    ET.register_namespace('ce', ce_namespace)
    ET.register_namespace('pref', pref_namespace)

    write_off = ET.SubElement(doc.document, "ns:ActWriteOffShop_v2")
    ET.SubElement(write_off, "awr:Identity").text = identity
    header = ET.SubElement(write_off, "{%s}Header" % awr_namespace)
    ET.SubElement(header, "awr:ActNumber").text = act_number
    ET.SubElement(header, "awr:ActDate").text = act_date
    ET.SubElement(header, "awr:TypeWriteOff").text = xtype
    ET.SubElement(header, "awr:Note").text = note
    content = ET.SubElement(write_off, "awr:Content")

    i = 1
    for p in positions:
        position = ET.SubElement(content, "awr:Position")
        ET.SubElement(position, "awr:Identity").text = str(i)
        ET.SubElement(position, "awr:Quantity").text = str(p['quantity'])
        product = ET.SubElement(position, "awr:Product" )
        ET.SubElement(product, "{%s}UnitType"% pref_namespace).text = 'Packed'
        ET.SubElement(product, "pref:Type").text = 'АП'
        ET.SubElement(product, "pref:FullName").text = p['FullName']
        ET.SubElement(product, "pref:ShortName").text = None
        ET.SubElement(product, "pref:AlcCode").text = p['AlcCode']
        ET.SubElement(product, "pref:AlcVolume").text = p['AlcVolume']
        ET.SubElement(product, "pref:Capacity").text = p['Capacity']
        ET.SubElement(product, "pref:ProductVCode").text = p['ProductVCode']

        '''
                        <pref:UnitType>Packed</pref:UnitType>
						<pref:Type>АП</pref:Type>
						<pref:FullName>Коньяк "Вершины Кавказа" 5-ти летний 1.0000 л.</pref:FullName>
						<pref:ShortName />
						<pref:AlcCode>0017878000001312143</pref:AlcCode>
						<pref:Capacity>1.000</pref:Capacity>
						<pref:ProductVCode>АП</pref:ProductVCode>'''

        marks = ET.SubElement(position, "awr:MarkCodeInfo")
        for m in p['marks']:
            ET.SubElement(marks, "MarkCode").text = m

        i += 1
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


def create_write_off_v3(fsrar_id, identity, act_number, act_date, note, xtype, positions=None,):
    doc = Doc(fsrar_id)

    awr_namespace = "http://fsrar.ru/WEGAIS/ActWriteOff_v3"
    ce_namespace = "http://fsrar.ru/WEGAIS/CommonV3"
    pref_namespace = "http://fsrar.ru/WEGAIS/ProductRef_v2"

    ET.register_namespace('awr', awr_namespace)
    ET.register_namespace('ce', ce_namespace)
    ET.register_namespace('pref', pref_namespace)

    write_off = ET.SubElement(doc.document, "ns:ActWriteOff_v3")
    ET.SubElement(write_off, "awr:Identity").text = identity
    header = ET.SubElement(write_off, "{%s}Header" % awr_namespace)
    ET.SubElement(header, "awr:ActNumber").text = act_number
    ET.SubElement(header, "awr:ActDate").text = act_date
    ET.SubElement(header, "awr:TypeWriteOff").text = xtype
    ET.SubElement(header, "awr:Note").text = note
    content = ET.SubElement(write_off, "awr:Content")

    i = 1

    for p in positions:
        position = ET.SubElement(content, "awr:Position")
        ET.SubElement(position, "awr:Identity").text = str(i)
        ET.SubElement(position, "awr:Quantity").text = str(p['quantity'])
        inform_f1_f2 = ET.SubElement(position, "awr:InformF1F2" )
        inform_f2 = ET.SubElement(inform_f1_f2, "awr:InformF2")
        ET.SubElement(inform_f2, "{%s}F2RegId"  % pref_namespace).text = p['F2RegId']
        marks = ET.SubElement(position, "awr:MarkCodeInfo")
        for m in p['marks']:
            ET.SubElement(marks, "{%s}amc" % ce_namespace).text = m

        i += 1
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


def create_query_resend_doc(fsrar_id, ttn):
    doc = Doc(fsrar_id)

    wa_namespace = "http://fsrar.ru/WEGAIS/ActTTNSingle_v4"
    ET.register_namespace('wa', wa_namespace)

    query_resend_doc = ET.SubElement(doc.document, "ns:QueryResendDoc")
    qps = doc.append_parameters(query_resend_doc)
    doc.append_parameter(qps, "WBREGID", ttn)

    #tree.write("./egais_cheques/{}-{}.xml".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), kassa), encoding="UTF-8", xml_declaration=True)
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


def create_query_nattn(fsrar_id,):
    doc = Doc(fsrar_id)
    query_nattn = ET.SubElement(doc.document, "ns:QueryNATTN")
    qps = doc.append_parameters(query_nattn)
    doc.append_parameter(qps, "КОД", fsrar_id)
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


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
    xml_str = ET.tostring(ET.ElementTree(doc.documents).getroot(), encoding="UTF-8", xml_declaration=True, )
    validate_xml(xml_str)
    return xml_str.decode("utf-8")


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


def act4(utm_url, fsrar_id, ttn, reject=False):
    global handmade
    missed_amc = None
    #missed_amc = list()
    #missed_amc.append({'identity': '1', 'inform_f2_reg_id': 'FB-000006573519268', 'real_quantity': 899,})
    #missed_amc.append({'identity': '2', 'inform_f2_reg_id': 'FB-000006573519269', 'real_quantity': 828,})
    xml_str = create_waybill_act_v4(fsrar_id,
                                   "000018",
                                    datetime.datetime.now().strftime("%Y-%m-%d"),
                                    ttn,
                                    handmade,
                                    missed_amc,
                                    reject,
                                    )
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "WayBillAct_v4")


def write_off_shop_v2(utm_url, fsrar_id, positions):
    global handmade
    # missed_amc = list()
    # missed_amc.append({'identity': 146485104, 'inform_f2_reg_id': 'FB-000005796838897', 'real_quantity': 0,})

    xml_str = create_write_off_shop_v2(fsrar_id,
                                       "1",
                                       "000017",
                                       datetime.datetime.now().strftime("%Y-%m-%d"),
                                       handmade,
                                       "Порча",  # '[Пересортица, Недостача, Уценка, Порча, Потери, Проверки, Арест, Иные цели, Реализация, Производственные потери]'. It must be a value from the enumeration
                                       positions,
                                    )
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    # return send_query(xml_str, utm_url, "WayBillAct_v4")

def write_off_v3(utm_url, fsrar_id, positions, act_number):
    global handmade
    # missed_amc = list()
    # missed_amc.append({'identity': 146485104, 'inform_f2_reg_id': 'FB-000005796838897', 'real_quantity': 0,})

    xml_str = create_write_off_v3(fsrar_id,
                                  "1",
                                  act_number,
                                  datetime.datetime.now().strftime("%Y-%m-%d"),
                                  handmade,
                                  # "Недостача",  # '[Пересортица, Недостача, Уценка, Порча, Потери, Проверки, Арест, Иные цели, Реализация, Производственные потери]'. It must be a value from the enumeration
                                  "Недостача",
                                  positions,
                                  )
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "ActWriteOff_v3")


def waybill_v4(utm_url, fsrar_id, shipper, consignee, transport, positions, number, base):
    global handmade
    xml_str = create_waybill_v4(fsrar_id,
                                number,
                                "1",
                                datetime.datetime.now().strftime("%Y-%m-%d"),
                                handmade,
                                shipper,
                                consignee,
                                transport,
                                positions,
                                base,
                               )
    # fsrar_id, number, identity, date, note, positions
    # fsrar_id, act_number, act_date, wb_reg_id, note, missed_amc=None, rejected=False
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "WayBill_v4")

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


def query_check_bcodes(utm_url, fsrar_id, fn):
    doc = Doc(fsrar_id)

    qf_namespace = "http://fsrar.ru/WEGAIS/QueryFilter"
    ET.register_namespace('', qf_namespace)

    #header = ET.SubElement(waybill_act, "{%s}Header" % wa_namespace)

    qf = ET.SubElement(doc.document, "ns:QueryFilter")
    with open(fn) as file:
        for line in file:
            if line and line.strip():
                ET.SubElement(qf, "{%s}bc" % (qf_namespace)).text = line.strip()

        tree = ET.ElementTree(doc.documents)
        xml_str = ET.tostring(tree.getroot(), encoding="UTF-8", xml_declaration=True, ).decode("utf-8")
        print(xml.dom.minidom.parseString(xml_str).toprettyxml())
        return send_query(xml_str, utm_url, "QueryFilter")


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


def get_actions(fsrar_id, url="https://kirsa.9733.ru/file/", utm_url='http://localhost:8080'):
    params = {'fsrar_id': fsrar_id, 'action': 'get_actions'}
    q = requests.post(url, params=params)
    assert q.status_code == 200
    data = json.loads(q.text)
    for x in data:
        action = x['action']
        if action == 'act4':
            q = act4(utm_url, fsrar_id, x['wbreg_id'])
            assert q.status_code == 200
            transport_id, sign, = parse_simple_response(q.text)
            params = {'fsrar_id': fsrar_id, 'action': 'store_sign', 'id': x['id'], 'transport_id': transport_id,
                      'sign': sign}
            q = requests.post(url, params=params)
            print(x)
            print(q.text)
        elif action == 'nattn':
            q = nattn(utm_url, fsrar_id)
            assert q.status_code == 200
            transport_id, sign, = parse_simple_response(q.text)
            params = {'fsrar_id': fsrar_id, 'action': 'store_sign', 'id': x['id'], 'transport_id': transport_id,
                      'sign': sign}
            q = requests.post(url, params=params)
            print(x)
            print(q.text)
        elif action == 'writeoff_v3':
            params = json.loads(x['params'])
            print(params)
            q = write_off_v3(utm_url, fsrar_id, params['positions'], params['number'])
            assert q.status_code == 200
            transport_id, sign, = parse_simple_response(q.text)
            params = {'fsrar_id': fsrar_id, 'action': 'store_sign', 'id': x['id'], 'transport_id': transport_id, 'sign': sign}
            q = requests.post(url, params=params)
            print(x)
            print(q.text)
        elif action == 'wb4':
            params = json.loads(x['params'])
            q = waybill_v4(utm_url, fsrar_id, params['shipper'], params['consignee'], params['transport'],
                           params['positions'], params['number'], params['base'])
            assert q.status_code == 200
            transport_id, sign, = parse_simple_response(q.text)
            params = {'fsrar_id': fsrar_id, 'action': 'store_sign', 'id': x['id'], 'transport_id': transport_id, 'sign': sign}
            q = requests.post(url, params=params)
            print(x)
            print(q.text)
        else:
            raise Exception("unknown action")

