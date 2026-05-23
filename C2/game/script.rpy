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
        if event == "begin": #TODO 進度計算方式待修改
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
    # TODO 重新編譯
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

    #清空存檔
    def reset_all_progress():
        # 清除所有的 persistent 資料
        persistent._clear()
        
        # 強制存檔，確保清除狀態被記錄
        renpy.save_persistent()
        
        # 重新啟動遊戲，回到主選單
        renpy.full_restart()


    
        

# 進度條變數 
default nvl_progress = 0.0      # 當前進度
default nvl_total_lines = 10    # 預設總行數 (防止錯誤用)
# 劇情變數
default persistent.pet = "dog"
default persistent.Owner = 1 #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
default persistent.pass_game =0
default persistent.help_2 = 0
# 章節進度
default persistent.unlocked_ch1_0 = True
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
label CH1_1:    #荒野求生
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
            $ persistent.pet = "cat"
            nvl_narrator "我竟然變成了一隻貓!"
        "小狗":
            $ persistent.pet = "dog"
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
label CH1_BE1:  #誤判
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
label CH1_2:    #登山隊
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
            $ persistent.Owner =1; #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
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
            $ persistent.Owner =2; #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
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
            $ persistent.Owner =5; #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
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
            $ persistent.Owner =4; #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
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
            $ persistent.Owner =3; #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
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
            $ persistent.Owner =3; #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
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
label CH1_3:    #訓練
    $ persistent.unlocked_ch1_3 = True
    scene game_ch1
    nvl_narrator "……"
    nvl_narrator "在我找到回去的方法之前，"
    nvl_narrator "我決定先在這棟木屋住下來。"
    nvl_narrator "日子一天一天的過，我漸漸跟他培養起感情，"
    nvl_narrator "也逐漸習慣了這個身體。"
   
    nvl_narrator "我發現他們似乎就是影片中的登山隊，"
    nvl_narrator "這支菁英小隊由隊長列文帶領，成員包括隊醫法布、隊員布爾金、沃寧、拉扎與奧金。"

    if(persistent.Owner==1): #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
        nvl_narrator "而我的主人正是登山隊的隊長。"
    elif(persistent.Owner==2):
        nvl_narrator "而我的主人正是登山隊的隊醫。"
    elif(persistent.Owner==4):
        nvl_narrator "而我的主人正是登山隊的隊員，同時負責攝影的工作。"
    else:
        nvl_narrator "而我的主人正是登山隊的隊員。"
    nvl_narrator "平常，我會跟他們一起去做登山的基本訓練，"
    nvl_narrator "休息時，他們也會陪我一起玩。"

    nvl_narrator "響片遊戲(45秒)"
    nvl_narrator "遊戲說明:當聽到響片聲，便按下空白鍵，越到後面越快"
    #TODO 遊戲未完成
    menu:
        "通過":
            $ persistent.pass_game = 1
            nvl_narrator "我們玩了響片遊戲一個月之後，"
            nvl_narrator "他在房間裝了幾個按鈕，"
            nvl_narrator "讓我可以表達需求，"
            nvl_narrator "我最常按的是食物。"
            nvl_narrator "他偶爾還會用雙手跟我溝通，"
            nvl_narrator "像是要不要出去玩。"
        "未通過":
            $ persistent.pass_game = 0
            nvl_narrator "雖然我玩的不怎麼樣，"
            nvl_narrator "但他還是很有耐心。"
            nvl_narrator "我們溝通還是主要透過他的解讀，"
            nvl_narrator "偶爾會用雙手跟我溝通，"
            nvl_narrator "像是要不要出去玩。"
    nvl_narrator "他時常還會把我當作訓練的一環:"

    if(persistent.Owner==1): #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
        nvl_narrator "他會把我放在地圖上，"
        nvl_narrator "假裝我是暴風雪。"
        nvl_narrator "然後開始規劃如何避開暴風雪的路線，"
        nvl_narrator "同時設想途中可能遇到的各種突發狀況。"
        nvl_narrator "作為隊長，"
        nvl_narrator "他必須確保整個團隊的安全。"
        nvl_narrator "隨著實地訓練的日子越來越近，"
        nvl_narrator "這樣的練習也變得越來越頻繁。 "
    elif(persistent.Owner==2):
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
    elif(persistent.Owner==4):
        nvl_narrator "他會在房間整理他的相機。"
        nvl_narrator "有時候，他會把燈關掉，"
        nvl_narrator "只留一點點光，"
        nvl_narrator "然後對著不同方向拍照。"
        nvl_narrator "有時候，他會打開窗戶，"
        nvl_narrator "讓冷風灌進來，"
        nvl_narrator "再拿起相機拍攝。"
        nvl_narrator "隨著實地訓練的日子越來越近，"
        nvl_narrator "他這樣的測試也變得越來越頻繁。"
    else:
        nvl_narrator "他會在房間裡做一些體能訓練。"
        nvl_narrator "有時會綁上負重袋，"
        nvl_narrator "再把我放到他的背上一起訓練。"
        nvl_narrator "他是登山隊中最強狀的人，"
        nvl_narrator "所以他的登山包也是最重的，"
        nvl_narrator "負責背負團隊需要的各種裝備。"
        nvl_narrator "隨著實地訓練的日子越來越近，"
        nvl_narrator "這樣的練習也變得越來越頻繁。 "
    
    nvl_narrator "日子到了要實地訓練的那一天，"
    nvl_narrator "我才驚覺這一天就是影片所說的那一天。"

    if(persistent.pass_game):
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
label CH2_1:    #登山
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
label CH2_2:    #木屋
    #TODO 探索
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
label CH2_3:    #狂奔
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
    if(persistent.pet=="dog"):
        nvl_narrator "「汪——！」我大聲呼喚著。"
    elif(persistent.pet=="cat"):
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
label CH2_4:    #雪洞
    $ persistent.unlocked_ch2_4 = True
    scene game_ch2
    nvl_narrator "我決定悄悄在狹小的洞穴裡巡視，看看大家都在做些什麼。"
    nvl clear
    scene cave_bg
    jump cave_loop
label cave_loop:
    if cave_investigation_count >= 6:
        jump CH2_4_end
    call screen cave_exploration_screen
    jump cave_loop
label click_backpack:
    if not checked_backpack:
        $ checked_backpack = True
        $ cave_investigation_count += 1
    "我瞄了一眼列文身邊的背包，發現它竟然異常沉重。"
    "我悄悄蹭了一下，背包發出了金屬撞擊聲。"
    "從小小的開口中，我看到裡面放了大量的冰鎬，可能有數十隻。"
    "一次適應性訓練為什麼要帶這麼多冰鎬？"
    jump cave_loop # 講完後，回到循環檢查，重新打開畫面
label click_levin:
    if not checked_levin:
        $ checked_levin = True
        $ cave_investigation_count += 1
    
    "「滋…滋…滋…」對講機裡傳來刺耳的雜音。"
    "「是不是電池問題？請更換電池。」山下的指導員詢問。"
    "列文換了電池，但雜音依舊。"
    "他只能對著麥克風大喊：「大雪導致了濕度問題，目前狀況良好，計畫明天下山！」"
    "隨後通訊徹底中斷，而列文則眉頭深鎖，似乎在思考什麼。"
    nvl clear
    jump cave_loop
label click_fabre:
    if not checked_fabre:
        $ checked_fabre = True
        $ cave_investigation_count += 1
    
    "法布拿著一罐沒有標籤的藥罐，對旁邊的隊員輕聲說："
    "「把這個吃下去，這能加快我們身體適應高山低氧的環境。」"
    nvl clear
    jump cave_loop
label click_ogin_burgin:
    if not checked_ogin_burgin:
        $ checked_ogin_burgin = True
        $ cave_investigation_count += 1
    
    "奧金正用敏銳的目光靜靜觀察著洞穴裡的每一個成員。"
    "他手裡緊緊抱著相機，雖然無法拍照，但他似乎在腦海中記錄著這一切。"
    "布爾金則在一旁閉目養神。"
    nvl clear
    jump cave_loop
label click_voronin_raza:
    if not checked_voronin_raza:
        $ checked_voronin_raza = True
        $ cave_investigation_count += 1
    
    "沃寧：「因為這只是適應性訓練，我們沒有過夜裝備，還好我們都很擅長挖雪洞。」"
    "拉扎低聲抱怨：「但羽絨服最怕潮濕了，在雪洞裡這衣服根本乾不了。」他用力擰著自己羽絨服上的雪水。"
    "沃寧：「希望明天會放晴。」"
    nvl clear
    jump cave_loop
label click_heat:
    if not checked_heat:
        $ checked_heat = True
        $ cave_investigation_count += 1
    
    "我湊近燃燒的卡式爐，"
    "溫暖的火焰讓我感到非常溫暖，"
    "但同時燃燒的火焰也散發著刺鼻的氣味。"
    "所以我____"
    menu:
        "遠離卡式爐":
            "我移動到離卡式爐較遠的角落。"
        "推倒卡式爐" if persistent.unlocked_ch3_5 or persistent.unlocked_ch3_BE5:
            nvl clear
            jump CH2_BE2
    jump cave_loop
label CH2_4_end:
    nvl_narrator "就在這時，洞外突然傳來微弱的動靜。"
    nvl clear
    jump CH2_5
label CH2_5:    #救援
    $ persistent.unlocked_ch2_5 = True
    scene game_ch2
    nvl_narrator "就在這時，洞外突然傳來微弱的動靜。"
    nvl_narrator "我豎起耳朵，隊員們也警覺地拿起手電筒。"
    nvl_narrator "雪洞外竟然有兩個人——是兩名全身濕透的日本登山客！"
    nvl_narrator "隊長列文看著他們，正準備挪動身體讓他們進來。"
    nvl_narrator "我決定_____:"
    menu:
        "保持安靜":
            $ persistent.help_2 = 1
            nvl_narrator "隊長列文沒有猶豫，將他們讓進了雪洞。"
            nvl_narrator "原本 6 個人的狹小空間，現在擠進了 8 個人（還有一隻我）。"
            nvl_narrator "空氣逐漸變得稀薄，"
            nvl_narrator "我也在不知不覺中睡去。 "
    
        "凶狠地堵在洞口":
            $ persistent.help_2 = 0
            nvl_narrator "我突然從主人的懷裡掙脫，"
            nvl_narrator "衝到雪洞最外側的入口，"
            nvl_narrator "對著那兩名日本客發出凶狠的低吼與咆哮。"
            if(persistent.pet=="dog"):
                nvl_narrator "「汪汪汪！」我露出尖牙，"
            elif(persistent.pet=="cat"):
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
label CH2_BE1:  #奧金
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
    nvl_narrator "是奧金，6人小隊中只有他幸免於難。"
    return
label CH2_BE2:  #熄滅
    $ persistent.unlocked_ch2_BE2 = True
    scene game_ch2
    nvl_narrator "我假裝失去平衡，撞上地上的卡式爐。 "
    nvl_narrator "「哐啷！」 一聲清脆的金屬碰撞聲在狹小的洞穴裡迴盪。"
    nvl_narrator " 卡式爐翻倒在地，裡面燃燒著的固體酒精塊滾落出來，直接掉進了濕漉漉的雪堆裡。"
    nvl_narrator "「嘶——」 一陣白煙升起，火苗瞬間熄滅。 "
    nvl_narrator "整個雪洞陷入了死一般的漆黑與死寂。"
    nvl_narrator "「不！」隊長列文驚呼一聲，立刻撲過去想撿起燃料，但已經太遲了。 "
    nvl_narrator "那些被雪水浸濕的固體酒精已經無法再次點燃。"
    nvl_narrator "「完了……這下我們真的要在這裡凍死了。」沃寧在黑暗中發出絕望的低語。"
    nvl_narrator "失去唯一的熱源後，雪洞裡的溫度急遽下降。 "
    nvl_narrator "但原本空氣中那股讓我不舒服的燃燒氣味，也隨著火焰的熄滅而漸漸消散了。"

    nvl_narrator "一夜的嚴寒宛如酷刑。 "
    nvl_narrator "沒有了卡式爐的熱度，所有人身上的濕羽絨服全都結成了一層硬邦邦的冰殼。"
    nvl_narrator "當清晨的微光透進雪洞時，大家都凍得面色慘白，渾身不受控制地劇烈發抖。"
    nvl_narrator "列文接通了無線電請求支援，隨後下令：「所有人……離開雪洞，立刻下山！」 "
    nvl_narrator "大家牽引著繩索，僵硬地踏出洞口。 "
    nvl_narrator "外頭依舊是伸手不見五指的濃霧。"
    nvl_narrator "「大家跟緊！千萬別掉隊！」列文隊長在前方大喊。"
    nvl_narrator "然而，長達十幾個小時在零下低溫且缺乏熱源的環境中，隊員們的人體調節系統已經瀕臨崩潰。 "
    nvl_narrator "走不到一半的路程，拉扎和攝影師奧金的步伐越來越慢，意識開始模糊。"
    nvl_narrator "「隊長……我不行了……好想睡一下……」奧金喃喃自語，身體搖搖欲墜。 "
    nvl_narrator "我知道，一旦他們在這裡閉上眼睛，就永遠醒不過來了。"
    nvl_narrator "我衝上前，死死咬住奧金的褲管，喉嚨裡發出焦急的低吼，拼命將他往前拽。 "
    nvl_narrator "這股微小的拉力，以及我溫熱的氣息，勉強喚醒了奧金的一絲理智。 "
    nvl_narrator "最後，奧金憑藉著頑強的意志力，走出了暴風雪。 "
    nvl_narrator "當木屋出現在眼前時，所有人都虛脫地倒在了門口的雪地上。"
    nvl_narrator "救援人員迅速將他們抬進屋內。 "
    nvl_narrator "小隊全員奇蹟般地生還了， 但因為失去了卡式爐的保暖，"
    nvl_narrator "嚴重的凍傷讓隊醫法布失去了三根手指，攝影師奧金的腳趾也面臨截肢。 "
    nvl_narrator "他們永遠告別了登山生涯。"
    return
label CH3_1:    #下山
    $ persistent.unlocked_ch3_1 = True
    scene game_ch3
    nvl_narrator "一夜的嚴寒與潮濕折磨著所有人，"
    nvl_narrator "到了隔天清晨，"
    nvl_narrator "列文接通了無線電請求支援後，"
    nvl_narrator "下令全體離開雪洞，開始下山。"
    nvl_narrator "我跟在主人的腳邊，雪地依然被濃霧籠罩。"

    nvl_narrator "沒走幾步，"
    nvl_narrator "隊醫法布突然重重地摔倒在雪地裡。"
    nvl_narrator "大家趕緊將他扶起，"
    nvl_narrator "但他走了幾步又再次摔倒。"
    nvl_narrator "法布說：「霧太濃了，我什麼都看不見！」"
    nvl_narrator "負責攙扶他的奧金看著法布，意識到："
    nvl_narrator "「法布的眼睛看不見了！」"
    nvl_narrator "我抬頭看著隊醫法布，他痛苦地捂著眼睛，"
    nvl_narrator "嚴重的「雪盲」讓他徹底失去了視覺。"

    nvl_narrator "隊長列文陷入了猶豫，"
    nvl_narrator "如果堅持下山，法布將可能喪命。"
    nvl_narrator "而在這片濃霧中，繼法布之後又有誰會倒下?"
    nvl_narrator "……"
    nvl_narrator "最終他下令："
    nvl_narrator "「全員返回雪洞！」"

    if(persistent.Owner==1): #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
        nvl_narrator "我知道身為隊長，他希望把所有人安全帶下山。"
        nvl_narrator "他深怕法布因此喪命，所以下令撤退。 "
        nvl_narrator "但我知道這將是個致命的決定，所以我______________"
        menu:
            "咬住他的對講機":
                nvl_narrator "我咬住他的對講機，試圖阻止他下達退回的指令。"
                nvl_narrator "他苦笑著看著我，"
                nvl_narrator "但為了維持隊長的威嚴與決斷，"
                nvl_narrator "他輕輕將我踢開，"
                nvl_narrator "並強行推動隊伍往回走。 "
            "擋在隊伍前面":
                nvl_narrator "我擋在隊伍前面，對著下山的方向狂吠"
                nvl_narrator "我不斷狂吠，"
                nvl_narrator "試圖告訴他山下木屋就在不遠處。"
                nvl_narrator "列文為了安撫我，"
                nvl_narrator "將我抱起，走回雪洞中。"
        jump CH3_2
    elif(persistent.Owner==2):
        nvl_narrator "看著法布痛苦地跪在雪地裡， "
        nvl_narrator "什麼都看不見。 "
        nvl_narrator "我______"
        menu:
            "緊緊貼著他的腿，充當他的導盲犬 ":
                nvl_narrator "我用身體蹭著他冰冷的腿，"
                nvl_narrator "引導他跟上隊伍的腳步，"
                nvl_narrator "慢慢往雪洞的方向退回。 "
                jump CH3_2
            "咬住他的褲管，拚命想把他往山下拖":
                jump CH3_BE2
    elif(persistent.Owner==4):
        nvl_narrator "此時奧金為了攙扶體格高大的法布，"
        nvl_narrator "已經筋疲力盡。"
        nvl_narrator "所以我______"
        menu:
            "鑽進法布的手臂下，幫主人一起頂著重量":
                nvl_narrator "我用小小的身軀幫忙分擔了一點重量，"
                nvl_narrator "奧金感激地看了我一眼，"
                nvl_narrator "我們艱難地往雪洞走去。 "
                jump CH3_2
            "離開主人，獨自衝下山去找救兵":
                jump CH3_BE3 #尋蹤"
    else:
        nvl_narrator "主人看著隊長列文下令退回那個狹小、潮濕的雪洞，"
        nvl_narrator "眼中閃過了一絲不甘與憤怒。"
        nvl_narrator "雖然下山是活下去的機會，"
        nvl_narrator "但他們也不想丟下隊友。"
        nvl_narrator "所以我_________"
        menu:
            "順從地走到他腳邊，示意一起回去":
                nvl_narrator "他摸了摸我的頭，"
                nvl_narrator "跟隨隊長往回走。"
                jump CH3_2
            "擋在主人面前，對著隊長列文低吼抗議":
                jump CH3_BE4 #叛變
            "咬住他的褲管，拚命想把他往山下拖" if persistent.Owner == 3:
                jump CH3_BE1 #脫隊
label CH3_2:    #撤退
    $ persistent.unlocked_ch3_2 = True
    scene game_ch3
    nvl_narrator "我們跌跌撞撞地退回雪洞。"
    nvl_narrator "這時，意外發生了。"
    if (persistent.help_2):#救日本人
        nvl_narrator "因為 8 個人的擠壓與衝撞，"
    else:#沒救日本人
        nvl_narrator "因為 6 個人的擠壓與衝撞，"
    nvl_narrator "雪洞的前廳突然坍塌了！"
    nvl_narrator "擋風的裝備全被掩埋，"
    nvl_narrator "所有人只能被迫擠在僅有約四平方公尺的後廳裡，"
    nvl_narrator "精疲力盡地圍著卡式爐等待救援。"
    if (persistent.help_2):#救日本人
        jump CH3_3
    else: #沒救日本人
        nvl_narrator "因為 6 個人的擠壓與衝撞，"
        jump CH3_BE5
label CH3_3:    #爭執
    $ persistent.unlocked_ch3_3 = True
    scene game_ch3

    nvl_narrator "夜幕再次降臨。"
    nvl_narrator "洞內的氧氣越來越稀薄，我感覺呼吸變得非常困難。"
    nvl_narrator "這時，隊長列文帶著沃寧和拉扎奮力挖開了被雪堵住的洞口。"
    nvl_narrator "一瞬間，冰冷的空氣灌了進來。"
    nvl_narrator "我探出頭去——天空放晴了！"
    nvl_narrator "山腳下木屋的燈光清晰可見，那是生存的希望。"
    nvl_narrator "但回頭看洞內，"
    nvl_narrator "隊醫法布已經奄奄一息，"
    nvl_narrator "隊員布爾金也處於一種奇怪的神經興奮狀態，"
    nvl_narrator "兩名日本人呼吸急促，隊員奧金也站不起來。"
    nvl_narrator "沃寧和拉扎激動地準備拿裝備下山，但列文再次猶豫了。"
    nvl_narrator "身為隊長，他不願意拋棄任何一名隊友，"
    nvl_narrator "「不准走！所有人退回雪洞！」列文大吼著下令。"
    nvl_narrator "似乎是連日的疲勞讓列文失去判斷力，"
    nvl_narrator "接通無線電之後，"
    nvl_narrator "他匯報：「情況尚在控制中，計畫明天下山」"
    nvl_narrator "身為國家重資打造的菁英小隊，"
    nvl_narrator "他不願灰頭土臉地向人求救。"
    nvl_narrator "沃寧和拉扎愣住了，隨後眼神轉為憤怒。"
    nvl_narrator "他們深知這是千載難逢的下山機會，"
    nvl_narrator "退回去只有死路一條。"
    nvl_narrator "沃寧衝上前，想要搶奪列文手中的無線電，"
    nvl_narrator "直接向山下呼救。"
    nvl_narrator "衝突瞬間爆發！"
    nvl_narrator "看著失控的隊員們，我該怎麼做？"
    menu:
        "咬住隊長列文的褲管":
            nvl_narrator "我想把列文往山下的方向拖，"
            nvl_narrator "告訴他必須帶大家下山！"
            nvl_narrator "但他此刻已經陷入了極度的固執與瘋狂，"
            nvl_narrator "他一把將我甩開，"
            nvl_narrator "死死護著無線電，"
            nvl_narrator "不讓沃寧呼救。"
        "擋在沃寧和拉扎面前大叫":
            nvl_narrator "我試圖阻止他們攻擊隊長，"
            nvl_narrator "但在生死存亡的恐懼面前，"
            nvl_narrator "我的叫聲顯得如此微弱。"
            nvl_narrator "他們完全無視了我，"
            nvl_narrator "紅著眼眶撲向列文。"
        "衝去保護無線電":
            nvl_narrator "我想護住那個能救命的黑盒子，"
            nvl_narrator "但他們在狹小的洞口扭打在一起。"
            nvl_narrator "混亂之中，"
            nvl_narrator "我看準時機咬住了無線電，"
            nvl_narrator "帶著它逃離爭執的隊員們。"
            nvl_narrator "我嘗試接通無線電，"
            nvl_narrator "但對講機的頻道已經跑掉，"
            nvl_narrator "我需要調整到正確的頻道:"
            $ user_input = renpy.input("請輸入正確的頻道：")
            $ is_correct = my_lib.check_password(user_input.encode('utf-8'))
            if is_correct == 1:
                jump CH3_GE2
            nvl_narrator "列文發現無線電被搶走而追了上來，"
            nvl_narrator "隊員們也緊追其後。"
            nvl_narrator "一陣混亂中，"
            nvl_narrator "我來不及接通無線電，"
            nvl_narrator "一隻沉重的登山靴踩了下來。"
        "留在雪洞裡" if persistent.unlocked_ch3_BE2:    
            jump CH3_GE1 #報恩
    jump CH3_4
label CH3_4:    #歷史重演
    $ persistent.unlocked_ch3_4 = True
    scene game_ch3
    
    nvl_narrator "無論我怎麼做，都無法阻止這場悲劇。"
    nvl_narrator "在激烈的肢體衝突中，"
    nvl_narrator "我聽到了骨頭碰撞的聲音，"
    nvl_narrator "看到他們因為極度絕望而互相撕咬。"
    nvl_narrator "「啪！」"
    nvl_narrator "那台用來通信的無線電被重重地砸碎在雪地上，"
    nvl_narrator "零件散落一地。"
    nvl_narrator "生存的最後一絲希望，斷絕了。"

    nvl_narrator "打鬥耗盡了他們最後一絲力氣，"
    nvl_narrator "三人倒在雪地裡，"
    nvl_narrator "開始陷入失溫症狀，"
    nvl_narrator "失溫症讓下視丘發出了錯誤的炎熱信號，"
    nvl_narrator "他們開始在寒冷的雪地中脫去外衣。"

    nvl_narrator "列文褲子褪到膝蓋以下，"
    nvl_narrator "倒在雪地裡仰望著星空，"
    nvl_narrator "身體溫暖的訊號讓他露出一絲微笑。"
    nvl_narrator "他在生命的最後一刻，"
    nvl_narrator "似乎想通了什麼， "
    nvl_narrator "一手指著天空，"
    nvl_narrator "慢慢被凍僵。"

    nvl_narrator "拉扎則陷入呼吸困難，"
    nvl_narrator "佝僂著身子趴在地上喘息，"
    nvl_narrator "最終，他的呼吸越來越微弱，"
    nvl_narrator "面部開始結冰。"

    nvl_narrator "沃寧則陷入精神異常，"
    nvl_narrator "半跪在雪地裡，"
    nvl_narrator "拿著日本客留下的雪板瘋狂地挖掘著，"
    nvl_narrator "似乎在尋找著什麼，"
    nvl_narrator "隨後他也失去了生機。"

    nvl_narrator "而其中一名日本客趁亂逃出了洞外，"
    nvl_narrator "防水的外衣讓他免於失溫症之苦，"
    nvl_narrator "他向山下走去，消失在黑夜中。"

    nvl_narrator "隔日早晨，"
    nvl_narrator "灌入雪洞的寒風將我叫醒，"
    nvl_narrator "不久，奧金甦醒了過來。"
    nvl_narrator "奧金驚恐地看著周圍，"
    nvl_narrator "隊友布爾金已經死亡，"
    nvl_narrator "身下是一大灘嘔吐物。"
    nvl_narrator "旁邊的隊醫法布一息尚存，"
    nvl_narrator "他顫抖著用手指沾著地上的血跡，"
    nvl_narrator "在雪洞的牆上畫下了一個詭異的渦流狀同心圓。"

    nvl_narrator "奧金虛弱地爬出洞口，"
    nvl_narrator "貪婪地呼吸著氧氣，"
    nvl_narrator "搖搖晃晃地向山下走去。"

    if(persistent.Owner==4): #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
        nvl_narrator "我跟著主人下山，"
        nvl_narrator "回到熟悉的木屋。"
        nvl_narrator "他帶著救援隊回到雪洞，"
        nvl_narrator "此時，除了奄奄一息的法布和剩下的一名日本客，"
        nvl_narrator "其他登山隊員已全數遇難。"
    elif(persistent.Owner==2): #1:隊長 2:隊醫 3:沃寧/拉札 4:奧金 5:布爾金
        nvl_narrator "我待在已經奄奄一息的法布身旁。"
        nvl_narrator "不久之後，"
        nvl_narrator "奧金帶著救援隊趕到。"
        nvl_narrator "此時，除了法布和剩下的一名日本客，"
        nvl_narrator "其他登山隊員已全數遇難。"
    else:
        nvl_narrator "我站在原處，看著主人永遠安靜地躺在雪地裡。"
        nvl_narrator "隨後，"
        nvl_narrator "奧金帶著救援隊趕到。"
        nvl_narrator "此時，除了奄奄一息的法布和剩下的一名日本客，"
        nvl_narrator "其他登山隊員已全數遇難。"
    nvl_narrator "法布用手指沾著血，"
    nvl_narrator "在牆上畫了一個渦流狀的同心圓。"
    nvl_narrator "在下山途中因低溫，"
    nvl_narrator "法布漸漸失去了意識。"
    nvl_narrator "另一名日本客雖然獲救下山，"
    nvl_narrator "卻從此行為能力退化，"
    nvl_narrator "甚至不記得也無法描述這段經歷。"
    nvl_narrator "……"
    nvl_narrator "我隨然回到了過去，"
    nvl_narrator "卻無法改變已發生的歷史。"
    nvl_narrator "隨後，我的身體變得越來越輕，"
    nvl_narrator "逐漸變得透明。"
    nvl_narrator "……"
    nvl_narrator "(END)"
    $ persistent.unlocked_ch3_5 = True
    return
label CH3_5:    #真相?
    $ persistent.unlocked_ch3_5 = True

    scene game_ch3
    nvl_narrator "…… 我猛然睜開眼睛。 "
    nvl_narrator "眼前的電腦螢幕依然亮著， "
    nvl_narrator "YouTube 中的影片已經結束。 "
    nvl_narrator "原來，那只是一場夢嗎？ "
    nvl_narrator "但我彷彿還能感受到那刺骨的寒風，"
    nvl_narrator "以及雪洞裡令人窒息的絕望。"
    nvl_narrator "我想從跳回影片的片段，解開我沒有完全解開的謎團："
    jump CH3_5_menu
label CH3_5_menu:
    menu:
        "「關於那異常沉重的背包與冰鎬……」 ":
            nvl_narrator "冰鎬是國際登山圈的通用貨幣，"
            nvl_narrator "他們可能想拿去和外國人交換裝備。"
            nvl_narrator "但這個數量也帶多了吧。"
            nvl_narrator "或者，他們可能背負著國家指派的秘密任務，"
            nvl_narrator "準備去採集岩石樣本。"
            jump CH3_5_menu

        "「關於燃燒的固體酒精……」":
            nvl_narrator "他們使用的卡式爐燃燒的是加了立德粉的固體酒精，"
            nvl_narrator "立德粉可以固化酒精和調節燃燒速率，平常雖然無毒，"
            nvl_narrator "但如果酒精中含有一定量的含氮有機物雜質，"
            nvl_narrator "在高溫又缺氧的燃燒下，"
            nvl_narrator "立德粉可能會催化這些氮有機物，"
            nvl_narrator "轉化成氫氰酸並揮發到空氣當中。"
            jump CH3_5_menu

        "「關於神秘的藥品……」":
            nvl_narrator "法布作為隊醫，攜帶著一種新藥，"
            nvl_narrator "可有效地加快人體適應高原低氧的環境。"
            nvl_narrator "列文小隊的秘密任務之一，就是使用並測試這種新藥。"
            nvl_narrator "可最終這藥物導致了團隊身體功能紊亂，並且由於法布信任這種新藥，"
            nvl_narrator "服用劑量比其他隊員都大，所以率先倒下。"
            jump CH3_5_menu

        "結束":
            pass 
    nvl_narrator "我靜靜地看著螢幕， 回想起木屋裡那些曾與我朝夕相處的隊員們。 無論真相究竟是新藥的副作用、毒氣的催化、還是人性在絕境下的崩潰， 他們最終都留在了那片白雪晴空之下。"
    nvl_narrator "《遊戲結束》"
    return
label CH3_BE1:  #脫隊
    $ persistent.unlocked_ch3_BE1 = True
    scene game_ch3
    nvl_narrator "我咬住主人的褲管，"
    nvl_narrator "拚命想把他往山下拖。"
    nvl_narrator "這給了沃寧和拉扎拒絕隊長命令的勇氣，"
    nvl_narrator "但他們沒有選擇直接與隊長發生衝突，"
    nvl_narrator "而是趁著濃霧脫隊。"
    nvl_narrator "最後，他們順利下山聯絡救援隊。"
    nvl_narrator "救援隊連夜帶著裝備上山，"
    nvl_narrator "卻在前往雪洞的路上發現其他隊員的屍體。"
    nvl_narrator "原來，隊長在他們脫隊不久後，"
    nvl_narrator "發現少了兩名隊員，"
    nvl_narrator "又下令回頭尋找。"
    nvl_narrator "最終，隊員們不敵濃霧與暴風雪，"
    nvl_narrator "紛紛倒在雪地之中。"
    if persistent.help_2:#救了日本人
        nvl_narrator "雪洞之中只剩下兩名日本登山客。"
    nvl_narrator "沃寧和拉扎陷入了深深的自責。"
    nvl_narrator "……"
    nvl_narrator "(END)"
    return
label CH3_BE2:  #冰縫
    $ persistent.unlocked_ch3_BE2 = True
    scene game_ch3
    nvl_narrator "我知道退回雪洞只有死路一條。"
    nvl_narrator "我死死咬住法布的褲管，"
    nvl_narrator "想把他拖下山。"
    nvl_narrator "但他完全失去視覺，"
    nvl_narrator "被我拖拽著偏離了隊伍路線，"
    nvl_narrator "一腳踩空跌入了冰縫中。"
    nvl_narrator "臨死前，他用殘存的力氣將我緊緊護在懷裡。"
    nvl_narrator "……"
    nvl_narrator "(END)"
    return
label CH3_BE3:  #尋蹤
    $ persistent.unlocked_ch3_BE3 = True
    scene game_ch3
    nvl_narrator "我知道主人已經撐不住了，"
    nvl_narrator "我轉身衝入暴風雪，"
    nvl_narrator "想回到木屋找人幫忙。"
    nvl_narrator "但我嬌小的身軀很快就被嚴寒吞噬。"
    nvl_narrator "最終，我倒在雪地裡，"
    nvl_narrator "再也無法起來……"
    nvl_narrator "隔天清晨，奧金獨自下山獲救，"
    nvl_narrator "而他一生都在尋找那隻為了救他而消失在雪地裡的寵物。 "
    nvl_narrator "(END)"
    return
label CH3_BE4:  #叛變
    $ persistent.unlocked_ch3_BE4 = True
    scene game_ch3
    nvl_narrator "我的低吼點燃了主人心中壓抑的怒火。"
    nvl_narrator "沃寧與拉扎再也無法忍受這種形同等死的決策，"
    nvl_narrator "直接在雪地裡與隊長爆發了激烈的肢體衝突。"
    nvl_narrator "在極寒與混亂中，裝備散落一地。"
    nvl_narrator "隊員們耗盡了體力，"
    nvl_narrator "倒在雪地中，"

    if persistent.help_2:
        nvl_narrator "兩名日本登山客則趁亂逃離，"
        nvl_narrator "往山下走去，"
        nvl_narrator "卻不慎掉入冰縫中。"

    nvl_narrator "沒有人活著回到木屋。 "
    nvl_narrator "(END)"
    return
label CH3_BE5:  #毒氣室
    $ persistent.unlocked_ch3_BE5 = True
    scene game_ch3
    nvl_narrator "所幸，洞內的空氣還算足夠，"
    nvl_narrator "隊員們靜靜地閉目養神，"
    nvl_narrator "我則逐漸進入昏睡中。"

    nvl_narrator "到了隔天清晨， "
    nvl_narrator "除了已經無力行走的法布，"
    nvl_narrator "布爾金也開始發生嚴重的神經抽搐與劇烈嘔吐，"
    nvl_narrator "甚至吐出了鮮血。 "
    nvl_narrator "空氣中瀰漫著詭異的氣味，"
    nvl_narrator "但所有人都以為只是高山症發作。"
    nvl_narrator "接著，奧金也癱倒在地，"
    nvl_narrator "陷入呼吸困難與麻痺。"
    nvl_narrator "此時，奄奄一息的法布沾了地上的血跡，"
    nvl_narrator "在地上畫出渦流狀的同心圓，"
    nvl_narrator "喃喃自語地說著：「固體酒精…立德粉…氫氰酸…」"

    nvl_narrator "聽到法布的警告，"
    nvl_narrator "隊長列文似乎意識到了什麼，"
    nvl_narrator "想帶著沃寧與拉扎挖開雪洞，"
    nvl_narrator "然而因整晚無法乾透的羽絨服，"
    nvl_narrator "此時沃寧與拉扎已陷入了嚴重的失溫症狀。"
    nvl_narrator "失溫症讓下視丘發出了錯誤的炎熱信號，"
    nvl_narrator "使他們開始瘋狂地撕扯自己濕透的羽絨服。"
    nvl_narrator "列文嘗試自己挖開雪洞，"
    nvl_narrator "卻也在成功之前因吸入過多燃燒固體酒精產生的毒氣而開始陷入呼吸困難。"
    nvl_narrator "最終，他們相繼倒在雪洞之中。"
    nvl_narrator "而我，也在這充滿毒氣的密閉雪洞裡，"
    nvl_narrator "漸漸失去了意識……"
    nvl_narrator "(END)"
    return
label CH3_GE1:  #報恩
    $ persistent.unlocked_ch3_GE1 = True
    scene game_ch3
    nvl_narrator "列文、沃寧和拉扎三人在洞口外打了起來，"
    nvl_narrator "為了避免被他們意外踩傷，"
    nvl_narrator "我選擇躲在洞裡。"
    nvl_narrator "隨著被挖開的洞口灌入冷風，"
    nvl_narrator "其中一位日本客呼吸逐漸恢復正常。"
    nvl_narrator "隨著三人的爭執越演越烈，"
    nvl_narrator "他嘗試逃離雪洞，"
    nvl_narrator "我也悄悄地跟了上去。"

    nvl_narrator "他開始往山下的木屋走去，"
    nvl_narrator "我則跑到前面探路。"

    nvl_narrator "不久之後，我發現前方有一個冰縫，"
    nvl_narrator "我站在原地大叫提醒他。"

    nvl_narrator "最終，"
    nvl_narrator "我們成功抵達木屋，"
    nvl_narrator "並呼叫救援隊。"

    nvl_narrator "隔天早上，"
    nvl_narrator "救援隊帶著隊員們回來，"
    nvl_narrator "除了布爾金已經因救援不及而身亡，"
    nvl_narrator "其他人都倖免於難。"

    nvl_narrator "法布的眼部需要經歷漫長的治療，"
    nvl_narrator "並且很難恢復原來的視力。"
    nvl_narrator "其他隊員則在短暫修整之後，"
    nvl_narrator "繼續進行訓練，"
    nvl_narrator "最後他們成為了這個山峰的專業救援隊。"

    nvl_narrator "而我始終找不到回到原來世界的方法，"
    nvl_narrator "只能和這些隊員們共度餘生。"
    nvl_narrator "(END)"
    return
label CH3_GE2:  #求救
    $ persistent.unlocked_ch3_GE2 = True
    scene game_ch3
    nvl_narrator "列文發現無線電被搶走而追了上來，"
    nvl_narrator "隊員們也緊追其後。"
    nvl_narrator "而我成功接通了無線電，"
    nvl_narrator "沃寧看到我成功接通，"
    nvl_narrator "大吼著：「求救，我們需要幫助!」"
    nvl_narrator "「滋...收到，請報告你們的精確位置與情況。」"
    nvl_narrator "對講機那一頭，"
    nvl_narrator "傳來了指導員清晰而穩定的回音。"
    nvl_narrator "聽到這個宛如奇蹟般的聲音，"
    nvl_narrator "三人的怒火與瘋狂瞬間停滯了。 "
    nvl_narrator "列文舉在半空中的拳頭無力地垂下，眼眶泛紅；"
    nvl_narrator "拉扎緊繃的身體也癱軟下來，跪在雪地裡大口喘息。"
    nvl_narrator "沃寧立刻從我嘴裡接過對講機，"
    nvl_narrator "他的聲音因為極度的寒冷與激動而劇烈發抖："
    nvl_narrator "「我們在原定路線的雪洞裡！"
    nvl_narrator "隊醫法布發生嚴重雪盲完全看不見，"
    nvl_narrator "布爾金出現奇怪的神經抽搐與昏迷，"
    nvl_narrator "洞裡還有兩名日本客！"
    nvl_narrator "我們需要緊急醫療支援，"
    nvl_narrator "重複，我們需要緊急醫療支援！」"
    nvl_narrator "「收到。救援隊立刻帶著裝備出發，"
    nvl_narrator "請你們務必保持清醒，固守待援！」"
    nvl_narrator "通訊結束後，雪洞外依舊是狂風的呼嘯聲。 "
    nvl_narrator "但這一次，那股令人窒息的絕望被徹底打破了。 "
    nvl_narrator "知道救援已經在路上，三人不再為了生存權互相撕咬。 "

    nvl_narrator "列文沉默地走上前，將快要凍僵的我緊緊抱進懷裡。 "
    nvl_narrator "「對不起……還有，謝謝你。」他哽咽著把臉埋在我的毛髮裡。"

    nvl_narrator "此時，固體酒精已經用盡，"
    nvl_narrator "為了避免失溫，所有人緊緊抱團取暖，"
    nvl_narrator "用彼此的體溫撐過這個漫長的黑夜。"
    nvl_narrator "隔天破曉，救援隊趕到。 "
    nvl_narrator "雖然布爾金和法布已經奄奄一息，"
    nvl_narrator "但包含那兩名日本客在內，"
    nvl_narrator "所有人都在失溫休克前被成功救下山。"

    nvl_narrator "法布的眼部需要經歷漫長的治療，"
    nvl_narrator "並且很難恢復原來的視力。"
    nvl_narrator "布爾金則在即時的搶救下保住性命，"
    nvl_narrator "隨著時間逐漸康復。"
    nvl_narrator "其他隊員則在短暫修整之後，"
    nvl_narrator "繼續進行訓練，"
    nvl_narrator "最後他們成為了這個山峰的專業救援隊。"

    nvl_narrator "而我始終找不到回到原來世界的方法，"
    nvl_narrator "只能和這些隊員們共度餘生。"
    nvl_narrator "(END)"
    return