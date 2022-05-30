import xml.etree.ElementTree as ET
import xml.dom.minidom
import argparse
import time
import requests

from egais import get_fsrar_id

parser = argparse.ArgumentParser()
parser.add_argument('--utm-url', help='utm_url')
parser.add_argument('--sklad-id', help='sklad-id')
args = parser.parse_args()

fsrar_id = get_fsrar_id(args.utm_url)

q = requests.get("{}/opt/out".format(args.utm_url))
assert q.status_code == 200
root = ET.fromstring(q.text)

files = dict()
for url in root.findall('url'):
    print(url.text)
    q = requests.get(url.text)
    assert q.status_code == 200
    files[url.attrib['replyId']] = q.text


# headers = {'Content-Disposition': 'attachment'}
#headers = {'Content-Type': 'multipart/form-data',}
#params = [('title', 'Waybill_v4.xml'), ('sklad_id', args.sklad_id)]
params = {'fsrar_id': args.sklad_id}
ret = requests.post("https://kirsa.9733.ru/file/",
                    files=files,
#                    headers=headers,
                    params=params)
print(ret)

