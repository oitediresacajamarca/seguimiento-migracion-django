from django.shortcuts import render
from .models import SeguimientoNominalNinio
from django.http import JsonResponse
from django.views import View
import happybase

connection = happybase.Connection('localhost',port=9092)
table = connection.table('seguimiento')
connection.create_table(
    'seguimiento',
    {'ninio': dict(max_versions=10)
        }
)


# Create your views here.

class migracion_con(View):
    def get(self,request):
        
        lista=SeguimientoNominalNinio.objects.filter(id_indicador=291)
        for item in lista:
            
            if item.fecha_atencion is None:
                item.fecha_atencion=''
            else:
                item.fecha_atencion=item.fecha_atencion.strftime('%d-%m-%Y')

            print (bytes(item.fecha_atencion,encoding='utf-8'))
          
            table.put(bytes(item.numero_documento,encoding='utf-8'), {bytes('ninio:ipress',encoding='utf-8'): bytes(item.renipress,encoding='utf-8'),
                       bytes('ninio:fecha atencion',encoding='utf-8'): bytes(item.fecha_atencion,encoding='utf-8')})
           
           
        return JsonResponse(list(lista.values()),safe=False)


