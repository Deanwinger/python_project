# 自制pdf文件
# step 1: 使用本地字符库, 地址/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf
# 目前的策略, 先本地生成, 然后传输, 接着删除本地记录

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
import base64

def pdf_loan_agreements():
    story = []
    stylesheet=getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    # 标题：段落的用法详见reportlab-userguide.pdf中chapter 6 Paragraph
    rpt_title = '<para autoLeading="off" fontSize=15 align=center><b><font face="mytype">借款协议</font></b><br/><br/><br/></para>'
    story.append(Paragraph(rpt_title,normalStyle))

    text = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>协议编号:XS201712010101</font><br/>
    <font face="mytype" fontsize=7>甲方(出借人): 蔡玲旋, 以下称“甲方”</font><br/>
    <font face="mytype" fontsize=7>证件号码: 1234567456789890X</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>乙方(借款人): 何桃, 以下称“乙方”</font><br/>
    <font face="mytype" fontsize=7>公司名称: 华为公司</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>丙方:深圳市榄盛咨询服务有限公司(简称“榄盛”、“www.lansheng8.com”),以下称“丙方”。</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>甲方、乙方系丙方网站——榄盛金融(www.lansheng8.com)注册会员,甲方、乙方承诺并保证其在丙
        方网站注册的信息是完全真实、准确、合法,用户名、密码系其本人持有和使用。甲方、乙方确认对本协
        议项下所涉一切行为具有完全民事行为能力、意思表示真实。</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>丙方系 www.lansheng8.com(以下简称“榄盛金融”)网站的所有人,有该网站的经营管理权,丙方为其
        注册会员提供投融资信息发布、咨询及交易管理等相关居间服务。</font><br/>
    <br></br><br></br>
    <font face="mytype" fontsize=7>乙方有借款需求,委托丙方网站发布借款筹资信息,并承诺通过丙方平台居间服务所获得的借款用于合法
        的商业用途。</font><br/>
    <br></br>
        <font face="mytype" fontsize=7>甲方自愿通过丙方榄盛金融平台向乙方提供借款、成立借贷关系,并保证用以借出的款项具有完全的支配
        能力、是其合法所得。</font><br/>
    <br></br>
    <font face="mytype" fontsize=7>现各方经协商一致,依据合同法等有关规定达成如下条款:</font><br/>
    <font face="mytype" fontsize=7>第一条 借贷基本信息</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
        <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
        <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
        <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
        <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    
    # </para>'''
    story.append(Paragraph(text,normalStyle))

    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    #     <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    #     <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    #     <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>

   

    # text = '''<para autoLeading="off" fontSize=8><font face="mytype" >程度定义：</font><br/>
    # <font face="mytype" color=red>1.Blocker：指系统无法执行。</font><br/><font face="mytype" fontsize=7>例如：系统无法启动或退出等</font><br/>
    # <font face="mytype" color=orange>2.Critical：指系统崩溃或严重资源不足、应用模块无法启动或异常退出、无法测试、造成系统不稳定。</font><br/>
    # <font face="mytype" fontsize=7>例如：各类崩溃、死机、应用无法启动或退出、按键无响应、整屏花屏、死循环、数据丢失、安装错误等
    # </font><br/>
    # <font face="mytype" color=darkblue>3.Major：指影响系统功能或操作，主要功能存在严重缺陷，但不会影响到系统稳定性、性能缺陷</font><br/><font face="mytype" fontsize=7>例如：功能未做、功能实现与需求不一致、功能错误、声音问题、流程不正确、兼容性问题、查询结果不正确、性能不达标等
    # </font><br/>
    # <font face="mytype" color=royalblue>4.Minor：指界面显示类问题</font><br/>
    # <font face="mytype" fontsize=7>例如：界面错误、边界错误、提示信息错误、翻页错误、兼容性问题、界面样式不统一、别字、排列不整齐，字体不符规范、内容、格式、滚动条等等
    # </font><br/>
    # <font face="mytype" color=grey>5.Trivial：本状态保留暂时不用</font><br/>
    # </para>'''
    # story.append(Paragraph(text,normalStyle))

    # text = '<para autoLeading="off" fontSize=9><br/><br/><br/><b><font face="mytype">五、BUGLIST：</font></b><br/></para>'
    # story.append(Paragraph(text,normalStyle))

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

    doc = SimpleDocTemplate('/home/ubuntu/alan/python_related/create_pdf/loan_agreements.pdf')
    doc.build(story)
    with open('/home/ubuntu/alan/python_related/create_pdf/loan_agreements.pdf') as fp:
        buff = base64.b64encode(fp.read().encode('utf-8'))
        print(buff)



if __name__ == '__main__':
    pdf_loan_agreements()    