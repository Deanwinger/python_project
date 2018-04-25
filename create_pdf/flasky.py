import os
basedir = os.path.realpath(__file__)
a = os.path.split(basedir)[0]
fonts_path = a + '/msyh.ttc'

from flask import Flask, make_response
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont 
pdfmetrics.registerFont(TTFont('mytype', fonts_path))
# from reportlab.pdfbase.ttfonts import TTFont 
# pdfmetrics.registerFont(TTFont('mytype', 'D:\python-related\create_pdf\msyh.ttc'))
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Line, Drawing
from reportlab.lib.colors import red, green

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

@app.route('/test', methods=['GET'])
def get_protocal():
    buff = BytesIO()
    buff = MyPrint(buff, 'A4').print_users()
    response = make_response(buff)
    response.headers["Content-Disposition"] = "attachment; filename=test.pdf"
    response.headers["Content-Type"] = "application/pdf"
    return response

def pdf_with_footer_and_headers():
    buff = BytesIO()
    doc = SimpleDocTemplate(buff)
    doc.build(story)
    pdf = buff.getvalue()
    buff.close()
    return pdf
    

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

# 用户增加页眉和页脚
class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # img = Image('/home/alanchen/work/pythons/python_project/create_pdf/btree.png')
        # img.drawHeight = 0
        # img.drawWidth = 30

        # Header
        parag2 = '''<para autoLeading="off" leading=18 leftIndent=30><br></br>
        <font face="mytype" fontsize=12><img src="/home/alanchen/work/pythons/python_project/create_pdf/yemei.jpeg" width="80" height="20" valign="bottom"/>  
        <img src="/home/alanchen/work/pythons/python_project/create_pdf/blank.jpeg" width="250" height="20" valign="top"/> 
        <b>GTDOLLAR数字资产ICO项目</b></font><br/>
        <br></br></para>'''
        # header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
        header = Paragraph(parag2, styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

        # Footer
        footer = Paragraph('This is a multi-line footer.  It goes on every page.   ' * 5, styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch/4,
                                leftMargin=inch/4,
                                topMargin=inch/2,
                                bottomMargin=inch/4,
                                pagesize=self.pagesize)

        # Our container for 'Flowable' objects
        story = []

        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        normalStyle = styles['Normal']
        # styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # users = User.objects.all()
        # users = ['a', 'b', 'c']
        # elements.append(Paragraph(' ', styles['Heading1']))
        # for i, user in enumerate(users):
        #     elements.append(Paragraph(user, styles['Normal']))

        # 添加页眉直线
        img = Drawing(400, 70)
        a = Line(20,50, 520, 50, strokeColor=colors.black, strokeWidth=1)
        img.add(a)
        story.append(img)

        parag1 = '''<para autoLeading="off" leading=18 leftIndent=130>
        <font face="mytype" fontsize=2></font></para>'''
        story.append(Paragraph(parag1, normalStyle))

        parag2 = '''<para autoLeading="off" leading=18 leftIndent=110><br></br>
        <font face="mytype" fontsize=12><img src="/home/alanchen/work/LS2018/GT-Dollar-API/app/material/yinzhang.jpeg" width="140" height="140" valign="top"/></font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag2, normalStyle))

        parag3 = '''<para autoLeading="off" leading=18 leftIndent=30>
        <font face="mytype" fontsize=14>发售人： <u>%s</u> （盖章）   <img src="/home/alanchen/work/LS2018/GT-Dollar-API/app/material/blank.jpeg" width="90 " height="0" valign="bottom"/>      认购人:  _______%s_______ （盖章）</font><br/>
        <br></br></para>'''% ('    alan    ', 'chen')
        story.append(Paragraph(parag3, normalStyle))

        parag4 = '''<para autoLeading="off" leading=18 leftIndent=130><br></br>
        <font face="mytype" fontsize=12><br/><br/></font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag4, normalStyle))

        parag5 = '''<para autoLeading="off" leading=18 leftIndent=30>
        <font face="mytype" fontsize=14>代表人(签字)：  ______%s______     <img src="/home/alanchen/work/LS2018/GT-Dollar-API/app/material/blank.jpeg" width="40" height="0" valign="bottom"/>          代表人(签字):  ________%s________</font><br/>
        <br></br></para>''' % ('alan', 'chen')
        story.append(Paragraph(parag5,normalStyle))



        doc.build(story, onFirstPage=self._header_footer, onLaterPages=self._header_footer)

        # Get the value of he BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf





if __name__ == '__main__':
    app.run(debug=True, port=8000)