from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow import DAG

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
with DAG(
    'Proyek_Akhir',
    default_args=default_args,
    description='Scheduling untuk task proyek akhir',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['proyek'],
) as dag:

    stream        = BashOperator(
                    task_id='Stream_data_twitter',
                    bash_command='python /home/stndb01/Documents/Data_Engineering/Proyek/stream.py'
                    #bash_command='python stream.py',
                    )

    extract        = BashOperator(
                    task_id='Extract_data_twitter',
                    bash_command='python /home/stndb01/Documents/Data_Engineering/Proyek/extract.py'
                    #bash_command='python extract.py',
                    )

    transform        = BashOperator(
                    task_id='Transform_data_twitter',
                    bash_command='python /home/stndb01/Documents/Data_Engineering/Proyek/transform.py'
                    #bash_command='python transform.py',
                    )

    load        = BashOperator(
                    task_id='Load_data_twitter',
                    bash_command='python /home/stndb01/Documents/Data_Engineering/Proyek/load.py'
                    #bash_command='python load.py',
                    )

    stream.set_downstream(extract)
    extract.set_downstream(transform)
    transform.set_downstream(load)
