import cv2
import os
from image_processing import load_image, preprocess_image
from needle_detection import detect_needle
from angle_calculation import calculate_angle
from pressure_calculation import calculate_pressure

def main():
    # 画像の読み込み
    input_path = '../data/sample/sample_meter.jpg'
    image = load_image(input_path)

    # 画像の前処理
    preprocessed_image = preprocess_image(image)
    
    # 前処理済み画像を保存
    processed_path = '../data/processed/processed_meter.jpg'
    cv2.imwrite(processed_path, preprocessed_image)

    # 針の検出
    needle_angle = detect_needle(preprocessed_image)

    # 角度の計算
    angle = calculate_angle(needle_angle)

    # 圧力値の計算
    pressure_value = calculate_pressure(angle)

    # 結果を保存
    output_path = '../data/output/results.txt'
    with open(output_path, 'w') as f:
        f.write(f'Pressure Value: {pressure_value}\n')

    print(f'Pressure Value: {pressure_value}')
    print(f'Results saved to {output_path}')

if __name__ == "__main__":
    main()
