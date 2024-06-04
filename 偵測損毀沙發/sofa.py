from transformers import pipeline
from PIL import Image
from google.colab import files

def describe_image(image_path, keywords):
    # 加載圖像到文本模型
    image_to_text = pipeline("image-to-text")

    # 打開並讀取圖像文件
    with Image.open(image_path) as img:
        # 使用模型描述圖像内容
        result = image_to_text(img)

    # 打印结果以查看键的結構
    print("模型返回的结果:", result)

    # 提取圖像描述
    description = result[0].get('generated_text', '未找到描述')

    # 檢查關键字
    for keyword in keywords:
        if keyword in description.lower():
            return False

    return True

# 上傳圖像文件
uploaded = files.upload()

# 獲取上傳文件的路徑
image_path = list(uploaded.keys())[0]

# 定義關键字列表
keywords = ["broken", "damaged", "torn", "worn", "ruined", "shabby", "tattered", "destroyed"]

# 描述圖像内容並檢查是否有破損的痕跡等
is_broken_sofa = describe_image(image_path, keywords)
if is_broken_sofa:
    print("這張圖片内容是壞掉的沙發")
else:
    print("這張圖片内容不是壞掉的沙發")

def start():
  if is_broken_sofa == 1:
    turn_12_on()
    storeFallData()
  else:
    turn_12_off()