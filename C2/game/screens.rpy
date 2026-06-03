################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 樣式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 遊戲內畫面
################################################################################


## Say 畫面 ######################################################################
##
## Say 畫面用於向玩家顯示對話。它有兩個參數 who 和 what，分別是說話角色的名字和
## 要顯示的文字。（who 參數可以為 None 如果沒有給出名字。）
##
## 此畫面必須建立 id 為 "what" 的可顯示文字，因為 Ren'Py 使用它來管理文字顯示。
## 它還可以建立 id "who" 和 id "window" 的可顯示文字應用程式樣式屬性。
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 如果有側面影像，請將其顯示在文字上方。不要顯示在手機版本上 - 沒有空間。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 使名稱框可用於透過角色物件進行樣式設定。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## 輸入畫面 ########################################################################
##
## 此畫面用於顯示 renpy.input 。prompt 參數用於傳入文字提示。
##
## 此畫面必須建立一個可顯示的輸入，透過 id "input" 以接受各種輸入參數。
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 選擇畫面 ########################################################################
##
## 此畫面用於顯示選單語句所呈現的遊戲內選項。第一個參數，項目，是一個物件列表，
## 每個物件都有標題和操作欄位。
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## 快捷選單畫面 ######################################################################
##
## 快捷選單顯示在遊戲中，以便輕鬆存取遊戲外選單。

screen quick_menu():
    if True:#quick_menu:
        ## 確保它出現在其他螢幕的頂端。
        zorder 500
        imagemap:
            ground "gui/quick_menu_idle.png"
            idle "gui/quick_menu_idle.png"
            hover "gui/quick_menu_hover.png"
            selected_idle "gui/quick_menu_hover.png"

            hotspot (142, 224, 71, 72) action Skip() alternate Skip(fast=True, confirm=True) #快進
            hotspot (141, 309, 75, 72) action [QuickSave(), Notify("進度已儲存！")]           #儲存     
            hotspot (139, 399, 78, 72) action ShowMenu('main_menu')                          #主頁
            hotspot (139, 488, 78, 74) action Preference("all mute", "toggle")               #禁音
            hotspot (141, 574, 75, 78) action ShowMenu("about")                              #關於
            hotspot (140, 667, 76, 71) action ShowMenu("help")                               #幫助
            hotspot (140, 753, 75, 75) action ShowMenu("preferences")                        #設定
            hotspot (140, 844, 75, 74) action ShowMenu("load")                               #載入
            hotspot (138, 931, 79, 76) action Quit(confirm=False)                            #離開




## 此代碼確保只要玩家沒有明確隱藏介面， quick_menu 畫面就會在遊戲中顯示。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## 主選單畫面 #######################################################################
##
## 用於在 Ren'Py 啟動時顯示主選單。
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    imagemap:
        ground "gui/main_menu_idle.png"
        idle "gui/main_menu_idle.png"
        hover "gui/main_menu_hover.png"
        hotspot (725, 187, 241, 141) action Start()
        hotspot (984, 189, 230, 137) action Continue()
        hotspot (452, 358, 205, 128) action ShowMenu("load")
        hotspot (669, 374, 192, 112) action ShowMenu("preferences")
        hotspot (873, 374, 191, 108) action ShowMenu("about")
        hotspot (1084, 372, 188, 116) action ShowMenu("help")
        hotspot (1290, 370, 187, 112) action Quit(confirm=False)
        hotspot (1565, 446, 266, 99) action Confirm( "警告：這將會清除所有的解鎖進度與紀錄！\n確定要繼續嗎？", yes=Function(reset_all_progress), no=NullAction() )



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 遊戲選單畫面 ######################################################################
##
## 這列出了遊戲選單畫面的基本公共結構。它透過畫面標題進行呼叫，並顯示背景、標題
## 和導覽。
##
## 滾動參數可以是 None，或者是 "viewport" 與 "vpgrid" 的其中之一。此畫面是要與一
## 個或多個子畫面一起使用，這些子畫面被嵌入（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 為導覽部分保留空間。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 關於畫面 ########################################################################
##
## 此畫面提供有關遊戲和Ren'Py的製作人員名單和版權資訊。
##
## 這個畫面沒有什麼特別的，因此它也可以作為如何製作自訂螢幕的範例。
screen about():
    tag menu
    modal True
    imagemap:
        ground 'gui/About_idle.PNG'
        idle 'gui/About_idle.PNG'
        hover 'gui/About_hover.PNG'

        hotspot (1751, 104, 71, 72) action If(main_menu, true=Hide("about"), false=Return())              # X
        hotspot (142, 401, 71, 73) action If(main_menu, true=Hide("about"), false=ShowMenu("main_menu"))  # Home
        hotspot (139, 488, 78, 74) action Preference("all mute", "toggle")  # Volume
        hotspot (142, 581, 70, 70) action ShowMenu("about")                 # Abuot
        hotspot (142, 670, 71, 70) action ShowMenu("help")                  # Help
        hotspot (141, 758, 72, 71) action ShowMenu("preferences")           # Setting
        hotspot (142, 848, 72, 69) action ShowMenu("load")                  # Load
        hotspot (142, 936, 72, 73) action Quit(confirm=False)               # Quit

# 【修改 1】最外層改用 fixed，允許內部的元件透過絕對坐標自由定位
    fixed:

        # 【位置 A】大標題與滾動視窗包在一起
        vbox:
            xpos 267 
            ypos 114
            spacing 25 # 標題與下方滾動內容之間的間距

            # 1. 固定在最上面的大標題
            text "程式設計（二）期末專題" size 56 bold True color "#000000" style "text"

            # 2. 下方的滾動視窗
            viewport id "about_text":
                xmaximum 1549
                ymaximum 750
                
                draggable True      
                mousewheel True     
                # 【修改 2】拿掉內建的 scrollbars "vertical"，因為下方你已經自訂了 vbar
                
                # 滾動視窗內部的 vbox（放詳細內容）
                vbox:
                    spacing 18 
                    xmaximum 1400

                    text "- 遊戲製作：許靖妤" size 48 color "#000000" style "text"
                    text "- 聲明：本遊戲劇情受真實事件啟發並進行改編，部分情節與\n設定為虛構創作，如有雷同，純屬巧合。" size 48 color "#000000" style "text"
                    
                    text "- 劇情靈感：YouTuber「自說自話的總裁」——\n{a=https://www.youtube.com/watch?si=wh2G8oP4qagpJELU&v=zeluE32TSoc}《1990年，一支蘇聯小隊消失，找到時，6人變成了8人？...》{/a}" size 48 color "#000000" style "text"
                    
                    text "- 圖片素材：Gemini AI 輔助生成" size 48 color "#000000" style "text"

                    null height 30 

                    text _("版本 [config.version!t]") size 40 color "#000000" style "text"
                    text _("使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 製作。") size 40 color "#000000" style "text"

        # 【位置 B】獨立定位的自訂滾動條（因為在外層是 fixed，這裡的 xpos 1763 才會真正生效！）
        vbar value YScrollValue("about_text"):#(1756, 203, 62, 775)
            xpos 1763
            ypos 203
            xsize 51
            ysize 775
            thumb Solid("#000000f1")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 載入和儲存畫面 #####################################################################
##
## 這些畫面負責讓玩家儲存遊戲並再次載入。由於它們幾乎共享所有共同點，因此兩者都
## 是透過第三個畫面 file_slots 實現的。
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load



default current_page = 1 
screen load():
    tag menu
    modal True
    imagemap:
        ground "gui/Load_idle[current_page].png"
        idle "gui/Load_idle[current_page].png"
        hover "gui/Load_hover[current_page].png"
        selected_idle "gui/Load_selected_idle[current_page].png"
        selected_hover "gui/Load_selected_hover[current_page].png"

        # ==========================================
        # 你的基礎選單按鈕 (保留原本的)
        # ==========================================
        hotspot (1751, 104, 71, 72) action If(main_menu, true=Hide("load"), false=Return())
        hotspot (142, 401, 71, 73) action If(main_menu, true=Hide("load"), false=ShowMenu("main_menu"))
        hotspot (139, 488, 78, 74) action Preference("all mute", "toggle")
        hotspot (142, 581, 70, 70) action ShowMenu("about")
        hotspot (142, 670, 71, 70) action ShowMenu("help")
        hotspot (141, 758, 72, 71) action ShowMenu("preferences")
        hotspot (142, 848, 72, 69) action ShowMenu("load")
        hotspot (142, 936, 72, 73) action Quit(confirm=False)

        hotspot (982, 911, 28, 52) action SetVariable("current_page", 1)
        hotspot (1026, 915, 30, 44) action SetVariable("current_page", 2)
        hotspot (1076, 913, 30, 48) action SetVariable("current_page", 3)

        if current_page == 1: # 第一章
            
            if persistent.unlocked_ch1_0:
                hotspot (342, 479, 227, 133) action [Start("CH1_0"), SelectedIf(True)]
            if persistent.unlocked_ch1_1:
                hotspot (639, 475, 230, 137) action [Start("CH1_1"), SelectedIf(True)]
            if persistent.unlocked_ch1_2:
                hotspot (941, 379, 231, 136) action [Start("CH1_2"), SelectedIf(True)]
            if persistent.unlocked_ch1_3:
                hotspot (1242, 475, 229, 141) action [Start("CH1_3"), SelectedIf(True)]
            if persistent.unlocked_ch1_BE1:
                hotspot (941, 574, 231, 140) action [Start("CH1_BE1"), SelectedIf(True)]
            if persistent.unlocked_ch2_1:
                hotspot (1545, 477, 228, 133) action [SetVariable("current_page", 2), SelectedIf(True)]

        elif current_page == 2: # 第二章
            if persistent.unlocked_ch2_1:
                hotspot (278, 477, 227, 131) action [Start("CH2_1"), SelectedIf(True)]
            if persistent.unlocked_ch2_2 :
                hotspot (539, 475, 224, 133) action [Start("CH2_2"), SelectedIf(True)]
            if persistent.unlocked_ch2_3 :
                hotspot (799, 389, 225, 132) action [Start("CH2_3"), SelectedIf(True)]
            if persistent.unlocked_ch2_4 :
                hotspot (1058, 479, 220, 129) action [Start("CH2_4"), SelectedIf(True)]
            if persistent.unlocked_ch2_5 :
                hotspot (1312, 387, 231, 138) action [Start("CH2_5"), SelectedIf(True)]
            if persistent.unlocked_ch2_BE1 :
                hotspot (801, 564, 229, 134) action [Start("CH2_BE1"), SelectedIf(True)]
            if persistent.unlocked_ch2_BE2 :
                hotspot (1316, 564, 229, 136) action [Start("CH2_BE2"), SelectedIf(True)]
            if persistent.unlocked_ch3_1:
                hotspot (1579, 473, 218, 135) action [SetVariable("current_page", 3), SelectedIf(True)]

        elif current_page == 3: # 第三章
            if persistent.unlocked_ch3_1:
                hotspot (282, 477, 227, 133) action [Start("CH3_1"), SelectedIf(True)]
            if persistent.unlocked_ch3_2 :
                hotspot (607, 476, 224, 133) action [Start("CH3_2"), SelectedIf(True)]
            if persistent.unlocked_ch3_3 :
                hotspot (929, 480, 225, 137) action [Start("CH3_3"), SelectedIf(True)]
            if persistent.unlocked_ch3_4 :
                hotspot (1254, 480, 225, 133) action [Start("CH3_4"), SelectedIf(True)]
            if persistent.unlocked_ch3_5 :
                hotspot (1577, 480, 224, 129) action [Start("CH3_5"), SelectedIf(True)]
            if persistent.unlocked_ch3_BE1 :
                hotspot (607, 127, 222, 134) action [Start("CH3_BE1"), SelectedIf(True)]
            if persistent.unlocked_ch3_BE2 :
                hotspot (605, 304, 224, 138) action [Start("CH3_BE2"), SelectedIf(True)]
            if persistent.unlocked_ch3_BE3 :
                hotspot (605, 647, 222, 134) action [Start("CH3_BE3"), SelectedIf(True)]
            if persistent.unlocked_ch3_BE4 :
                hotspot (605, 814, 224, 136) action [Start("CH3_BE4"), SelectedIf(True)]
            if persistent.unlocked_ch3_BE5 :
                hotspot (927, 649, 223, 136) action [Start("CH3_BE5"), SelectedIf(True)]
            if persistent.unlocked_ch3_GE1 :
                hotspot (1252, 306, 223, 132) action [Start("CH3_GE1"), SelectedIf(True)]
            if persistent.unlocked_ch3_GE2 :
                hotspot (1252, 643, 227, 140) action [Start("CH3_GE2"), SelectedIf(True)]

## 首選項畫面 #######################################################################
##
## 首選項畫面允許玩家設定遊戲以更好地適合自己。
## setting
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    modal True
    imagemap:
        ground 'gui/setting_idle.PNG'
        idle 'gui/setting_idle.PNG'
        hover 'gui/setting_hover.PNG'
        selected_idle 'gui/setting_hover.PNG'
        #selected_hover 'gui/setting_hover.PNG'

        hotspot (322, 239, 47, 46) action Preference("display", "window")
        hotspot (322, 303, 45, 47) action Preference("display", "fullscreen")
        hotspot (321, 494, 48, 49) action Preference("skip", "toggle")
        hotspot (321, 559, 47, 47) action Preference("after choices", "toggle")
        hotspot (322, 622, 46, 48) action Preference("transitions", "toggle")
        #hotspot (321, 835, 46, 46) action StylePreference("text_font", "Cubic") 
        #hotspot (322, 898, 44, 46) action StylePreference("text_font", "Iansui")
        
        hotspot (321, 835, 46, 46) action gui.SetPreference("font", "Cubic_11.ttf") # 字體
        hotspot (322, 898, 44, 46) action gui.SetPreference("font", "Iansui-Regular.ttf")   # 字體

        hotspot (1751, 104, 71, 72) action If(main_menu, true=Hide("preferences"), false=Return())              # X
        hotspot (142, 401, 71, 73) action If(main_menu, true=Hide("preferences"), false=ShowMenu("main_menu"))  # Home
        hotspot (139, 488, 78, 74) action Preference("all mute", "toggle")  # Volume
        hotspot (142, 581, 70, 70) action ShowMenu("about")                 # Abuot
        hotspot (142, 670, 71, 70) action ShowMenu("help")                  # Help
        #hotspot (141, 758, 72, 71) action ShowMenu("preferences")          # Setting
        hotspot (142, 848, 72, 69) action ShowMenu("load")                  # Load
        hotspot (142, 936, 72, 73) action Quit(confirm=False)               # Quit

        bar pos (843, 242) value Preference("font size") style "pref_slider"
        bar pos (841, 455) value Preference("text speed") style "pref_slider"
        bar pos  (839, 658)  value Preference("music volume") style "pref_slider"
        bar pos  (841, 869)  value Preference("sound volume") style "pref_slider"

        text "A":
            pos (1609, 264)    # 設定 X 和 Y 座標
            yanchor 0.5
            size (42 * preferences.font_size)            # 建議加上字體大小設定，避免預設字體太大塞不進 78x81 的框內
            color "#000000"    # 文字顏色 (這表示白色，可依需求更改)

init -5 python:
    style.pref_slider.xmaximum =  3114*3 
    style.pref_slider.xmaximum =  243*3
    style.pref_slider.left_bar =  Frame("gui/slider/set_Slider_left.png")
    style.pref_slider.right_bar =  Frame("gui/slider/Set_Slider_right.png")
    

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## 歷史畫面 ########################################################################
##
## 這是向玩家顯示對話歷史記錄的畫面。 雖然這個畫面沒有什麼特別的，但它必須存取儲
## 存在 _history_list 中的對話歷史記錄。
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 避免預測該螢幕，因為它可能非常大。
    predict False

    use game_menu(_("歷史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 如果 history_height 為None，這會正確排列事物。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 從角色中取得 who 文字的顏色（如果已設定）。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("對話歷史記錄為空。")


## 這決定了允許在歷史螢幕上顯示哪些標籤。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 幫助畫面 ########################################################################
##
## 提供有關按鍵和滑鼠綁定資訊的畫面。 它使用其他畫面 (keyboard_help, mouse_help,
## and gamepad_help) 來顯示實際幫助。

screen help():
    tag menu
    modal True

    # 1. 直接讀取完整清單（固定 7 頁），不再過濾
    $ total_chars = len(help_characters)
    
    # 取得當前頁面的角色資料
    $ char = help_characters[current_char_index]
    
    # 2. 檢查當前角色是否已解鎖 (回傳 True 或 False)
    $ is_unlocked = eval(char["condition"])

    $ display_avatar = char["avatar"]
    if display_avatar == "player":
        if persistent.pet == "cat":
            $ display_avatar = "gui/avatar_player_cat.png"
        else:
            $ display_avatar = "gui/avatar_player_dog.png"
    imagemap:
        ground 'gui/Help_idle.PNG'
        idle 'gui/Help_idle.PNG'
        hover 'gui/Help_hover.PNG'

        hotspot (1751, 104, 71, 72) action If(main_menu, true=Hide("help"), false=Return())              # X
        hotspot (142, 401, 71, 73) action If(main_menu, true=Hide("help"), false=ShowMenu("main_menu"))  # Home
        hotspot (139, 488, 78, 74) action Preference("all mute", "toggle")  # Volume
        hotspot (142, 581, 70, 70) action ShowMenu("about")                 # About
        hotspot (142, 670, 71, 70) action ShowMenu("help")                  # Help
        hotspot (141, 758, 72, 71) action ShowMenu("preferences")           # Setting
        hotspot (142, 848, 72, 69) action ShowMenu("load")                  # Load
        hotspot (142, 936, 72, 73) action Quit(confirm=False)               # Quit

    # 內容容器
    hbox:
        xpos 336      
        ypos 262          
        #spacing 50        

        # 【左邊：頭像區判斷】
        if is_unlocked:
            # 已解鎖：顯示正常頭像
            add display_avatar yalign 0.0 maxsize (515, 565)#(332, 263, 515, 565)
        else:
            # 未解鎖：顯示一張問號替代圖（請確保 gui 資料夾下有這張圖，或改成你現有的黑影圖）
            add "gui/avatar_locked.png" yalign 0.0 maxsize (515, 565)

        # 【右邊：文字訊息區】(972, 269) 
        vbox:
            xpos 40
            ypos 20
            spacing 20
            xminimum 800
            xmaximum 800

            # 無論解鎖與否，都顯示角色名稱
            text char["name"]:
                size 40
                bold True
                color "#000000"

            # 說明文字判斷
            if is_unlocked:
                # 已解鎖：顯示詳細介紹
                text char["desc"]:
                    size 34
                    color "#000000"
                    line_spacing 10 
            else:
                # 未解鎖：只顯示問號
                text "？？？":
                    size 34
                    color "#888888" # 沒解鎖時用灰色文字暗示
                    line_spacing 10 

    # 下方切換分頁按鈕（使用 total_chars 固定的總頁數）
    hbox:
        xpos 900
        ypos 850
        spacing 40

        if current_char_index > 0:
            textbutton "<":
                action SetVariable("current_char_index", current_char_index - 1)
                text_bold True          
                text_size 28            
                text_idle_color "#000000"  
                text_hover_color "#4472C4" 
        else:
            textbutton "<":
                action None
                text_bold True
                text_size 28
                text_idle_color "#555555"  

        # 顯示總頁數（例如：1 / 7）
        text "[current_char_index + 1] / [total_chars]":
            size 28 
            yalign 0.5 
            bold True
            color "#000000"

        if current_char_index < total_chars - 1:
            textbutton ">":
                action SetVariable("current_char_index", current_char_index + 1)
                text_bold True          
                text_size 28            
                text_idle_color "#000000"  
                text_hover_color "#4472C4" 
        else:
            textbutton ">":
                action None
                text_bold True
                text_size 28
                text_idle_color "#555555"


################################################################################
## 附加畫面
################################################################################


## 確認畫面 ########################################################################
##
## 當 Ren'Py 想問玩家是或否問題時，會呼叫確認畫面。
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 確保顯示此畫面時其他畫面不會收到輸入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("是") action yes_action
                textbutton _("否") action no_action

    ## 右鍵點選並結束回答 "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## 快進提示畫面 ######################################################################
##
## 顯示 skip_indicator 畫面以指示快進正在進行中。
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("快進中")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此變換用於使箭頭依序閃爍。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我們必須使用帶有黑色右指小三角形字形的字型。
    font "DejaVuSans.ttf"


## 提醒畫面 ########################################################################
##
## 通知畫面用於向玩家顯示訊息。 （例如，當遊戲快速儲存或截取螢幕截圖時。）
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 畫面 ######################################################################
##
## 此畫面用於 NVL 模式對話和選單。
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        viewport id "nvl_text_area":
            yinitial 1.0
            # 移除 yfill True，讓內部可以自由長高
            ysize 802               # 統一使用這個高度
            xsize 1461
            #scrollbars "vertical"   # 加入垂直滾動條
            mousewheel True         # 允許使用滑鼠滾輪滾動
            draggable True          # 允許滑鼠點擊拖曳

            vbox:
                #xsize 1100          # 根據你的 gui.nvl_text_width 調整
                xfill True          # 強制填滿寬度，這樣內部的 xpos 才會準確
                spacing gui.nvl_spacing
                
                use nvl_dialogue(dialogue)

                if items:
                    vbox:
                        id "menu"
                        spacing gui.nvl_spacing
                        xpos gui.nvl_button_xpos 
                        
                        for i in items:
                            textbutton i.caption:
                                action i.action
                                style "nvl_button"

    vbar value YScrollValue("nvl_text_area"):
        xpos 1763
        ypos 114
        xsize 51
        ysize 860
        
        # 設定滾動條的外觀
        # base_bar Solid("#ffffff33")  # (可選) 滾動條底槽的顏色
        thumb Solid("#000000f1")       # 滾動塊的顏色



screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                #yfit gui.nvl_height is None
                yfit True
                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 這控制可以一次顯示的 NVL 模式條目的最大數量。
define config.nvl_list_length = None

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

#style nvl_button is button
#style nvl_button_text is button_text

style nvl_window:
    xfill False
    yfill False
    #(282, 122, 1520, 847)
    xpos 269
    ypos 120
    xsize 1461
    ysize 860


style nvl_entry:
    xfill False
    #ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    size gui.nvl_text_size        # 字體大小
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    # 關閉預設的屬性繼承，讓我們可以完全自訂
    #properties gui.button_properties("nvl_button")
    
    # 對齊方式：和你的對話文字切齊 (假設你之前設為 20)
    xpos gui.nvl_button_xpos
    xanchor 0.0

    
    idle_background Solid("#d3d3d3") 
    hover_background Solid("#5e5e5e") 
    
    # 設定按鈕的內邊距 (上下左右留白)
    padding (20, 15, 0, 15)
    
    xsize gui.nvl_button_size


style nvl_button_text:
    #properties gui.text_properties("nvl_button")
    
    xalign gui.nvl_button_xalign
    size gui.nvl_text_size
    
    # 設定文字的顏色
    idle_color  "#4e4e4e"
    hover_color "#ffffff"

screen nvl_black(dialogue, items=None):
    # 1. 滿版純黑背景
    # add Solid("#000000")
    add "images/main_menu.png"
    # 2. 放置在畫面正中央的文字容器
    vbox:
        align (0.5, 0.5)    # 整個區塊在畫面正中央
        spacing 40          # 每一行對話之間的間距
        
        # 3. 顯示對話文字 (捨棄原本的 nvl_dialogue，自訂乾淨的樣式)
        for d in dialogue:
            text d.what:
                id d.what_id
                xalign 0.5       # 讓文字區塊本身置中
                textalign 0.5    # 讓多行文字的排版置中
                size gui.nvl_text_size          # 黑屏文字通常會稍微大一點，可自行調整
                color "#000000"  # 純白字體
                
        # 4. 顯示選單按鈕
        if items:
            vbox:
                xalign 0.5
                spacing 20
                # 這裡加一點上方的留白，讓按鈕和文字拉開距離
                yoffset 30 
                
                for i in items:
                    textbutton i.caption:
                        action i.action
                        
                        # 直接在這裡寫按鈕樣式，不依賴外面的設定
                        text_align 0.5
                        text_size gui.nvl_text_size
                        text_color "#888888"        # 預設灰色
                        text_hover_color "#ffffff"  # 滑鼠游標移過去變白色
    add "gui/nvl.png"

## 放大圖
screen enlarge_image(img_path):
    # 設為 True 確保玩家在關閉此畫面之前，不能點擊後方的對話
    modal True
    zorder 100
    
    # 加上一個半透明的黑色背景，讓大圖更顯眼
    add Solid("#000000CC")
    
    # 在畫面正中央顯示放大的圖片
    add img_path align (0.5, 0.5)
    
    # 建立一個隱形的按鈕覆蓋全螢幕，點擊任何地方都會關閉大圖
    button:
        xfill True
        yfill True
        action Hide("enlarge_image", transition=dissolve)

## 氣泡畫面 ########################################################################
##
## 氣泡螢幕用於在使用對話氣泡時向玩家顯示對話。氣泡螢幕採用與 say 螢幕相同的
## 參數，必須建立一個 id 為 "what" 的可顯示內容，並且可以建立可顯示內容帶有
## "namebox", "who", 和 "window" ID。
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

## 洞穴互動畫面 ########################################################################
# 宣告變數來記錄探索進度
default cave_investigation_count = 0
default checked_backpack = False
default checked_levin = False
default checked_fabre = False
default checked_ogin = False
default checked_burgin = False
default checked_voronin_raza = False
default checked_heat = False
# 定義洞穴互動螢幕
screen cave_exploration_screen():
    #use quick_menu
    imagemap:
        ground "images/cave_bg.png"
        idle "images/cave_bg.png"
        hover "images/cave_bg.png"
        hotspot (1658, 770, 227, 246) action Jump("click_backpack")     # 1. 背包
        hotspot (1417, 474, 381, 284) action Jump("click_levin")        # 2. 隊長列文
        hotspot (1164, 413, 200, 399) action Jump("click_fabre")        # 3. 隊醫法布
        hotspot (1014, 442, 120, 351) action Jump("click_ogin")          # 4. 奧金
        hotspot (759, 424, 186, 343) action Jump("click_burgin")         # 5. 布爾金
        hotspot (291, 421, 455, 560) action Jump("click_voronin_raza")  # 6. 沃寧與拉扎   
        hotspot (924, 843, 114, 95) action Jump("click_heat")           # 7. 卡式爐  
        if  (checked_levin):
            hotspot(1491, 559, 58, 89) action Jump("click_radio")    
        
    use quick_menu
screen cave_choice(items, dialogue=None):
    style_prefix "choice"
    
    # 假設你想把洞穴的選項放在畫面右下角
    vbox:
        align (0.5, 0.5)
        spacing 10
        for i in items:
            textbutton i.caption:
                action i.action
                #background "images/cave_button_bg.png" # 專屬的石頭風格背景
                text_color "#000000"
                text_hover_color "#ffffff"
## 木屋造句畫面 ########################################################################
# 初始解鎖的詞庫
default unlocked_subjects = {"我"}
default unlocked_verbs = {"走向"}
default unlocked_nouns = set()
default unlocked_places = {"大廳"}
default current_place = "大廳"
default place_items_map = {
    "大廳": {"大門", "密碼鎖", "合照", "桌子", "六扇房門"},
    "列文的房間": {"背包", "登山證書"},
    "法布的房間": {"白色粉末", "實驗記錄"},
    "布爾金的房間": {"健身器材"},
    "奧金的房間": {"相框"},
    "拉扎的房間": {"防水塗料"},
    "沃寧的房間": {"生存裝備", "羽絨服"}
}
# 玩家目前選中的詞
default current_subject = "我"
default current_verb = None
default current_noun = None
# 控制右側面板切換
default right_panel_mode = "verb" 

screen sentence_puzzle_game():
    zorder 50
    modal False
    #use quick_menu 
    add "images/bg_puzzle_game.png"
    
    # =================【 左側大框：自訂文字歷史區 】=================
    frame:
        pos (306, 149)
        xsize 888
        ysize 697
        background None
        
        viewport id "puzzle_vp":
            mousewheel True
            draggable True
            yinitial 1.0 
            
            vbox:
                spacing 15 
                
                # [靜態] 過去的歷史紀錄
                for t in puzzle_history:
                    if t["img"] is not None:
                        imagebutton:
                            # 這裡將圖片限制在最大寬度 250，高度 150，自動等比例縮放 (fit="contain")
                            idle Transform(t["img"], xysize=(500, 500), fit="contain")
                            action Show("image_popup_viewer", img_path=t["img"])
                    if t["text"] is not None:
                        text t["text"]:
                            color "#000000"
                            size gui.nvl_text_size
                            line_spacing 5
                            xsize 850
                # [動態] 當前最新的一句話
                if current_puzzle_text != "":
                    # 顯示縮圖
                    if current_puzzle_img is not None:
                            imagebutton:
                                idle Transform(current_puzzle_img, xysize=(500, 500), fit="contain")
                                action Show("image_popup_viewer", img_path=current_puzzle_img)
                                # 如果你希望打字完才顯示圖片，可以把這段縮排移到 else (打字完畢) 區塊裡
                    if puzzle_is_typing:
                        # 正在打字中：啟動 slow_cps，不放閃標
                        text current_puzzle_text:
                            color "#000000"
                            size gui.nvl_text_size
                            line_spacing 5
                            xsize 850
                            slow_cps True  # 【關鍵】純 Screen 的打字機效果
                        
                        # 當字打完時自動關閉聲音並顯示閃標
                        if preferences.text_cps == 0:
                            timer 0.01 action [SetVariable("puzzle_is_typing", False), Stop("sound")]
                        else:
                            # 依據字數與玩家設定的打字速度計算時間，加 0.1 秒緩衝
                            $ type_duration = len(current_puzzle_text) / float(preferences.text_cps)
                            timer type_duration + 0.1 action [SetVariable("puzzle_is_typing", False), Stop("sound")]
                            
                    else:
                        # 打字完畢：瞬間顯示完整文字，並用文字標籤 {image=...} 將閃標無縫接在最後面！
                        text current_puzzle_text + " {image=typing_cursor}":
                            color "#000000"
                            size gui.nvl_text_size
                            line_spacing 5
                            xsize 850

        vbar value YScrollValue("puzzle_vp"):
            xpos 910
            ypos -17
            xsize 50
            ysize 720
            thumb Solid("#000000f1")      
        
    # =================【 右側大框：詞庫選擇區 】=================
    frame:
        pos (1330, 126)
        xsize 471
        ysize 745
        background None
        padding (10, 10)
        
        vbox:
            spacing 15
            
            # 右上角：動詞/名詞 切換標籤
            hbox:
                spacing 8
                textbutton "動詞":
                    action SetVariable("right_panel_mode", "verb")
                    text_color ("#2b579a" if right_panel_mode == "verb" else "#888888")
                    text_bold (True if right_panel_mode == "verb" else False)
                    text_size (min(gui.nvl_text_size, 35))
                    text_hover_bold True
                    
                textbutton "名詞":
                    action SetVariable("right_panel_mode", "noun")
                    text_color ("#e06666" if right_panel_mode == "noun" else "#888888")
                    text_bold (True if right_panel_mode == "noun" else False)
                    text_size (min(gui.nvl_text_size, 35))
                    text_hover_bold True

                textbutton "地點":
                    action SetVariable("right_panel_mode", "place")
                    text_color ("#6aa84f" if right_panel_mode == "place" else "#888888") 
                    text_bold (True if right_panel_mode == "place" else False)
                    text_size (min(gui.nvl_text_size, 35))
                    text_hover_bold True
            # 下方滾動列表
            hbox:
                spacing 15
                viewport id "words_vp":
                    xsize 380  
                    ysize 650
                    draggable True
                    mousewheel True
                    vbox:
                        spacing 8
                        if right_panel_mode == "verb":
                            for v in sorted(list(unlocked_verbs)):
                                textbutton v:
                                    action SetVariable("current_verb", v)
                                    text_color "#000000"
                                    text_size gui.nvl_text_size
                                    text_hover_bold True
                        elif right_panel_mode == "place":
                            for p in sorted(list(unlocked_places)):
                                textbutton p:
                                    action SetVariable("current_noun", p)
                                    text_color ("#6aa84f" if p == current_place else "#000000")
                                    text_size gui.nvl_text_size
                                    text_hover_bold True
                        elif right_panel_mode == "noun":
                            
                            # 1. 取得「當前地點」擁有的所有物品 (如果該地點沒有設定，預設給空集合)
                            $ current_place_items = place_items_map.get(current_place, set())
                            
                            # 2. 取交集 (&)：找出「已解鎖」且「在這個地點」的物品
                            $ valid_nouns = current_place_items.intersection(unlocked_nouns)
                            
                            # 3. 取差集 (-)：找出「已解鎖」但「不在這個地點」的物品
                            $ disabled_nouns = unlocked_nouns - valid_nouns
                            
                            # 4. 優先顯示：當前地點的可用物品 (正常顏色，可點擊)
                            for n in sorted(list(valid_nouns)):
                                textbutton n:
                                    action SetVariable("current_noun", n)
                                    text_color "#000000"
                                    text_size (max(gui.nvl_text_size, 30))
                                    text_hover_bold True
                                    
                            # 5. 後置顯示：其他地點的物品 (灰色，不可點擊)
                            for n in sorted(list(disabled_nouns)):
                                textbutton n:
                                    action None            # 【關鍵】設定為 None 就會變成不可點擊的純文字狀態
                                    text_color "#b3b3b3"   # 給予淺灰色，暗示玩家當前空間沒有這個東西
                                    text_size (max(gui.nvl_text_size, 30))
        vbar value YScrollValue("words_vp"):
            xpos 390#(1735, 140)
            ypos 5
            xsize 50
            ysize 720
                            
            # 設定滾動條的外觀
            # base_bar Solid("#ffffff33")  # (可選) 滾動條底槽的顏色
            thumb Solid("#000000f1") 

    # =================【 下方長條：組合預覽區 】=================
    frame: 
        pos (280, 906)
        xsize 176 ysize 78 background None
        text current_subject color "#000000" align (0.5, 0.5) size gui.nvl_text_size bold True
            
    frame:
        pos (531, 906)
        xsize 174 ysize 78 background None
        if current_verb:
            text current_verb color "#2b579a" align (0.5, 0.5) size gui.nvl_text_size bold True
        else:
            text "動詞" color "#aaa" align (0.5, 0.5) size gui.nvl_text_size 
                
    frame:
        pos (760, 906)
        xsize 540 ysize 78 background None
        if current_noun:
            text current_noun color "#e06666" align (0.5, 0.5) size gui.nvl_text_size bold True
        else:
            text "名詞/地點" color "#aaa" align (0.5, 0.5) size gui.nvl_text_size 

    # =================【 右下角：功能按鈕點擊區 】=================
    if current_subject and current_verb and current_noun:
        textbutton "執行":
            pos (1328, 906)
            xsize 211 ysize 78
            action Return("execute")
            text_color "#000000" 
            text_size gui.nvl_text_size 
            text_bold True 
            text_xalign 0.5
            text_yalign 0.5
    else:
        textbutton "執行":
            pos (1328, 906)
            xsize 211 ysize 78
            action None
            text_color "#ffffff66" 
            text_size gui.nvl_text_size 
            text_xalign 0.5 
            text_yalign 0.5

    textbutton "重設":
        pos (1587, 906)
        xsize 211 ysize 78
        action [SetVariable("current_verb", None), SetVariable("current_noun", None)]
        text_color "#000000" 
        text_size gui.nvl_text_size 
        text_bold True 
        text_xalign 0.5 
        text_yalign 0.5
    use quick_menu

# =================【 圖片放大彈出視窗 】=================
screen image_popup_viewer(img_path):
    zorder 100    # 確保在最上層
    modal True    # 阻擋玩家點擊背後的按鈕
    
    # 用一個佔滿全螢幕的隱形按鈕當作背景，點擊任何地方就會關閉放大圖
    button:
        action Hide("image_popup_viewer")
        background Solid("#000000cc") # 半透明黑底，讓視覺聚焦在圖片上
        xfill True
        yfill True
        
    # 在畫面正中央顯示完整圖片
    add img_path:
        align (0.5, 0.5)
# =================【 輸入視窗 】=================
screen popup_input(prompt):
    default current_text = ""

    # 確保玩家不能點擊背景
    modal True 
    
    # 半透明黑色背景 
    add "#00000080" 

    # 彈出視窗框架
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400 
        padding (30, 30)

        vbox:
            xalign 0.5
            spacing 20

            # 顯示提示文字
            text prompt:
                xalign 0.5
                text_align 0.5

            # 顯示剩餘機會
            text "剩餘機會：[3-lock_errors]":
                xalign 0.5
                color "#ffaaaa" 
                size 22

            # 輸入框
            input:
                id "input"
                xalign 0.5
                length 20 
                # 【修改】將輸入框的值綁定到 current_text 變數
                value ScreenVariableInputValue("current_text")

            # 【新增】使用 hbox 將按鈕水平排列
            hbox:
                xalign 0.5
                spacing 40 # 兩個按鈕之間的距離

                # 確認按鈕
                textbutton "確認":
                    # 按下後，回傳目前綁定的文字變數
                    action Return(current_text) 
                
                # 取消按鈕
                textbutton "取消":
                    action Jump("puzzle_main_loop") # 按下後回傳 None 代表取消

screen popup_input_nvl(prompt):
    zorder 100
    default current_text = ""

    # 確保玩家不能點擊背景
    modal True 
    
    # 半透明黑色背景 
    add "#00000080" 

    # 彈出視窗框架
    frame:
        xalign 0.5
        yalign 0.5
        xsize 450 
        padding (30, 30)

        vbox:
            xalign 0.5
            spacing 20

            # 顯示提示文字
            text prompt:
                xalign 0.5
                text_align 0.5

            # 輸入框
            input:
                id "input"
                xalign 0.5
                length 20 
                # 【修改】將輸入框的值綁定到 current_text 變數
                value ScreenVariableInputValue("current_text")

            hbox:
                xalign 0.5
                spacing 40 # 兩個按鈕之間的距離

                # 確認按鈕
                textbutton "確認":
                    # 按下後，回傳目前綁定的文字變數
                    action Return(current_text) 