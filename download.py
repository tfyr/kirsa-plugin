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
'''

i = 0
while True:
    i += 1
    print("attempt {}".format(i))
    q = requests.get("{}/opt/out".format(args.utm_url))
    if q.status_code == 200:
        root = ET.fromstring(q.text)
        for url in root.findall('url'):
            print(url.text)
            # q = requests.get(url.text)
            # assert q.status_code == 200
            # exit = True
            # print(q.text)
            # break
    time.sleep(60)'''

#files = dict()
#files['xml_file'] = ("query.xml", "test", 'text/xml')


files = {
    "ReplyRests_v2.xml": open("data/ReplyRests_v2.xml", "r"),
    "ReplyRestsShop_v2.xml": open("data/ReplyRestsShop_v2.xml", "r"),
    #"test_file_3": open("my_file_3.txt", "rb")
}

# headers = {'Content-Disposition': 'attachment'}
#headers = {'Content-Type': 'multipart/form-data',}
#params = [('title', 'Waybill_v4.xml'), ('sklad_id', args.sklad_id)]
params = {'fsrar_id': args.sklad_id}
ret = requests.post("{}/file/".format("http://localhost:8015"),
                    files=files,
#                    headers=headers,
                    params=params)

