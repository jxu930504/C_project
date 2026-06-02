from PIL import Image


def scale_pixel_art(input_path, output_path, target_width=1920, target_height=1080):
    # 讀取 1024x576 的圖片
    img = Image.open(input_path)
    
    # 關鍵：繼續使用 NEAREST，保持邊緣銳利，不產生模糊漸層
    scaled_img = img.resize((target_width, target_height), Image.Resampling.NEAREST)
    
    # 儲存圖片
    scaled_img.save(output_path, format="PNG")
    print(f"成功！已輸出 {target_width}x{target_height} 的圖片：{output_path}")

# ==========================================
# 執行範例
# ==========================================
if __name__ == "__main__":
    # 替換成你實際的檔案路徑
    input_file = "cave_bg.png" 
    output_file = "cave_bg.png"
    
    scale_pixel_art("avatar_player_cat.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_player_cat.png",510,565)
    scale_pixel_art("avatar_player_dog.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_player_dog.png",510,565)
    """
    scale_pixel_art("avatar_aojin.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_aojin.png",510,565)
    scale_pixel_art("avatar_buerjin.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_buerjin.png",510,565)
    scale_pixel_art("avatar_laza.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_laza.png",510,565)
    scale_pixel_art("avatar_woning.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_woning.png",510,565)
    scale_pixel_art("unlock_fabu.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\unlock_fabu.png",510,565)
    scale_pixel_art("avatar_levin.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_levin.png",510,565)
    scale_pixel_art("avatar_locked.png" , "D:\\大四\\程設二\\專題\\C2\\game\\gui\\avatar_locked.png",510,565)
    
    
    
    scale_pixel_art("拉扎.png" , "拉扎_small.png",256,256)
    scale_pixel_art("奧金.png" , "奧金_small.png",256,256)
    scale_pixel_art("布爾金.png" , "布爾金_small.png",256,256)
    scale_pixel_art("列文.png" , "列文_small.png",256,256)
    scale_pixel_art("合照改改.png" , "合照_small.png",256,240)
    scale_pixel_art("沃寧.png" , "沃寧_small.png",256,256)
    scale_pixel_art("法布.png" , "法布_small.png",256,256)
    
    "D:\大四\程設二\專題\PX\奧金.png"
    "D:\大四\程設二\專題\PX\布爾金.png"
    "D:\大四\程設二\專題\PX\列文.png"
    "D:\大四\程設二\專題\PX\合照改改.png"
    "D:\大四\程設二\專題\PX\沃寧.png"
    "D:\大四\程設二\專題\PX\拉扎.png"
    "D:\大四\程設二\專題\PX\法布.png"
    """
