# https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html
# https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html#airflow.providers.docker.operators.docker.DockerOperator
# https://docker-py.readthedocs.io/en/stable/containers.html#mounts

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

def test():
    print("test complete")

default_args = {
    'description':'Orchestrates the dbt weather data',
    'start_date':datetime(2025, 4, 30),
    'catchup':False,
}

dag = DAG(
    dag_id="weather-dbt-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=6),

)

with dag:
    task2=DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/toby/repos/weather_pipeline/dbt/my_project',
                  target='/usr/app',
                  type='bind'),
            Mount(source='/home/toby/repos/weather_pipeline/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind'),
        ],
        network_mode='weather_pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )