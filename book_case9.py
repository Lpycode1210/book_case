#统计文学作品中出现某一些词的数量
excludes ={"the","and","of","you","a"",i"}#除去这几个单词
def gettext():
    txt =open ("hamlet.txt","r").read()
    txt =txt.lower()#所有大写字母都被转换为小写
    for ch in '!''#$%&()*+,-./:;<>=?@[\\]^_':
        txt = txt.replace(ch,"")#它会将字符串 txt 中的所有 ch 替换为空字符串,即删除这些字符
    return txt
hamlettxt = gettext()
words=hamlettxt.split()#将变量hamlettxt中的文本内容按空格分割成单词，并将结果存储在变量 words 中

# hamlettxt = "To be, or not to be, that is the question."
# words = hamlettxt.split()
# print(words)
# ['To', 'be,', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question.']


counts={}
for word in words:
    counts[word]=counts.get(word,0) +1
items list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1>5}".format(word,count))




