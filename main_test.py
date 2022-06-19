import unittest

import requests


class TestSum(unittest.TestCase):
    def test_send_waybill(self, ):
        files = dict()
        #f = open('data/TTN-0557370828.xml', 'r')
        #files["Waybill_v4"] = f.read()
        #f.close()

        #f = open('data/TTN-0557370828-history.xml', 'r')
        #files["History_v4"] = f.read()
        #f.close()

        f = open('data/FORM2REGINFO.xml', 'r')
        files["FORM2REGINFO"] = f.read()
        f.close()

        params = {'fsrar_id': 'test'}
        q = requests.post("http://localhost:8015/file/",
                          files=files,
                          params=params)
        assert q.status_code == 200


if __name__ == "__main__":
    unittest.main()