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


    
        

# === 定義進度條所需的變數 ===
default nvl_progress = 0.0      # 當前進度
default nvl_total_lines = 10    # 預設總行數 (防止錯誤用)
default pet = "dog"
default Owner = 1
default pass_game =0
#

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
    # TODO : 腳本設計
    $ quick_menu = False
    nvl clear
    #scene intro_1
    scene gui nvl
    nvl_dark "某天，我照常打開YouTube看影片。"
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
    nvl_dark "影片漸漸到了尾聲，"
    nvl_dark "我不知不覺睡著了。"
    nvl_dark "隔天醒來我發現我在雪地裡"

    nvl_dark "好奇怪"
    nvl_dark "這些樹好高"
    nvl_dark "太陽離我好遠"
    nvl_dark "低頭看了看自己"
    nvl_dark "我怎麼變成了"
    nvl_dark "我怎麼變成了_____"
    menu:
        "貓咪":
            $ pet = "cat"
        "小狗":
            $ pet = "dog"
    nvl_dark "在這個世界待了幾天之後，"
    nvl_dark "我發現我回到了那個影片的時空背景下。"
    
label ch1:

    nvl clear
    scene game_ch1
    $ quick_menu = True
    $ nvl_progress = 0.0
    $ nvl_total_lines = 40

    nvl_narrator "連日的大雪，我已經好幾天沒有吃到東西了"
    nvl_narrator "好多同伴都撐不下去，倒在了路邊，再也沒有起來"
    nvl_narrator "不知道我還能撐多久"
    nvl_narrator "……"
    nvl_narrator "欸?"
    nvl_narrator "我怎麼好像聞到食物的味道"
    nvl_narrator "我順著味道走過去，來到一棟木屋前"
    nvl_narrator "這間木屋竟然沒有關門，味道隨著風從屋裡飄出"
    nvl_narrator "我鑽過門縫，走了進去，裡面分成好幾個房間"
    nvl_narrator "風把味道混合在一起，但我還是分得出來"
    nvl_narrator "風曬過的肉味、清香的草藥味、淡淡的麥香味，還有濃濃的奶香味"

    #nvl_narrator "\n{a=showimg:images/note_large.png}{image=images/note_small.png}{/a}"# {a=showimg:大圖檔名}{image=小圖檔名}{/a}

    
    nvl_narrator "你想順著哪個味道走向哪個房間呢?"
    
    

    menu:
        "風曬過的肉味":
            nvl_narrator "過了一陣子，門開了"
            nvl_narrator "他看了我一眼，沒有說話"
            nvl_narrator "只是側過身，讓我進去"
            nvl_narrator "我走進房間，發現剛剛聞到的是肉乾的味道"
            nvl_narrator "……"
            nvl_narrator "他給了我一些水和食物，吃完之後，我在房間裡閒逛"
            nvl_narrator "房間裡掛滿了登山證書，有些邊角已經泛黃"
            nvl_narrator "旁邊整齊地擺著繩索、冰斧、頭燈，還有收拾好的登山裝備"
            nvl_narrator "桌上還有一張地圖，上面畫滿了路線，有些被劃掉，又重新畫過"
            nvl_narrator "最後我在房間裡找了一個地方休息"

        "清香的草藥味":
            nvl_narrator "(我走到了有草藥味的門前……)"
            nvl_narrator "過了一陣子，門開了"
            nvl_narrator "他看了我一眼，沒有說話"
            nvl_narrator "只是側過身，讓我進去"
            nvl_narrator "我走進房間，發現剛剛聞到的是熱湯的味道"
            nvl_narrator "……"
            nvl_narrator "他給了我一些水和食物，吃完之後，我在房間裡閒逛"
            nvl_narrator "桌上擺滿了醫療用品"
            nvl_narrator "繃帶、藥瓶、針筒，整齊地排列著"
            nvl_narrator "旁邊堆著幾本厚重的醫學書，翻到一半"
            nvl_narrator "紙上畫著人體的圖，還有密密麻麻的標記"
            nvl_narrator "最後我在房間裡找了一個地方休息"

        "淡淡的麥香味":
            nvl_narrator "(我走到了有麥香味的門前……)"
            nvl_narrator "過了一陣子，門開了"
            nvl_narrator "他看了我一眼，沒有說話"
            nvl_narrator "只是側過身，讓我進去"
            nvl_narrator "我走進房間，發現剛剛聞到的是麵包的味道"
            nvl_narrator "……"
            nvl_narrator "他給了我一些水和食物，吃完之後，我在房間裡閒逛"
            nvl_narrator "房間有點亂，背包隨意丟在角落，衣服堆在椅子上"
            nvl_narrator "還有一些健身器材散落在地上"
            nvl_narrator "最後我在房間裡找了一個地方休息"

        "濃濃的奶香味":
            nvl_narrator "(我走到了有奶香味的門前……)"
            nvl_narrator "過了一陣子，門開了"
            nvl_narrator "他看了我一眼，沒有說話"
            nvl_narrator "只是側過身，讓我進去"
            nvl_narrator "我走進房間，發現剛剛聞到的是起司的味道"
            nvl_narrator "……"
            nvl_narrator "他給了我一些水和食物，吃完之後，我在房間裡閒逛"
            nvl_narrator "牆上掛滿了照片"
            nvl_narrator "桌上擺著相機和鏡頭，還有一疊沖洗好的照片"
            nvl_narrator "最後我在房間裡找了一個地方休息"

    
    nvl_narrator "……"
    nvl_narrator "日子一天一天的過，我漸漸跟他培養起感情"
    nvl_narrator "我發現他們就是影片中的登山隊"
    nvl_narrator "而我的主人是______"
    menu:
        "隊長":
            $ Owner = 1
        "隊醫":
            $ Owner = 2
        "隊員":
            $ Owner = 3
        "攝影":
            $ Owner = 4
    nvl_narrator "我會跟他們一起去做登山的基本訓練"
    nvl_narrator "他們平時也會陪我一起玩"

    nvl_narrator "響片遊戲(45秒)"
    nvl_narrator "遊戲說明:當聽到響片聲，便按下空白鍵，越到後面越快"
    #TODO 遊戲未完成
    menu:
        "通過":
            $ pass_game = 1
            nvl_narrator "響片遊戲我們玩了一個月之後"
            nvl_narrator "他幫我用了幾個按鈕"
            nvl_narrator "讓我可以表達需求"
            nvl_narrator "我最常按的是食物"
            nvl_narrator "他偶爾還會用雙手跟我溝通"
            nvl_narrator "像是要不要出去玩"
        "未通過":
            $ pass_game = 0
            nvl_narrator "雖然我玩的不怎麼樣"
            nvl_narrator "但他還是很有耐心"
            nvl_narrator "我們溝通還是主要透過他的解讀"
            nvl_narrator "偶爾會用雙手跟我溝通"
            nvl_narrator "像是要不要出去玩"
    nvl_narrator "他時常還會把我當作訓練的一環"

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
    
    nvl_narrator "日子到了要實地訓練的那一天"
    nvl_narrator "我才驚覺這一天就是影片所說的那一天"

    if(pass_game):
        nvl_narrator "我急忙的用按鈕按”不要”"
        nvl_narrator "他蹲下來問我什麼不要"
        nvl_narrator "我圍著他轉"
        nvl_narrator "還是沒能表達出來"
        nvl_narrator "讓他們不要去實地訓練"
        nvl_narrator "最後到了出發時間"
        nvl_narrator "他們一行人就出發了"
    else:
        nvl_narrator "我急忙的用手去扒他"
        nvl_narrator "他蹲下來問我怎麼了"
        nvl_narrator "我圍著他轉"
        nvl_narrator "還是沒能表達出來"
        nvl_narrator "讓他們不要去實地訓練"
        nvl_narrator "最後到了出發時間"
        nvl_narrator "他們一行人就出發了"
    nvl_narrator "我知道即使我阻止了他們"
    nvl_narrator "他們還是會照常出發"
    nvl_narrator "因為他們是國家資助的登山隊"
    nvl_narrator "必須完成國家指派的任務"
    nvl_narrator "……"
    nvl_narrator "希望因為我的到來改變這件事情的走向"

    nvl clear
    window hide

label ch2:
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