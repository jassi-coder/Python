from reportlab.platypus import SimpleDocTemplate,Table,Paragraph,TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
#data which we are going to display as tables
Data=[
    ["Course name","Duration","Price (Rs.)"],
    [
        "Full Stack development",
        "6 months",
        "28,500/-",
     ],
     [
      "Python development",
      "4 months",
      "20,500/-"],

     [
      "Mern development",
      "6 months",
      "27,500/-"],

      ["Web development",
       "6 months",
       "30,000/-"],
    
 
    
]
#Creating a Base Document Template of page size A4
pdf=SimpleDocTemplate("reciept.pdf",pagesize=A4)
#Standard stylesheet defined within reportlab itself
styles=getSampleStyleSheet()
#fetching the style od top level heading (Heading1)
title_style=styles["Heading1"]
#0:left,1:center,2:right
title_style.alignment=1

#Creating the paragraph with
#the heading text and passing the styles of it
title=Paragraph("Appwars Courses",title_style)

#Creates a table style object and in it,
#defines the styles row wise
#the tuples which look like coordinates
#are nothing but rows and columns
style=TableStyle(
    [
        ("BOX",(0,0),(-1,-1),1,colors.black),
        ("GRID",(0,0),(5,5),1,colors.black),
        ("BACKGROUND",(0,0),(3,0),colors.gray),
        ("TEXTCOLOR",(0,0),(-1,0),colors.whitesmoke),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

    ]
)

#Creates a table object and passes the style to it
table=Table(Data,style=style)

#final step which builds the
#actual pdf putting together all the elements
pdf.build([title,table])