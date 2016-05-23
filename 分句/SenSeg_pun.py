# -*- coding: utf-8 -*-

"""
功能：根据标点符号规则进行分句，亚马逊中文书评；读取某个目录下的所有XML文件。
时间：2016年4月12日 20:37:22
性能：目前跟哈工大语言云的分句基本一致（测试了3000句子，分句100%一致）2016年4月12日测试
"""

import xml.dom.minidom
import re
import codecs
import os


def fenju(par, par2):                                # par——文件名；par2——文件编号
    bdlist = [u"。", u"？", u"！", u"；", u"…"]      # 分句标点
    filepath = path + "\\" + par                     # 文件路径
    dom = xml.dom.minidom.parse(filepath)            # 加载读取XML文件
    root = dom.documentElement                       # 获取XML文档对象
    titles = dom.getElementsByTagName('title')
    scores = dom.getElementsByTagName('score')
    contents = root.getElementsByTagName("content")  # 注意获取的的是一组标签,contents[0]表示第一个

    # 获取书名，并用于新建文本命名
    booktitle = titles[0].firstChild.data
    newfolder = path + u"\分句后"                     # 在原路径新建一个文件夹，名为“分句后”
    if not os.path.exists(newfolder):
        os.mkdir(newfolder)

    newfile = codecs.open(newfolder + u"\【分句后】" + str(par2) + "." +
                          booktitle + ".xml", "a", "utf-8")      # 新建一个存放数据的文本

    file1 = codecs.open(filepath, "r")
    newfile.truncate()
    for line in file1.readlines()[0:6]:                          # 前XX行
        newfile.write(line.decode("utf-8"))

    # 写入评分项
    score0 = scores[0].firstChild.data
    score = re.findall(r'(\w*[0-9].[0-9])\w*.', score0)[0]
    newfile.write("  <score>" + score + "</score>\n")

    file2 = codecs.open(filepath, "r")
    for line in file2.readlines()[7:12]:
        newfile.write(line.decode("utf-8"))
    newfile.write("\n")

    for x in range(len(contents)):                           # 书评数量
        content = contents[x].firstChild.data                # 获取书评内容
        reviewtitle = titles[x + 1].firstChild.data          # 获取书评题目

        wz_pat = re.compile("http[s]*:[/.?%&=\-\w]*", re.S)  # 删除以http或https开头的网址
        content = wz_pat.sub("", content)

        # 中英文标点替换（英文句号在下面单独处理）
        en_bd = ["'", "\"", "?", "!", ",", ";", ":"]
        zh_bd = [u"’", u"”", u"？", u"！", u"，", u"；", u"："]
        for j in range(len(en_bd)):
            content = content.replace(en_bd[j], zh_bd[j])
            reviewtitle = reviewtitle.replace(en_bd[j], zh_bd[j])

        dot_pat = re.compile(u'[\u4e00-\u9fa5][.]+')         # 检测中文后的英文句号
        dots = re.findall(dot_pat, content)
        for b in dots:
            b1 = b.replace(".", u"。")
            content = content.replace(b, b1)

        space_pat = re.compile(u' [\u4e00-\u9fa5]')          # 检测中文之前的空格并删除
        items = re.findall(space_pat, content)
        for a in items:
            a1 = a.replace(" ", "")
            content = content.replace(a, a1)

        bdpattern = re.compile(u'[~，。！？… ]{2,}')          # 对于两个及以上的连续标点和空格，只保留最后一个
        mulbd = re.findall(bdpattern, content)               # 注意正则列表的最后一项是空格（在…的后面）
        for item in mulbd:
            content = content.replace(item, item[-1])

        content = content.replace(u"…", u"……")                 # 修正中文省略号

        char_pat = re.compile(u'([&]+(amp;|lt;|gt;|quot;)?)')     # 删除干扰字符
        content = char_pat.sub("", content)
        char_pat2 = re.compile(u'[‘’<>“”*]')                      # 删除不常用字符，可补充
        content = char_pat2.sub("", content)
        char_pat3 = re.compile(u'#\d+；')                         # 删除特殊字符 #数字;
        content = char_pat3.sub("", content)
        reviewtitle = char_pat.sub("", reviewtitle)
        reviewtitle = char_pat2.sub("", reviewtitle)

        pat0 = re.compile(u'[《][^》]*?[。？！；…][^》]*?[》]')     # 将书名号里的分句标点改为空格
        pat1 = re.compile(u'[。？！；…]+')
        dd = re.findall(pat0, content)
        for d in dd:
            d1 = pat1.sub(" ", d)
            content = content.replace(d, d1)

        if content[-1] not in bdlist:                            # 如果内容的最后没有标点，则加一个句号
            content += u"。"
        content = content.replace(u"。", u"。chur").replace(u"！", u"！chur").replace(u"？", u"？chur")
        content = content.replace(u"；", u"；chur").replace(u"……", u"……chur")
        content = re.split("chur", content)            # 分句

        str0 = "\"" + str(x + 1) + "\""
        newfile.write("<review ID=" + str0 + ">\n" +
                      "  <reviewtitle>" + reviewtitle + "</reviewtitle>\n")

        i = 1
        zh_pat = re.compile(u'[\u4e00-\u9fa5]+')       # 正则表达式，匹配中文字符
        for j in range(len(content)-1):                # 考虑到分割的最后一个为空，不是句子，所以-1
            if zh_pat.search(content[j]):              # 如果句子content[i]中含有中文，才写入
                str1 = "\"" + str(i) + "\""            # 注意编号
                newfile.write("  <sentence ID=" + str1 + ">" + content[j] + "</sentence>\n")
                i += 1

        newfile.write("</review>\n\n")
        # 注意，如果书评通篇没有中文，则分句后在新文本里将没有句子。

    newfile.write("</allreviews>\n\n</bookxml>")
    newfile.close()
    file1.close()

# 主程序
count = 0
path = raw_input(u"正在进行分句处理，请输入文件目录:").decode("utf-8")
filenames = os.listdir(path)                               # 列出目录下的文件/目录
for filename in filenames:
    if ".xml" in filename:
        num = re.findall(r'(\w*[0-9]+)\w*.', filename)[0]  # 提取文件编号,以便后面命名
        print u"正在处理文件:", filename
        fenju(filename, num)
        count += 1

print u"已完成分句！处理文件数:", count
