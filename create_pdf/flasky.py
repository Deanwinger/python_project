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
    ('FONTSIZE',(0,0),(-1,-1),6),#字体大小
    ('ALIGN',(-1,0),(-2,0),'LEFT'),#对齐
    ('VALIGN',(-1,0),(-2,0),'LEFT'),  #对齐
    ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.black),#设置表格框线为红色，线宽为0.5
    ]))
    story.append(component_table)

    parag1 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第二条 乙方还款资金来源及担保</font><br/>
    </para>''' 
    story.append(Paragraph(parag1,normalStyle))

    # 表格2数据：用法详见reportlab-userguide.pdf中chapter 7 Table
    component_data2= [
        ['出票人', '腾讯公司'],
        ['收款人',' 华为公司'],
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
    ('FONTSIZE',(0,0),(-1,-1),6),#字体大小
    ('ALIGN',(-1,0),(-2,0),'LEFT'),#对齐
    ('VALIGN',(-1,0),(-2,0),'LEFT'),  #对齐
    ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.black),#设置表格框线为红色，线宽为0.5
    ]))
    story.append(component_data2)

    parag2 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第三条 甲方权利、义务</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag2,normalStyle))

    parag3 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>1.甲方应按协议约定在借款期限起始日前将借款本金通过榄盛金融对接的第三方支付平台进行支付。甲方应确保在划转之时其账户中有足够的资金以完成放款。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag3,normalStyle))

    parag4 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>2.甲方同意以网络页面点击确认的方式签订本协议,并不以此为由拒绝履行本协议项下的义务,即便在签订时本协议并没有乙方的信息、第一条、第二条的相关信息、签订日期信息等。甲方同意以前述方式签订本协议后即视为不可撤销及变更地授权榄盛金融平台根据最终撮合结果自主生成前述信息,且未经榄盛金融及乙方的同意,甲方不得否认本协议项下债权债务关系或以任何方式撤回、撤销本协议。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag4,normalStyle))

    parag5 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>3.甲方同意并授权榄盛金融或榄盛金融的合作方(第三方支付方、银行)根据本协议约定从其支付账户中划转借款金额至乙方指定账户以履行放款义务。甲方出借的款项支付至乙方指定账户后,甲乙双方借贷关系成立并生效,由乙方无条件承担还款责任。借款到期后,甲方同意并授权榄盛金融或榄盛金融的合作方(第三方支付方、银行)根据本协议约定将借款本金及利息划转至其指定账户即视为乙方已履行还款义务。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag5,normalStyle))

    parag6 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>4.甲方理解并同意,借款金额从其第三方支付账户划转之日起至起息日(不含)的这段期间内不产生任何收益(包括但不限于利息)。本协议项下的借款本息或受偿款项划转至甲方的第三方支付账户需要一定的时间,前述时间一般不超过三个工作日。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag6,normalStyle))

    parag7 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>5.甲方有权通过第三方支付平台及时足额收取本息,同时应按相关法律要求缴纳由利息所得带来的可能的税费。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag7,normalStyle))

    parag8 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>6.甲方应确保其提供信息和资料的真实性、准确性、有效性,不得提供虚假信息或隐瞒重要事实,否则应承担一切不利后果。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag8,normalStyle))

    parag9 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>7.甲方应按照丙方签订的居间合同、榄盛金融或向甲方提供服务的第三方明示的收费项目和规则向丙方及其他第三方支付居间服务费用。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag9,normalStyle))

    parag10 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第四条 乙方权利、义务</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag10,normalStyle))

    parag11 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>1. 乙方同意以网络页面点击确认或其他方式(包括但不限于签字或签章确认等方式)签订本协议,并不以此为由拒绝履行本协议项下的义务,即便在签订时本协议并没有甲方的信息、第一条、第二条的相关信息、签订日期信息等。乙方同意以上述方式签订本协议后即视为不可撤销及变更地授权榄盛金融平台根据最终撮合结果自主生成前述信息,且未经榄盛金融及甲方的同意,乙方不得否认本协议项下债权债务关系或以任何方式撤回、撤销本协议。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag11,normalStyle))

    parag12 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>2.乙方同意并授权榄盛金融或榄盛金融的合作方(第三方支付方、银行)根据本协议约定将借款金额划转至乙方指定账户即视为甲方履行完毕放款义务。乙方应保证其指定账户状态正常,确保资金划入、划出交易的完成。如因前述指定账户不正常导致的所有损失(如借款资金无法及时入账、还款资金无法划转等)应由其自行承担。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag12,normalStyle))

    parag13 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>3.乙方为甲方授权委托的第三方质押、兑付上票据提供一切便利和协助以保证甲方借款能够及时足额得到清偿。乙方应在挃定的还款日前将借款的本金及利息汇入与榄盛金融对接第三方支付的指定账户即视为乙方履行了还款义务。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag13,normalStyle))

    parag14 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>4.若甲方、乙方借贷关系成立后,因政策法律、政府监管原因被强制解除或撤销或无效,则乙方应在该事由发生之日起一个工作日内将甲方的借款通过榄盛金融平台对接的第三方支付无息返还至甲方持有、指定的账户。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag14,normalStyle))

    parag15 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>5.乙方应按本协议约定之用途使用借款不得用于本协议外的其他用途。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag15,normalStyle))

    parag16 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>6.乙方应按与丙方签订的居间合同、榄盛金融或向乙方提供服务的第三方明示的收费项目和规则向丙方及其他第三方支付居间服务费用。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag16,normalStyle))

    parag17 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>7.未经甲方、丙方一致同意,乙方不得将本协议项下的任何权利义务转让给任何其他方。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag17,normalStyle))

    parag18 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>8.乙方应确保其提供的信息和资料的真实性、准确性、合法性、有效性,不得提供虚假信息或隐瞒重要
事实,否则应承担一切不利后果。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag18,normalStyle))

    parag19 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>9.如乙方发生或可能发生危及其履约、还款能力的任何事态时,乙方应在事态发生(或知晓其可能发生)之日起 3 日内书面通知甲方和丙方,乙方自行或根据甲方、丙方的要求积极采取补救措施,以保证甲方资金安全,避免甲方、丙方可能遭受的相关损失。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag19,normalStyle))

    parag20 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>10.为审核乙方发布的信息的真实性、合法性和有效性及乙方履行本协议的能力及相关资讯,乙方应根据丙方或甲方的要求提供有关证照、凭证、证明和其他资料,以便丙方或甲方了解生产经营状况、信用等级、还款能力、借款用途、借款使用情况及其相关信息。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag20,normalStyle))

    parag21 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第五条 丙方的权利、义务</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag21,normalStyle))

    parag22 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>1.丙方仅为甲乙双方成立借贷关系提供居间服务并负责榄盛金融平台的运行和维护。丙方不保证乙方可及时获得借款,也不保证甲方借出款项能及时足额得到偿还,甲方与乙方借贷交易过程中的风险由其自行承担。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag22,normalStyle))

    parag23 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>2.如因甲方或乙方以及本协议之外的第三方的原因,造成本合同无法履行,丙方并承担任何责任。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag23,normalStyle))

    parag24 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>3.甲乙双方一致同意,出现下列事由而导致甲方乙方合同不能履行或者相关损失, 丙方不承担任何法律责任: 1)丙方榄盛金融系统或第三方支付停机维护期间;2)电信设备出现故障不能进行数据传输的;3)由于黑客攻击、网络供应商技术调整或故障、网站升级、银行方面的问题等原因而造成的榄盛金融服务中断或延迟;4)因台风、地震、海啸、洪水、停电、战争、恐怖袭击等不可抗力因素,造成榄盛金融系统障碍不能提供服务的。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag24,normalStyle))

    parag25 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>4.丙方应对甲方和乙方的信息及本协议内容负有保密义务,不得用于本业务无关的任何其他用途。如一方违约,丙方可向守约方披露。应司法、仲裁机构及行政机关的要求丙方亦可披露本协议及相关信息。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag25,normalStyle))

    parag26 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>5.甲方、乙方在丙方登记的住所、通信地址、电子邮箱、联系电话等事项变更时,应在有关事项变更之日起 3 日内书面通知丙方,否则,造成的一切不利后果由其自行承担。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag26,normalStyle))

    parag27 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第六条 票据质押担保</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag27,normalStyle))

    parag28 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>1.为保证本协议项下的借款本息能得到及时足额偿还,乙方以本协议事条所列银行承兑汇票向本协议所涉借贷项目的所有出借人质押,甲方作为出借人之一,即为质权人之一。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag28,normalStyle))

    parag29 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>2.乙方保证提供质押的银行承兑汇票真实、合法、有效,不存在挂失、止付、查封及冻结行为,也不存在任何法律纠纷,乙方合法取得票据,基础交易关系真实无瑕疵、背书连续,对上述汇票有充分的、无争议的权益</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag29,normalStyle))

    parag30 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>3.票据质押担保的范围:为借贷项目下每个出借人的借款本金、利息、逾期利息、罚息、违约金及其实现债权的全部费用,包括但不限于诉讼费、鉴定费、保管费、评估费、拍卖费、律师费、差旅费、税款、手续费、公证费等。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag30,normalStyle))

    parag31 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>4.乙方应按甲方或甲方授权委托的第三方(受托人)的要求,将银行承兑汇票交付甲方或甲方委托办理质押手续的第三方占有,并配合甲方或其受托人办理票据质押、背书、行使票据权利等手续。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag31,normalStyle))

    parag32 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>5.质押期间,乙方不得对票据及票据权利进行任何形式的处分,未经甲方及甲方授权委托管理票据的第三方书面同意的情况下,不得在对质押票据申请挂失止付、查封、冻结等保全措施及申请除权判决。在乙方向全体出借人清偿全部应付本息及其它应付费用之前,该质押不得解除。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag32,normalStyle))

    parag33 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>6.乙方如不能按时足额归还借款本息、支付费用或其他可能危及甲方债权的情势,甲方有权委托第三方以质押汇票变现,实现债权。不足受偿部分,甲方有权继续向乙方追偿。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag33,normalStyle))

    parag34 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第七条 违约责任</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag34,normalStyle))

    parag35 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>1.协议各方均应严格履行协议义务,非经各方协商一致,任何一方不得解除本协议。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag35,normalStyle))

    parag36 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>2.任何一方违约,违约方应赔偿因违约使得其他各方产生的一切损失,包括但不限于中介费用、诉讼费、律师费、差旅费等。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag36,normalStyle))

    parag37 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>3.本协议约定的还款方式为到期一次性还本付息。乙方不得提前还款,但本协议另有约定的除外。若乙方逾期还款,乙方同意除按本协议规定支付利息外,每逾期一天按借款金额万分之六支付罚息,甲方有权起诉乙方偿还借款本息。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag37,normalStyle))

    parag38 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>4.若乙方逾期支付居间服务费或提供虚假信息造成甲方、丙及其它第三方之损失的,丙方有权提起诉讼要求支付居间费用、赔偿损失。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag38,normalStyle))

    parag39 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第八条 取消交易</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag39,normalStyle))

    parag40 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>鉴于丙方是为借贷双方提供对接居间服务,促成双方建立借贷关系的居间方,为了维护借贷双方的权益,保护借贷双方的资金安全,甲乙双方同意当丙方有权取消该次交易,借贷双方扣缴的费用按照流标处理返还其各自账户,因借贷交易生成的列表予以删除。但借贷双方被第三方收取的费用(包含但不限于身份认证、学历认证等费用)不予返还。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag40,normalStyle))

    parag41 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第九条 争议解决</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag41,normalStyle))

    parag42 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>对于因本协议履行而发生的争议,三方可协商解决,协商不成的向丙方所在地法院提起诉讼。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag42,normalStyle))

    parag43 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>第十条 附则</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag43,normalStyle))


    parag44 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>1.本协议采用电子文本形式制成,甲乙双方同意按照榄盛金融网站要求所填写的确认信息是其合法有效的电子签名,并保存在丙方为此设立的专用服务器上备查,各方均认可该形式的协议效力。甲方、乙方应当妥善保管其在丙方所留注册信息、密码等,若因非丙方原因导致上述信息泄露而造成甲方、乙方损失,则由甲 方、乙方自行承担相应责任。</font><br/>
    <br></br></para>''' 
    story.append(Paragraph(parag44,normalStyle))

    parag45 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>2.本协议的任何条款因法律、法规、政策的变化而无效或不可执行时,不影响本协议的其他条款的效力。</font><br/>
    </para>''' 
    story.append(Paragraph(parag45,normalStyle))

    parag46 = '''<para autoLeading="off">
    <font face="mytype" fontsize=7>3.本协议自文本最终生成之日成立,于乙方指定账户收到借款之日生效。</font><br/>
    </para>''' 
    story.append(Paragraph(parag46,normalStyle))

    buff = BytesIO()
    doc = SimpleDocTemplate(buff)
    doc.build(story)
    pdf = buff.getvalue()
    buff.close()
    return pdf






if __name__ == '__main__':
    app.run(debug=True)