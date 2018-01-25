import xlsxwriter


def main():
    workbook = xlsxwriter.Workbook('statistic.xlsx') # 建立文件

    worksheet = workbook.add_worksheet('daily') # 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误

    # 设置粗体，默认是False
    bold = workbook.add_format({'bold': True})

    # cell_dict = {
    #     'A1' : '投资日期',
    #     'B1' : '客户姓名',
    #     'C1' : '手机号',
    #     'D1' : '投资期限',
    #     'E1' : '投资金额', 
    #     'F1' : '红包', 
    #     'G1' : '充值',
    #     'H1' : '今日新投',
    #     'I1' : '今日复投',
    #     'J1': '月份',
    #     'K1': '项目利息',
    #     'L1': '客户利息',
    #     'M1': '公司总支出',
    #     }
    # for key, val in cell_dict.items():
    #     worksheet.write(key, val, bold) # 写入

    cell_list = [
        '投资日期',
        '客户姓名',
        '手机号',
        '投资期限',
        '投资金额', 
        '红包', 
        '充值',
        '今日新投',
        '今日复投',
        '月份',
        '项目利息',
        '客户利息',
        '公司总支出',
    ]
    row = 0
    col = 0
    for s in cell_list:
        worksheet.write(row, col, s, bold)
        col += 1

    workbook.close()


if __name__ == '__main__':
    main()


# Start from the first cell. Rows and columns are zero indexed. 按标号写入是从0开始的，按绝对位置'A1'写入是从1开始的
# row = 0
# col = 0
 
# Iterate over the data and write it out row by row.
# for item, cost in (expenses):
#     worksheet.write(row, col,     item)
#     worksheet.write(row, col + 1, cost)
#     row += 1

