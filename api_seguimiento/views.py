from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.
import happybase as hb
import json
import os


class consulta(View):
    def get(self, request,agnio,mes,ipress,id_indicador,curso):
        periodo=str(int(agnio)*100+int(mes))
        lisg={}
        try:
            connection=self.Crea_coneccion()
            
            table_i= connection.table('PERIODO_'+str(periodo)+':SEGUIMIENTO_'+curso)
        
        
            
            for key, data in table_i.scan(filter="SingleColumnValueFilter('CMI_2022','ipress adscripcion',=, 'binary:"+ipress+"',true,true)  AND (ColumnPrefixFilter('"+id_indicador+"')) "):
                dicc_data={}          
                for key1,data1 in data.items():
                
                    dicc_data[key1.decode('utf-8')]=data1.decode('utf-8')
                    lisg[key.decode('utf-8')] =dicc_data
            connection.close()
            
        except Exception as e:
            print (e)
            print ('error de coneccion')
            
        


            '''
                lisg[key.decode('utf-8')]=json.dumps(data)
                print('============================================================')
                print(type(data))
                
                print('============================================================')
            
            
            '''


        return JsonResponse(list(lisg.items()),safe=False)
    
    def Crea_coneccion(self):
        try:
            print(os.environ.get('SERVER_HBASE'))
            con=  hb.Connection(os.environ.get('SERVER_HBASE'),port=int(os.environ.get('PORT_HBASE')) )
            
            return con
        except Exception as e:
            print (e)
            con.close()



    


