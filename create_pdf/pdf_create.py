# 自制pdf文件

from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont 
# pdfmetrics.registerFont(TTFont('mytype', '/usr/share/fonts/myfont/MSYH.TTF'))
pdfmetrics.registerFont(TTFont('mytype', 'D:\python-related\create_pdf\msyh.ttc'))   
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

    scnd_title = '<para autoLeading="off" fontSize=11 align=center><b><font face="mytype">第一部分:借款信息及相关明细</font></b><br/><br/></para>'
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
        ['借款利率','12.0%/年', '每月利息', '详见《还款事项提醒函》'], 
        ['还款方式', '每月等额本息', '还款期数', '36个月'],
        ['借款用途','日常消费(女,38岁,内蒙古自治区兴安盟)'], 
        ['月偿还本息数额', '人民币(大写)叁仟玖佰陆拾玖元壹角壹分,人民币(小写)3969.11元'],
        ['借款人还款账户', '户名:张秀', '账号:6222000609400204402'],
        ['','开户行:中国工商银行'], 
        ['注：借款人线上主动还款的，可不填写还款账户信息。', '', '', '']
    ]
    #创建表格对象，并设定各列宽度
    # component_table = Table(component_data, colWidths=[50,390])
    component_table = Table(component_data, colWidths=[95,105,105,125])
    #添加表格样式
    component_table.setStyle(TableStyle([
    ('FONTNAME',(0,0),(-1,-1), 'mytype'),#字体
    ('FONTSIZE',(0,0),(-1,-1),9),#字体大小
    ('LEADING',(0,0),(-1,-1),9),#设置行距
    ('SPAN',(0,0),(3,0)),#合并第一行前三列
    ('SPAN',(0,1),(3,1)),#合并第二行前三列
    ('SPAN',(1,2),(3,2)),#合并第三行前三列
    ('SPAN',(0,4),(3,4)),#合并第五行前三列
    ('SPAN',(1,5),(3,5)),#合并第六行前三列
    ('SPAN',(0,6),(0,7)),#合并第七, 八行前三列
    ('SPAN',(2,6),(3,6)),#合并第七, 行前三列
    ('SPAN',(1,7),(3,7)),#合并第八行前三列
    ('SPAN',(1,10),(3,10)),#合并第十一行前三列
    ('SPAN',(1,11),(3,11)),#合并第十二行前三列
    ('SPAN',(2,12),(3,12)),#合并第十三行前三列
    ('SPAN',(1,13),(3,13)),#合并第十四行前三列
    ('SPAN',(0,14),(3,14)),#合并第十四行前三列
    ('ALIGN',(0,6),(1,6),'LEFT'),#对齐
    ('VALIGN',(0,6),(0,6),'MIDDLE'),  #对齐
    ('LINEBEFORE',(0,0),(0,-2),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-2),0.5,colors.black),#设置表格框线为黑色，线宽为0.5
    ]))
    story.append(component_table)

    parag1 = '''<para autoLeading="off" leading=18 align=center><br></br><br></br>
    <font face="mytype" fontsize=9>第二部分：本协议相关具体条款</font><br/>
    </para>'''
    story.append(Paragraph(parag1,normalStyle))

    parag2 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>第1条 名词定义</font><br/>
    </para>'''
    story.append(Paragraph(parag2,normalStyle))

    parag3 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>除非上下文另有解释，下列用语具有以下含义：</font><br/>
    </para>'''
    story.append(Paragraph(parag3,normalStyle))

    parag4 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1.1 本协议：指本《宜人贷借款协议》第一部分、第二部分及所有附件中的任何条款、明细和信息。</font><br/>
    </para>'''
    story.append(Paragraph(parag4,normalStyle))

    parag6 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1.3 借款人：指本协议第一部分中列明的借款人，为符合中华人民共和国法律规定的具有完全民事权利能力和民事行为能力，能独立行使本协议项下权利和履行本协议项下义务的自然人、法人及其他组织。借款人为“宜人贷平台”的实名注册用户，在宜人贷平台上发布需求信息，从出借人处获得资金。</font><br/>
    </para>'''
    story.append(Paragraph(parag6,normalStyle))

    parag7 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1.4 宜人贷平台：指恒诚科技发展（北京）有限公司（以下简称“恒诚公司”）经营的提供网络借贷信息中介服务的互联网平台。</font><br/>
    </para>'''
    story.append(Paragraph(parag7,normalStyle))

    parag8 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1.5 支付机构：指在出借人、借款人、服务方等各方主体之间作为中介机构提供资金转移服务的银行或非银行机构。</font><br/>
    </para>'''
    story.append(Paragraph(parag8,normalStyle))

    parag9 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1.6 资金存管机构：指为网络借贷业务提供资金存管服务的商业银行，亦可称为“存管人”。本协议中特指与恒诚公司签署存管合同（具体名称以实际签署协议为准）、为宜人贷平台的网络借贷业务提供资金存管服务的银行。</font><br/>
    </para>'''
    story.append(Paragraph(parag9,normalStyle))

    parag10 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1.7 借款出借日期：指出借人通过支付机构或（及）资金存管机构将出借款项支付至借款人收款账户之日。</font><br/>
    </para>'''
    story.append(Paragraph(parag10,normalStyle))

    parag11 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>第2条 双方的权利及义务</font><br/>
    </para>'''
    story.append(Paragraph(parag11,normalStyle))

    parag12 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.1 出借人的权利及义务</font><br/>
    </para>'''
    story.append(Paragraph(parag12,normalStyle))

    parag13 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.1.1 出借人已了解本协议所有内容并自愿依照本协议相关约定行使相关权利、履行相关义务。</font><br/>
    </para>'''
    story.append(Paragraph(parag13,normalStyle))

    parag14 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.1.2 出借人有自行选择借款人，并最终决定是否出借资金给特定借款人的权利。</font><br/>
    </para>'''
    story.append(Paragraph(parag14,normalStyle))

    parag15 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.1.3 出借人应基于合法目的使用宜人贷平台,不得通过该平台从事任何违法犯罪活动。</font><br/>
    </para>'''
    story.append(Paragraph(parag15,normalStyle))

    parag16 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.1.4 出借人按照本协议的约定履行出借义务。</font><br/>
    </para>'''
    story.append(Paragraph(parag16,normalStyle))

    parag17 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.1.5 出借人有权通过宜人贷平台查看出借相关信息及借款人还款情况。</font><br/>
    </para>'''
    story.append(Paragraph(parag17,normalStyle))

    parag18 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.1.6 出借人在资金出借、转让过程中产生的相关税费，由出借人自行向主管税务机关申报、缴纳。</font><br/>
    </para>'''
    story.append(Paragraph(parag18,normalStyle))

    parag19 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2 借款人的权利及义务</font><br/>
    </para>'''
    story.append(Paragraph(parag19,normalStyle))

    parag20 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.1 借款人已认真阅读和理解本协议所有内容并自愿按本协议相关约定行使相关权利、履行相关义务。</font><br/>
    </para>'''
    story.append(Paragraph(parag20,normalStyle))

    parag21 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.2 借款人按本协议约定的借款明细及《还款事项提醒函》列明的还款明细履行还款义务，按月足额偿还本金和利息。</font><br/>
    </para>'''
    story.append(Paragraph(parag21,normalStyle))

    parag22 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.3 出借人委托恒诚公司要求借款人按本协议约定进行还款时，借款人有义务无条件地、及时地按照恒诚公司发出的要求进行还款并向恒诚公司提供协助。</font><br/>
    </para>'''
    story.append(Paragraph(parag22,normalStyle))

    parag23 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.4 借款人成功获得借款后，每个自然月履行一次还款义务。每月还款日期=借款出借日期（例如，借款出借日期为6月26日，借款人的还款日期为自7月起的每月26日），如还款当月无上述日期，则该月的最后一天为当月的还款日。如还款日为法定假日或公休日，还款日不顺延。</font><br/>
    </para>'''
    story.append(Paragraph(parag23,normalStyle))

    parag24 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.5 借款人可通过委托划扣和主动支付两种方式进行还款。借款人采用委托划扣方式还款的，借款人委托恒诚公司通过支付机构或（及）资金存管机构每月从本协议第一部分约定的还款账户中准确划扣及支付月偿还本息数额。</font><br/>
    </para>'''
    story.append(Paragraph(parag24,normalStyle))

    parag25 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=25>2.2.6 借款人采用委托划扣方式还款的，须在每月还款日当日（不得迟于17:00）或之前将本协议第一部分约定的月偿还本息数额存入还款账户，并确保在支付机构或（及）资金存管机构成功划扣及处理前还款账户中有足额的月偿还本息数额，如因金额不足造成划款失败的，借款人构成违约。</font><br/>
    </para>'''
    story.append(Paragraph(parag9,normalStyle))

    parag26 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.7 借款人主动还款的，借款人委托恒诚公司通过支付机构或（及）资金存管机构处理其还款申请及流程操作。</font><br/>
    </para>'''
    story.append(Paragraph(parag26,normalStyle))

    parag27 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.8 借款人保证本协议中约定的收款账户和还款账户为其名下合法有效的银行账户。如借款人需要变更还款账户，应当在还款账户变更后1个工作日内通过恒诚公司办理账户变更手续。因借款人未及时办理变更手续导致借款人未能按时还款的，借款人须按照本协议第5条承担因此而产生的违约责任。</font><br/>
    </para>'''
    story.append(Paragraph(parag27,normalStyle))

    parag28 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.9 借款人签署本协议之日起至借款全部清偿之日止，借款人有义务在下列信息变更之日起三日内通过恒诚公司提供更新后的信息给出借人：</font><br/>
    </para>'''
    story.append(Paragraph(parag28,normalStyle))

    parag29 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.9.1 借款人的工作单位、居住地址、住所电话、手机号码、电子邮箱等；</font><br/>
    </para>'''
    story.append(Paragraph(parag29,normalStyle))

    parag30 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.9.2 借款人家庭联系人或紧急联系人工作单位、居住地址、住所电话、手机号码等。</font><br/>
    </para>'''
    story.append(Paragraph(parag30,normalStyle))

    parag31 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>2.2.9.3 因借款人不提供或不及时提供上述变更信息而导致出借人产生的损失，包括调查费用、仲裁费用及律师费用及委托其他公民参加仲裁所产生的费用等将由借款人承担。</font><br/>
    </para>'''
    story.append(Paragraph(parag31,normalStyle))

    parag32 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>第3条 费用的支付</font><br/>
    </para>'''
    story.append(Paragraph(parag32,normalStyle))

    parag33 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>依据《宜人贷信息咨询与服务协议》（编号：B0000108424300008266649-1），借款人需向恒诚公司支付信息咨询服务费人民币（大写）叁万肆仟肆佰元整，￥（小写）34400.00元；现借款人和出借人同意和授权恒诚公司通过支付机构或（及）资金存管机构从本协议第一条约定的借款本金中扣除前述信息咨询服务费并将扣除费用后的资金支付至借款人收款账户。</font><br/>
    </para>'''
    story.append(Paragraph(parag33,normalStyle))

    parag34 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>第4条 承诺及保证</font><br/>
    </para>'''
    story.append(Paragraph(parag34,normalStyle))

    parag35 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.1 出借人、借款人各自在此确认为具有完全民事权利能力和完全民事行为能力的自然人、法人及其他组织，有权签订并履行本协议。</font><br/>
    </para>'''
    story.append(Paragraph(parag35,normalStyle))

    parag36 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.2 出借人保证，自身为宜人贷平台注册用户并在本协议有效期内保持宜人贷平台注册用户身份； 其提供的资金均为自有资金且来源合法。</font><br/>
    </para>'''
    story.append(Paragraph(parag36,normalStyle))

    parag37 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.3 借款人承诺如实向出借人、提供信息（包括但不限于姓名或名称、证件类型、证件号码、学历、联系方式、联系地址、职业 信息、联系人信息等）、在所有网络借贷信息中介机构未偿还借款信息以及借款用途等相关信息。借款人承诺并保证其向出借人、 恒诚公司（宜人贷平台）提供的所有信息均为真实、准确、完整、合法和有效的。</font><br/>
    </para>'''
    story.append(Paragraph(parag37,normalStyle))

    parag38 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.4 借款人承诺依照本协议约定用途使用借款资金、不得挪用本协议借款资金用于出借等其他目的或用途。</font><br/>
    </para>'''
    story.append(Paragraph(parag38,normalStyle))

    parag39 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.5 借款人承诺依照本协议约定及时向出借人如实报告影响或可能影响出借人权益的重大信息。</font><br/>
    </para>'''
    story.append(Paragraph(parag39,normalStyle))

    parag40 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.6 借款人保证自身具有与借款金额相匹配的还款能力并依照本协议约定履行还款义务。</font><br/>
    </para>'''
    story.append(Paragraph(parag40,normalStyle))

    parag41 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.7 借款人承诺没有通过故意变换身份、虚构融资项目或借款用途、夸大融资项目收益前景等欺诈形式申请或取得借款。</font><br/>
    </para>'''
    story.append(Paragraph(parag41,normalStyle))

    parag42 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.8 借款人承诺没有同时通过多个网络借贷信息中介机构，或者通过变换项目名称或借款用途、对项目内容进行非实质性变更等方式，就同一融资项目进行重复融资。</font><br/>
    </para>'''
    story.append(Paragraph(parag42,normalStyle))

    parag43 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.9 借款人承诺没有在网络借贷信息中介机构以外的公开场所发布同一融资项目的信息。</font><br/>
    </para>'''
    story.append(Paragraph(parag43,normalStyle))

    parag44 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.10 出借人、借款人承诺，不得利用恒诚公司或（及）宜人贷平台进行信用卡套现、洗钱或其他违法犯罪行为，否则应依法承担由此产生的法律责任与后果。</font><br/>
    </para>'''
    story.append(Paragraph(parag44,normalStyle))

    parag45 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>4.11 出借人、借款人应妥善保管自己宜人贷平台的注册用户名和密码，自行承担因注册用户名和密码丟失、泄露或允许他人使用所产生的后果。任何一方通过其用户名和密码登陆的任何操作均视为该方本人的真实意思表示。</font><br/>
    </para>'''
    story.append(Paragraph(parag45,normalStyle))

    parag47 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>第5条 违约责任</font><br/>
    </para>'''
    story.append(Paragraph(parag47,normalStyle))

    parag48 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.1 如借款人未按照本协议约定的还款日足额还款，则应向出借人支付逾期还款违约金。</font><br/>
    </para>'''
    story.append(Paragraph(parag48,normalStyle))

    parag49 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.2 逾期还款违约金为当期应还本息数额及以后各期应还本息总额的0.01%，按日计收。</font><br/>
    </para>'''
    story.append(Paragraph(parag49,normalStyle))

    parag50 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.3 逾期还款违约金每期单独计算。借款人多期还款产生逾期的情况，借款人应向出借人支付各期逾期还款违约金的总和。</font><br/>
    </para>'''
    story.append(Paragraph(parag50,normalStyle))

    parag51 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.4 如因借款人原因导致或（及）资金存管机构未能及时、足额扣划或（及）支付当月应还本息的，借款人仍应按本协议4.2条约定支付逾期还款违约金。</font><br/>
    </para>'''
    story.append(Paragraph(parag51,normalStyle))

    parag52 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.5 若借款人偿还本协议项下各款项的金额不足，偿还先后顺序为逾期还款违约金、应还利息、应还本金。</font><br/>
    </para>'''
    story.append(Paragraph(parag52,normalStyle))

    parag53 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.6 借款人发生如下违约行为时，出借人有权解除或提前终止本协议，借款人须在出借人提出解除或协议之日起三日内一次性支付全部本金、利息和逾期还款违约金。</font><br/>
    </para>'''
    story.append(Paragraph(parag53,normalStyle))

    parag54 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.6.1 借款人擅自改变本协议第一条规定的借款用途；</font><br/>
    </para>'''
    story.append(Paragraph(parag54,normalStyle))

    parag55 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.6.2 严重违反还款义务（逾期达到15天及以上）；</font><br/>
    </para>'''
    story.append(Paragraph(parag55,normalStyle))

    parag56 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.6.3 借款人提供虚假资料或者故意隐瞒重要事实。</font><br/>
    </para>'''
    story.append(Paragraph(parag56,normalStyle))

    parag57 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.7 借款人同意，出借人可通过恒诚公司将其违约的相关信息依法进行披露。如借款人存在涉嫌欺诈等犯罪行为，出借人有权向相关国家机关报案，以追究其刑事责任。</font><br/>
    </para>'''
    story.append(Paragraph(parag57,normalStyle))

    parag58 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>5.8 因借款人违约而导致出借人产生的损失，包括本息损失、仲裁费用、调查费用、律师费用及委托其他公民参加仲裁所产生的费用等由借款人承担。</font><br/>
    </para>'''
    story.append(Paragraph(parag58,normalStyle))

    parag59 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>第6条 关于债权转让</font><br/>
    </para>'''
    story.append(Paragraph(parag59,normalStyle))

    parag61 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>6.2在出借人的债权转让后，借款人需对新债权人继续履行本协议下其对出借人的所有义务，不得以未接到债权转让通知为由拒绝履行还款义务。</font><br/>
    </para>'''
    story.append(Paragraph(parag61,normalStyle))

    parag62 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>第7条 关于法律适用及管辖</font><br/>
    </para>'''
    story.append(Paragraph(parag62,normalStyle))

    parag63 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>7.1 适用法律。本协议的全部事项，包括但不限于本协议的效力、解释、履行以及争议的解决均受中国法律管辖；本协议项下任一条款如与中国法律中的强制性规范相抵触，应在该等强制性规范所不禁止的最大限度内进行解释和执行，且任何该等与强制性规范相抵触的约定不应影响本协议其他条款的效力。</font><br/>
    </para>'''
    story.append(Paragraph(parag63,normalStyle))

    parag64 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>7.2 争议管辖。双方一致同意，如发生争议，不论争议金额大小，均提交北京仲裁委员会适用北京仲裁委员会仲裁规则项下的简易程序进行仲裁。仲裁裁决为终局的，对双方均具有约束力。</font><br/>
    </para>'''
    story.append(Paragraph(parag64,normalStyle))

    parag65 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>7.3 在仲裁期间，本协议中不涉及争议的条款仍须履行，各方均不得以解决争议为由拒不履行其在本协议项下的任何义务。</font><br/>
    </para>'''
    story.append(Paragraph(parag65,normalStyle))

    parag66 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>1第8条 关于其他</font><br/>
    </para>'''
    story.append(Paragraph(parag66,normalStyle))

    parag67 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>8.1 本协议项下的附件属于本协议不可分割的组成部分。本协议任何条款的标题仅系为方便援引和阅读而设置，不得被用于解释本协议任何条款的依据。</font><br/>
    </para>'''
    story.append(Paragraph(parag67,normalStyle))

    parag68 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>8.2 借款人可自行购买借款人人身意外险（以下简称“借意险”），以降低出借人出借资金无法获得偿付的风险。若借款人出现符合借意险出险情形时，该保险理赔款用以偿还其基于本合同所欠出借人的全部款项。借款人仍对保险理赔款不足以清偿的差额部分承担还款义务。是否购买借意险以其另行签署的保险协议成立并生效为准。</font><br/>
    </para>'''
    story.append(Paragraph(parag68,normalStyle))

    parag71 = '''<para autoLeading="off" leading=18>
    <font face="mytype" fontsize=9>借款人： 张秀         签署日期：2017年11月16日</font><br/>
    </para>'''
    story.append(Paragraph(parag71,normalStyle))



    doc = SimpleDocTemplate('D:\python-related\create_pdf\sa_loan_agreements.pdf')
    doc.build(story)
    return

    



if __name__ == '__main__':
    pdf_loan_agreements()    

