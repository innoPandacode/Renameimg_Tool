import os

# 目標資料夾路徑
destination_dir = r'C:\Users\DQE\Desktop\testautobot\findaida64\用來訓練\20230823_DataBase'

def rename_jpg_files(folder_path):
    # 獲取目錄中的檔案列表並進行排序
    file_list = os.listdir(folder_path)
    file_list.sort()

    # 索引計數，用於生成新的檔案名稱
    index = 1
    for filename in file_list:
        if filename.lower().endswith('.jpg'):
            # 獲取檔案副檔名
            _, file_extension = os.path.splitext(filename)

            # 檢查檔案名是否以4位數字和底線開頭
            if filename[:5].replace('_', '').isdigit():
                # 將現有的五位數字和底線替換為索引值和底線
                new_filename = f'{index:04d}_{filename[6:]}'
            else:
                # 在檔案名前添加4位索引和底線
                new_filename = f'{index:04d}_{filename}'

            # 構建完整的檔案路徑
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            # 重新命名檔案
            os.rename(old_path, new_path)

            # 增加索引計數
            index += 1

    print(f'{folder_path} 目錄中的檔案已成功重新命名。')

# 遍歷目標資料夾中的所有子目錄
for root, _, _ in os.walk(destination_dir):
    rename_jpg_files(root)
