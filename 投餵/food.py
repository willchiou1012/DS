from transformers import pipeline
from PIL import Image
from google.colab import files

def describe_image(image_path, keywords):
    # 加載圖像到文本模型
    image_to_text = pipeline("image-to-text")

    # 打開並讀取圖像文件
    with Image.open(image_path) as img:
        # 使用模型描述图像内容
        result = image_to_text(img)

    # 打印结果以查看鍵的結構
    print("模型返回的结果:", result)

    # 提取圖像描述
    description = result[0].get('generated_text', '未找到描述')

    # 檢查關鍵字
    for keyword in keywords:
        if keyword in description.lower():
            return False

    return True

# 上船圖片文件
uploaded = files.upload()

# 獲取上傳文件的路徑
image_path = list(uploaded.keys())[0]

# 定義關鍵字列表
keywords = ["food", "meal", "dish", "snack", "fruit", "vegetable", "nut", "drink", "fish"]

# 描述圖像内容並檢查是否包含空碗或食物等
is_unempty_bowl = describe_image(image_path, keywords)
if is_unempty_bowl:
    print("這張圖片內容是空碗")
else:
    print("這張圖片內容不是空碗")

def start():
  if is_unempty_bowl == 0:
    turn_11_off()
    storeFallData()
  else:
    turn_11_on()