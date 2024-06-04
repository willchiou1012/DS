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
            return True

    return False

# 上傳圖像文件
uploaded = files.upload()

# 獲取上傳文件的路徑
image_path = list(uploaded.keys())[0]

# 定義關鍵字列表
keywords = ["ball", "sphere", "basketball", "football", "soccer ball", "tennis ball", "volleyball", "baseball"]

# 描述圖像内容並檢查是否包含球
is_ball_in_image = describe_image(image_path, keywords)
if is_ball_in_image:
    print("這張圖片内容包含球")
else:
    print("這張圖片内容不包含球")

def start():
    if is_ball_in_image == 1:
        turn_13_on()
        storeFallData()
    else:
        turn_13_off()