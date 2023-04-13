import os
import sys
import pandas as pd 
from database import DatabaseHelper
from query import Query


class DigimrAutomations:

    def __init__(self):
        self.database = DatabaseHelper()
        

    def best_call_statuses_count(self):
        best_call_status_df = self.database.fetch(Query.TOTAL_DOCTORS_WITH_BEST_CALL_STATUS.format(product_ids="164",
        from_Date ='2022-12-16' , to_Date ='2022-12-26'))
        return best_call_status_df
    
    def uni(self):
        df = self.database.fetch(Query.universal)
        df.to_csv("uni_final.csv")

    def best_call(self):
        best_call_logs = self.database.fetch(Query.BEST_CALL_LOGES.format(product_ids="164",
        from_Date='2022-12-16' , to_Date ='2022-12-26' ))
        return best_call_logs

    def calllogs(self):
        call_logs  = pd.DataFrame(self.database.fetch(Query.CALL_LOGES.format(product_ids="164",from_Date ='2022-12-16' ,
        to_Date ='2022-12-26') ))
        
        call_logs.drop(['file_name'], axis= 1 , inplace= True)
        print(call_logs)
        return call_logs

    def to_excel(self):

        df1 = self.best_call_statuses_count()
        df2 = self.best_call()
        df3 = self.calllogs()
        with pd.ExcelWriter('Sanofi ALLEGRA.xlsx') as writer: 
            df1.to_excel(writer, sheet_name='best_call_status')
            df2.to_excel(writer, sheet_name='best_call_logs')
            df3.to_excel(writer, sheet_name='call_logs')

    def best_call_by_sep(self):
        call  = self.database.fetch(Query.BEST_CALL_STATUS_SPECIALITY.format(product_ids="52",from_Date ='2022-12-08' ,
         to_Date ='2022-12-01'))
        call.to_excel("output.xlsx")

    def telecaller_wise_summary(self):
        data = self.database.fetch(Query.PROJECT_TELLCALLER_CALL_STUTSS.format(from_Date="2022-12-08", to_Date = "2022-11-10"))
        data.to_excel('telecaller_wise_summary.xlsx')

    def product_wise_summary(self):
        data = self.database.fetch(Query.data)
        data.to_excel('data.xlsx')

    def pending_calls(self):
        data = self.database.fetch(Query.PENDING_CALLS)
        data.to_excel('pending_calls.xlsx')

    def total_call_optins(self):
        data = self.database.fetch(Query.total_call_optins.format(product_ids="99",from_Date ='2022-01-23' ,
        to_Date ='2022-09-21'))
        data.to_excel('optins.xlsx')

    def No_Respones(self):
        data = self.database.fetch(Query.NO_Respons.format(product_ids="99",from_Date ='2022-01-23' ,
        to_Date ='2022-09-21'))
        data.to_excel('No_Respones.xlsx')

    # def bhf(self):
    #     data 


    


if __name__ == '__main__':
    dg = DigimrAutomations()
    dg.product_wise_summary()
    


