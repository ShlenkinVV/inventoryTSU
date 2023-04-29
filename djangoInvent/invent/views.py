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
        # Basic table:
        pdf.add_page()
        n=item[0].num_kab
        pdf.cell(0,0, f"КАБИНЕТ { n }")
        pdf.ln()
        with pdf.table() as table:
            header = table.row()
            header.cell("Наименование")
            header.cell("Идентификатор")
            header.cell("Количество")
            header.cell("Ответсвенный")
            for data_row in item:
                row = table.row()
                row.cell(data_row.name)
                row.cell(data_row.num)
                row.cell(data_row.count)
                row.cell(data_row.response)
                
        pdf.output("my_pdf.pdf", 'F')

        #return HttpResponse("GOOOD")
        buffer = io.BytesIO()
        return FileResponse(open("my_pdf.pdf", "rb"))
    else:
        return HttpResponse("Нет объектов для печати!")


#################################################################################################################################

    # pdf = FPDF() 
    # pdf.add_page() 

    # pdf.set_font('Arial', 'B', 16) 
    # pdf.cell(40, 10, 'Sample PDF') 
    # pdf.ln()
    # for index, row in df.iterrows(): 
    #     for value in row: 
    #         pdf.cell(40, 10, str(value), border=1) 
    #     pdf.ln() 

    # # Convert dataframe to HTML table and add it to PDF 
    # #pdf.write_html(pd.DataFrame.to_html(df)) 
    
    # # Save the PDF 
    # pdf.output("my_pdf.pdf", 'F')

    # #return HttpResponse("GOOOD")
    # buffer = io.BytesIO()
    # return FileResponse(open("my_pdf.pdf", "rb"))

    ###########################################################################
  
    # buffer = io.BytesIO()

  
    # p = canvas.Canvas(buffer)


    # items = Inventar.objects.all()


    # pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    # p.setFont('Arial', 10)

    # data = [[0]*4 for i in range(4)]

    
    # for i, item in enumerate(items):
    #         data[i][0] = str(item.name).encode('utf-8')
    #         data[i][1] = str(item.num)
    #         data[i][2] = str(item.response).encode('utf-8')
    #         data[i][3] = str(item.count).encode('utf-8')

    # t=Table(data)
    
    # p.draw

####################################################################################################
    # for i, item in enumerate(items):
    #     p.drawString(80,750-(i*25), str(item.name).encode('utf-8'))
    #     p.drawString(130,750-(i*25), str(item.num))
    #     p.drawString(180,750-(i*25), str(item.response).encode('utf-8'))
    #     p.drawString(230,750-(i*25), str(item.count).encode('utf-8'))


    # Close the PDF object cleanly, and we're done.
    # p.showPage()
    # p.save()

    # # FileResponse sets the Content-Disposition header so that browsers
    # # present the option to save the file.
    # buffer.seek(0)
    # return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

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
