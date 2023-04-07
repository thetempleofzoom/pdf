from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

def lines(x1, x2, y):
    while 297-y >10:
        pdf.line(x1, y, x2,y)
        y = y+10

for index, row in df.iterrows():
    pdf.add_page()
    #header
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(254,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)

    lines(10,200, 21)

    #footer
    pdf.ln(265)
    pdf.set_font('Times', 'I', 8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=8, txt=row['Topic'], align="R")

    for i in range(row['Pages']-1):
        pdf.add_page()

        lines(10, 200, 11)
        #footer
        pdf.set_xy(10, 287)
        pdf.set_font('Times', 'I', 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, txt=row['Topic'], align="R")


        
pdf.output("output.pdf", "F")
