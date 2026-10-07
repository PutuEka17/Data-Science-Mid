from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


# ==========================================================
# DAG DATA EKONOMI WORLD BANK API
# ==========================================================

with DAG(
    dag_id="economic_world_bank_etl",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["WorldBank", "Economic", "ETL"],
    description="Pipeline ETL data ekonomi dari World Bank API"
) as dag:

    # ======================================================
    # TASK 1 — EXTRACT
    # ======================================================

    extract_api = BashOperator(
        task_id="extract_api",

        bash_command="""
        cd /opt/airflow/project
        python extract_api.py
        """
    )


    # ======================================================
    # TASK 2 — MEMBENTUK 3 TABEL
    # ======================================================

    create_tables = BashOperator(
        task_id="create_tables",

        bash_command="""
        cd /opt/airflow/project
        python create_tables.py
        """
    )


    # ======================================================
    # TASK 3 — ASSESSMENT
    # ======================================================

    assess_tables = BashOperator(
        task_id="assess_tables",

        bash_command="""
        cd /opt/airflow/project
        python assess_tables.py
        """
    )


    # ======================================================
    # TASK 4 — CLEANING
    # ======================================================

    clean_tables = BashOperator(
        task_id="clean_tables",

        bash_command="""
        cd /opt/airflow/project
        python clean_tables.py
        """
    )


    # ======================================================
    # URUTAN PROSES ETL
    # ======================================================

    extract_api >> create_tables >> assess_tables >> clean_tables