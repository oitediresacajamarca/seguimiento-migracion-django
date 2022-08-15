from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.
import happybase as hb
import json
import os


class consulta(View):
    separador='$'
    def get(self, request,agnio,mes,ipress,id_indicador,curso):
        periodo=str(int(agnio)*100+int(mes))
        lisg=[]
        try:
            connection=self.Crea_coneccion()
            
            table_i= connection.table('PERIODO_'+str(periodo)+':SEGUIMIENTO_'+curso)
        
        
            filter_text="SingleColumnValueFilter('CMI_2022','ipress adscripcion',=, 'binary:"+ipress+"',true,true) "
            print(filter_text)
            for key, data in table_i.scan(filter=filter_text):
          
              
                activida=[]
                for key1,data1 in data.items():
                    
                    indices=key1.decode('utf-8').split('$')
                    indicador=indices[1]
                    campo= indices[2]
                    existe=False
                    print(key1)
                    indice_encontrar=1000
                    print (id_indicador)

                    if indices[0]==id_indicador:
                        for i in range(0, len(activida)):
                                                   

                            if activida[i]["indicador"]== indices[1]:
                                existe=True 
                                indice_encontrar=i
                                activida[indice_encontrar][indices[2]]=data1.decode('utf-8')                    
                            
                            else:
                                existe=False
                        
                        if existe==False:
                            activida.append({"indicador":indices[1]})
                            activida[len(activida)-1][indices[2]]=data1.decode('utf-8')
                            
                  
                        
                       



                lisg.append({'numero_documento':key.decode('utf-8'),'actividades':activida})
         
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


        return JsonResponse(lisg,safe=False)
    
    def Crea_coneccion(self):
        try:
            print(os.environ.get('SERVER_HBASE'))
            con=  hb.Connection(os.environ.get('SERVER_HBASE'),port=int(os.environ.get('PORT_HBASE')) )
            
            return con
        except Exception as e:
            print('error de coneccion')
            print (e)
            con.close()



    


