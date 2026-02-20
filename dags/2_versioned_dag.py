from airflow.sdk import dag,task

@dag(
        dag_id = "versioned_dag"
)
def versioned_dag():
    @task.python
    def first_task():
        print("first task")
    @task.python
    def second_task():
        print("second_task")
    @task.python
    def third_task():
        print("third task")
    @task.python
    def versioned_task():
        print("Version 2.0")
        
    
    first = first_task()
    second = second_task()
    third  = third_task()
    fourth = versioned_task()

    first >> second >> third >> fourth

versioned_dag()
