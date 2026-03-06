"""
DAG 01: Hello World
Learning: Basic DAG structure, BashOperator, task dependencies
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'kiran',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='01_hello_world',
    default_args=default_args,
    description='My first DAG - Hello World',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['learning', 'beginner'],
) as dag:

    task_hello = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from Airflow! Current time: $(date)"',
    )

    task_env = BashOperator(
        task_id='print_environment',
        bash_command='echo "Running on: $(hostname) | User: $(whoami)"',
    )

    task_complete = BashOperator(
        task_id='complete',
        bash_command='echo "Pipeline finished successfully!"',
    )

    task_hello >> task_env >> task_complete
