# 自制pdf文件
# step 1: 使用本地字符库, 地址/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf

from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont 
pdfmetrics.registerFont(TTFont('mytype', '/usr/share/fonts/myfont/MSYH.TTF'))  
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle


def pdf_create():
    story = []
    stylesheet=getSampleStyleSheet()
    normalStbyle = stylesheet['Normal']

    #表格数据：用法详见reportlab-userguide.pdf中chapter 7 Table
    component_data= [
        ['借款金额', '人民币: 1.00元'],
        ['借款期限','22 天'],
        ['借款期间','2017年11月12日起至2017年12月04日止'],
        ['起息日','2017年11月12日'],
        ['到期利息','人民币: 0.01元'],
        ['借款目的','资金周转'],
        ['还款方式','一次性还本付息'], 
        ['到期还款日', '2017年12月04日'],
    ]
    #创建表格对象，并设定各列宽度
    component_table = Table(component_data, colWidths=[80,430])
    #添加表格样式
    component_table.setStyle(TableStyle([
    ('FONTNAME',(0,0),(-1,-1), 'mytype'),#字体
    ('FONTSIZE',(0,0),(-1,-1),6),#字体大小
    # ('SPAN',(0,0),(3,0)),#合并第一行前三列
    # ('BACKGROUND',(0,0),(-1,0), colors.lightskyblue),#设置第一行背景颜色
    # ('SPAN',(-1,0),(-2,0)), #合并第一行后两列
    ('ALIGN',(-1,0),(-2,0),'LEFT'),#对齐
    ('VALIGN',(-1,0),(-2,0),'LEFT'),  #对齐
    ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.black),#设置表格框线为红色，线宽为0.5
    ]))
    story.append(component_table)

    doc = SimpleDocTemplate('/home/ubuntu/alan/python_related/create_pdf/rpt.pdf')
    doc.build(story)



if __name__ == '__main__':
    pdf_create()