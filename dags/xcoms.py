from airflow.sdk import dag,task

@dag(
        dag_id = "xcoms"
)
def xcoms():
    @task.python
    def first_task():
        fetched_data = {"data":[1,2,3,4,5]}
        return fetched_data
    @task.python
    def second_task(data:dict):
        fetched_data=data['data']
        transformed_data = fetched_data*2
        transformed_data_dict = {"transf_data":transformed_data}
        return transformed_data_dict
    @task.python
    def third_task(data:dict):
        load_data = data
        return load_data

        
    
    first = first_task()
    second = second_task(first)
    third  = third_task(second)


xcoms()
