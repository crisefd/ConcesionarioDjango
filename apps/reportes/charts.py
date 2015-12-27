from django_google_charts import charts
from .models import StepCount
from apps.usuarios.models import User

class StepChart(charts.Chart):
    chart_slug = 'steps_chart'
    columns = (
        ('datetime', "Date"),
        ('number', "Steps"),
    )

    def get_data(self):
        return User.objects.values_list('last_login', 'branch_id')