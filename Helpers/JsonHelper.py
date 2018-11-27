import json

class JsonHelper():

    def load_json_file(self, file_location):
        with open(file_location) as json_data:
           dictionary_data = json.loads(json_data.read())
        return dictionary_data

    def covert_into_json(self, dictionary_data):
        json_data = json.dumps(dictionary_data)
        return json_data