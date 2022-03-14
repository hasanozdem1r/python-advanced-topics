import csv


class CsvOperations:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, newline="", mode="r") as csv_file:
            food_file = csv.reader(csv_file, delimiter=" ", quotechar="|")
            for row in food_file:
                print(row)

    def write_csv(self, food_name="", scientific_name="", group="", sub_group=""):
        with open(self.file_path, newline="", mode="a") as csv_file:
            food_write = csv.writer(csv_file, delimiter=" ", quotechar="|")
            food_write.writerow([food_name, scientific_name, group, sub_group])


csv_obj = CsvOperations("data_sources/generic-food.csv")

# read all rows
csv_obj.read_csv()

# write row by row
csv_obj.write_csv("banana", "antalya banana", "fruit", "fruit")
