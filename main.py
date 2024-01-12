# import datetime
# import json
import xml.etree.ElementTree as ET
# import xml.dom.minidom
import argparse
import time
import requests

from egais import parse_simple_response, get_fsrar_id, resend_doc, act3, act4, query_rests_v2, query_bcode, nattn, query_check_bcodes

parser = argparse.ArgumentParser()
parser.add_argument('--cmd', help='command like resend, act')
parser.add_argument('--ttn', help='ttn')
parser.add_argument('--fb', help='fb')
parser.add_argument('--fn', help='filename')
parser.add_argument('--utm-url', help='utm_url')
args = parser.parse_args()

utm_url = args.utm_url or 'http://localhost:8080'

fsrar_id = get_fsrar_id(utm_url)

if args.cmd == 'resend':
    q = resend_doc(utm_url, fsrar_id, args.ttn)
elif args.cmd == 'nattn':
    q = nattn(utm_url, fsrar_id)
elif args.cmd == 'act3':
    q = act3(utm_url, fsrar_id, args.ttn)
elif args.cmd == 'act4':
    q = act4(utm_url, fsrar_id, args.ttn)
elif args.cmd == 'rests':
    q = query_rests_v2(utm_url, fsrar_id)
elif args.cmd == 'bcode':
    q = query_bcode(utm_url, fsrar_id, args.fb)
elif args.cmd == 'check-bcodes':
    q = query_check_bcodes(utm_url, fsrar_id, args.fn)
    print(q.text)

#assert q.status_code == 200
#print(q.text)


def get_document_by_guid(guid):
    i = 0
    while (True):
        i += 1
        if i > 20:
            break
        print("attempt {}".format(i))
        q = requests.get("{}/opt/out".format(utm_url))
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

