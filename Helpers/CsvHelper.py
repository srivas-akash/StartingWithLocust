import csv


class CsvHelper:
    """This helps in getting different csvs and enabling the usage of them later"""

    def get_file_reader_instance(self, path):
        """Takes the file path and gets the reader instance for it"""

    @staticmethod
    def get_csv_values(path):
        """Gets the csv from a path
        
        Args:
            path: location of the csv file
            
        Returns:
            Dictonary<string, string> where 1st key is the coloumn name and value is a list of values.
            
        Please make sure that for relational columns like consumer key and sceret we use the same numeber of values in each columns
        """
        rows = []
        return_values = dict()

        with open(path, "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            fields = next(csv_reader)

            for row in csv_reader:
                rows.append(row)
            for i in (0, len(fields) - 1):
                col_values = []
                for row in rows:
                    col_values.append(row[i])
                    return_values[fields[i]] = col_values

        return return_values
