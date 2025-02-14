import os
import random
import shutil

# 定义数据集文件夹路径
data_folder = ""

# 定义训练集和测试集的路径
train_folder = ""
test_folder = ""

# 定义数据划分比例
train_ratio =   # 训练集比例
test_ratio =   # 测试集比例

# 获取数据文件夹中的所有文件
data_files = [file for file in os.listdir(data_folder) if file.endswith(('.jpg', '.png', '.jpeg'))]

# 打乱文件列表顺序
random.shuffle(data_files)

# 划分训练集和测试集的文件数量
train_split_index = int(len(data_files) * train_ratio)

# 划分数据集
train_files = data_files[:train_split_index]
test_files = data_files[train_split_index:]

# 创建训练集和测试集文件夹（如果不存在）
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# 将训练集文件复制到指定目录
for file in train_files:
    source_file = os.path.join(data_folder, file)
    destination_file = os.path.join(train_folder, file)
    shutil.copy(source_file, destination_file)

# 将测试集文件复制到指定目录
for file in test_files:
    source_file = os.path.join(data_folder, file)
    destination_file = os.path.join(test_folder, file)
    shutil.copy(source_file, destination_file)


