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
    
        

# === 定義進度條所需的變數 ===
default nvl_progress = 0.0      # 當前進度
default nvl_total_lines = 10    # 預設總行數 (防止錯誤用)
default pet = "dog"
#

# 宣告角色。 
#nvl
# === 1. NVL 模式角色 ===
define s = Character('我', kind=nvl, color="#349634", callback=type_sound, ctc="typing_cursor", ctc_position="nestled")
define nvl_narrator = Character(None, kind=nvl, callback=type_sound, ctc="typing_cursor", ctc_position="nestled")

define nvl_dark = Character(None, kind=nvl, screen="nvl_black",what_color="#ffffff", callback=type_sound, ctc="typing_cursor", ctc_position="nestled")

# === 2. ADV 模式角色 ===
define p = Character('我', callback=type_sound, ctc="typing_cursor", ctc_position="nestled")
define npc = Character('神祕男子', color="#ff4444", callback=type_sound, ctc="typing_cursor", ctc_position="nestled")
define narrator = Character(None, callback=type_sound, ctc="typing_cursor", ctc_position="nestled")
# 遊戲從這裡開始。
define menu = nvl_menu
label start:
    # TODO : 腳本設計
    $ quick_menu = False
    nvl clear
    nvl_dark "某天，我照常打開YouTube看影片"
    nvl_dark "發現YouTube推薦了我從沒有看過的類型"
    nvl_dark "我從來都不看懸疑推理類的影片"
    nvl_dark "但今天突然心血來潮決定看一看"
    nvl_dark "........"
    nvl_dark "一覺醒來"
    nvl_dark "我變成了一隻_____"
    menu:
        "貓咪":
            $ pet = "cat"
        "小狗":
            $ pet = "dog"
    
    
label ch1:

    nvl clear
    scene game_ch1
    $ quick_menu = True
    $ nvl_progress = 0.0
    $ nvl_total_lines = 40

    nvl_narrator "連日的大雪，我已經好幾天沒有吃到東西了。"
    nvl_narrator "好多同伴都撐不下去，倒在路邊，再也沒有起來。"
    nvl_narrator "不知道我還能撐多久。"
    nvl_narrator "……"
    nvl_narrator "欸?"
    nvl_narrator "我怎麼好像聞到食物的味道。"
    nvl_narrator "我順著味道走過去，來到一棟木屋前。"
    nvl_narrator "\n{a=showimg:images/note_large.png}{image=images/note_small.png}{/a}"# {a=showimg:大圖檔名}{image=小圖檔名}{/a}

    nvl_narrator "這間木屋竟然沒有關門，味道隨著風從屋裡飄出。"
    nvl_narrator "我鑽過門縫，走了進去，裡面分成好幾個房間。"
    nvl_narrator "風把味道混合在一起，但我還是分得出來。"
    nvl_narrator "風曬過的肉味、清香的草藥味、淡淡的麥香味，還有濃濃的奶香味。"
    nvl_narrator "你想順著哪個味道走向哪個房間呢?"
    
    

    menu:
        "風曬過的肉味":
            nvl_narrator "(我走到了有肉味的門前……)"
            nvl_narrator "過了一陣子，門開了。"
            nvl_narrator "他看了我一眼，沒有說話。"
            nvl_narrator "只是側過身，讓我進去。"
            nvl_narrator "我走進房間，發現剛剛聞到的，是肉乾的味道。"
            nvl_narrator "他給了我一些水和食物，吃完之後，我在房間裡閒逛。"
            nvl_narrator "他的房間裡掛滿了登山證書，有些邊角已經泛黃。"
            nvl_narrator "旁邊整齊地擺著繩索、冰斧、頭燈，還有收拾好的登山裝備。"
            nvl_narrator "桌上還有一張地圖，上面畫滿了路線，有些被劃掉，又重新畫過。"

        "清香的草藥味":
            nvl_narrator "(我走到了有草藥味的門前……)"
            nvl_narrator "過了一陣子，門開了。"
            nvl_narrator "他看了我一眼，沒有說話。"
            nvl_narrator "只是側過身，讓我進去。"
            nvl_narrator "我走進房間，發現剛剛聞到的，是熱湯的味道。"
            nvl_narrator "他給了我一些水和食物，吃完之後，我在房間裡閒逛。"
            nvl_narrator "桌上擺滿了醫療用品。"
            nvl_narrator "繃帶、藥瓶、針筒，整齊地排列著。"
            nvl_narrator "旁邊堆著幾本厚重的醫學書，翻到一半。"
            nvl_narrator "紙上畫著人體的圖，還有密密麻麻的標記。"

        "淡淡的麥香味":
            nvl_narrator "(我走到了有麥香味的門前……)"
            nvl_narrator "過了一陣子，門開了。"
            nvl_narrator "他看了我一眼，沒有說話。"
            nvl_narrator "只是側過身，讓我進去。"
            nvl_narrator "我走進房間，發現剛剛聞到的，是麵包的味道。"
            nvl_narrator "房間有點亂，背包隨意丟在角落，衣服堆在椅子上。"

        "濃濃的奶香味":
            nvl_narrator "(我走到了有奶香味的門前……)"
            nvl_narrator "過了一陣子，門開了。"
            nvl_narrator "他看了我一眼，沒有說話。"
            nvl_narrator "只是側過身，讓我進去。"
            nvl_narrator "我走進房間，發現剛剛聞到的，是起司的味道。"
            nvl_narrator "牆上掛滿了照片。"
            nvl_narrator "雪山、隊伍，還有他們的合照。"
            nvl_narrator "桌上擺著相機和鏡頭，還有一疊沖洗好的照片。"

    
    nvl_narrator "你會跟著主人一起出門訓練，跑步、負重，"
    nvl_narrator "朝夕相處的陪伴，你們的感情越來越好。"
    nvl_narrator "他不訓練的時候，你們常常用寵物按鈕溝通，他也時常為你準備鮮食。"
    
    nvl_narrator "日子來到登山隊要登山的這一天，"
    nvl_narrator "你隱隱約約的覺得這次的登山行不會很順利，"
    nvl_narrator "你可以用寵物按鈕跟主人說說話，你想說什麼?"

    menu nvl_narrator:
        "不要去":
            jump Ch1_end
        "模糊提醒":
            jump Ch1_end
        "什麼都不說":
            jump Ch1_end
    # 清除 NVL 畫面，準備切換到動態對話模式
    nvl clear
    window hide


label Ch1_end:
    #"【第一章：- 完】"
    return