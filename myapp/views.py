from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

import datetime

from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'invoice_id': 1233434,
        }

        html = template.render(context)
        return HttpResponse(html)


class downloadPdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'invoice_id': 1233434,
        }
        pdf = render_to_pdf('download.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


