# 圧力計リーダー

このプロジェクトは、圧力計の画像から圧力値を読み取るためのものです。画像処理と解析はPythonとOpenCVを使用して行われます。

## アルゴリズム
画像入力→グレースケール→ぼかし処理→メーターの円と中心座標取得→メーターの0を取得→針の座標取得→角度計算→メーター値出力

## プロジェクト構成
仮想環境名　`wrs`

### 仮想環境の構築
```sh
python3 -m venv wrs
source wrs/bin/activate
pip install -r requirements.txt
```

2回目以降は`source wrs/bin/activate`のみで実行で良い

### 実行コマンド
```sh
python src/main.py
```

## ファイルとディレクトリの説明

### `data/`

- `raw/`: 生の画像データを保存します。
  - `example_meter.jpg`: 圧力計のサンプル画像。

- `processed/`: 前処理された画像データを保存します。
  - `processed_meter.jpg`: 前処理後の画像。

- `output/`: 処理結果を保存します。
  - `results.txt`: 画像から計算された圧力値を含むテキストファイル。

### `src/`

- `__init__.py`: ディレクトリがPythonパッケージであることを示します。
  
- `main.py`: メインスクリプト。他のモジュールから関数を呼び出して、画像の前処理、針の検出、角度の計算、そして圧力値の計算を実行します。

- `image_processing.py`: 画像の前処理に関連する関数を定義します。例えば、グレースケール変換やぼかし処理など。

- `needle_detection.py`: 圧力計の針を画像内で検出するための関数を定義します。

- `angle_calculation.py`: 針の位置に基づいて角度を計算するための関数を定義します。

- `pressure_calculation.py`: 角度から圧力値を計算するための関数を定義します。

### `tests/`

- `__init__.py`: ディレクトリがPythonパッケージであることを示します。

- `test_image_processing.py`: `image_processing.py`の関数に対するテストを含みます。

- `test_needle_detection.py`: `needle_detection.py`の関数に対するテストを含みます。

- `test_angle_calculation.py`: `angle_calculation.py`の関数に対するテストを含みます。

- `test_pressure_calculation.py`: `pressure_calculation.py`の関数に対するテストを含みます。

### `requirements.txt`

プロジェクトに必要なPythonライブラリのリストを含みます。以下のコマンドでインストールします：

```bash
pip install -r requirements.txt
```