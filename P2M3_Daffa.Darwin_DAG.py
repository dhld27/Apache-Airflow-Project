import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch






def queryPostgreSQL():
    '''
    When this function is activated, this function fetching the data from PostgreSQL to load the dataset.
    '''
    connString = "dbname='postgres' host='postgres' user='airflow' password='airflow' port='5432'"
    conn = db.connect(connString)
    df = pd.read_sql("select * from table_m3", conn)
    df.to_csv('P2M3_Daffa_Darwin_data_raw2.csv')
    print("---Data Saved---")

def cleaningData():
    '''
    When this function is activated, This function triggers the cleaning and manipulating data 
    to make the dataset more decent.
    '''
    df = pd.read_csv("P2M3_Daffa_Darwin_data_raw2.csv")
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.columns=df.columns.str.lower()
    df.columns=df.columns.str.replace(' ','_')
    df["Date"]=pd.to_datetime(df["Date"])
    df.to_csv("P2M3_Daffa_Darwin_dataCleaned.csv")

def insertElasticsearch():
    '''
    When this function is activated, the cleaned dataset can be imported to Elasticsearch
    '''
    es = Elasticsearch()
    df= pd.read_csv("P2M3_Daffa_Darwin_dataCleaned.csv")
    for i,r in df.iterrows():
        doc = r.to_json()
        res = es.index(index="p2m3daffadarwin", doc_type="doc", body=doc)
        print(res)

defaultArgs = {
    'owner': 'Daffa',
    'start_date': dt.datetime(2024, 5, 22),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('M3DBDag',
         default_args = defaultArgs, 
         schedule_interval = '30 6 * * *',
         catchup = False) as dag:
    
    getData = PythonOperator(task_id = 'QueryPostgreSQL',
                                python_callable = queryPostgreSQL)
    
    cleanData = PythonOperator(task_id = 'CleaningData', 
                                    python_callable = cleaningData)
    
    insertData = PythonOperator(task_id = 'InsertDataElasticsearch', 
                                    python_callable = insertElasticsearch)
    
getData >> cleanData >> insertData