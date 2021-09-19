#PACKAGE IMPORTS
from pathlib import Path
import openpyxl as oxl


file=Path('data_sources','VOCABULARY.xlsx')


class XlsxOperations:

    def __init__(self,file_path:str)->None:
        self._file_path=file_path
        self._workbook_obj=oxl.load_workbook(self._file_path)
        self._sheet_obj=self._workbook_obj.active

    def read_all_xlsx(self)->list:
        max_row=self._sheet_obj.max_row
        result_df:list=[]
        for item in range(1,max_row+1):
            cell_obj = self._sheet_obj.cell(row=item, column=1)
            result_df.append(str(cell_obj.value))
        # remove duplicates
        result_df=list(set(result_df))
        return result_df

xlsx_obj=XlsxOperations(file)
result:list=xlsx_obj.read_all_xlsx()
print(len(result))
