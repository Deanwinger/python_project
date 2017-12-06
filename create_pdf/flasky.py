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
import base64
from io import BytesIO


app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload_pdf():
    pdf = pdf_loan_agreements()
    response = make_response(pdf)
    response.headers["Content-Disposition"] = "attachment; filename=protocol.pdf"
    response.headers["Content-Type"] = "application/pdf"
    return response


def pdf_loan_agreements():
    story = []
    stylesheet=getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    # 标题：段落的用法详见reportlab-userguide.pdf中chapter 6 Paragraph
    rpt_title = '<para autoLeading="off" fontSize=15 align=center><b><font face="mytype">借款协议</font></b><br/><br/><br/></para>'
    story.append(Paragraph(rpt_title,normalStyle))

    protocol_id = 'XS201712010101'
    name = 'Alan Chen'
    id_num = '1234567456789890X'
    borrower = '何桃'
    company_name = '华为公司'
    BEC = '何桃'
    text = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>协议编号: %s </font><br/>
    <font face="mytype" fontsize=7>甲方(出借人): %s, 以下称“甲方”</font><br/>
    <font face="mytype" fontsize=7>证件号码: %s</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>乙方(借款人): %s, 以下称“乙方”</font><br/>
    <font face="mytype" fontsize=7>公司名称: %s</font><br/>
    <font face="mytype" fontsize=7>法定代表人: %s</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>丙方:深圳市榄盛咨询服务有限公司(简称“榄盛”、“www.lansheng8.com”),以下称“丙方”。</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>甲方、乙方系丙方网站——榄盛金融(www.lansheng8.com)注册会员,甲方、乙方承诺并保证其在丙方网站注册的信息是完全真实、准确、合法,用户名、密码系其本人持有和使用。甲方、乙方确认对本协议项下所涉一切行为具有完全民事行为能力、意思表示真实。</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>丙方系 www.lansheng8.com(以下简称“榄盛金融”)网站的所有人,有该网站的经营管理权,丙方为其注册会员提供投融资信息发布、咨询及交易管理等相关居间服务。</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>乙方有借款需求,委托丙方网站发布借款筹资信息,并承诺通过丙方平台居间服务所获得的借款用于合法的商业用途。</font><br/>
    <br></br>
    <font face="mytype" fontsize=7>甲方自愿通过丙方榄盛金融平台向乙方提供借款、成立借贷关系,并保证用以借出的款项具有完全的支配能力、是其合法所得。</font><br/>
    <br></br>
    <font face="mytype" fontsize=7>现各方经协商一致,依据合同法等有关规定达成如下条款:</font><br/>
    <font face="mytype" fontsize=7>第一条 借贷基本信息</font><br/>
    # </para>''' % (protocol_id, name, id_num, borrower, company_name, BEC)
    story.append(Paragraph(text,normalStyle))

    # 表格数据：用法详见reportlab-userguide.pdf中chapter 7 Table
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

    buff = BytesIO()
    doc = SimpleDocTemplate(buff)
    doc.build(story)
    pdf = buff.getvalue()
    buff.close()
    return pdf






if __name__ == '__main__':
    app.run(debug=True)