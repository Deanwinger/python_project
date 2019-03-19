from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
import xlsxwriter


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MongoEngine(app)
api = Api(app)


# Demo
class HelloWorld(Resource):
    def get(self):
        row = 0
        col = 0

        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet()
        # worksheet.set_column('B:B', len('hello world')+1)
        # worksheet.write('B5', 'hello world')
        resume = {"age":25,"gender":"男","is_tongzhao":False,"top_edu_degree":"本科","last_major":"计算机及其应用","overseas_education":None,"ethnicity":"汉","nationality":"中国","english_level":"大学英语4级",
        "hukou":"河北省石家庄","current_location":"海淀区颐和园路东口","last_school":"北京大学","expected_locations":[],"expected_job_title":"运营","last_job_title":"java","last_company":"电子商务","year_of_work_experience":15,
        "birthday":"1982-08-01T00:00:00Z","marital_status":"已婚",
        "summary":"良好工作心态,具备沟通.领悟.执行能力.语言表达能力,适应性强,自学性强,能够承受一定的工作压力。\n自学能力强,有勇于接受挑战的精神。\n做事认真负责,具有强烈的事业心.\n良好的团队合作精神,优秀的表达能力,能承受一定的工作压力\n数据库开发程序员.维护人员.统计分析员.数据仓库开发员.数据营销。\n为人踏实稳重\n对工作认真负责\n有极强的团队合作精神和独立完成工作的能力\n适应环境能力较好\n责任心强\n具有敏感的洞察力\n工作努力\n善于突破自己\n勤于思考工作中的问题并加以改善\n有较强的文字功底\n高中时曾担任校刊《绿岛》主编",
        "last_school_props":{"_pos":["nixt"],"_root":"北京大学","city":"北京市","country":"中国","domestic_ranking":1,"international_ranking":30,"level":"本科","regulator":"教育部",
        "tags":["key_uni","erben_above","sanben_above","985","211","first_class_uni","yiben_above","综合类"],"text":"北京大学","type":"公办"},
        "current_location_props":{"_root":"海淀区颐和园路东口","text":"海淀区颐和园路东口"},"last_company_props":{"_root":"电子商务","industry":"电子商务","industry_tags":["电子商务"],
        "it_level":1000,"subindustry":"","tags":["电子商务"],"text":"电子商务"},"last_job_title_props":{"head":[],"head_rank":3,"modifier":["java"],"normalized":["java开发工程师"]},
        "expected_job_title_props":{"head":[],"head_rank":3,"modifier":["运营"],"normalized":["运营专员"]},"_tags":[{"name":"education.211","rank":0,"title":"211","kind":"good"},
        {"name":"education.985","rank":0,"title":"985","kind":"good"}],"channel":"system","skills":[{"skill_name":"jsp","skill_level":"熟练"},
        {"skill_name":"servlet","skill_level":"熟练"},{"skill_name":"jdbc","skill_level":"熟练"},{"skill_name":"javascript","skill_level":"熟练"},{"skill_name":"xml","skill_level":"熟练"},
        {"skill_name":"xhtml"},{"skill_name":"html"},{"skill_name":"css"},{"skill_name":"mysql"},{"skill_name":"pl-sql"},{"skill_name":"数据库开发"},{"skill_name":"struts2","skill_level":"熟练"},
        {"skill_name":"spring","skill_level":"熟练"},{"skill_name":"hiberate","skill_level":"熟练"},{"skill_name":"ajax","skill_level":"熟练"},{"skill_name":"java","skill_level":"熟悉"},{"skill_name":"j2ee","skill_level":"熟悉"},
        {"skill_name":"多线程","skill_level":"熟悉"},{"skill_name":"sqlsever"},{"skill_name":"db2"},{"skill_name":"oracle"},{"skill_name":"olap"},{"skill_name":"powerbuilder"},
        {"skill_name":"tsql"},{"skill_name":"api"},{"skill_name":"sql"},{"skill_name":"etl"},{"skill_name":"数据挖掘"},{"skill_name":"sybase"},{"skill_name":"erwin"},{"skill_name":"designer"},
        {"skill_name":"数据建模"},{"skill_name":"数据库"},{"skill_name":"visual basic"},{"skill_name":"脚本"},{"skill_name":"sqlsever"},{"skill_name":"bsd"},{"skill_name":"shell"}],
        "educations":[{"school_name":"北京大学","major":"计算机及其应用","start_date":"2003-04-01T00:00:00Z","end_date":"2007-07-01T00:00:00Z","degree":"本科","degree_rank":7,"school_type":1,"edu_nature":"自考",
        "school_name_props":{"_pos":["nixt"],"_root":"北京大学","city":"北京市","country":"中国","domestic_ranking":1,"international_ranking":30,"level":"本科","regulator":"教育部",
        "tags":["key_uni","erben_above","sanben_above","985","211","first_class_uni","yiben_above","综合类"],"text":"北京大学","type":"公办"},"major_props":{"_root":"计算机及其应用","text":"计算机及其应用"}},
        {"school_name":"华北水利水电学院","major":"计算机科学与技术","start_date":"2001-09-01T00:00:00Z","end_date":"2005-07-01T00:00:00Z","degree":"本科","degree_rank":7,
        "school_name_props":{"_pos":["nixt"],"_root":"华北水利水电大学","city":"郑州市","country":"中国","domestic_ranking":313,"level":"本科","regulator":"河南省",
        "tags":["erben_above","sanben_above","yiben_above","理工类"],"text":"华北水利水电学院","type":"公办"},"major_props":{"_pos":["nmaj"],"_root":"计算机","first_level":"工学",
        "related":["计算机应用技术","计算机网络技术","计算机信息管理","计算机系统与维护","软件技术","软件与信息服务","动漫制作技术","嵌入式技术与应用","数字展示技术","数字媒体应用技术","信息安全与管理","移动应用开发",
        "云计算技术与应用","电子商务技术","医学信息工程","电信工程及管理","电子信息科学与技术","电磁场与无线技术","信息安全","船舶电子电气工程","广播电视工程","空间信息与数字技术","it","自动化","智能电网信息工程",
        "电波传播与天线","水声工程","集成电路设计与集成系统","电子与计算机工程","信息工程","电子科学与技术","数字媒体艺术","互联网","信息管理与信息系统","电气类","物联网工程","电气工程及其自动化","软件工程",
        "地球信息科学与技术","工学","电子信息工程","交通设备与控制工程","网络工程","数字媒体技术","信息对抗技术","生物信息学","智能科学与技术","信息与计算科学","通信工程","网络安全与执法","电气工程与智能控制",
        "地理信息科学","通讯"],"second_level":"计算机","text":"计算机科学与技术","third_level":["计算机科学与技术","软件工程","网络工程","信息安全","物联网工程","数字媒体技术","智能科学与技术",
        "空间信息与数字技术","电子与计算机工程"]}},{"school_name":"北京化工大学","major":"自动化","start_date":"1997-09-01T00:00:00Z","end_date":"2001-06-01T00:00:00Z","degree":"本科",
        "degree_rank":7,"school_type":2,"school_name_props":{"_pos":["nixt"],"_root":"北京化工大学","city":"北京市","country":"中国","domestic_ranking":73,"level":"本科","regulator":"教育部",
        "tags":["key_uni","erben_above","sanben_above","211","yiben_above","理工类"],"text":"北京化工大学","type":"公办"},"major_props":{"_pos":["nmaj","nski"],"_root":"自动化","first_level":"工学",
        "related":["机械设计制造及其自动化","电子信息工程","信息对抗技术","集成电路设计与集成系统","电信工程及管理","农业机械化及其自动化","医学信息工程","计算机科学与技术","电子信息科学与技术","电磁场与无线技术","信息安全",
        "船舶电子电气工程","广播电视工程","空间信息与数字技术","智能电网信息工程","电波传播与天线","水声工程","电子与计算机工程","电子科学与技术","信息工程","数字媒体艺术","信息管理与信息系统","电气类","物联网工程","软件工程",
        "电气工程及其自动化","地球信息科学与技术","工学","交通设备与控制工程","网络工程","数字媒体技术","生物信息学","智能科学与技术","信息与计算科学","通信工程","网络安全与执法","电气工程与智能控制","地理信息科学","农业电气化"],
        "second_level":"自动化","text":"自动化","third_level":["自动化","轨道交通信号与控制"],"undergraduate":True}}],"employments":[{"company_name":"电子商务","title":"java",
        "description":"tck测试,lta测试,sms/ems/mms测试,wap测试;iot测试(移动通信产品接口兼容性测试),sim\niot测试,fota/delta测试,e2e测试,gprs测试。\n3.\n担任odm产品(olga;kim/melody;gesila/folorence;anasia/anable)手机项目的interface的backup,主要工作是分配工作任务,对测试流程进行监督和指导,并筛选需要的测试用例,每轮汇总测试报告和测试进度给project\nleader;同时解决测试中途出现的各种问题(比如对resource\n的调整,遇到a,b级影响版本发布等严重问题的解决)。根据突发事件的程度进行衡量采取一定的解决措施来确保项目的正常进行。\n4.\n熟悉中国移动的各种需求,如mms测试规范,wap2.0/wap1.2终端测试规范,pim测试规范,java测试规范,drm测试规范,generic测试规范等等。\n5.\n熟悉各种协议,mms/sms,wap\n协议(wap1.2\nand\nwap2.0),\nir\n红外协议,\n蓝牙协议,oma协议,jsr协议,drm等。\n6.\n能够熟练运用各种测试工具,如(flash\ngordarn,tracer,\ndebug\nmux,\ncsst,crasher,\nplatform\nassistent,\nemaiii等)。\n:1年工作经验\n期望薪水: 面议\n期望从事行业: 通信(设备・运营・增值服务)\n期望工作性质: 全职\n到岗时间: 面谈\n海外工作经历:\n没有\n现从事职业: 软件工程师\n现职位级别:\n中级职位(两年以上工作经验)\n北京驰讯通科技有限公司","start_date":"2007-12-01T00:00:00Z",
        "end_date":"2018-07-12T00:00:00Z","industry":"计算机软件","company_name_props":{"_root":"电子商务","industry":"电子商务","industry_tags":["电子商务"],"it_level":1000,
        "subindustry":"","tags":["电子商务"],"text":"电子商务"},"title_props":{"head":[],"head_rank":3,"modifier":["java"],"normalized":["java开发工程师"]}},{"company_name":"北京摩视新媒科技有限公司",
        "title":"开发经理","description":"担任","start_date":"2006-11-01T00:00:00Z","end_date":"2018-07-12T00:00:00Z","company_name_props":{"_root":"摩视新媒科技","industry_tags":["科技"],"it_level":1000,
        "locations":["北京"],"tags":["科技"],"text":"北京摩视新媒科技有限公司"},"title_props":{"head":["经理"],"head_rank":4,"modifier":["开发"],"normalized":["开发经理"]}},{"company_name":"中国索尼爱立信移动通讯产品有限公司",
        "company_nature":"外商独资.外企办事处","description":"2年工作经验\n期望薪水: 税前月薪rmb6500\n元\n期望从事行业: 通信(设备・运营・增值服务)\n期望工作性质: 全职\n到岗时间: 面谈\n海外工作经历:\n没有\n现从事职业: 其他类\n现职位级别:\n中级职位(两年以上工作经验)\n目前薪水: 税前月薪rmb6000\n元",
        "start_date":"2005-08-01T00:00:00Z","end_date":"2018-07-12T00:00:00Z","industry":"计算机软件","company_name_props":{"_root":"索尼爱立信移动通讯产品","industry_tags":["通讯","产品"],"it_level":1000,"locations":["中国"],"tags":["通讯","产品"],
        "text":"中国索尼爱立信移动通讯产品有限公司"},"title_props":{"head_rank":3}},{"company_name":"sql","company_nature":"外商独资.外企办事处","company_scale":"500-999人","title":"数据库","description":"server\n2000\n项目描述:属于一个j2se的桌面开发程序,提供联系人的各种信息的增,删,改,查功能的的实现.观察者模式.\n:6年工作经验\n期望薪水: 税前月薪rmb10000\n元\n期望从事行业: 通信(设备・运营・增值服务)\n互联网・电子商务\n期望工作性质: 全职\n到岗时间: 面谈\n海外工作经历:\n没有\n现从事职业: 信息技术专员\n现职位级别:\n高级职位(非管理类)\n目前薪水: 税前月薪rmb8000\n元\n北京讯能网络有限公司\n公司简单描述:\nwww.tom.com",
        "start_date":"2004-05-01T00:00:00Z","end_date":"2018-07-12T00:00:00Z","industry":"银行","company_name_props":{"_root":"sql","it_level":1000,"tags":[],"text":"sql"},"title_props":{"head":[],"head_rank":3,
        "modifier":["数据库"],"normalized":["数据库"]}},{"title":"shell","description":"client,tomcat5.0\n数据库:oracle9i\n项目描述: 澳门新闻的搜索包括(本澳新闻,大陆新闻,台湾新闻,国际新闻,珠三角资讯,经济,体育)\n北京联通彩信业务前台和后台的页面设计和逻辑的开发,和彩信的发送",
        "start_date":"2007-10-01T00:00:00Z","end_date":"2007-11-01T00:00:00Z","company_name_props":{},"title_props":{"head":[],"head_rank":3,"modifier":["shell"],"normalized":["shell"]}},
        {"title":"shell","description":"client,tomcat5.0\n数据库:oracle9i\n项目描述:杂志商城后台信息操作平台\n杂志商城后台信息操作平台包括(杂志管理,订单管理,个人信息,订单查询,订单配发管理)前端页面显示用到jsp,css,javascript等技术,业务层是模拟mvc的架构,数据访问层用的hibernate3.0,",
        "start_date":"2007-08-01T00:00:00Z","end_date":"2007-10-01T00:00:00Z","company_name_props":{},"title_props":{"head":[],"head_rank":3,"modifier":["shell"],"normalized":["shell"]}},
        {"title":"wap工程师","description":"工作职责和业绩:\n手机报采集系统\n手机报采集系统分为(业务管理,发布新闻,发布历史,审核新闻,发送日志,个人信息)表现层是用jsp显示,业务层\n是模拟mvc的架构,访问层用的是封装后的jdbc连接数据源.数据库是oralce9i,数据库管理客户端是\nplsqldeveloper.服务器用的是resin3.0,服务器操作系统是linux9.0,开发环境jdk5.0+eclipse3.2\n在后台设计中页面用jsp,同时用到css来控制页面效果,用js实现客户端页面的数据验证和一些动态的显示效果,并提供页面框架的之间的参数的传递协调",
        "job_location":"北京朝阳东直门","start_date":"2007-01-01T00:00:00Z","end_date":"2007-08-01T00:00:00Z","company_name_props":{},"title_props":{"head":["工程师"],"head_rank":3,"modifier":["wap"],"normalized":["wap工程师"]}},
        {"company_name":"北京世纪豪杰计算机技术公司","title":"工程师","description":"担任","start_date":"2005-07-01T00:00:00Z","end_date":"2006-11-01T00:00:00Z","company_name_props":{"_root":"世纪豪杰计算机技术","industry_tags":["计算机技术"],"it_level":1000,
        "locations":["北京"],"tags":["计算机技术"],"text":"北京世纪豪杰计算机技术公司"},"title_props":{"head":["工程师"],"head_rank":3,"modifier":[],"normalized":["工程师"]}},{"company_name":"清华紫光集团","department":"无线业务部","title":"数据库统计分析员",
        "description":"工作职责和业绩:\n联通业务数据的分析和数据仓库的建立与维护;\n及时准确向业务部门提交数据;\n数据挖掘和用户的个性化分析,数据营销。\n离职/换岗原因:无","job_location":"王府井东方广场","start_date":"2001-07-01T00:00:00Z","end_date":"2004-05-01T00:00:00Z",
        "company_name_props":{"_root":"清华紫光股份有限公司","location":["北京","广西"],"score":54,"tags":[""],"text":"清华紫光集团"},"title_props":{"head":["分析员"],"head_rank":3,"modifier":["数据库","统计"],"normalized":["数据库统计分析员"]}},
        {"title":"项目管理","description":"项目名称:上海农行设备管理系统\n项目描述:管理农行计算机,atm机采购设备。","start_date":"2003-03-01T00:00:00Z","end_date":"2003-09-01T00:00:00Z","company_name_props":{},"title_props":{"head":[],"head_rank":3,
        "modifier":["项目管理"],"normalized":["项目管理员"]}}],"secondary_employments":[{"title":"shell","description":"client,resin3.0\n数据库:oracle9i\n项目描述: (1)联通c网g网的各省的搜索业务包括(天气,铃声,公交,航班,铁路,美食,生活,最新新闻,招聘,租售楼房)\n其中公交搜索是灵图提供接口,通过xml来获取数据.\n(2)股票搜索包括(个股行情查询,即时行情,买卖盘,k线图,分时图),图片的抓取和图片匹配\n(3)奥运业务包括(奥运票务早知道搜索,奥运聊天室,奥运留言版,明星*08奥运之星投票,奥运今日头条新闻)\n(4)鉴宝业务包括(鉴宝评论,鉴宝在线聊,鉴宝投票,鉴宝新闻等)\n(5)根据本公司的后台改建凤凰uni网站主要以新闻为主,包括(焦点,社会,财经,军事,娱乐,时尚,旅游,影视,深度解读,商旅访谈,证券,娱闻八卦,麻辣大赏,理财,评论,内地,港台,欧美,最新博客)\n以上业务用到的技术有前台页面用到wml和jsp显示,业务层是模mvc的架构,访问层用的是jdbc通过数据源连接数据库",
        "start_date":"2006-09-01T00:00:00Z","end_date":"2007-01-01T00:00:00Z","job_nature":"实习","company_name_props":{},"title_props":{}},{"company_name":"北京同定世纪科技有限公司","company_nature":"私营.民营企业","company_scale":"1-49人","title":"shell",
        "description":"client,resin3.0\n数据库:oracle9i\n项目描述: 联通g网的wap网站开发包括以下功能:(聊天室,论坛,博客和新闻发布系统)前台页面用wml和jsp显示,在后台页面设计中用到jsp,css,javascript等技术,业务层是模mvc的架构,访问层用的是jdbc通过数据源连接数据库","start_date":"2006-01-01T00:00:00Z",
        "end_date":"2006-05-01T00:00:00Z","job_nature":"实习","company_name_props":{"_root":"北京同定世纪科技有限公司","industry":"企业服务","industry_tags":["科技"],"locations":["北京"],"subindustry":"行业信息化及解决方案","tags":["法律服务","教育信息化","企业服务","科技","行业信息化及解决方案"],
        "text":"北京同定世纪科技有限公司"},"title_props":{}},{"company_name":"长城计算机学校","title":"数据库","description":"oracle9i\n项目描述:青海省政府办公自动化系统\n开发技术:\n利用jsp+struts+jdbc+tomcat+powerdesigner架构开发,部门与人员数维护,,单位负责人,服务项目,系统管理,权限的控制和管理,抽象工厂模式.责任描述:用javascript对页面数据的处理,业务逻辑的实现.用junit实现单元测试.",
        "start_date":"2005-11-01T00:00:00Z","end_date":"2005-12-01T00:00:00Z","job_nature":"实习","company_name_props":{"_root":"成都市金牛区长城计算机学校","industry":"教育","industry_tags":["计算机","学校"],"subindustry":"教育综合服务",
        "tags":["教育综合服务","学校","教育","计算机"],"text":"长城计算机学校"},"title_props":{}},{"title":"数据库","description":"oracle9i\n项目描述:网络学校管理系统\n开发技术:用户注册登录.上传文件模块.留言版.分页显示用户信息,管理员授权,资源共享,其中基于j2ee的架构开发,并且jsp页面;利用struts架构开发,抽象工厂模式.",
        "start_date":"2005-08-01T00:00:00Z","end_date":"2005-09-01T00:00:00Z","job_nature":"实习","company_name_props":{},"title_props":{}},
        {"title":"java程序员","description":"工作职责和业绩:\n工作平台:window2000\nserver\n开发工具:eclipse\nb/s模式\n项目描述:网络购物系统\n开发技术:jsp+sql\nserver\n2000","job_location":"北京","start_date":"2005-06-01T00:00:00Z","end_date":"2005-07-01T00:00:00Z","job_nature":"实习","company_name_props":{},
        "title_props":{}},{"company_name":"北京晓亚电脑公司","department":"产品部","title":"产品经理","description":"2005年大学毕业后,我加入了筹备中的北京世纪豪杰计算机技术公司的数码分部(后更名为“北京豪杰数码技术有限公司”)。豪杰早先主要以软件业务为主,做得比较有名的就是《超级解霸》,在04年底公司老总梁肇新有了往数码硬件发展的念头,故开始筹备豪杰旗下的数码子公司。\n我到豪杰自05年7月至06年3月担任产品部工程师,主要负责:\n1.\n对代工厂提供的样机进行测试,找出bug并提出我方需求;\n2.\n对产品进行维修方面的评估,并制定维修方案,协助售后部门为售后维修做好准备;\n3、\n提炼产品卖点,对经销商进行产品销售培训;\n06年3月升任产品经理,主要负责:\n1、\n产品工程师的工作内容;\n2.\n制定公司产品发展规划,并根据规划完成产品选型,测试,定制化,宣传预案;\n3.\n进行市场调研工作,分析产品卖点,售价,配置,销量等,为各级领导提供每周数码产品市场调研报告;\n4.\n进行用户调研工作,收集用户体验,输出给研发.评测,以优化产品;\n任期内主导了豪杰掌霸(硬件)1380.1380+.1350.3380.6380等的研发.策划及上市;\n完成了豪杰超级酷霸(软件)的商品化,定制化.宣传文案策划.主辅料采购等工作;\n豪杰超级酷霸软件(coolbar)是公司老总梁肇新立志打造中国版“ipod+itunes”中的“itunes”一环,在本人主持下进行了商品化开发,在功能和易用性都发生了质的变化,并最终从随机附带软件变为独立商品来运作,产品在4个月内销量达20余万套(终端零售+oem)。\n北京晓亚电脑公司是一家国内较大的数码产品代理商,曾成功导入韩国iriver(艾利和)。我通过imp3.net论坛的一次活动得到了该公司老板的赏识,负责兼职管理该公司网站论坛,并每周用1个半工作日的时间协助售后服务工作。在兼职工作期间,通过改进safa\n110r的维修方法,为公司节省开支至少6万余元,获得了公司领导的表扬。\n2006.6―2007.3",
        "start_date":"2005-03-01T00:00:00Z","end_date":"2005-07-01T00:00:00Z","industry":"计算机软件/数码产品","job_nature":"实习","salary":"2500~4500元/月","company_name_props":{"_root":"晓亚电脑","industry_tags":["电脑"],"it_level":1000,"locations":["北京"],
        "tags":["电脑"],"text":"北京晓亚电脑公司"},"title_props":{}}],"projects":[],"trainings":[{"training_content":"2005-05-01\n长城计算机学校\njava软件工程师\n北京,\n培训时长:8个月\n2004-08-01\n迈思奇\nbi\n北京,\n培训时长:4天","org":"长城计算机学校"}],
        "certificates":"java软件工程师证书\n1.熟练jsp.servlet.jdbc.javascript.wml.xml\n2.熟练tomcat5.0.jboss4.0\n.weblogic8.1容器使用管理.\n3.熟练sqlserver2000.oracle9i\nmysql的操作和pl/sql的数据库开发.\n4.熟练struts1.1.spring.hibernate框架,了解ajax.webwork2.0\n5.熟练使用的集成开发环境eclipse3.1\n6.熟悉使用常用的java模式.j2ee模式.多线程模式。\n外语/方言\n英语:\n良好\n英语等级:\n未参加\n英语口语水平:\n一般\n公共英语二级\njava软件工程师证书\n获得时间:2005\n年\n公共英语等级证书\n获得时间:2007\n年\n3.李铮\n:无\nbi\n2003-10-01\nitpub\noracle\nocp\n北京,\n培训时长:7天\n:无\noracle\n9i。\n外语/方言\n中文普通话:\n母语\n英语:\n熟练\n英语等级:\n大学英语考试四级\n英语口语水平:\n一般\n英语四级",
        "languages":[{"language":"英语","cert_level":"大学英语4级"}],"politics_status":"团员","hobbies":"打球,\n游泳,看书.\n2.等等.\n期间自学并熟练掌握了:photoshop7.0.firworks\nmx.flash\nmx,dreamweavers\nmx,swishmax.\n3.韩建章","parse_status":1,
        "_understand_version":{"core_version":"0.1","policy_version":"0.2.2"},"is_favorite":True,"category":1,"doubt":[{"area":"education","content":{"edu_time_overlapped":"候选人的教育经历时间冲突","work_before_graduate":"候选人第一段工作经历早于毕业时间"}},
        {"area":"employment","content":{"work_gap":"候选人在2003/09至2004/05存在工作空档期","short_time_work":"候选人存在3段工作经历时长不足半年"}}],"is_super":False,"_categories":[{"name":"技术_测试","major":"技术","minor":"测试","detail":"",
        "score":0.893306673589588,"detail_score":0,"minor_score":0.893306673589588}],"_prog_languages":[{"name":"java","score":0.9198425325700702}],"name":None,"surname":None,"email":None,"wechat":None,"phone":None,
        "current_industry":None,"current_salary":None,"top_edu_degree_rank":7,"last_major_props":{"_root":"计算机及其应用","text":"计算机及其应用"},"personal_id":None,"birthplace":None,"graduation_year":None,"expected_onboard_time":None,"expected_salary":None,"expected_industry":None,
        "expected_job_nature":None,"expected_work_type":None,"current_status":None,"qq":None,"facebook":None,"instagram":None,"weibo":None,"github":None,"linked_in":None,"website":None,"expected_locations_props":None}

        # TODO 时间格式需要调整
        rec = [
            ["姓名", resume.get("name")],
            ["目前工作状态", resume.get("current_status")],
            ["手机", resume.get("phone")],
            ["邮箱", resume.get("email")],
            ["性别", resume.get("gender")],
            ["出生年月", resume.get("birthday")],
            ["现居住地", resume.get("current_location")],
            ["户口/国籍", resume.get("hukou")],
            ["婚姻状况", resume.get("marital_status")],
            ["政治面貌", resume.get("politics_status")],
            ["目前年收入", resume.get("current_salary")],
            ["求职意向", resume.get("expected_job_title")],
            ["期望薪资", resume.get("expected_salary")],
            ["职能/职位", resume.get("last_job_title")],
            ["工作类型", resume.get("current_job_nature")],
            ["自我评价", resume.get("summary")]
        ]

        rec.append(["教育经历", ""])
        if resume.get("educations", None):
            for edu in resume["educations"]:
                rec.append(["开始时间", edu.get("start_date")])
                rec.append(["结束时间", edu.get("end_date")])
                rec.append(["学校名称", edu.get("school_name")])
                rec.append(["学历", edu.get("degree")])
                rec.append(["专业", edu.get("major")])

        rec.append(["工作经验", ""])
        if resume.get("employments", None):
            for emp in resume["employments"]:
                rec.append(["开始时间", emp.get("start_date")])
                rec.append(["结束时间", emp.get("end_date")])
                rec.append(["公司名称", emp.get("company_name")])
                rec.append(["职能/职位", emp.get("title")])
                rec.append(["部门", emp.get("department")])
                rec.append(["薪资", emp.get("salary")])
                rec.append(["行业", emp.get("industry")])
                rec.append(["公司规模", emp.get("company_scale")])
                rec.append(["公司性质", emp.get("company_nature")])
                rec.append(["工作描述", emp.get("description")])

        if resume.get("projects", None):
            rec.append(["项目经验", ""])
            for proj in resume["projects"]:
                rec.append(["开始时间", proj.get("start_date")])
                rec.append(["结束时间", proj.get("end_date")])
                rec.append(["项目名称", proj.get("project_name")]) 
                rec.append(["所属公司", proj.get("company")]) 
                rec.append(["项目描述", proj.get("description")])

        if resume.get("honors", None):
            rec.append(["所获荣誉", ""])
            for honor in resume["honors"]:
                rec.append(["荣誉名称", honor.get("name")])
                rec.append(["获得荣誉时间", honor.get("time")])

        if resume.get("credentials"):
            rec.append(["证书", ""])
            for cred in resume["credentials"]:
                rec.append(["证书名称", cred.get("name")]) 
                rec.append(["获得证书时间", cred.get("time")])

        if resume.get("skills"):
            rec.append(["技能", ""])
            for skill in resume["skills"]:
                rec.append(["技能名称", skill.get("skill_name")]) 
                rec.append(["技能等级", skill.get("skill_level")]) 

        if resume.get("languages"):
            rec.append(["语言", ""])
            for lang in resume["languages"]:
                rec.append(["语言名称", lang.get("language")]) 
                rec.append(["语言等级", lang.get("cert_level")]) 

        for i, j in rec:
            worksheet.write(row, col, i)
            worksheet.write(row, col+1, j)
            row += 1

        workbook.close()

        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5566)



            # ["工作经验", ""],
            # ["工作周期", resume["start_date"]],
            # ["公司名称", resume[""]],
            # ["职能/职位", resume[""]],
            # ["部门", resume[""]],
            # ["薪资", resume[""]],
            # ["行业", resume[""]],
            # ["公司规模", resume[""]],
            # ["公司性质", resume[""]],
            # ["工作描述", resume[""]],
            # # ["项目经验", ""],
            # ["项目周期", resume[""]],
            # ["项目名称", resume[""]],
            # ["所属公司", resume[""]],
            # ["项目描述", resume[""]],
            # ["教育经历", ""],
            # ["开始结束时间", resume[""]],
            # ["学校名称", resume[""]],
            # ["学历", resume[""]],
            # ["专业", resume[""]],
            # # ["在校情况", ""],
            # ["校内荣誉", resume[""]],
            # ["获得荣誉时间", resume[""]],
            # ["荣誉名称", resume[""]],
            # ["证书", ""],
            # ["获得证书时间", resume[""]],
            # ["证书名称", resume[""]],
            # ["技能", ""],
            # ["技能名称": resume[""]]
            # ["技能等级", resume[""]],
            # ["语言", ""],
            # ["语言名称": resume[""]]
            # ["语言等级", resume[""]]