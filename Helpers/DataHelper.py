from JsonHelper import JsonHelper

class DataHelper():
    def build_data_for_token_post(self, user_email, user_password):
        json_helper = JsonHelper()
        file_path = r"../Resources/UserTokenModel.json"
        dictionary_data = json_helper.load_json_file(file_path)
        dictionary_data["UserEmail"] = user_email
        dictionary_data["Password"] = user_password
        json_data = json_helper.covert_into_json(dictionary_data)
        print(json_data)
        return json_data

