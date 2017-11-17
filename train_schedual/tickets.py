# https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-17&leftTicketDTO.from_station=IOQ&leftTicketDTO.to_station=CWQ&purpose_codes=ADULT
# docopt 可以按我们在文档字符串中定义的格式来解析参数

"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets beijing shanghai 2016-08-25
"""
from docopt import docopt
import requests
from stations import stations


def client():
    arguments = docopt(__doc__)
    print(arguments)
    from_station = stations[arguments['<from>']]
    to_station = stations[arguments['<to>']]
    date = arguments['<date>']

    #构建url
    url = "https://kyfw.12306.cn/otn/leftTicket/query?\
            leftTicketDTO.train_date={}\
            &leftTicketDTO.from_station={}\
            &leftTicketDTO.to_station={}\
            &purpose_codes=ADULT".format(date, from_station, to_station)

    r = requests.get(url, verify=False)
    print(r.json())


if __name__ == "__main__":
    client()