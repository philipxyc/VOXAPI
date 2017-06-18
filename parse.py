import re

text = '''
政治制度是寓国家本质与形式于一体，是国体与政体的总和
本单元主要讲两部分内容:
第一、有以下三点我国早期国家政治制度王位世袭制、分封制和宗法制及其主要特点。
构成中国古代早期政治制度的主要特点的是世袭制、分封制、宗法制。
第二、我国古代封建社会政体中央集权制度的发展历程与深远影响。
⑴发展历程：历程：理论提出者韩非子。发展五阶段为秦朝形成、汉朝巩固、隋唐完善、宋元加强、明清强化(顶峰)。②两大矛盾：皇权和相权、中央和地方矛盾。
⑵深远影响：下一个话题国家的形成与发展、国体与政体、官僚政治与行政管理、文化教育等传统均有关系。
中国古代各时期的阶段特征
1．夏商西周时期的阶段特征
⑴政治制度：世袭制、分封制、宗法制。
⑵经济状况：农业上出现少量青铜农具；主要土地制度井田制。手工业推行工商食官制度；商朝出现原始瓷器；西周生产斜纹提花织物。
2．春秋战国时期的阶段特征
⑴政治：分封制、宗法制走向崩溃，封建制度逐渐形成。
⑵经济：农业上井田制破坏，土地私有制形成；小农经济成为最基本的经济形态；重农抑商政策开始出现。手工业以官营手工业为主导，民营手工业和家庭手工业并存。商业上官营控制商业局面被打破。
⑶思想文化：思想上出现“百家争鸣”局面；科技上出现司南和《石氏星表》、算筹记数法。文艺上出现《诗经》、《离骚》等文学作品和帛画《人物驭龙图》等。
3．秦汉时期的阶段特征
⑴政治：①下一个问题统一全国；确下一个问题立专制主义中央集权制度。②两汉时期，中央形成中外朝制度；地方推行郡国并行制；选官实行察举制。
⑵经济：①秦朝统一货币、度量衡。②两汉时期，农业上牛耕普及，出现耧车、代田法和二牛一人的犁耕法；手工业上开始用煤冶铁，东汉烧制出成熟的青瓷。商业上，西汉开通了陆上、海上丝绸之路。
⑶文化：①秦朝推行焚书坑儒政策，禁锢思想，摧残文化。②两汉时期，思想上从“无为而治”到“罢黜百家，独尊儒术”；科技上蔡伦改进造纸术，出现系列论著，如《九章算术》《伤寒杂病论》《汜胜之书》等。文学上汉赋成为当时最高成就。
4.魏晋南北朝时期的阶段特征
⑴政治：三省体制开始形成；选官上推行九品中正制。
⑵经济：农业上推行均田制，北方形成耕耙耱技术。手工业上发明灌钢法，烧制白瓷。
⑶文化：佛教、道教盛行，冲击儒学；汉字发展进入自觉阶段，东晋王羲之被称为“书圣”。画家顾恺之留下了《女史箴图》《洛神赋图》等传世佳作。
5.隋唐时期的阶段特
⑴政治：中央完善三省六部制；后期地方出现藩镇割据局面；选官上隋朝创立科举制，唐朝继承并完善。
⑵经济：农业上，继续推行均田制，发明灌溉工具筒车，江东出现曲辕犁。手工业上，制瓷业形成南青北白两大系统。商业上，农村集市发展，柜坊和飞钱问世；城市中市坊分开；瓷器开始大量出口。
⑶文化：思想上三教合一；科技上发明雕版印刷术，火药开始用于军事；文学上是诗歌的黄金时期，出现短篇小说传奇。艺术上出现三大画家即隋朝的展子虔，唐朝的阎立本和吴道子；书法上有楷书大家颜真卿、柳公权，草书大家张旭、怀素等。
'''

text = '''
有以下两个要点
首先哈哈哈水库附近啊算了JFK撒大了JFK撒酒疯的发生了就发生纠纷撒了解发撒扩大解放啊考几分速度咯加分撒旦立刻发阿三
其次啊可怜的飞机阿拉山口飞机撒开了JFK拉丝机拉开士大夫金龙卡手机发撒辣椒粉ask就发生考了几分
有以下三个部分
第一
绿卡的数据flak艰苦拉萨大家
开始大幅加快垃圾斯洛伐克大家阿斯利康就
绿卡圣诞节分厘卡时间分厘卡似的
第二
卡死的垃圾分厘卡时间分厘卡撒酒疯卢卡斯ADSL看风景阿拉山口附近的啊
卢卡斯的解放拉萨就flask积分
卡死的解放拉萨金佛时代富婆啊司法
第三
卡萨丁JFK拉萨解放啦就是了放假啊上了飞机的拉链拉开圣诞节分厘卡啊代理商积分拉丝机拉屎啊撒旦立刻就弗利萨就

'''
wordlist = {
    # candidate word for parallel relationship (but or and also...)
    'paral':[
        "两部分"
        "有两个",
        "以下两点",
        "以下两个",
        # "三部分",
        # "有三个",
        # "以下三点",
        # "以下三个",
    ],

    # candidate word for change topic
    'tpflag':[
        "首先",
        "其次",
        "第一",
        "第二",
        # "第三",
        "第一点",
        "第二点",
        # "第三点",
        "下一个问题",
        "下一个话题",
        "接下来有一点",
        "最后一点",
    ],

    # candidate word for enlight
    # 'enlight':[
    #     "重要",
    #     "极其",
    # ],
}

# def kw_detection(text):
#     max_kw = 5
#     params = {'top_k': max_kw}
#     data = json.dumps(text)
#     print(data)
#     headers = {'X-Token': 'HIqI4DsM.15958.iMvyeSHo0VcM'}
#     resp = requests.post(KEYWORDS_URL, headers=headers, params=params, data=data.encode('utf-8'))
#
#     for weight, word in resp.json():
#         print(weight, word)
#     print(resp.json())
#     return resp.json()


info_topic = []
info_relation = []

word_test = text.split()
word_test = [[item] for item in word_test]

# pass 1
for item in word_test:
    for temp in wordlist['tpflag']:
        if item[0].find(temp) != -1:
            item.append([1])
            break
# pass 2
for item in word_test:
    for temp in wordlist['paral']:
        if item[0].find(temp) != -1:
            item.append([2])
            break

for i in range(len(word_test)):
    if [1] in word_test[i]:
        info_topic.append(i)
    if [2] in word_test[i]:
        info_relation.append(i)

print(info_topic)
print(info_relation)


for i in word_test:
    print(i)
print(word_test)

kw_list = []
new_list = []
temp = 0

if info_topic:
    new_list.append(word_test[:info_topic[0]])
    for i in range(len(info_topic)):
        if (i < len(info_topic)-1):
            new_list.append(word_test[info_topic[i]+1:info_topic[i+1]]) # merge the sentenses of one topic
    new_list.append(word_test[info_topic[-1]+1:])

print()
for i in new_list:
    ans = ''
    print(i)
    for j in i:
        ans += j
    print(ans)
    kw_temp = kw_detection(ans)
    print(kw_temp)



# pass 2

# pass 3
