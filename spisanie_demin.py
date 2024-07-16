import mysql.connector

from egais import get_fsrar_id, write_off_v3

sql = '''select distinct p.incomepos_ptr_id, p.inform_b_reg 
           from kirsa_incomeposalco p, ip where ip.id=p.incomepos_ptr_id 
                and ip.sklad_id=55
                and exists (select id from kirsa_amc a where a.incomepos_alco_id=ip.id)
                and p.inform_b_reg<>'FB-000006638627341'
          order by p.inform_b_reg
          limit 125, 40'''

cnx = mysql.connector.connect(user='nash', password=None,
                              host='localhost',
                              database='demands27')
positions = []
with cnx.cursor() as cursor:
    cursor.execute(sql)
    for id, fb in cursor.fetchall():
        q = 0
        cursor.execute('select code from kirsa_amc where incomepos_alco_id=%s', (id,))
        codes = []
        for code, in cursor.fetchall():
            q += 1
            print(fb, code)
            codes.append(code)

        positions.append(
            {'quantity': q,
                'F2RegId': fb,
                'marks': codes
             })

    utm_url = 'http://localhost:8088'
    fsrar_id = get_fsrar_id(utm_url)
    write_off_v3(utm_url, fsrar_id, positions, "18")

# last_id 277