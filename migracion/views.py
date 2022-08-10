from django.shortcuts import render
from .models import SeguimientoNominalNinio
from django.http import JsonResponse
from django.views import View
import happybase

connection = happybase.Connection('localhost',port=9092)

'''connection.create_table(
    'seguimiento',
    {'ninio': dict(max_versions=10)}
)
'''

# Create your views here.

class migracion_con(View):
    def get(self,request,agnio,mes):
        anio = agnio
        mes = mes
        periodo=str(int(anio)*100+int(mes))
        
        print(str(int(anio)*100+int(mes)))
        
        lista=SeguimientoNominalNinio.objects.filter(id_indicador=291,anio=agnio,mes=mes)
        lis_u=lista.values('id_actividad','id_indicador').distinct()

        dic={}

        for item in lis_u.values('id_actividad','id_indicador').distinct():
            print(item['id_actividad'])
            dic[str(item['id_indicador'])+'_'+str(item['id_actividad'])]={}
        
        print(dic)
        '''
        connection.create_table('PERIODO_'+str(periodo)+':SEGUIMIENTO_NINIO',dic)
        '''
        table_i= connection.table('PERIODO_'+str(periodo)+':SEGUIMIENTO_NINIO')
        dicres={}

        for item in lista.values():
            print(item)
            dicres[str(item['id_indicador'])+'_'+str(item['id_actividad'])+':ipress']=item['renipress']

            if(item['fecha_atencion'] is None):
                item['fecha_atencion']=''
            else :
                item['fecha_atencion']=item['fecha_atencion'].strftime('%d-%m-%Y')

            
            
            dicres[str(item['id_indicador'])+'_'+str(item['id_actividad'])+':fecha atencion']=item['fecha_atencion']
            
            dicres[str(item['id_indicador'])+'_'+str(item['id_actividad'])+':cumple']=item['cumple']
           
            dicres[str(item['id_indicador'])+'_'+str(item['id_actividad'])+':id_cita']=item['id_cita']
            table_i.put(item['numero_documento'],dicres)
        
        print(dicres.values())
        
        
        
        


       
        

       
        '''
        print(lis_u.values('id_actividad','id_indicador').distinct())
        print(lista.count())
        connection.create_table('PERIODO_'+str(periodo)+':SEGUIMIENTO_NINIO',{'preubas': dict(max_versions=10)})
        print('PERIODO_'+str(periodo)+':SEGUIMIENTO_NINIO')


        table= connection.table('PERIODO_'+str(periodo)+':SEGUIMIENTO_NINIO')
        table.put('çrea',{'indicador 200:ipress':'300'},)
        '''
        

     
        '''
      
        for item in lista:

            print('PERIODO_'+str(item.anio*100+item.mes))
            
            if item.fecha_atencion is None:
                item.fecha_atencion=''
            else:
                item.fecha_atencion=item.fecha_atencion.strftime('%d-%m-%Y')

            print (bytes(item.fecha_atencion,encoding='utf-8')) 
            
            
            table.put(bytes(item.numero_documento,encoding='utf-8'), {bytes('ninio:ipress',encoding='utf-8'): bytes(item.renipress,encoding='utf-8'),
                       bytes('ninio:fecha atencion',encoding='utf-8'): bytes(item.fecha_atencion,encoding='utf-8')})
            
            '''  
           
        return JsonResponse(list(lista.values()),safe=False)
