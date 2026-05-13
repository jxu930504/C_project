# 遊戲腳本位於此檔案。
image typing_cursor:
    # 使用純文字符號 "|" 作為游標，你也可以換成圖標
    Text("|", color="#000000", size=gui.nvl_text_size)
    alpha 1.0
    pause 0.4
    alpha 0.0
    pause 0.4
    repeat

init python:
    def type_sound(event, interact=True, **kwargs): #打字音
        if event == "begin":
            # 確保總行數大於 0，避免發生除以零的數學錯誤
            if store.nvl_total_lines > 0:
                # 自動計算這行對話佔全部的百分之幾
                step = 100.0 / store.nvl_total_lines
                
                # 增加進度
                store.nvl_progress += step
                
                # 安全機制：確保進度條不會破表超過 100
                if store.nvl_progress > 100.0:
                    store.nvl_progress = 100.0
        if not interact:
            return
        # 當文字正在「顯示中」 (show) 且玩家沒有跳過動畫時播放
        if event == "show":
            # 這裡播放你的音效檔案，建議使用非常短促的聲音 (0.1秒左右)
            # loop=True 代表如果文字沒跑完就一直循環播放
            renpy.music.play("audio/clicks.mp3", channel="sound", loop=True)
        
        # 當文字顯示「完畢」 (slow_done) 或被玩家「跳過」 (end) 時停止聲音
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    
    #引入C函式
    import ctypes
    import os

    dll_path = os.path.join(config.gamedir, "C/password_checker.dll")

    try:
        my_lib = ctypes.CDLL(dll_path)
        
        # 設定函數參數與回傳型態
        # input_password 是字串 (c_char_p)，回傳值是整數 (c_int)
        my_lib.check_password.argtypes = [ctypes.c_char_p]
        my_lib.check_password.restype = ctypes.c_int
        
        dll_loaded = True
    except Exception as e:
        dll_loaded = False


    
        

# 進度條變數 
default nvl_progress = 0.0      # 當前進度
default nvl_total_lines = 10    # 預設總行數 (防止錯誤用)
# 劇情變數
default pet = "dog"
default Owner = 1
default pass_game =0
default help_2 = 0
# 章節進度
default persistent.unlocked_ch1_0 = False
default persistent.unlocked_ch1_1 = False
default persistent.unlocked_ch1_2 = False
default persistent.unlocked_ch1_3 = False
default persistent.unlocked_ch1_BE1 = False

default persistent.unlocked_ch2_1 = False
default persistent.unlocked_ch2_2 = False
default persistent.unlocked_ch2_3 = False
default persistent.unlocked_ch2_4 = False
default persistent.unlocked_ch2_5 = False
default persistent.unlocked_ch2_BE1 = False
default persistent.unlocked_ch2_BE2 = False

default persistent.unlocked_ch3_1 = False
default persistent.unlocked_ch3_2 = False
default persistent.unlocked_ch3_3 = False
default persistent.unlocked_ch3_4 = False
default persistent.unlocked_ch3_5 = False
default persistent.unlocked_ch3_BE1 = False
default persistent.unlocked_ch3_BE2 = False
default persistent.unlocked_ch3_BE3 = False
default persistent.unlocked_ch3_BE4 = False
default persistent.unlocked_ch3_BE5 = False
default persistent.unlocked_ch3_GE1 = False
default persistent.unlocked_ch3_GE2 = False

# 宣告角色。 
#nvl
# === 1. NVL 模式角色 ===
define s = Character('我', kind=nvl, color="#349634", callback=type_sound, ctc="typing_cursor", ctc_position="nestled")
define nvl_narrator = Character(None, kind=nvl, callback=type_sound, ctc="typing_cursor", ctc_position="nestled")

define nvl_dark = Character(None, kind=nvl, screen="nvl_black",what_color="#ffffff", callback=type_sound, ctc="typing_cursor", ctc_position="nestled")

# === 2. ADV 模式角色 ===
define p = Character('我', callback=type_sound, ctc="typing_cursor", ctc_position="nestled")
define narrator = Character(None, callback=type_sound, ctc="typing_cursor", ctc_position="nestled")
# 遊戲從這裡開始。
define menu = nvl_menu


label start:
    $ quick_menu = False
    nvl clear
    #scene intro_1
    jump CH1_0
label CH1_0:
    nvl clear
    $ persistent.unlocked_ch1_0 = True
    scene intro_1
    nvl_dark "某天，我一如往常地打開YouTube看影片。"
    nvl_dark "發現YouTube推薦我從來不看的懸疑影片。"
    nvl_dark "不知道怎麼了，我決定看這個影片。"
    nvl_dark "……"
    scene intro_2
    nvl_dark "例行的登山訓練，整個登山隊卻只剩一人存活。"
    nvl_dark "有人半脫褲子倒在雪洞前，"
    nvl_dark "有人手指天空面帶微笑地死去，"
    nvl_dark "有人用血在雪地上畫下渦漩，"
    nvl_dark "這一切讓所有人百思不得其解。"
    nvl_dark "最後結論雖然是所有人皆因失溫症而死，"
    nvl_dark "但還是有很多說不清的地方。"
    nvl_dark "……"
    scene intro_3
    nvl_dark "看著看著，"
    nvl_dark "我不知不覺睡著了。"
label CH1_1: #荒野求生
    $ persistent.unlocked_ch1_1 = True
    nvl clear
    scene game_ch1
    $ quick_menu = True
    $ nvl_progress = 0.0
    $ nvl_total_lines = 40
    nvl_narrator "(好冷，一陣刺骨的寒風吹來)"
    nvl_narrator "我睜開眼睛，"
    nvl_narrator "發現我躺在雪地裡，"
    nvl_narrator "太陽似乎才剛升起，"
    nvl_narrator "天色還很暗。"
    nvl_narrator "好奇怪，"
    nvl_narrator "我明明躺在雪地裡卻不覺得冷。"
    nvl_narrator "……"
    nvl_narrator "我看了看自己的手，"
    nvl_narrator "我怎麼變成了____"
    menu:
        "小貓":
            $ pet = "cat"
            nvl_narrator "我竟然變成了一隻貓!"
        "小狗":
            $ pet = "dog"
            nvl_narrator "我竟然變成了一隻狗!"
    nvl_narrator "(咕嚕咕嚕…)"
    nvl_narrator "我的肚子好餓，"
    nvl_narrator "沒時間搞清楚發生什麼事了，"
    nvl_narrator "我需要先找些食物。"
    nvl_narrator "環顧四周，"
    nvl_narrator "我決定朝著_________走:"
    menu:
        "隱約發光的遠方":
            nvl_narrator "我看到遠處似乎有一棟發光的建築物，"
            nvl_narrator "決定開始朝那裡走去，"
            nvl_narrator "一段時間後，"
            nvl_narrator "我看到一棟木屋。"
            jump CH1_2
        "視野良好的山峰":
            jump CH1_BE1
label CH1_BE1:    #誤判
    $ persistent.unlocked_ch1_BE1 = True
    scene game_ch1
    nvl_narrator "我決定先往視野良好的山峰走去，"
    nvl_narrator "那裡應該有良好的視野，"
    nvl_narrator "這樣我就能知道去哪裡找食物。"
    nvl_narrator "……"
    nvl_narrator "走了好久，"
    nvl_narrator "山峰比看起來的還遠，"
    nvl_narrator "我已經快撐不下去了…"
    nvl_narrator "我倒在雪地中，"
    nvl_narrator "覺得身體越來越冷…"
    nvl_narrator "<END-誤判>"
    return
label CH1_2: #登山隊
    $ persistent.unlocked_ch1_2 = True
    scene game_ch1
    nvl_narrator "我離木屋還有一段距離，"
    nvl_narrator "但我的體力已經接近極限，"
    nvl_narrator "不知道我還能撐多久。"
    nvl_narrator "……"
    nvl_narrator "欸?"
    nvl_narrator "我怎麼好像聞到食物的味道，"
    nvl_narrator "我打起精神順著味道走過去，來到木屋前。"
    nvl_narrator "這間木屋的門竟然沒有關好，味道隨著風從屋裡飄出。"
    nvl_narrator "我鑽過門縫，走了進去，裡面分成好幾個房間。"
    nvl_narrator "風把味道混合在一起，但我還是分得出來。"
    nvl_narrator "我走到了有_______的門前"
    menu: 
        "風曬過的肉味":
            $ Owner =1;
            nvl_narrator "(我走到了有風曬過的肉味的門前)"
            nvl_narrator "過了一陣子，門開了。 "
            nvl_narrator "他看了我一眼，沒有說話。 "
            nvl_narrator "只是側過身，讓我進去。 "
            nvl_narrator "我走進房間，發現剛剛聞到的是肉乾的味道。 "
            nvl_narrator "…… "
            nvl_narrator "他給了我一些水和食物，"
            nvl_narrator "吃完之後，我在房間裡閒逛。"
            nvl_narrator "房間裡掛滿了登山證書，有些邊角已經泛黃。"
            nvl_narrator "旁邊整齊地擺著繩索、頭燈，還有收拾好的登山裝備。"
            nvl_narrator "但在角落裡，放著一個異常沉重的背包。 "
            nvl_narrator "桌上還有一張地圖，上面畫滿了路線，"
            nvl_narrator "有些被劃掉，又重新畫過，"
            nvl_narrator "透出一股不容妥協的責任感。 "
            nvl_narrator "最後我在房間裡找了一個地方休息。"
        "清香的草藥味":
            $ Owner =2;
            nvl_narrator "(我走到了有清香的草藥味的門前)"
            nvl_narrator "過了一陣子，門開了。"
            nvl_narrator "他看了我一眼，沒有說話。"
            nvl_narrator "只是側過身，讓我進去。 "
            nvl_narrator "我走進房間，發現剛剛聞到的是熱湯的味道。 "
            nvl_narrator "…… "
            nvl_narrator "他給了我一些水和食物，"
            nvl_narrator "吃完之後，我在房間裡閒逛。 "
            nvl_narrator "桌上擺滿了醫療用品。 "
            nvl_narrator "繃帶、針筒，還有幾個藥瓶整齊地排列著。 "
            nvl_narrator "旁邊堆著幾本厚重的醫學書，翻到一半。 "
            nvl_narrator "紙上畫著人體的圖，還有密密麻麻的標記。 "
            nvl_narrator "最後我在房間裡找了一個地方休息。"
        "淡淡的麥香味":
            $ Owner =3;
            nvl_narrator "(我走到了有淡淡的麥香味的門前)"
            nvl_narrator "過了一陣子，門開了。 "
            nvl_narrator "他看了我一眼，沒有說話。 "
            nvl_narrator "只是側過身，讓我進去。 "
            nvl_narrator "我走進房間，發現剛剛聞到的是麵包的味道。 "
            nvl_narrator "…… "
            nvl_narrator "他給了我一些水和食物，吃完之後，我在房間裡閒逛。 "
            nvl_narrator "房間有點亂，背包隨意丟在角落，衣服堆在椅子上。 "
            nvl_narrator "還有一些健身器材散落在地上。 "
            nvl_narrator "他似乎是個容易神經興奮的人，"
            nvl_narrator "坐在那裡手腳仍不自覺地快速活動著。 "
            nvl_narrator "最後我在房間裡找了一個地方休息。"
        "濃濃的奶香味":
            $ Owner =4;
            nvl_narrator "(我走到了有濃濃的奶香味的門前)"
            nvl_narrator "過了一陣子，門開了。 "
            nvl_narrator "他看了我一眼，沒有說話。 "
            nvl_narrator "只是側過身，讓我進去。 "
            nvl_narrator "我走進房間，發現剛剛聞到的是起司的味道。 "
            nvl_narrator "…… "
            nvl_narrator "他給了我一些水和食物，"
            nvl_narrator "吃完之後，我在房間裡閒逛。 "
            nvl_narrator "牆上掛滿了照片。 "
            nvl_narrator "桌上擺著相機和鏡頭，"
            nvl_narrator "還有一疊沖洗好的照片。 "
            nvl_narrator "他靜靜地看著我在房間裡走動，"
            nvl_narrator "展現出極為敏銳的觀察力。 "
            nvl_narrator "最後我在房間裡找了一個地方休息。"
        "濃烈的煙燻味":
            $ Owner =3;
            nvl_narrator "(我走到了有濃烈的煙燻味的門前)"
            nvl_narrator "過了一陣子，門開了。 "
            nvl_narrator "他看了我一眼，沒有說話。 "
            nvl_narrator "只是側過身，讓我進去。 "
            nvl_narrator "我走進房間，發現剛剛聞到的是烤香腸的味道。 "
            nvl_narrator "…… "
            nvl_narrator "他給了我一些水和食物，"
            nvl_narrator "吃完之後，我在房間裡閒逛。 "
            nvl_narrator "房間裡的裝備極度精簡且實用，"
            nvl_narrator "他正專注地檢查著禦寒的羽絨服。 "
            nvl_narrator "他的眼神銳利，透著一股極強的務實感與求生欲，"
            nvl_narrator "彷彿隨時準備應對最極端的生存考驗。 "
            nvl_narrator "最後我在房間裡找了一個地方休息。"
        "溫熱的茶香味":
            $ Owner =3;
            nvl_narrator "(我走到了有溫熱的茶香味的門前)"
            nvl_narrator "過了一陣子，門開了。 "
            nvl_narrator "他看了我一眼，沒有說話。 "
            nvl_narrator "只是側過身，讓我進去。 "
            nvl_narrator "我走進房間，發現剛剛聞到的是熱紅茶的味道。 "
            nvl_narrator "…… "
            nvl_narrator "他給了我一些水和食物，"
            nvl_narrator "吃完之後，我在房間裡閒逛。 "
            nvl_narrator "他正細心地替裝備塗抹防水層，"
            nvl_narrator "房間沒有太多花俏的裝飾。 "
            nvl_narrator "他桌角還著幾卷備用的相機底片，"
            nvl_narrator "似乎他也曾負責過拍照的工作。 "
            nvl_narrator "最後我在房間裡找了一個地方休息。"    
label CH1_3: #訓練
    $ persistent.unlocked_ch1_3 = True
    scene game_ch1
    nvl_narrator "……"
    nvl_narrator "在我找到回去的方法之前，"
    nvl_narrator "我決定先在這棟木屋住下來。"
    nvl_narrator "日子一天一天的過，我漸漸跟他培養起感情，"
    nvl_narrator "也逐漸習慣了這個身體。"
   
    nvl_narrator "我發現他們似乎就是影片中的登山隊，"
    nvl_narrator "這支菁英小隊由隊長列文帶領，成員包括隊醫法布、隊員布爾金、沃寧、拉扎，"
    nvl_narrator "與攝影師奧金。"
    if(Owner==1):
        nvl_narrator "而我的主人正是登山隊的隊長。"
    elif(Owner==2):
        nvl_narrator "而我的主人正是登山隊的隊醫。"
    elif(Owner==3):
        nvl_narrator "而我的主人正是登山隊的隊員。"
    elif(Owner==4):
        nvl_narrator "而我的主人正是登山隊的攝影師。"
    nvl_narrator "平常，我會跟他們一起去做登山的基本訓練，"
    nvl_narrator "休息時，他們也會陪我一起玩。"

    nvl_narrator "響片遊戲(45秒)"
    nvl_narrator "遊戲說明:當聽到響片聲，便按下空白鍵，越到後面越快"
    #TODO 遊戲未完成
    menu:
        "通過":
            $ pass_game = 1
            nvl_narrator "我們玩了響片遊戲一個月之後，"
            nvl_narrator "他在房間裝了幾個按鈕，"
            nvl_narrator "讓我可以表達需求，"
            nvl_narrator "我最常按的是食物。"
            nvl_narrator "他偶爾還會用雙手跟我溝通，"
            nvl_narrator "像是要不要出去玩。"
        "未通過":
            $ pass_game = 0
            nvl_narrator "雖然我玩的不怎麼樣，"
            nvl_narrator "但他還是很有耐心。"
            nvl_narrator "我們溝通還是主要透過他的解讀，"
            nvl_narrator "偶爾會用雙手跟我溝通，"
            nvl_narrator "像是要不要出去玩。"
    nvl_narrator "他時常還會把我當作訓練的一環:"

    if(Owner==1):
        nvl_narrator "他會把我放在地圖上，"
        nvl_narrator "假裝我是暴風雪。"
        nvl_narrator "然後開始規劃如何避開暴風雪的路線，"
        nvl_narrator "同時設想途中可能遇到的各種突發狀況。"
        nvl_narrator "作為隊長，"
        nvl_narrator "他必須確保整個團隊的安全。"
        nvl_narrator "隨著實地訓練的日子越來越近，"
        nvl_narrator "這樣的練習也變得越來越頻繁。 "
    elif(Owner==2):
        nvl_narrator "他需要協助隊長規劃訓練計畫，"
        nvl_narrator "也負責規劃每天的菜單。"
        nvl_narrator "他常常拿我當作他的試驗對象，"
        nvl_narrator "每天變著花樣的幫我準備食物。"
        nvl_narrator "除了這些，他還會研究在高山環境中"
        nvl_narrator "，該如何更精準的用藥。"
        nvl_narrator "除了這些，他還會研究在高山環境中，"
        nvl_narrator "該如何更精準地用藥。"
        nvl_narrator "隨著實地訓練的日子越來越近，"
        nvl_narrator "他也越來越頻繁地翻閱高山相關的論文。"
    elif(Owner==3):
        nvl_narrator "他會在房間裡做一些體能訓練。"
        nvl_narrator "有時會綁上負重袋，"
        nvl_narrator "再把我放到他的背上一起訓練。"
        nvl_narrator "他是登山隊中最強狀的人，"
        nvl_narrator "所以他的登山包也是最重的，"
        nvl_narrator "負責背負團隊需要的各種裝備。"
        nvl_narrator "隨著實地訓練的日子越來越近，"
        nvl_narrator "這樣的練習也變得越來越頻繁。 "
    elif(Owner==4):
        nvl_narrator "他會在房間整理他的相機。"
        nvl_narrator "有時候，他會把燈關掉，"
        nvl_narrator "只留一點點光，"
        nvl_narrator "然後對著不同方向拍照。"
        nvl_narrator "有時候，他會打開窗戶，"
        nvl_narrator "讓冷風灌進來，"
        nvl_narrator "再拿起相機拍攝。"
        nvl_narrator "隨著實地訓練的日子越來越近，"
        nvl_narrator "他這樣的測試也變得越來越頻繁。"
    
    nvl_narrator "日子到了要實地訓練的那一天，"
    nvl_narrator "我才驚覺這一天就是影片所說的那一天。"

    if(pass_game):
        nvl_narrator "我急忙的用按鈕按「不要」，"
        nvl_narrator "他蹲下來問我什麼不要。"
        nvl_narrator "我圍著他轉，"
        nvl_narrator "還是沒能表達出來，"
        nvl_narrator "讓他們不要去實地訓練。"
        nvl_narrator "最後到了出發時間，"
        nvl_narrator "他們一行人就出發了。"
    else:
        nvl_narrator "我急忙的用手去扒他"
        nvl_narrator "我急忙的用手去扒他，"
        nvl_narrator "他蹲下來問我怎麼了。"
        nvl_narrator "我圍著他轉，"
        nvl_narrator "還是沒能表達出來，"
        nvl_narrator "讓他們不要去實地訓練。"
        nvl_narrator "最後到了出發時間，"
        nvl_narrator "他們一行人就出發了。"
    nvl_narrator "我知道即使我阻止了他們"
    nvl_narrator "他們還是會照常出發"
    nvl_narrator "因為他們是國家資助的登山隊"
    nvl_narrator "必須完成國家指派的任務"
    nvl_narrator "……"

    nvl clear
    window hide

    jump CH2_1

label CH2_1: #登山
    nvl clear
    $ persistent.unlocked_ch2_1 = True
    scene game_ch2
    nvl_narrator "……"
    nvl_narrator "距離登山隊出發已經幾個小時了，"
    nvl_narrator "他們這次實地訓練只是適應性訓練，"
    nvl_narrator "預計當天就會回來。"
    nvl_narrator "但我知道，這將是場災難。"
    nvl_narrator "……"
    nvl_narrator "也許我能做什麼，"
    nvl_narrator "但木屋的大門被鎖上了，我無法離開這裡。"
label CH2_2: #木屋
    $ persistent.unlocked_ch2_2 = True
    scene game_ch2
    nvl_narrator "(房間探索)"

    $ user_input = renpy.input("請輸入密碼：")
    $ is_correct = my_lib.check_password(user_input.encode('utf-8'))
    if is_correct == 1:
        "(大門已開啟)"
        jump CH2_3
    else:
        jump CH2_BE1
label CH2_3: #狂奔
    $ persistent.unlocked_ch2_3 = True
    scene game_ch2
    nvl_narrator "我打開了房門，"
    nvl_narrator "離開木屋，"
    nvl_narrator "開始朝著他們要攀登的厄爾布魯士峰跑去。"
    nvl_narrator "踏入白茫茫的雪地，"
    nvl_narrator "刺骨的寒風夾雜著冰渣打在我的身上，"
    nvl_narrator "但我卻感覺不到冷。"
    nvl_narrator "我循著記憶中熟悉的味道拼命向前跑。"
    nvl_narrator "大約跑了 40 分鐘，周圍的環境突然發生了劇變。"
    nvl_narrator "原本還能看見山腳下的木屋微弱的燈光，"
    nvl_narrator "此刻卻被一陣突如其來的濃霧徹底覆蓋。"
    nvl_narrator "能見度瞬間趨近於零，狂風在耳邊呼嘯。"
    if(pet=="dog"):
        nvl_narrator "「汪——！」我大聲呼喚著。"
    elif(pet=="cat"):
        nvl_narrator "「喵——！」我大聲呼喚著。"
    nvl_narrator "就在不遠處的雪坡上，我看到了幾個模糊的身影。"
    nvl_narrator "是他們！他們正在焦急地就地挖掘雪洞。"
    nvl_narrator "主人聽到了我的叫聲，"
    nvl_narrator "停下了手中的冰斧，"
    nvl_narrator "滿臉震驚地看著我。"
    nvl_narrator "「你怎麼會在這裡？！」他一把將我抱起，"
    nvl_narrator "迅速塞進他厚實的羽絨服裡。"
    nvl_narrator "雖然我不覺得冷，"
    nvl_narrator "但感受到他胸膛傳來的急促心跳，"
    nvl_narrator "我知道情況非常糟糕。"

    nvl_narrator "挖掘的過程中，天空開始下起濕雪。"
    nvl_narrator "當我們躲進剛挖好的雪洞時，"
    nvl_narrator "夜幕已經降臨，"
    nvl_narrator "山上的風速達到了驚人的每秒 30 米，"
    nvl_narrator "濕度接近 100\%。"
    nvl_narrator "隊員們的羽絨服幾乎全濕透了，"
    nvl_narrator "而在這種環境下，衣服根本無法乾透。"
label CH2_4: #雪洞
    $ persistent.unlocked_ch2_4 = True
    scene game_ch2
    # TODO 雪洞探索
    nvl_narrator "(雪洞探索)"
label CH2_5: #救援
    $ persistent.unlocked_ch2_5 = True
    scene game_ch2
    nvl_narrator "就在這時，洞外突然傳來微弱的動靜。"
    nvl_narrator "我豎起耳朵，隊員們也警覺地拿起手電筒。"
    nvl_narrator "雪洞外竟然有兩個人——是兩名全身濕透的日本登山客！"
    nvl_narrator "隊長列文看著他們，正準備挪動身體讓他們進來。"
    nvl_narrator "我決定_____:"
    menu:
        "保持安靜":
            $ help_2 = 1
            nvl_narrator "隊長列文沒有猶豫，將他們讓進了雪洞。"
            nvl_narrator "原本 6 個人的狹小空間，現在擠進了 8 個人（還有一隻我）。"
            nvl_narrator "空氣逐漸變得稀薄，"
            nvl_narrator "我也在不知不覺中睡去。 "
    
        "凶狠地堵在洞口":
            $ help_2 = 0
            nvl_narrator "我突然從主人的懷裡掙脫，"
            nvl_narrator "衝到雪洞最外側的入口，"
            nvl_narrator "對著那兩名日本客發出凶狠的低吼與咆哮。"
            if(pet=="dog"):
                nvl_narrator "「汪汪汪！」我露出尖牙，"
            elif(pet=="cat"):
                nvl_narrator "「嘶——！」我露出尖牙，"
            nvl_narrator "只要他們一靠近，我就作勢要咬上去。 "
            nvl_narrator "主人錯愕地想把我拉回來："
            nvl_narrator "「你在做什麼？快回來！」 "
            nvl_narrator "但我死死卡在狹窄的洞口。 "
            nvl_narrator "那兩名日本客本就處於嚴重的失溫與虛弱狀態，"
            nvl_narrator "加上雙方語言不通，根本無法向列文求救。 "
            nvl_narrator "看著一隻近乎發狂的動物堵住去路，"
            nvl_narrator "他們眼裡閃過一絲絕望，"
            nvl_narrator "最終只能互相攙扶著，"
            nvl_narrator "轉身隱沒在狂風與濃霧之中。"
    nvl clear
    window hide
    jump CH3_1
label CH2_BE1: #奧金
    $ persistent.unlocked_ch2_BE1 = True
    scene game_ch2
    nvl_narrator "沒辦法，"
    nvl_narrator "我無法逃出木屋，"
    nvl_narrator "只能繼續在房子裡待著。"
    nvl_narrator "我謹慎地分配食物跟水，"
    nvl_narrator "過了幾天，"
    nvl_narrator "就在食物跟水都要吃完的時候，"
    nvl_narrator "有人進來了屋子。"
    nvl_narrator "……"
    nvl_narrator "是奧金，只有他幸免於難。"
    return
    # TODO 可補後續
label CH2_BE2:
    $ persistent.unlocked_ch2_BE2 = True
    scene game_ch2

    return
label CH3_1:
    $ persistent.unlocked_ch3_1 = True
    scene game_ch3
    return
label CH3_2:
    $ persistent.unlocked_ch3_2 = True
    scene game_ch3
    return
label CH3_3:
    $ persistent.unlocked_ch3_3 = True
    scene game_ch3
    return
label CH3_4:
    $ persistent.unlocked_ch3_4 = True
    scene game_ch3
    return
label CH3_5:
    $ persistent.unlocked_ch3_5 = True
    scene game_ch3
    return

label CH3_BE1:
    $ persistent.unlocked_ch3_BE1 = True
    scene game_ch3

    return
label CH3_BE2:
    $ persistent.unlocked_ch3_BE2 = True
    scene game_ch3

    return
label CH3_BE3:
    $ persistent.unlocked_ch3_BE3 = True
    scene game_ch3

    return
label CH3_BE4:
    $ persistent.unlocked_ch3_BE4 = True
    scene game_ch3

    return
label CH3_BE5:
    $ persistent.unlocked_ch3_BE5 = True
    scene game_ch3

    return
label CH3_GE1:
    $ persistent.unlocked_ch3_GE1 = True
    scene game_ch3

    return
label CH3_GE2:
    $ persistent.unlocked_ch3_GE2 = True
    scene game_ch3

    return






label test_c:
    # TODO 以下劇本未完成
    $ user_input = renpy.input("請輸入通關密碼：")
    
    # 將使用者輸入的字串轉成 bytes 傳給 C 語言
    $ is_correct = my_lib.check_password(user_input.encode('utf-8'))

    # 判斷 C 語言回傳的結果 (1 或 0)
    if is_correct == 1:
        "密碼正確！保險箱已開啟。"
        jump puzzle_solved
    else:
        "密碼錯誤！警報器開始作響！"

label puzzle_solved:
    "你在裡面發現了關鍵的證據！"
    return

label Ch1_end:
    "【第一章：- 完】"
    return