from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .forms import UploadFileForm
from .models import UploadFile

import csv
# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'webinter/index.html')

def handle_uploaded_file(f):
    with open('file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'webinter/ok2check.html')
    else:
        form = UploadFileForm()
    return render(request, 'webinter/upload.html', {'form': form})
    
def check(request):
    checkpath = 'InterVar/example/myinter.hg19_multianno.txt.intervar'
    with open(checkpath, 'r') as rf:
        csvR = csv.reader(rf, delimiter='\t')
        lines = list(csvR) 
    # line = ['0', '1']
    # s = 'zhang'
    return render(request, 'webinter/check.html', {'lines': lines})
    # return HttpResponse('you have permissions.')
    # return render(request, 'webinter/check.html', {'str': s})

def downloadresult(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
    checkpath = 'InterVar/example/myinter.hg19_multianno.txt.intervar'
    writer = csv.writer(response, delimiter='\t')
    with open(checkpath, 'r') as rf:
        csvR = csv.reader(rf)
        lines = list(csvR)
    writer.writerows(lines)
    return response


def ok2check(request):

    return render(request, 'webinter/ok2check.html')


# @login_required
# def files(request):
#     return HttpResponse('you have permissions.')