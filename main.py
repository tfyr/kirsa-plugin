import datetime
import xml.etree.ElementTree as ET
import xml.dom.minidom
import argparse
import time
import requests

from egais import create_accept_act_v4, send_query, parse_simple_response, create_query_resend_doc, get_fsrar_id


def resend_doc(utm_url, fsrar_id, ttn):
    xml_str = create_query_resend_doc(fsrar_id, ttn)
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "QueryResendDoc")


def act(utm_url, fsrar_id, ttn):
    xml_str = create_accept_act_v4(fsrar_id,
                                   "000017",
                                   datetime.datetime.now().strftime("%Y-%m-%d"),
                                   ttn,
                                   "Создано вручную, с любовью и вниманием к деталям.")
    print(xml.dom.minidom.parseString(xml_str).toprettyxml())
    return send_query(xml_str, utm_url, "WayBillAct_v4")


parser = argparse.ArgumentParser()
parser.add_argument('--cmd', help='command like resend, act')
parser.add_argument('--ttn', help='ttn')
parser.add_argument('--utm-url', help='utm_url')
args = parser.parse_args()

fsrar_id = get_fsrar_id(args.utm_url)

if args.cmd == 'resend':
    q=resend_doc(args.utm_url, fsrar_id, args.ttn)
elif args.cmd == 'act':
    q=act(args.utm_url, fsrar_id, args.ttn)

assert q.status_code == 200
print(q.text)

guid, sign = parse_simple_response(q.text)

i = 0
exit = False
while (not exit):
    i += 1
    if i > 20:
        break
    time.sleep(15)
    print("attempt {}".format(i))
    q = requests.get("{}/opt/out".format(args.utm_url))
    assert q.status_code == 200
    root = ET.fromstring(q.text)
    for url in root.findall('url'):
        if url.attrib and 'replyId' in url.attrib and url.attrib['replyId'] == guid:
            print(url.text)
            q = requests.get(url.text)
            assert q.status_code == 200
            exit = True
            print(q.text)
            break
