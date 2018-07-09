# _*_ encoding:utf-8 _*_
import jieba.analyse
'''
@auther liudong
使用TF-IDF算法从文本中提取关键字
extract_tags中的变量：{
    topK:返回的关键字的数量  默认值是20
    allowPOS: 允许使用的指定词性的词。默认值为空，即不过滤
    withWeight:只有在allowPOS不为空的时候才可以使用
                如果是 True，返回一个成对的list，其中的元素是pair(word,weight)
                如果是 False，返回一个word的列表
}

'''
s = "云计算在电子政务中的应用\
     电子政务为信息的公开和共享创造了条件,将现代信息和通信技术运用到其管理和服务职能中,\
     随着电子政务的发展,政府逐渐意识到电子政务集中建设的必要性及优越性.为了更好解决政府\
     在电子政务及信息化办公过程中所带来的信息孤岛问题,服务器管理分散问题,维护及硬件成本过\
     快增长等问题,云计算的出现,正是电子政务变革的大好机遇.云计算是国家“十二五”规划中的重点\
     关注项目,它将成为当前电子政务建设必须重视的发展趋势.本文通过对云计算概念的描述,分析云计\
     算在电子政务应用中的优缺点及其前景.据半岛电视台援引叙利亚国家电视台称，叙利亚已经对美国、\
     英国、法国的空袭进行了反击。据介绍，在叙军武器库中，对西方最具威慑力的当属各型战术地对地弹\
     道导弹。尽管美英法是利用巡航导弹等武器发动远程空袭，但叙军要对等还击却几乎是“不可能完成的任务”。\
     目前叙军仍能作战的战机仍是老旧的苏制米格-29、米格-23、米格-21战斗机和苏-22、苏-24轰炸机，它们\
     在现代化的西方空军面前难有自保之力，因此叙军的远程反击只能依靠另一个撒手锏——地对地战术弹道导弹."
seg = jieba.analyse.extract_tags(s, topK=20, withWeight=True)
for tag,weight in seg:
    print "%s %s" %(tag,weight)
cut = jieba.cut(s)
words = list(cut)
print len(words)


'''
输出结果：
电子政务 0.495686267737
叙军 0.302652341846
米格 0.168175681045
计算 0.141731945749
地对地 0.138037283271
空袭 0.113679705394
远程 0.102667309887
叙利亚 0.10217382322
信息 0.0997568485969
电视台 0.0968933023606
反击 0.0966262924485
战术 0.0897257285797
撒手锏 0.0777926565791
24 0.0756630854614
21 0.0756630854614
22 0.0756630854614
23 0.0756630854614
云计 0.0756630854614
29 0.0756630854614
法是 0.0756630854614
322
'''

