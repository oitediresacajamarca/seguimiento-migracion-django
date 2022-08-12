from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.
import happybase
import json

connection = happybase.Connection('localhost',port=9092)

class consulta(View):
    def get(self, request,agnio,mes,ipress):
        periodo=str(int(agnio)*100+int(mes))
        
        table_i= connection.table('PERIODO_'+str(periodo)+':SEGUIMIENTO_NINIO')
       
       
        lisg={}
        for key, data in table_i.scan(filter="SingleColumnValueFilter('291_207','ipress',=, 'binary:000004645')"):
            dicc_data={}          
            for key1,data1 in data.items():
                print(key1.decode('utf-8'))
                print(data1.decode('utf-8'))
                dicc_data[key1.decode('utf-8')]=data1.decode('utf-8')
            lisg[key.decode('utf-8')] =dicc_data
           
    


        '''
            lisg[key.decode('utf-8')]=json.dumps(data)
            print('============================================================')
            print(type(data))
            
            print('============================================================')
           
        
        '''


        return JsonResponse(list(lisg.items()),safe=False)


