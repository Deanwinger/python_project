    # parag5 = '''<para autoLeading="off" leading=18>
    # <font face="mytype" fontsize=9>1.2 出借人：指本协议附件一中列明的出借人，为符合中华人民共和国法律（不包括香港特别行政区、澳门特别行政区和台湾地区的法律法规，下同）规定的具有完全民事权利能力和民事行为能力，能独立行使本协议项下权利和履行本协议项下义务的自然人、法人及其他组织。出借人为“宜人贷平台”的实名注册用户，经宜人贷平台提供的信息中介服务，出借资金给借款人。</font><br/>
    # <br></br></para>'''
    # story.append(Paragraph(parag5,normalStyle))

    #     parag46 = '''<para autoLeading="off" leading=18><br></br>
    # <font face="mytype" fontsize=9>4.12 借款人拟提前还款的，应按照恒诚公司要求的流程办理提前还款手续。借款人须支付当月应还本息及剩余未还本金、全部应还未还本息（如有）、逾期还款违约金(如有)。借款人可通过委托划扣和主动支付两种方式进行提前还款。借款人采用委托划扣方式还款的，借款人委托恒诚公司通过支付机构或（及）资金存管机构从本协议第一部分约定的借款人还款账户中准确划扣提前还款各款项。</font><br/>
    # <br></br></para>'''
    # story.append(Paragraph(parag46,normalStyle))

    #     parag60 = '''<para autoLeading="off" leading=18><br></br>
    # <font face="mytype" fontsize=9>6.1出借人有权将本协议项下的债权向他人转让。债权转让后，出借人委托恒诚公司通过包括但不限于电子邮件、特快专递、快递等灵活形式通知借款人。如宜人贷平台或恒诚公司通过电子邮件方式向借款人发送债权转让通知，则可以将《债权转让通知》发送至借款人下列邮箱 - ，或将《债权转让通知》发送至借款人在宜人贷平台的收件箱，邮件发出之日视为借款人收到该等通知并生效。借款人应向债权受让人继续履行本协议的后续还款义务。</font><br/>
    # <br></br></para>'''
    # story.append(Paragraph(parag60,normalStyle))

    #     parag69 = '''<para autoLeading="off" leading=18>
    # <font face="mytype" fontsize=9>8.3 由于借款人签署本协议时恒诚公司作为向出借人和借款人提供借贷撮合的网络借贷信息中介机构，尚未为其撮合出借人，故本协议自借款人签署时成立且一经签署，借款人即不可撤销。出借人通过签署本协议附件的方式对本协议的所有内容进行确认。出借人的详细信息亦在本协议附件，即《宜人贷借款协议》附件中列明。借款人对此流程和合同签署方式无异议，且借款人承诺对出借人无特殊资质要求，完全认可和接受恒诚公司为其撮合的出借人。借款人不得以本协议未列明出借人具体信息、出借人未签署本协议等为由否认亲自签署本协议、否认本合同内容、拒绝履行本合同中约定的借款人应履行的义务和责任。</font><br/>
    # <br></br></para>'''
    # story.append(Paragraph(parag69,normalStyle))

    #     parag70 = '''<para autoLeading="off" leading=18><br></br>
    # <font face="mytype" fontsize=9>8.4 本协议自借款本金扣除《宜人贷信息咨询与服务协议》中约定的信息咨询服务费后的款项支付到借款人指定收款账户时生效；借款人依照本协议约定履行完毕全部义务时，本协议终止。出借人及借款人双方可通过包括但不限于手写签名或盖章、点击、勾选、电子签名、数据电文等方式签署本协议或（及）本协议附件，出借人及借款人双方均不得以合同签署方式不同为由，否认本协议的法律效力。</font><br/>
    # <br></br></para>'''
    # story.append(Paragraph(parag70,normalStyle))

    # component_table.setStyle(TableStyle([
    # ('FONTNAME',(0,0),(-1,-1), 'mytype'),#字体
    # ('FONTSIZE',(0,0),(-1,-1),9),#字体大小
    # ('LEADING',(0,0),(-1,-1),9),#设置行距
    # # ('SPAN',(0,0),(3,0)),#合并第一行前三列
    # ('SPAN',(0,1),(3,1)),#合并第二行前三列
    # ('SPAN',(1,2),(3,2)),#合并第三行前三列
    # ('SPAN',(0,4),(3,4)),#合并第五行前三列
    # ('SPAN',(1,5),(3,5)),#合并第六行前三列
    # # ('SPAN',(0,6),(0,7)),#合并第七, 八行前三列
    # # ('SPAN',(2,6),(3,6)),#合并第七, 行前三列
    # # ('SPAN',(1,7),(3,7)),#合并第八行前三列
    # ('SPAN',(1,10),(3,10)),#合并第十一行前三列
    # ('SPAN',(1,11),(3,11)),#合并第十二行前三列
    # ('SPAN',(2,12),(3,12)),#合并第十三行前三列
    # ('SPAN',(1,13),(3,13)),#合并第十四行前三列
    # ('SPAN',(0,14),(3,14)),#合并第十四行前三列
    # ('ALIGN',(0,6),(1,6),'LEFT'),#对齐
    # ('VALIGN',(0,6),(0,6),'MIDDLE'),  #对齐
    # ('LINEBEFORE',(0,0),(0,-2),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    # ('TEXTCOLOR',(0,1),(-2,-1),colors.black),#设置表格内文字颜色
    # ('GRID',(0,0),(-1,-2),0.5,colors.black),#设置表格框线为黑色，线宽为0.5
    # ]))

    def get_matches(self, num):
        dics = {'1': '壹',
                '2': '贰',
                '3': '叁',
                '4': '肆', 
                '5': '伍', 
                '6': '陆', 
                '7': '柒',
                '8': '捌',
                '9': '玖',}
        target_str = ''
        num_formats = '%.2f' % num
        num_str = str(num_formats)
        num_list = num_str.split('.')
        if num_list[-1] and num_list[-2]:
            target_str += '整'

    # def check_num(self, num):
    #     origin = num
    #     limit = len(str(num))
    #     n=0
    #     while n < limit
    #         multi = 10**n 
    #         origin = origin // multi * multi
    #         if origin == num:
    #             continue
    #         else: