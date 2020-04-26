import random



def 幾時():
    日子 = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日",
            "禮拜一","禮拜二","禮拜三","禮拜四","禮拜五","禮拜六","禮拜日"
            "今日","聽日","後日","大後日",
            "一月","二月","三月","四月","五月","六月",
            "七月","八月","九月","十月","十一月","十二月",
            "春天","夏天","秋天","冬天"]
            
    時間 = ["一個鐘","兩個鐘","三個鐘","四個鐘","五個鐘","六個鐘",
            "七個鐘","八個鐘","九個鐘","十個鐘","十一個鐘","十二個鐘",
            "一點鐘","兩點鐘","三點鐘","四點鐘","五點鐘","六點鐘",
            "七點鐘","八點鐘","九點鐘","十點鐘","十一點鐘","十二點鐘",
            "5分鐘","10分鐘","15分鐘","20分鐘","30分鐘","40分鐘","50分鐘"]
            
    前後 = ["之前","之後"]
    內後 = ["之內","之後"]
    
    時間語素 =  時間[random.randint(0,len(時間)-1)] #+ 前後[random.randint(0,len(前後)-1)] 
    日子語素 =  日子[random.randint(0,len(日子)-1)] #+ 內後[random.randint(0,len(內後)-1)] 
    
    幾時先 = ["陣間","今朝","聽朝","今晚","聽晚",
            時間語素,日子語素,時間語素,日子語素,時間語素,日子語素,]
    成句野 = 幾時先[random.randint(0,len(幾時先)-1)]
    
    return 成句野

def 求其一條戰線():
    八股文 = [["Facebook","like同share"],
              ["Twitter","retweets"],
              ["白宮聯署","簽"],
              ["Youtube","睇"],
              ["選民登記","登記"],
              ["申訴專員公署","投訴"],
              ["區議會","關注"],
              ["立法會","關注"],
              ["城規會","關注"],
              ["連儂牆","睇"],
              ["連儂牆","貼"],
              ["文宣","整"],
              ["黃色經濟圈","幫趁"],
              ["Steam","留言"],
              ["功能組別","登記"],
              ["Reddit","uppost"],
              ["4chan","留言"],
              ["5ch","解釋"],
              ["周庭youtube channel","睇"],
              ["BNO平權","聯署"],
              ["國際","推"]]
    戰線語素 = 八股文[random.randint(0,len(八股文)-1)]
    #print("戰線語素",戰線語素)
    return 戰線語素

def 戰線手足():
    手足 = 求其一條戰線()[0]
    手足 = 手足 + "戰線手足"
    return 手足
    
def 召喚爸爸():
    八股文 = ["所羅門","特朗普","陳雲","大學教授","政府AO",
        "老豆搵仔","我個藍絲老母","燒生","劉世良",
        "肥老黎","文匯報","大公報","環球時報",
        "黃洋達","李慧玲","吳志森","Steam",
        "品蔥手足","大陸網友","郭文貴",
        "文宣手足","烏克蘭網友","台灣網友","日本網友",
        "韓國網友","智利網友","印尼網友","瑞典網友",
        "英國網友","美國網友","CIA","FBI",
        "英國內政部","人權法案委員會","美國眾議院","美國參議院",
        "英國眾議院","英國參議院","英國領使館","美國領使館",
        "赤柱手足","沙咀手足","荔枝角手足","石壁手足",
        "龍心","劉馬車","羅志祥","楊岳橋","民間記者會",
        "好多人","好多手足","山海經","推背圖","張塔羅牌",
        "個卜卦","個星象圖","個碟仙","個筆仙",
        "陳義士","何義士","張義士","黃義士","王義士","林義士",
        "梁義士","郭義士","曾義士",
        "攬炒團隊","攬炒巴打","香討巴打","5p手足","南亞手足",
        "中大巴打","理大巴打","浸大手足","科大手足",
        "城大巴打","開大巴打","嶺大手足","樹仁手足","教大巴打",
        "鬼佬教授","鬼佬手足","鬼佬老世","鬼佬朋友",
        戰線手足(),戰線手足(),戰線手足(),戰線手足(),戰線手足(),戰線手足()]
        
        #"","","","",
    return str(八股文[random.randint(0,len(八股文)-1)])
    
def 係咪():
    八股文 = ["冇人識做","冇人記得","忘記哂","變咗condom",
              "變哂condom","畀你地拋棄咗","唔想光復香港",
              "變哂義工","想餓死手足","已經認輸","已經冇人理",
              "唔想煲底見","唔記得我地約咗煲底見","場運動已經完咗",
              "場運動就嚟贏","場運動就嚟輸","場運動冷卻咗",
              "我地就嚟贏","我地就嚟贏","我地已經冷卻咗",
              "冇人會理","冇人再去理","冇人關心",
              "已經光復咗香港","時代革命成功咗","同popo好番哂",
              "可以當乜事都冇發生過","已經輸哂","已經投降",
              "可以做返港豬","已經冇人再理政治","全部人移哂民",
              "忘記左612","忘記左721","忘記左831",
              "已經唔洗再理","等到懵左","已經唔識唱願榮光歸香港",
              "已經冇人"]
              #"","","",
    係咪語素 = str(八股文[random.randint(0,len(八股文)-1)])
    return 係咪語素    





#####################
# 我屌哂你地老母
#####################
def 屌老母():
    屌老母大全 = ["我屌哂你地老母",
                    成個熱門都係(),
                    "我屌哂你地老母，" + 成個熱門都係(),
                    "我屌哂你地老母，咁大件事冇人提？",
                    成個熱門都係() + ",咁大件事冇人提？",
                    戰況(),
                    著哂火要人(),
                    著哂火要人() + ",咁大件事冇人提？",
                    著哂火要人() + "，但係" + 成個熱門都係(),
                    著哂火要人() + "你哋係咪想輸？",
                    著哂火要人() + "全世界同我入嚟！"
                    "全世界同我入嚟！",
                    "我屌哂你地老母，全世界同我入嚟！",
                    "全世界同我入嚟！咁大件事冇人提？",
                    "你哋係咪想輸？",
                    "我屌哂你地老母，你哋係咪想輸？",
                    "係咪仲未有人意識到" + 著哂火要人() + "有幾嚴重？",
                    "點解" + 幾時() + 召喚爸爸() + "嗰單嘢沉得咁快"] 
    成句野 = 屌老母大全[random.randint(0,len(屌老母大全)-1)]
    return 成句野

def 成個熱門都係():
    八股文 = ["唔關事嘅post","無關痛癢嘅post","港女post",
              "咸濕野","羅志祥","日本地震","郭紹傑",
              "美心太子女","淘寶開箱","化粧品","youtuber",
              "伍公子","大J","龍門","國難五金",
              "達哥","pewdiepie","689","鄧炳強",
              "區議會","立法會","法庭新聞","八掛新聞",
              "口罩post","裝備post","行動post",
              "林鄭月娥",幾時()+"個記者會",幾時()+"個行動",
              幾時()+"個遊行",幾時()+"個集會",
              "頭先個記者會","而家個記者會",
              "頭先個行動","而家個行動",
              "頭先個遊行","而家個遊行",
              "頭先個集會","而家個集會",
              召喚爸爸(),召喚爸爸(),召喚爸爸()]
              
    係唔係 = ["係","冇"]
    成句野 = "成個熱門都" + \
            係唔係[random.randint(0,len(係唔係)-1)] + \
            八股文[random.randint(0,len(八股文)-1)]
    return 成句野
    
    
#####################
# 唔准再講
#####################
def 唔准再講():
    八股文 = ["唔准再講","唔准再提","中止討論","禁止討論",
            "不得再討論","唔好再講","唔好再提","要忘記件事"]
            
    成句野 = "我宣佈" + 幾時()+ "之後" + 八股文[random.randint(0,len(八股文)-1)]
    return 成句野


#####################
# 點對得住
#####################
def 點對得住():  
    八股文 = ["仲對得住","你對得住","問心你仲有面對住",
                "乜你覺得咁樣做就對得住","你問下良心你對得住"]
    成句野 = 八股文[random.randint(0,len(八股文)-1)] + 召喚爸爸() + "咩？"
    return 成句野


#####################
# 問點解
#####################
def 問點解():
    成句野 = 召喚爸爸() + "問我點解" + 係咪()
    return 成句野


#####################
# 係咪已經變成condom
#####################
def condom():
    八股文 = [召喚爸爸(),戰線手足()]
    前 = str(八股文[random.randint(0,len(八股文)-1)])
    後 = "係咪已經變成condom"
    成句野 = 前 + 後
    return 成句野
    

#####################
# 已經提哂水
#####################
def 已經提哂水():
    前 = 召喚爸爸()
    中 = "已經提哂水，係咪"
    後 = 係咪()
    成句野 = 前 + 中 + 後
    return 成句野
    
    
#####################
# 著哂火要人
#####################    
def 著哂火要人():
    八股文 = ["著哂火","要人","輸緊成條街"]
    要人語素 = 求其一條戰線()[0] + "戰線" + 八股文[random.randint(0,len(八股文)-1)]
    return 要人語素


#####################
# 冇人講
#####################  
def 冇人講():
    成句野 = 0
    
    
#####################
# 戰況
##################### 
def 戰況():
    呢條戰線 = 求其一條戰線()
    前 = 呢條戰線[0] + 著哂火要人()
    中 = "，你今日"
    後 = 呢條戰線[1] + "左未？"
    成句野 = 前 + 中 + 後

    #print(1,呢條戰線)
    #print(2,前)
    #print(3,中)
    #print(4,後)
    #print(5,成句野)
    return 成句野
    
    
#####################
# 問係咪
#####################    
def 問係咪():
    成句野 = "係咪" + 係咪()
    return 成句野
    
    
#####################
# 其實我哋
##################### 
def 其實我哋():
    八股文 = ["就嚟贏","就嚟輸","已經贏左","已經輸左"]
              #"","","",
    成句野 = "其實我地" + str(八股文[random.randint(0,len(八股文)-1)])    
    return 成句野


#####################
# 應承我
##################### 
def 應承我():
    成句野 = "應承我，如果見到呢個post嘅話，推上熱門()"
    return 成句野
    
def 推上熱門():
    八股文 = ["一定要推上熱門","一定要推上頭條","一定要推上國際新聞"]
              #"","","",
    成句野 = 幾時() + "之內" + str(八股文[random.randint(0,len(八股文)-1)])   
    return 成句野
 
 
#####################
# 如果唔係
#####################     
def 如果唔係():
    八股文 = ["我地就嚟贏","我地就嚟輸","我地已經贏咗","我地已經輸咗",
            "我地好快會贏","我地好快輸",
            "我地正式玩完","呢場運動正式收皮"]
              #"","","",
    成句野 = "如果唔係我宣佈" + str(八股文[random.randint(0,len(八股文)-1)])   
    return 成句野    
    
    
#####################
# 開心樂園餐
##################### 
def 開心樂園餐():
    print(屌老母())

    for n in range(random.randint(1,5)):
        print(點對得住())

    print(問點解()) 
    print(求其一條戰線()[0] + "戰線" + 著哂火要人()) 
    print(condom())
    print(已經提哂水())

    for n in range(random.randint(1,10)):
        print(問係咪())
    print(其實我哋())    
    print(唔准再講())
    print(應承我())
    print(如果唔係())
    print("\n")
    

    
    
while True:
    query = input("你想要幾多篇連八股? : ")
    
    if type(int(query)) != int:
        print("請輸入有效數字")
    
    elif type(int(query)) == int:
        for k in range(int(query)):
            開心樂園餐()
