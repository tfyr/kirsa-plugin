import json
import re
import xml.etree.ElementTree as ET
import xml.dom.minidom
import argparse
import time
import requests

from egais import get_fsrar_id, get_actions

parser = argparse.ArgumentParser()
parser.add_argument('--utm-url', help='utm_url')
parser.add_argument('--sklad-id', help='sklad-id')
args = parser.parse_args()

fsrar_id = get_fsrar_id(args.utm_url)

fname = './last_id.txt'
try:
    f = open(fname, 'r')
    last_id = int(f.read())
    f.close()
except FileNotFoundError:
    last_id = 0
print("last id:", last_id)

q = requests.get("{}/opt/out".format(args.utm_url))
assert q.status_code == 200
root = ET.fromstring(q.text)

files = dict()
i = 0
for url in root.findall('url'):
    m = re.match(r"http:\/\/.*\/opt\/out\/(.*)\/(\d+)", url.text)
    if m:
        entity = m.group(1)
        id = int(m.group(2))
        if id <= last_id:
            print("skip, id:", id)
            continue
        last_id = id

    print(id, url.text)
    q = requests.get(url.text)
    assert q.status_code == 200
    files["{}-{}{}".format(id, entity, ("-"+url.attrib['replyId']) if 'replyId' in url.attrib else '')] = q.text
    i += 1


# headers = {'Content-Disposition': 'attachment'}
#headers = {'Content-Type': 'multipart/form-data',}
#params = [('title', 'Waybill_v4.xml'), ('sklad_id', args.sklad_id)]
if len(files):
    params = {'fsrar_id': fsrar_id}
    print(files)
    print(params)
    q = requests.post("https://kirsa.9733.ru/file/",
                      files=files,
    #                  headers=headers,
                      params=params)
    assert q.status_code == 200
    f = open(fname, 'w')
    f.write(str(last_id))
    f.close()
print('download ok')

get_actions(fsrar_id=fsrar_id)


