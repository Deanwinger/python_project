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
from reportlab.lib.units import inch, mm
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
    response.headers["Content-Disposition"] = "attachment; filename=protocol.zip" # 如果要进行浏览器预览，需要注释掉该header
    response.headers["Content-Type"] = "application/zip"
    return response

@app.route('/test', methods=['GET'])
def get_protocal():
    buff = BytesIO()
    buff = MyPrint(buff, 'Letter').print_users()
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

    # 用户增加页眉和页脚
    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # img = Image('/home/alanchen/work/pythons/python_project/create_pdf/btree.png')
        # img.drawHeight = 0
        # img.drawWidth = 30

        # Header
        parag1 = '''<para autoLeading="off" leading=18 leftIndent=30><br></br>
        <font face="mytype" fontsize=12><img src="/home/alanchen/work/pythons/python_project/create_pdf/yemei.jpeg" width="80" height="20" valign="bottom"/>  
        <img src="/home/alanchen/work/pythons/python_project/create_pdf/blank.jpeg" width="270" height="20" valign="top"/> 
        <b>GTDOLLAR数字资产ICO项目</b></font><br/>
        <br></br></para>'''
        # header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
        header = Paragraph(parag1, styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

        # 添加页眉直线
        # img = Drawing(400, 70)
        # a = Line(20,50, 520, 50, strokeColor=colors.black, strokeWidth=1)
        # img.add(a)
        parag2 = '''<para autoLeading="off" leading=18 leftIndent=30><br></br>
        <font face="mytype" fontsize=12>  
        <img src="/home/alanchen/work/pythons/python_project/create_pdf/black.png" width="520" height="2" valign="top"/> </font><br/>
        <br></br></para>'''
        line = Paragraph(parag2, styles['Normal'])
        w, h = line.wrap(doc.width, doc.topMargin)
        line.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h - 30)

        # Footer
        # parag3 = '''<para autoLeading="off" leading=18 align=center><br></br>
        # <font face="mytype" fontsize=12>第 %d 页</font><br/>
        # <br></br></para>''' % 2
        # footer = Paragraph(parag3, styles['Normal'])
        # w, h = footer.wrap(doc.width, doc.bottomMargin)
        # footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch/6,
                                leftMargin=inch/4,
                                topMargin=inch/2,
                                bottomMargin=inch/6,
                                pagesize=self.pagesize)

        # Our container for 'Flowable' objects
        story = []

        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        normalStyle = styles['Normal']

        title = '<para autoLeading="off" fontSize=18 align=center><br/><br/><br/><b><font face="mytype">私募认购合同</font></b><br/><br/><br/></para>'
        story.append(Paragraph(title,normalStyle))

        parag6 = '''<para autoLeading="off" leading=12 leftIndent=30>
        <font face="mytype" fontsize=12>第一条 总则</font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag6,normalStyle))
        
        parag7 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>1.订立本认购合同的目的是明确本认购合同当事人的权利义务、规范GTDOLLAR数字资产项目（以下简称“本项目”）的运作，保护本项目货币资产持有人的权益。</font></para>'''
        story.append(Paragraph(parag7,normalStyle))

        parag8 = '''<para autoLeading="off" leading=18 leftIndent=50>
        <font face="mytype" fontsize=12>2.订立本认购合同的原则: </font></para>'''
        story.append(Paragraph(parag8,normalStyle))
        
        parag9 = '''<para autoLeading="off" leading=18 leftIndent=50>
        <font face="mytype" fontsize=12>订立本认购合同的原则是平等自愿、诚实信用、充分保护本项目货币资产持有人的权益。</font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag9,normalStyle))

        parag10 = '''<para autoLeading="off" leading=25 leftIndent=30 rightIndent=50>
        <font face="mytype" fontsize=12>第二条、项目基本情况</font></para>'''
        story.append(Paragraph(parag10,normalStyle))
        
        parag11 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>1.项目名称: “GTDOLLAR数字资产”项目（即：ICO数字货币项目）。</font></para>'''
        story.append(Paragraph(parag11,normalStyle))
        
        parag12 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>2.本项目货币资产持有人以其所认购的“GTDOLLAR数字资产”比例承担有限责任，分享经营利益，和分担经营风险。</font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag12,normalStyle))

        parag13 = '''<para autoLeading="off" leading=25 leftIndent=30 rightIndent=50>
        <font face="mytype" fontsize=12>第三条 发行数量、发行单价、资金总额 </font></para>'''
        story.append(Paragraph(parag13,normalStyle))

        parag14 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>1.项目运作流程：</font></para>'''
        story.append(Paragraph(parag14,normalStyle))
        
        parag15 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>2.本项目利用区块链总发行量为：30 亿枚，本次募集每枚单价为：1 美金，总额为：30 亿美金;</font></para>'''
        story.append(Paragraph(parag15,normalStyle))

        parag16 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>3.本项目 ICO 上市原始股发售价格：2美金/枚，GTC 市值60亿美金；</font></para>'''
        story.append(Paragraph(parag16,normalStyle))
        
        parag17 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>4.本项目 ICO 上市挂牌价格：4 美金/枚，GTC 市值 120 亿美金。</font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag17,normalStyle))

        parag18 = '''<para autoLeading="off" leading=25 leftIndent=30 rightIndent=50>
        <font face="mytype" fontsize=12>第四条 认购人权利与义务 </font></para>'''
        story.append(Paragraph(parag18,normalStyle))

        parag19 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>1.认购人依据自身能力，根据本合同第三条第 2 点之规定，对本项目 资产进行认购：</font></para>'''
        story.append(Paragraph(parag19,normalStyle))
        
        parag20 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>认购人                  ，认购		            枚（认购资产总额	                 万美金）；</font></para>'''
        story.append(Paragraph(parag20,normalStyle))

        parag21 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>2.认购时间：	    年	    月		日。认购人须于以上认购时间之前, 100%支付其认购金(即：                 万美金)，即视为完成本轮资产认购，认购人享受1:2的配额期权；</font></para>'''
        story.append(Paragraph(parag21,normalStyle))
        
        parag22 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>3.认购人的全部资本分为等额数字资产币。认购人以数字资产币形式出现，数字资产币是 GTDOLLAR 签发的数字资产币。数字货币采取区块链记名方式，认购人所持有的数字资产币即为其区块链凭证。</font></para>'''
        story.append(Paragraph(parag22,normalStyle))

        parag23 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>4.认购人可对认购总额的（包括配额部分）的货币资产进行流通销售。原始股挂牌上市七个工作日前，认购人须支付其配额期权部分的全部认购金，未能及时支付的该部分配额资产，项目将予以收回。</font></para>'''
        story.append(Paragraph(parag23,normalStyle))
        
        parag24 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>5.原始股发售完成 15 个工作日后, 如本项目未能成功上市ICO交易所，本项目将全额退回各认购人已支付的认购金额款项。</font><br/>
        <br></br><br/><br></br><br></br><br></br><br></br></para>'''
        story.append(Paragraph(parag24,normalStyle))

        parag25 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>6.上市锁定期：为维持本项目上市期间经营管理及价格的稳定性，确保资产价格上升，保障资产所有人利益最大化，ICO挂牌上市之日起6个月内视为上市锁定期。期间，
        认购人手中剩余货币资产均不得流通交易；上市锁定期满后，方可自由交易其剩余的所有货币资产。</font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag25,normalStyle))

        parag26 = '''<para autoLeading="off" leading=25 leftIndent=30 rightIndent=50>
        <font face="mytype" fontsize=12>第五条 附则  </font></para>'''
        story.append(Paragraph(parag26,normalStyle))

        parag27 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>1.认购人应将认购的款项汇至指定银行账户。汇款时间以款项收到日期为准。汇款账户：</font></para>'''
        story.append(Paragraph(parag27,normalStyle))

        parag28 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>2.由于不可抗力因素，致使本合同无法履行的，经双方一致同意后，可以终止本合同。</font></para>'''
        story.append(Paragraph(parag28,normalStyle))

        parag29 = '''<para autoLeading="off" leading=18 leftIndent=50 rightIndent=50>
        <font face="mytype" fontsize=12>3.本合同一式_贰_份，签约人各执一份，于	   年	    月	  日在  地签订，并自签订后生效。</font><br/>
        <br></br></para>'''
        story.append(Paragraph(parag29,normalStyle))
        ########################################################################################
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

        doc.build(story, onFirstPage=self._header_footer, onLaterPages=self._header_footer, canvasmaker=NumberedCanvas)

        # Get the value of he BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf

# 统计页数
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
 
    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()
 
    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
 
    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(118 * mm, 15 * mm + (0.2 * inch),
                             "page %d of %d" % (self._pageNumber, page_count))




if __name__ == '__main__':
    app.run(debug=True, port=8000)