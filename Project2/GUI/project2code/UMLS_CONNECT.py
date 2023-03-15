import time

import mysql
from mysql import connector
import pysolr
# create solr connection

from datetime import datetime
def date_parser(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    #format the dates as strings in the ISO format expected by Solr
    start_date_iso = start_date.isoformat() + 'Z'
    end_date_iso = end_date.isoformat() + 'Z'
    #construct the Solr date query
    return start_date_iso, end_date_iso


def UMLS_SEARCH(keyword,result_queue):
    cnx = mysql.connector.connect(user='umls', password='umls', host='172.16.34.1', port='3307', database='umls2020')
    cursor = cnx.cursor()
    # query format
    query = (f"""
    select distinct m2.STR
    from MRCONSO as m1
    join MRREL on m1.CUI = MRREL.CUI1
    join MRCONSO as m2 on MRREL.CUI2 = m2.CUI
    where m1.SAB = 'CHV'
    and m1.LAT = 'ENG'
    and m2.SAB = 'CHV'
    and m2.LAT = 'ENG'
    and MRREL.REL = 'SY'
    and m1.STR = '{keyword}' limit 30;""")
    # start query
    cursor.execute(query)
    result = []
    result.append(keyword)
    # print result
    for row in cursor.fetchall():
        result.append(row[0])
    cursor.close()
    cnx.close()
    result_queue.put(result)

    return




def solr_search(KeyWord,FromDate,ToDate,DiagnosesNum,Expired,result_solr):
    s = pysolr.Solr('http://localhost:8983/solr/test')
    query = ''
    if KeyWord != '':
        if type(KeyWord) == list:
            query += f'text:"{KeyWord[0]}"'
            for i in range(1,len(KeyWord)):
                query += f'OR text:"{KeyWord[i]}"'

        else:
            query += f'text:"{KeyWord}"'
    if FromDate != '' and ToDate != '':
        FromDate,ToDate = date_parser(FromDate,ToDate)
        if query != '':
            query +=" AND "
        # query += f'chartdate:"{FromDate} TO {ToDate}"'
        query += f'chartdate:[{FromDate} TO {ToDate}]'
    if DiagnosesNum != '':
        if query != '':
            query +=" AND "
        DiagnosesNum = DiagnosesNum.replace(".", "")
        query += f'diagnoses:"{DiagnosesNum}"'
    if Expired != None:
        if query != '':
            query += " AND "
        if Expired.lower() == "yes":
            Expired = 1
        else:
            Expired = 0
        query += f'expire_flag:"{Expired}"'
    # send query to solr
    print("The query we sent to solr is: ", query)
    results = s.search(query, **{
      'rows': 20,
      'fl': 'id'
    })
    # print result
    res = []
    for result in results:
        #print(result['id'], result['text'])
        res.append(result['id'])

    result_solr.put(res)
    total_doc_count = s.search(query, rows=0)
    num_matches = total_doc_count.hits
    result_solr.put(num_matches)
    return