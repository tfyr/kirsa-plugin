import re
import xml.etree.ElementTree as ET
import argparse
import requests
# import time
# import json
# import xml.dom.minidom

from egais import get_fsrar_id, get_actions

parser = argparse.ArgumentParser()
parser.add_argument('--utm-url', help='utm_url')
parser.add_argument('--backend-url', help='backend_url')
parser.add_argument('--less-or-equal-id', help='less_or_equal_id')
args = parser.parse_args()

utm_url = args.utm_url or 'http://localhost:8080'
backend_url = args.backend_url or 'https://kirsa.9733.ru'

fsrar_id = get_fsrar_id(utm_url)

def download():
    fname = './last_id.txt'   # 51
    try:
        f = open(fname, 'r')
        last_id = int(f.read())
        f.close()
    except FileNotFoundError:
        last_id = 0
    print("last id:", last_id)

    q = requests.get(f"{utm_url}/opt/out")
    assert q.status_code == 200
    root = ET.fromstring(q.text)

    files_list = list()
    files_dict = dict()
    i = 0
    new_last_id = last_id


    less_or_equal_id = int(args.less_or_equal_id) if args.less_or_equal_id else None

    for url in root.findall('url'):
        m = re.match(r"http:\/\/.*\/opt\/out\/(.*)\/(\d+)", url.text)
        if m:
            entity = m.group(1)
            id = int(m.group(2))
            if id <= last_id:
                print("skip, id:", id)
                continue
            new_last_id = id
            if less_or_equal_id and id > less_or_equal_id:
                break

        print(id, url.text)
        q = requests.get(url.text)
        assert q.status_code == 200
        # files_dict[f"files"] =  ("{}-{}{}".format(id, entity, ("-"+url.attrib['replyId']) if 'replyId' in url.attrib else ''), q.text, 'text/plain')
        files_list.append( (f"files",  ("{}-{}{}".format(id, entity, ("-"+url.attrib['replyId']) if 'replyId' in url.attrib else ''), q.text, 'text/plain')))
        # files = {"files": ('x1', q.text, 'text/plain')}
        i += 1


    # headers = {'Content-Disposition': 'attachment'}
    #headers = {'Content-Type': 'multipart/form-data',}
    #params = [('title', 'Waybill_v4.xml'), ('sklad_id', args.sklad_id)]
    if len(files_list):
        params = {'fsrar_id': fsrar_id}
        print(params)
        q = requests.post(f"{backend_url}/kirsa-egais/upload-file",
                          files=files_list,
                          # headers=headers,
                          params=params,
                          )
        assert q.status_code == 200
        f = open(fname, 'w')
        f.write(str(new_last_id))
        f.close()
    print('download ok')


download()
get_actions(fsrar_id=fsrar_id, utm_url=utm_url)


