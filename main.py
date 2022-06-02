import datetime
import xml.etree.ElementTree as ET
import xml.dom.minidom
import argparse
import time
import requests

from egais import create_accept_act_v4, send_query, parse_simple_response, create_query_resend_doc, get_fsrar_id, resend_doc, act3, act4, query_rests_v2, query_bcode
from parseRestShop import parse_rests_v2

parser = argparse.ArgumentParser()
parser.add_argument('--cmd', help='command like resend, act')
parser.add_argument('--ttn', help='ttn')
parser.add_argument('--fb', help='fb')
parser.add_argument('--utm-url', help='utm_url')
args = parser.parse_args()

fsrar_id = get_fsrar_id(args.utm_url)

if args.cmd == 'resend':
    q = resend_doc(args.utm_url, fsrar_id, args.ttn)
elif args.cmd == 'act3':
    q = act3(args.utm_url, fsrar_id, args.ttn)
elif args.cmd == 'act4':
    q = act4(args.utm_url, fsrar_id, args.ttn)
elif args.cmd == 'rests':
    q = query_rests_v2(args.utm_url, fsrar_id)
elif args.cmd == 'bcode':
    q = query_bcode(args.utm_url, fsrar_id, args.fb)

#assert q.status_code == 200
#print(q.text)


def get_document_by_guid(guid):
    i = 0
    while (True):
        i += 1
        if i > 20:
            break
        print("attempt {}".format(i))
        q = requests.get("{}/opt/out".format(args.utm_url))
        assert q.status_code == 200
        root = ET.fromstring(q.text)
        for url in root.findall('url'):
            if url.attrib and 'replyId' in url.attrib and url.attrib['replyId'] == guid:
                print(url.text)
                q = requests.get(url.text)
                assert q.status_code == 200
                return q.text

guid, sign = parse_simple_response(q.text)
print(get_document_by_guid(guid))

#guid = '6ac54137-27c4-4d23-95d2-4fd117a355ce'
#parse_rests_v2(get_document_by_guid(guid))
