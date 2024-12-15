import jieba
import re

def load_stopwords(stopwords_file):
    """加载停用词表"""
    with open(stopwords_file, "r", encoding="utf-8") as file:
        stopwords = set([line.strip() for line in file])
    return stopwords

def segment_text(input_file, output_file, stopwords_file=None, dict_file=None):
    """以段落为单位进行分词并删除标点符号"""

    # 加载停用词表
    stopwords = set()
    if stopwords_file:
        stopwords = load_stopwords(stopwords_file)
    
    # 加载词典
    if dict_file:
        jieba.load_userdict(dict_file)

    # Step 1: 读取文件内容
    with open(input_file, "r", encoding="utf-8") as file:
        paragraphs = file.readlines()  # 按行读取文件（每行视为一个段落）

    # Step 2: 逐段处理
    with open(output_file, "w", encoding="utf-8") as output_file:
        for paragraph in paragraphs:
            # 去除段落中的英文字母、数字和标点符号
            paragraph = re.sub(r'[A-Za-z0-9]+', '', paragraph)  # 删除所有英文字母和数字
            paragraph = re.sub(r'[^\u4e00-\u9fa5]+', '', paragraph)  # 仅保留中文字符
            
            # 使用jieba分词
            seg_list = jieba.cut(paragraph)
            # 过滤掉空字符串和停用词
            segmented_paragraph = " ".join([word for word in seg_list if word.strip() and word not in stopwords])
            
            # 将分词结果作为一行写入文件
            if segmented_paragraph:  # 如果段落不为空
                output_file.write(segmented_paragraph + "\n")

    print("分词完成，结果已保存到", output_file.name)

# 使用示例
input_file_path = "./Data/Jieba/Nahan.txt"  # 需要分词的文件路径
output_file_path = "./Data/Jieba/JiebaResult.txt"  # 希望输出的文件路径
dict_files_path = "./Data/Jieba/Dict.txt"  # 指定让jieba默认分词的词语（如不需要可不填）
stopwords_file_path = "./Data/Jieba/Stopwords.txt" #停用词文件路径（如不需要可不填）

segment_text(input_file_path, output_file_path, stopwords_file_path, dict_files_path)

