import mysql.connector

from egais import get_fsrar_id, write_off_v3

sql = '''select distinct p.incomepos_ptr_id, p.inform_b_reg 
           from kirsa_incomeposalco p, ip where ip.id=p.incomepos_ptr_id 
                and ip.sklad_id=55
                and exists (select id from kirsa_amc a where a.incomepos_alco_id=ip.id)
                and p.inform_b_reg in (select s1 from x) 
                -- and p.inform_b_reg in ('FB-000006905493717')
                -- and p.inform_b_reg not in (
                --    'FB-000005164416307','FB-000005186655583','FB-000005218352818','FB-000005218352825',
                --    'FB-000005218352827','FB-000005218352832','FB-000005242251484','FB-000005242251491',
                --    'FB-000005336941242','FB-000005336941250')
          order by p.inform_b_reg'''

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
    write_off_v3(utm_url, fsrar_id, positions, "32")

# last_id 277