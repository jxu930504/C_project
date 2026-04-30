#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 移除字串尾端的換行符號 (\n 或 \r)
void strip_newline(char *str) {
    int len = strlen(str);
    while (len > 0 && (str[len - 1] == '\n' || str[len - 1] == '\r')) {
        str[len - 1] = '\0';
        len--;
    }
}

int main() {
    // 設定輸入與輸出的檔案名稱
    const char *input_filename = "input.txt";
    const char *output_filename = "output.rpy";

    FILE *fin = fopen(input_filename, "r");
    FILE *fout = fopen(output_filename, "w");

    // 檢查檔案是否成功開啟
    if (fin == NULL) {
        printf("錯誤：無法開啟輸入檔案 '%s'，請確認檔案是否存在於同一目錄下。\n", input_filename);
        return 1;
    }
    if (fout == NULL) {
        printf("錯誤：無法建立輸出檔案 '%s'。\n", output_filename);
        fclose(fin);
        return 1;
    }

    char buffer[1024], Character[20]="nvl_narrator";; // nvl_dark

    // 逐行讀取檔案
    while (fgets(buffer, sizeof(buffer), fin) != NULL) {
        strip_newline(buffer);

        // 如果該行有文字，則套用 nvl_narrator 格式
        if (strlen(buffer) > 0) {
            fprintf(fout, "%s \"%s\"\n", Character, buffer);
        } else {
            // 如果是空行，則直接在腳本中保留空行以增加可讀性
            fprintf(fout, "\n");
        }
    }

    printf("轉換成功！請查看 '%s' 檔案。\n", output_filename);

    // 關閉檔案
    fclose(fin);
    fclose(fout);

    return 0;
}
