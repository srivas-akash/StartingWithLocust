import sys
import random
sys.path.insert(0,r"..\Helpers")
from CsvHelper import CsvHelper
from DataHelper import DataHelper
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    
    @staticmethod
    def on_start():
        global user_list
        global csv_helper
        global data_helper
        
        data_helper = DataHelper()
        csv_helper = CsvHelper()
        user_list_file_name = "../Resources/UserDetails.csv"
        user_list =  csv_helper.get_csv_values(user_list_file_name)
    
    @task
    def get_user_token(self):
        user_emails = user_list["EmailId"]
        user_passwords = user_list["Password"]
        value = random.randint(0, len(user_emails) - 1)
        email = user_emails[value]
        password = user_passwords[value]
        data = data_helper.build_data_for_token_post(email, password)
        headers = {"content-type": 'application/json'}
        print(data)
        response = self.client.post("/api/tokens", data = data, headers= headers, verify = False)
        actual_status_code = response.status_code
        assert actual_status_code == 200, "correct status for token should be received expected 200  found = {0}".format(actual_status_code)
         
class WebsiteUser(HttpLocust):
    """
        defines the user task behavior
    """
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000