# -*- coding: utf-8 -*

import xlrd
import openpyxl


# 读取excel文件
# xlrd 仅支持 xls 文件格式的excel
def read_excel_file_by_xlrd(excel_file_path):
    # 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
    wb = xlrd.open_workbook(excel_file_path)
    # 通过Book对象的sheet_names方法可以获取所有表单名称
    sheetnames = wb.sheet_names()
    print(sheetnames)
    # 通过指定的表单名称获取Sheet对象（工作表）
    sheet = wb.sheet_by_name(sheetnames[0])
    # 通过Sheet对象的 nrows 和 ncols 属性获取表单的行数和列数
    print(sheet.nrows, sheet.ncols)
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            # 通过Sheet对象的cell方法获取指定Cell对象（单元格）
            # 通过Cell对象的value属性获取单元格中的值
            value = sheet.cell(row, col).value
            print(value, end='\t')
        print()
    # 获取最后一个单元格的数据类型
    # 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
    last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
    print(last_cell_type)
    # 获取第一行的值（列表）
    print(sheet.row_values(0))
    # 获取指定行指定列范围的数据（列表）
    # 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
    print(sheet.row_slice(3, 0, 5))


# 读取excel文件
# openpyxl 仅支持 2007年excel版本 文件格式的excel
def read_excel_file_by_openpyxl(excel_file_path):
    # 加载一个工作簿 ---> Workbook
    wb = openpyxl.load_workbook(excel_file_path)
    # 获取工作表的名字
    print(wb.sheetnames)
    # 获取工作表 ---> Worksheet
    sheet = wb.worksheets[0]
    # 获得单元格的范围
    #print(sheet.dimensions)
    # 获得行数和列数
    print(sheet.max_row, sheet.max_column)

    # 获取指定单元格的值
    # print(sheet.cell(3, 3).value)

    # 需要查询关键词合集
    set_channel = {'拼多多', '抖音'}
    count_map = {}  # 统计每个关键词出现多少次
    count_total = 0
    # 读取所有单元格的数据
    print("print excel all data\n")
    for row_ch in range(2, sheet.max_row + 1):
        print(row_ch, end='\t')
        # 请几行包含需要筛选的关键词
        channel_value = sheet.cell(row_ch, 3).value
        print_flag = channel_value in set_channel
        if print_flag:
            count_map[channel_value] = count_map.get(channel_value, 0) + 1
            count_total = count_total + 1

        for col_ch in 'ABCDEFG':
            value = sheet[f'{col_ch}{row_ch}'].value
            # if type(value) == datetime.datetime:
            #     print(value.strftime('%Y年%m月%d日'), end='\t')
            # elif type(value) == int:
            #     print(f'{value:<10d}', end='\t')
            # elif type(value) == float:
            #     print(f'{value:.4f}', end='\t')
            # else:
            if print_flag:
                print(value, end='\t')
        print()

    print(count_map)
    print(count_total)


if __name__ == "__main__":
    print("main begin\n")
    read_excel_file_by_openpyxl('../data_file/2020年销售数据.xlsx')
