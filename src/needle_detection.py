import cv2
import numpy as np

#画像内の針の検出を行っている。ここで計算方法のチューニングを行う必要がある
"""
    入力：前処理した画像(グレースケール、ぼかし)
    出力: タプル型の、針の両端座標(x1, y1, x2, y2)→(x1,y1)と(x2,y2)を結ぶ直線を検出したって意味。
"""
def detect_needle(image):
    # エッジ検出
    edges = cv2.Canny(image, 50, 150)
    '''
    ヒステリシス手法
    cv2.Canny(image, threshold1, threshold2)
    image:入力画像
    threshold1:エッジ検出するピクセルの強度の最小値
    threshold2:エッジ検出するピクセルの強度の最大値
    '''
    
    # Hough変換を使用して直線を検出
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
    '''
    cv2.HoughLinesP(image, rho, theta, threshold, lines=None, minLineLength=0, maxLineGap=0)
    image:Cannyエッジ検出の結果
    rho:直線を検出する際の解像度(ピクセル単位)(通常は1ピクセル)
    theta:直線の傾きをどの程度細かく分割するか(np.pi / 180は1度)
    threshold:直線とみなすための最低値、これが大きいほど、強いエッジのみが直線と検出される
    lines:直線を保存するための出力配列(いじらなくていい)
    minLineLength:検出する直線の最小長さ
    minLineGap:直線が途中で切れていても一本とみなすピクセル値。設定した値以下の途切れは直線とみなす
    '''
    
    if lines is not None:
        # 最初の検出された線を返す
        for line in lines:
            x1, y1, x2, y2 = line[0]
            return (x1, y1, x2, y2)
    return None