# 自制pdf文件

from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont 
pdfmetrics.registerFont(TTFont('mytype', '/usr/share/fonts/myfont/MSYH.TTF'))
# pdfmetrics.registerFont(TTFont('mytype', 'D:\python-related\create_pdf\msyh.ttc'))   
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
    rpt_title = '<para autoLeading="off" fontSize=15 align=center><b><font face="mytype">授权委托书</font></b><br/><br/><br/></para>'
    story.append(Paragraph(rpt_title,normalStyle))

    parag1 = '''<para autoLeading="off" leading=18><br></br><br></br>
    <font face="mytype" fontsize=9>授权人:---</font><br/>
    </para>'''
    story.append(Paragraph(parag1,normalStyle))

    parag2 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>证件类型:身份证</font><br/>
    </para>'''
    story.append(Paragraph(parag2,normalStyle))

    parag3 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>证件号码:-----------</font><br/>
    </para>'''
    story.append(Paragraph(parag3,normalStyle))

    parag4 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>被授权人:深圳市榄盛资讯服务 有限公司 (以下简称:榄盛公司)</font><br/>
    </para>'''
    story.append(Paragraph(parag4,normalStyle))

    parag5 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>为了让被授权人在服务期内能够更好的为授权人提供服务,现授权人特此向被授权人做出如下授权:</font><br/>
    <br></br></para>'''
    story.append(Paragraph(parag5,normalStyle))

    parag6 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1、授权范围:</font><br/>
    <br></br></para>'''
    story.append(Paragraph(parag6,normalStyle))

    parag7 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>(1)代授权人在榄盛金融平台上进行榄盛金融账号的注册并将授权人姓名或者名称、证件类型、证件号码及授权人名下任一在用银行卡账号提交给资金存管机构,以便为授权人开设账户,供出借资金存管使用。</font><br/>
    </para>'''
    story.append(Paragraph(parag7,normalStyle))

    parag8 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>(2)代授权人管理用于榄盛金融平台业务的数字证书及数字证书的更新。</font><br/>
    </para>'''
    story.append(Paragraph(parag8,normalStyle))

    parag9 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>(3)代授权人确认《榄盛金融借款协议》的所有条款,并使用授权人的数字证书以授权人的名义签署协议(包括但不限于《榄盛金融借款协议》及相应附件、《债权转让协议》等)。</font><br/>
    </para>'''
    story.append(Paragraph(parag9,normalStyle))

    parag10 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>(4)在服务期内,被授权人自行或委托第三方进行还款管理;</font><br/>
    </para>'''
    story.append(Paragraph(parag10,normalStyle))

    parag11 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>(5)在借款人提前还款、出借人退出等各种情况下,代授权人进行债权转让,使用授权人的数字证书签署《债权转让协议》并代为发出债权转让通知。</font><br/>
    </para>'''
    story.append(Paragraph(parag11,normalStyle))

    parag12 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>(6)在借款人发生或可能发生违约时,授权被授权人采取以下一项或几项救济措施:</font><br/>
    </para>'''
    story.append(Paragraph(parag12,normalStyle))

    parag13 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>立即暂缓、取消发放全部或部分借款;</font><br/>
    </para>'''
    story.append(Paragraph(parag13,normalStyle))

    parag14 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>宣布借款全部提前到期, 要求借款人应立即偿还所有应付款项;</font><br/>
    </para>'''
    story.append(Paragraph(parag14,normalStyle))

    parag15 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>解除或提前终止《榄盛金融借款协议》;</font><br/>
    </para>'''
    story.append(Paragraph(parag15,normalStyle))

    parag16 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>采取法律、法规以及本协议约定的其他救济措施。</font><br/>
    <br></br></para>'''
    story.append(Paragraph(parag16,normalStyle))

    parag17 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2、授权期限:</font><br/>
    <br></br></para>'''
    story.append(Paragraph(parag17,normalStyle))

    parag18 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>本授权委托书自授权人签署时生效,授权人可通过包括但不限于手写签名或盖章、点击、勾选、电子签名、数据电文等方式签署本委托书。除授权人作出书面相反意思表示外,本《授权委托书》之授权期限与《出借信息咨询与服务协议》(编号:---------------)期限一致。</font><br/>
    </para>'''
    story.append(Paragraph(parag18,normalStyle))

    parag19 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>授权人:---签署</font><br/>
    </para>'''
    story.append(Paragraph(parag19,normalStyle))

    parag20 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>签署日期:---年---月---日</font><br/>
    </para>'''
    story.append(Paragraph(parag20,normalStyle))

    doc = SimpleDocTemplate('sa_contract.pdf')
    doc.build(story)
    return

    



if __name__ == '__main__':
    pdf_loan_agreements()    

