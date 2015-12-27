from django.shortcuts import render
from .charts import StepChart

def report_view(request):
    return render(request, 'prueba_reporte.html', {
        'chart': StepChart(),
    })