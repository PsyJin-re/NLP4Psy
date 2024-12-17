import csv
import re

# 输入和输出文件路径
input_csv = "F:/5_ECNU/2_Data analysis method/Natural Language processing/NLP4Psy/Data/Spider/极越/极越_output.csv"  # 替换为你的CSV文件路径
output_txt = "F:/5_ECNU/2_Data analysis method/Natural Language processing/NLP4Psy/Data/Spider/极越/极越.txt"  # 输出的TXT文件路径

# 省份列表
provinces = [
    "北京", "天津", "上海", "重庆", "河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", 
    "江西", "山东", "河南", "湖北", "湖南", "广东", "海南", "四川", "贵州", "云南", "陕西", "甘肃", 
    "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏", "新疆", "香港", "澳门"
]

# 创建一个正则表达式，用于匹配省份信息
provinces_pattern = "|".join(provinces)  # 省份名称用“|”拼接，表示“或”
provinces_regex = re.compile(provinces_pattern)

# 打开CSV文件并读取每一行
with open(input_csv, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # 打开TXT文件准备写入
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        for row in csv_reader:
            # 假设每一行的文本在第一列
            text = row[0] if row else ""
            
            # 删除数字
            cleaned_text = re.sub(r'\d+', '', text)
            
            # 删除空格
            cleaned_text = cleaned_text.replace(" ", "")
            
            # 删除省份信息
            cleaned_text = provinces_regex.sub("", cleaned_text)
            
            # 写入到TXT文件中
            txt_file.write(cleaned_text + '\n')

print(f"处理完成！已将去掉数字、空格和省份信息的文本写入 {output_txt}")
