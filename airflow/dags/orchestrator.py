from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from api_requests.insert_records import insert_records_main

def test():
    print("test complete")

default_args = {
    'description':'Orchestrate weather data',
    'start_date':datetime(2025, 4, 30),
    'catchup':False,
}

dag = DAG(
    dag_id="weather-api-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=6),

)

with dag:
    task=PythonOperator(
        task_id='test',
        python_callable=insert_records_main
    )