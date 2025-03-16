import jieba#中文分词库，用于将中文文本分割成一个个单独的词语。在中文自然语言处理（NLP）中，\
# 分词是一个基础且重要的步骤，因为中文文本没有像英文那样的明显分隔符（如空格）来区分单词

excludes={"将军","却说","荆州","二人",'不可','不能','如此'}
txt = open("三国演义。txt","r",encoding = 'utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮"or word =="孔明曰":
        rword='孔明'
    elif word=="关公"or word=="云长":
        rword="关羽"
    elif word=="玄德"or word=="玄德曰":
        rword="刘备"
    elif word=="孟德"or word=="孟德曰":
        rword="曹操"
    else:
        rword=word
    counts[rword] = counts.get(rword,0)+1#从字典 counts 中获取键为 rword 的值。如果 rword 不存在于字典中，\
    # 则返回默认值 0。
for word in excludes:
    del(counts[word])#从字典 counts 中删除键为 word 的项
items=list(counts.items())#返回一个视图对象，包含字典 counts 中的所有键值对
items.sort(key=lambda x:x[1],reverse=True)#items.sort对列表 items 进行原地排序.\
# key=lambda x: x[1]按照每个元组的第二个元素.reverse=True指定按降序排序从高到低
for i in range(5):#排列完后只取了五个
    word,count= items[i]
    print("{0:<10}{1:>5}".format(word,count))

