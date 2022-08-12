from django.shortcuts import render
from .models import SeguimientoNominalNinio
from django.http import JsonResponse
from django.views import View
import happybase

connection = happybase.Connection('172.18.20.37',port=9092,protocol='compact', timeout=None,
            autoconnect=True,
            transport='framed',  # Default: 'buffered'  <---- Changed.
            )

'''connection.create_table(
    'seguimiento',
    {'ninio': dict(max_versions=10)}
)
'''

# Create your views here.

class migracion_con(View):
    
    def get(self,request,agnio,mes,id_curso):
        print(id_curso)
        anio = agnio
        mes = mes
        periodo=str(int(anio)*100+int(mes))
        nombre_curso=''
        indicador_min=0
        indicador_max=199
        if id_curso=='1':
            nombre_curso='MATERNO'
            indicador_min=0
            indicador_max=100

        if id_curso=='2':
            nombre_curso='NINIO'
            indicador_min=200
            indicador_max=299
            print(nombre_curso)
        if id_curso=='3':
            nombre_curso='ADOLECENTE'
            indicador_min=300
            indicador_max=399
        if id_curso=='4':
            nombre_curso='JOVEN'
            indicador_min=400
            indicador_max=499
        if id_curso=='5':
            nombre_curso='ADULTO'
            indicador_min=500
            indicador_max=599
        if id_curso=='6':
            nombre_curso='ADULTO_MAYOR'
            indicador_min=600
            indicador_max=699
        print(nombre_curso)

            
        
        print(str(int(anio)*100+int(mes)))
        
        lista=SeguimientoNominalNinio.objects.filter(anio=agnio,mes=mes,id_curso_de_vida=id_curso,id_indicador=291)
        print('taamaanaio')
        print(len(lista))
        '''
        lis_u=lista.values('id_actividad','id_indicador').distinct()

        dic={}

        for item in lis_u.values('id_actividad','id_indicador').distinct():
            print(item['id_actividad'])
            dic[str(item['id_indicador'])+'_'+str(item['id_actividad'])]={}
        
        print(dic)
        '''
       
        try :
     
            connection.create_table('PERIODO_'+str(periodo)+':SEGUIMIENTO_'+nombre_curso,{'CMI_2022':{}})

        except:
            print('ya existe la tabla')
     
        
        table_i= connection.table('PERIODO_'+str(periodo)+':SEGUIMIENTO_'+nombre_curso)
        dicres={}
        print('columnas generadas')

        for item in lista.values():
            print(item)
            dicres={}
            dicres['CMI_2022:'+str(item['id_indicador'])+'_'+str(item['id_actividad'])+'_ipress']=item['renipress']

            if(item['fecha_atencion'] is None):
                item['fecha_atencion']=''
            else :
                item['fecha_atencion']=item['fecha_atencion'].strftime('%d-%m-%Y')
            
            if(item['id_cita'] is None):
                item['id_cita']=''
            else :
                item['id_cita']=item['id_cita']
            
            if(item['id_indicador'] is None):
                item['id_indicador']=''
            else :
                item['id_indicador']=item['id_indicador']

            
            
            dicres['CMI_2022:'+str(item['id_indicador'])+'_'+str(item['id_actividad'])+'_fecha atencion']=item['fecha_atencion']
            
            dicres['CMI_2022:'+str(item['id_indicador'])+'_'+str(item['id_actividad'])+'_cumple']=item['cumple']
           
            dicres['CMI_2022:'+str(item['id_indicador'])+'_'+str(item['id_actividad'])+'_id_cita']=item['id_cita']
            
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
