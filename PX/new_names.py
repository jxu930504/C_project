import os
import shutil

# ================= 參數設定區 =================
source_dir = "D:\\大四\\程設二\\專題\\UI"  # 原始圖片所在資料夾 (請修改為您的路徑)
txt_file = "new_names.txt"      # 包含新檔名的文字檔路徑 (請修改為您的路徑)
output_dir = "D:\\大四\\程設二\\專題\\C2\\game\\gui"  # 存放重新命名後圖片的指定路徑 (請修改為您的路徑)

# ==============================================

def rename_and_copy_images():
    file_start = 1
    file_end = 27

    prompt = f"Start-End numbers ({file_start}-{file_end}): "
    user_input = input(prompt)
    start_num, end_num = map(int, user_input.split())
    
    # 1. 如果目標資料夾不存在，則自動建立
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"已建立目標資料夾: {output_dir}")

    # 2. 讀取文字檔中的新檔名
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            # 讀取每一行，並去除前後的空白與換行符號，排除空行
            new_names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"錯誤：找不到文字檔 '{txt_file}'")
        return

    # 檢查新檔名數量是否足夠
    if len(new_names) < end_num:
        print(f"警告：文字檔中的檔名數量不足 {file_num} 個 (目前有 {len(new_names)} 個)。")

    # 3. 開始依序處理 1.png 到 16.png
    for i in range(start_num, end_num+1):
        old_filename = f"投影片{i}.png"
        old_filepath = os.path.join(source_dir, old_filename)

        # 確認文字檔中還有對應的新檔名可以使用
        if i - 1 < len(new_names):
            new_filename = new_names[i - 1]
            
            # 確保新檔名帶有 .png 副檔名
            if not new_filename.lower().endswith('.png'):
                new_filename += '.png'
                
            new_filepath = os.path.join(output_dir, new_filename)

            # 確認原始檔案確實存在
            if os.path.exists(old_filepath):
                try:
                    # 使用 shutil.copy2 複製檔案 (會保留原檔案的建立時間等 metadata)
                    # 如果你想直接「移動」檔案而不是複製，請把下面這行改成 shutil.move(old_filepath, new_filepath)
                    shutil.copy2(old_filepath, new_filepath)
                    print(f"成功: {old_filename} -> {new_filename}")
                except Exception as e:
                    print(f"發生錯誤: 無法處理 {old_filename}，原因: {e}")
            else:
                print(f"找不到原始檔案: {old_filepath}")
        else:
            print(f"跳過 {old_filename}: 文字檔中沒有提供第 {i} 個新檔名。")

    print("\n🎉 所有檔案處理完成！")

# 執行主程式
if __name__ == "__main__":
    rename_and_copy_images()
