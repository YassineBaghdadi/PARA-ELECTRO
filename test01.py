from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import sqlite3

from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph

con = sqlite3.connect('src/db.db')
headers = []
for i in con.execute('PRAGMA table_info(products);').fetchall():
    headers.append(i[1])



doc = SimpleDocTemplate('test.pdf', pagesize=letter)
# #
# pdfmetrics.registerFont(TTFont('s', 'src/fonts/Sansation-Regular.ttf'))
# # pdfmetrics.registerFont(TTFont('s', 'src/fonts/blackjack.otf'))
# # pdfmetrics.registerFont(TTFont('gvr', 'src/fonts/GreatVibes-Regular.otf'))
# # pdfmetrics.registerFont(TTFont('ksr', 'src/fonts/KaushanScript-regular.otf'))
# pdfmetrics.registerFont(TTFont('p', 'src/fonts/Pacifico.ttf'))
# pdfmetrics.registerFont(TTFont('head', 'src/fonts/SEASRN__.ttf'))
#
# doc.setFont('s', 10)
# doc.drawString(100, 100, 'Yassine Baghdadi')
import pandas as pd
styles_list = getSampleStyleSheet()
data = [headers]
for i in con.execute('SELECT * FROM products').fetchall():
    tt = []
    for c in i:
        tt.append(Paragraph(str(c), styles_list['Normal']))
    data.append(tt)

df = pd.DataFrame(data=data, columns=headers)
df.reset_index(drop=True, inplace=True)

title = Paragraph('PARA-ELECTRO', styles_list['title'], )


table = Table(data, )
style = TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)
                    ])

width, height = letter
table.setStyle(style)
# table.drawOn(doc, 50, 700)
elem = [title, table]
doc.build(elem)