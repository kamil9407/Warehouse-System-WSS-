from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import AddWare
from .forms import ImportWareForm
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from django.shortcuts import render


def index(request):
    return render(request, 'importwares/index.html')

def generate_pdf(request):
    if request.method == 'POST':
        form = ImportWareForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            title = data['name']
            
            # Renderuj HTML za pomocą danych z formularza
            html = render_to_string('importwares/report_template.html', {'data': data, 'title':title})
            
            # Generowanie PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            
            if pisa_status.err:
                return HttpResponse('Błąd podczas generowania PDF: %s' % pisa_status.err, status=500)
            return response
    else:
        form = ImportWareForm()
    
    return render(request, 'importwares/import_ware.html', {'form': form},)

def create_whole_report(request):
    template_path = 'importwares/report_all.html'
    wares = AddWare.objects.all()
    context = {'wares': wares}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def ware_list_view(request):
    wares = AddWare.objects.all()
    return render(request, 'importwares/ware_list.html', {'wares': wares})

def ware_detail_view(request, pk):
    ware = get_object_or_404(AddWare, pk=pk)
    return render(request, 'importwares/ware_detail.html', {'ware': ware})
