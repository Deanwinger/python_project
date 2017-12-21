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
from io import BytesIO
import base64


def pdf_loan_agreements():
    story = []
    stylesheet=getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    # 标题：段落的用法详见reportlab-userguide.pdf中chapter 6 Paragraph
    rpt_title = '<para autoLeading="off" fontSize=15 align=center><b><font face="mytype">宜人贷借款协议</font></b><br/><br/><br/></para>'
    story.append(Paragraph(rpt_title,normalStyle))

    sub_title = '<para autoLeading="off" fontSize=10 align=right><font face="mytype">协议编号:B0000108424300008266649</font><br/><br/><br/></para>'
    story.append(Paragraph(sub_title,normalStyle))

    scnd_title = '<para autoLeading="off" fontSize=11 align=center><b><font face="mytype">第一部分:借款信息及相关明细</font></b><br/><br/><br/></para>'
    story.append(Paragraph(scnd_title,normalStyle))

    # text = '''<para autoLeading="off">
    # <font face="mytype" fontsize=7>协议编号:XS201712010101</font><br/>
    # <font face="mytype" fontsize=7>甲方(出借人): 蔡玲旋, 以下称“甲方”</font><br/>
    # <font face="mytype" fontsize=7>证件号码: 1234567456789890X</font><br/>
    # <br></br><br></br>
    # <font face="mytype" fontsize=7>乙方(借款人): 何桃, 以下称“乙方”</font><br/>
    # <font face="mytype" fontsize=7>公司名称: 华为公司</font><br/>
    # <font face="mytype" fontsize=7>法定代表人: 何桃</font><br/>
    # <br></br><br></br>
    # <font face="mytype" fontsize=7>丙方:深圳市榄盛咨询服务有限公司(简称“榄盛”、“www.lansheng8.com”),以下称“丙方”。</font><br/>
    # <br></br><br></br>
    # <font face="mytype" fontsize=7>甲方、乙方系丙方网站——榄盛金融(www.lansheng8.com)注册会员,甲方、乙方承诺并保证其在丙
    #     方网站注册的信息是完全真实、准确、合法,用户名、密码系其本人持有和使用。甲方、乙方确认对本协
    #     议项下所涉一切行为具有完全民事行为能力、意思表示真实。</font><br/>
    # <br></br><br></br>
    # <font face="mytype" fontsize=7>丙方系 www.lansheng8.com(以下简称“榄盛金融”)网站的所有人,有该网站的经营管理权,丙方为其
    #     注册会员提供投融资信息发布、咨询及交易管理等相关居间服务。</font><br/>
    # <br></br><br></br>
    # <font face="mytype" fontsize=7>乙方有借款需求,委托丙方网站发布借款筹资信息,并承诺通过丙方平台居间服务所获得的借款用于合法
    #     的商业用途。</font><br/>
    # <br></br>
    #     <font face="mytype" fontsize=7>甲方自愿通过丙方榄盛金融平台向乙方提供借款、成立借贷关系,并保证用以借出的款项具有完全的支配
    #     能力、是其合法所得。</font><br/>
    # <br></br>
    # <font face="mytype" fontsize=7>现各方经协商一致,依据合同法等有关规定达成如下条款:</font><br/>
    # </para>'''
    # story.append(Paragraph(text,normalStyle))

    # 表格数据：用法详见reportlab-userguide.pdf中chapter 7 Table
    component_data= [
        ['出借人:详见《宜人贷借款协议》附件', '', '', ''],
        ['借款人', '', '', ''],
        ['姓名(名称)','张秀', '', ''],
        ['证件类型','身份证',  '证件号码', '152301197907151042'],
        ['借款明细', '', '', ''],
        ['借款本金','人民币(大写)壹拾壹万玖仟伍佰元整,人民币(小写)119500.00元', '', ''],
        ['借款人收款账户','户名:张秀', '账号:6222000609400204402', ''],
        ['','开户行:中国工商银行', '', ''], 
        # ['借款利率','12.0%/年', '每月利息', '详见《还款事项提醒函》'], 
        # ['还款方式', '每月等额本息', '还款期数', '36个月'],
        # ['借款用途','日常消费(女,38岁,内蒙古自治区兴安盟)'], 
        # ['月偿还本息数额', '人民币(大写)叁仟玖佰陆拾玖元壹角壹分,人民币(小写)3969.11元'],
        # ['借款人还款账户', '户名:张秀', '账号:6222000609400204402'],
        # ['','开户行:中国工商银行'], 
    ]
    #创建表格对象，并设定各列宽度
    # component_table = Table(component_data, colWidths=[50,390])
    component_table = Table(component_data, colWidths=[105,105,105,125])
    #添加表格样式
    component_table.setStyle(TableStyle([
    ('FONTNAME',(0,0),(-1,-1), 'mytype'),#字体
    ('FONTSIZE',(0,0),(-1,-1),6),#字体大小
    # ('SPAN',(0,0),(3,0)),#合并第一行前三列
    # ('SPAN',(-1,0),(-2,0)), #合并第一行后两列
    ('SPAN',(0,0),(3,0)),#合并第一行前三列
    ('SPAN',(0,1),(3,1)),#合并第二行前三列
    ('SPAN',(1,2),(3,2)),#合并第三行前三列
    # ('SPAN',(0,0),(4,0)),#合并第四行前三列
    ('SPAN',(0,4),(3,4)),#合并第五行前三列
    ('SPAN',(1,5),(3,5)),#合并第六行前三列
    ('SPAN',(0,6),(0,7)),#合并第七, 八行前三列
    ('SPAN',(2,6),(3,6)),#合并第七, 八行前三列
    ('SPAN',(1,7),(3,7)),#合并第八行前三列
    # ('SPAN',(0,0),(4,0)),#合并第九行前三列
    # ('SPAN',(0,0),(4,0)),#合并第十行前三列
    # ('SPAN',(0,0),(4,0)),#合并第十一行前三列
    # ('SPAN',(0,0),(4,0)),#合并第十二行前三列
    # ('SPAN',(0,0),(4,0)),#合并第十三行前三列
    # ('SPAN',(0,0),(4,0)),#合并第十四行前三列
    ('ALIGN',(0,6),(1,6),'LEFT'),#对齐
    ('VALIGN',(0,6),(0,6),'MIDDLE'),  #对齐
    # ('ALIGN',(-1,0),(-2,0),'LEFT'),#对齐
    # ('VALIGN',(-1,0),(-2,0),'LEFT'),  #对齐
    ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.black),#设置表格框线为红色，线宽为0.5
    ]))
    story.append(component_table)

    # buff = BytesIO()
    # doc = SimpleDocTemplate('/home/ubuntu/alan/python_related/create_pdf/loan_agreements.pdf')
    # doc.build(story)
    # pdf = buff.getvalue()
    # buff.close()
    # return pdf
    doc = SimpleDocTemplate('/home/ubuntu/alan/python_related/create_pdf/sa_loan_agreements.pdf')
    doc.build(story)
    return

    



if __name__ == '__main__':
    pdf_loan_agreements()    