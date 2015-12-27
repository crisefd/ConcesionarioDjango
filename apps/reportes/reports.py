from apps.usuarios.models import User
from apps.model_report.report import reports, ReportAdmin

class MyReport(ReportAdmin):
    title = _('User Report Name')
    model = User
    fields = [
        'email',
    ]
    list_order_by = ('username',)
    type = 'report'

reports.register('my-report', MyReport)