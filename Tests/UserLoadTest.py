from locust import Locust, TaskSet, task
sys.path.insert(0, r"C:\Source\Locust\StartingWithLocust\Helpers")

class UserBehaviour(TaskSet):
    
    @staticmethod
    def on_start():
        global user_list
        global xml_helper
        global csv_helper
        global json_helper

        xml_helper = new xml_helper
    
