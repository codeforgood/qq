__author__ = 'sravi'

import requests
import psycopg2


def count_words_at_url(url, config):
    resp = requests.get(url)
    return len(resp.text.split())


def query_postgres(query, config):
    pg_conn_params = config.get('SOURCE').get('PG')
    conn = psycopg2.connect(database=pg_conn_params.get('DBNAME'),
                            user=pg_conn_params.get('USER'),
                            password=pg_conn_params.get('PASSWORD'))
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print records
