from django.shortcuts import render
from .models import Inventar
from django.db.models import Q
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

import pandas as pd 
from fpdf import FPDF

from reportlab.lib.pagesizes import letter
import io

def some_view(request):




#########################################################################################################
    #df = pd.DataFrame(list((Inventar.objects.all()) # Create PDF object and specify it's properties 

    search_post = request.GET.get('search')

    if search_post != "None":
        item = Inventar.objects.filter(Q(name__icontains=search_post) | Q(num__icontains=search_post) | Q(num_kab__num__icontains=search_post))
    else:
        item = Inventar.objects.all()

    if len(item) > 0:
        pdf = FPDF()
        pdf.add_font(family="DejaVu", fname="C:\\Users\\Владимир\\invent\\djangoInvent\\invent\\DejaVuSans.ttf", style="")
        pdf.add_font(family="DejaVu", fname="C:\\Users\\Владимир\\invent\\djangoInvent\\invent\\DejaVuSans-Bold.ttf", style="B")
        pdf.set_font("DejaVu", size=13)
        set_kab=set()
        for it in item:
            set_kab.add(it.num_kab)

        for kab in set_kab:
            pdf.add_page()
            pdf.cell(0,0, f"КАБИНЕТ { kab }")
            pdf.ln()
            count = 0
            with pdf.table(col_widths=(10, 30, 35, 25, 30)) as table:
                header = table.row()
                header.cell("№")
                header.cell("Наименование")
                header.cell("Идентификатор")
                header.cell("Количество")
                header.cell("Ответственный")
                for data_row in item:
                    if data_row.num_kab == kab:
                        row = table.row()
                        count +=1
                        row.cell(str(count))
                        row.cell(data_row.name)
                        row.cell(data_row.num)
                        row.cell(data_row.count)
                        row.cell(data_row.response)
                
        pdf.output("my_pdf.pdf", 'F')

        buffer = io.BytesIO()
        return FileResponse(open("my_pdf.pdf", "rb"))
    else:
        return HttpResponse("Нет объектов для печати!")



def MyView(request):
    search_post = request.GET.get('search')

    if search_post:
        posts = Inventar.objects.filter(Q(name__icontains=search_post) | Q(num__icontains=search_post) | Q(num_kab__num__icontains=search_post))
        
    else:
        posts = Inventar.objects.all()

    
    pdf_enabled = True
    if len(posts) == 0:
        pdf_enabled = False
    return render(request, "list.html", {"query_results":posts, "search_post":search_post, "pdf_enabled":pdf_enabled})


# Create your views here.
