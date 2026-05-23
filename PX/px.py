from PIL import Image


def scale_pixel_art(input_path, output_path):
    # 讀取 1024x576 的圖片
    img = Image.open(input_path)
    
    # 目標尺寸 1920x1080
    target_width = 1920
    target_height = 1080
    
    # 關鍵：繼續使用 NEAREST，保持邊緣銳利，不產生模糊漸層
    scaled_img = img.resize((target_width, target_height), Image.Resampling.NEAREST)
    
    # 儲存圖片
    scaled_img.save(output_path, format="PNG")
    print(f"成功！已輸出 1920x1080 的圖片：{output_path}")

# ==========================================
# 執行範例
# ==========================================
if __name__ == "__main__":
    # 替換成你實際的檔案路徑
    input_file = "cave_bg.png" 
    output_file = "cave_bg.png"
    
    scale_pixel_art(input_file, output_file)
