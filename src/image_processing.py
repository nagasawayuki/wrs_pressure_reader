import cv2


#画像を指定したファイルパスから読み込みます。
def load_image(filepath):
    image = cv2.imread(filepath)
    if image is None:
        raise FileNotFoundError(f"Image at path {filepath} not found.")
    return image


#画像の前処理を行います。グレースケール変換とぼかしを適用します。
def preprocess_image(image):
    '''
        グレースケール変換：形状認識は、輝度の変化に基づいて行われる。余計な色情報を省いたほうが早くて精度が上がる
        ぼかし：画像のノイズを低減し、重要なエッジを目立たせる
    '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred


