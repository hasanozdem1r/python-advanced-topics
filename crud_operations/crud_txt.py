# this demo simply register system to txt file
# each line includes : name surname id_number phone_number

file=open("employee_database.txt","a")

class File_Operations:

    def __init__(self,file_path:str):
        self._file_path=file_path
        #if file is not exist it will create a new file
        self._file=open(self._file_path,"a")
        self._file.close()
    def show_all_employees(self) -> None :
        with  open(self._file_path,mode="r",encoding="utf-8") as file:
            for line in file:
                print(line,end='')

    def write_line(self,employee_information:str)-> None:
        with  open(self._file_path, mode="a", encoding="utf-8") as file:
            file.write(employee_information)


txt_obj=File_Operations("employee_database.txt")

#txt_obj.write_line("Hasan Özdemir 1234567890 534534534 \n")

#txt_obj.show_all_employees()