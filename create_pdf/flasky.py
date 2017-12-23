from flask import Flask, make_response
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont 
pdfmetrics.registerFont(TTFont('mytype', '/usr/share/fonts/myfont/MSYH.TTF'))
# from reportlab.pdfbase.ttfonts import TTFont 
# pdfmetrics.registerFont(TTFont('mytype', 'D:\python-related\create_pdf\msyh.ttc'))
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle
from flask import Flask, make_response, send_file
from io import BytesIO
import base64
import zipfile



app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload_pdf():
    buff = get_zip_file()
    response = make_response(buff)
    response.headers["Content-Disposition"] = "attachment; filename=protocol.zip"
    response.headers["Content-Type"] = "application/zip"
    return response

def get_zip_file():
    pdf = pdf_loan_agreements()

    buffer=BytesIO()
    zfile = zipfile.ZipFile(buffer, 'a', zipfile.ZIP_DEFLATED, allowZip64=False)
    zfile.writestr('test.pdf', pdf)
    zfile.close()

    buffer.seek(0)
    return buffer.getvalue()


def pdf_loan_agreements():
    story = []
    stylesheet=getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    # 标题：段落的用法详见reportlab-userguide.pdf中chapter 6 Paragraph
    rpt_title = '<para autoLeading="off" fontSize=18 align=center><b><font face="mytype">借款协议</font></b><br/><br/><br/></para>'
    story.append(Paragraph(rpt_title,normalStyle))

    protocol_id = 'XS201712010101'
    name = 'Alan Chen'
    id_num = '1234567456789890X'
    borrower = '何桃'
    company_name = 'XX公司'
    BEC = '何桃'
    text = '''<para autoLeading="off" leading=20 leading=20>
    <font face="mytype" fontsize=9>协议编号: %s </font><br/><br></br>
    <font face="mytype" fontsize=9>甲方(出借人): %s, 以下称“甲方”</font><br/><br></br>
    <font face="mytype" fontsize=9>证件号码: %s</font><br/><br></br>
    <br></br><br></br>
    <font face="mytype" fontsize=9>乙方(借款人): %s, 以下称“乙方”</font><br/><br></br>
    <font face="mytype" fontsize=9>公司名称: %s</font><br/><br></br>
    <font face="mytype" fontsize=9>法定代表人: %s</font><br/><br></br>
    <br></br><br></br>
    <font face="mytype" fontsize=9>现各方经协商一致,依据合同法等有关规定达成如下条款:</font><br/><br></br>
    <font face="mytype" fontsize=9>第一条 借贷基本信息</font><br/><br></br>
    </para>''' % (protocol_id, name, id_num, borrower, company_name, BEC)
    story.append(Paragraph(text,normalStyle))

    # 表格1数据：用法详见reportlab-userguide.pdf中chapter 7 Table
    component_data= [
        ['借款金额', '人民币: 1.00元'],
        ['借款期限','22 天'],
        ['借款期间','2017年 11月 12日起至 2017年 12月 04日止'],
        ['起息日','2017年 11月 12日'],
        ['到期利息','人民币: 0.01元'],
        ['借款目的','资金周转'],
        ['还款方式','一次性还本付息'], 
        ['到期还款日', '2017年 12月 04日'],
    ]
    #创建表格对象，并设定各列宽度
    component_table = Table(component_data, colWidths=[50,390])
    #添加表格样式
    component_table.setStyle(TableStyle([
    ('FONTNAME',(0,0),(-1,-1), 'mytype'),#字体
    ('FONTSIZE',(0,0),(-1,-1),9),#字体大小
    ('ALIGN',(-1,0),(-2,0),'MIDDLE'),#对齐
    ('VALIGN',(-1,0),(-2,0),'MIDDLE'),  #对齐
    ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.black),#设置表格框线为红色，线宽为0.5
    ]))
    story.append(component_table)

    parag1 = '''<para autoLeading="off" leading=20><br></br>
    <font face="mytype" fontsize=9>第二条 乙方还款资金来源及担保</font><br/>
    <br></br>
    </para>''' 
    story.append(Paragraph(parag1,normalStyle))

    # 表格2数据：用法详见reportlab-userguide.pdf中chapter 7 Table
    component_data2= [
        ['出票人', 'XX公司'],
        ['收款人',' XX公司'],
        ['出票日期','2017年 01月 01日'],
        ['到期日期','2018年 12月 30日'],
        ['付款人(承兑人)','中国农业银行'],
        ['金额','人民币: 200元'],
    ]
    #创建表格对象，并设定各列宽度
    component_data2 = Table(component_data, colWidths=[100,340])
    #添加表格样式
    component_data2.setStyle(TableStyle([
    ('FONTNAME',(0,0),(-1,-1), 'mytype'),#字体
    ('FONTSIZE',(0,0),(-1,-1),9),#字体大小
    ('ALIGN',(-1,0),(-2,0),'MIDDLE'),#对齐
    ('VALIGN',(-1,0),(-2,0),'MIDDLE'),  #对齐
    ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.black),#设置表格框线为红色，线宽为0.5
    ]))
    story.append(component_data2)

    parag2 = '''<para autoLeading="off" leading=20><br></br>
    <font face="mytype" fontsize=9>第三条 甲方权利、义务</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag2,normalStyle))


    buff = BytesIO()
    doc = SimpleDocTemplate(buff)
    doc.build(story)
    pdf = buff.getvalue()
    buff.close()
    return pdf






if __name__ == '__main__':
    app.run(debug=True)