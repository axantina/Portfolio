# Embedded IoT Smart Greenhouse

Arduino-based smart greenhouse system using a soil moisture sensor, LDR sensor, LCD I2C, keypad, relay, LED, and water pump control.

This is an academic embedded systems project developed during university coursework.

---

## English

## Project Overview

This project is a simple smart greenhouse automation system using Arduino.  
The system reads environmental sensor data and automatically controls a water pump and LED lighting based on soil moisture and light intensity.

The project uses:
- Soil moisture sensor to detect soil condition
- LDR sensor to detect light intensity
- LCD I2C to display sensor values
- Keypad to select displayed sensor data
- Relay module to control a water pump
- LED lighting controlled by light condition

## Features

- Reads soil moisture sensor values
- Reads LDR light sensor values
- Displays selected sensor data on LCD I2C
- Controls water pump using relay based on soil moisture level
- Controls LED lighting based on surrounding light intensity
- Uses keypad input to switch displayed sensor values

## Hardware Components

| Component | Description |
|---|---|
| Arduino Uno | Main microcontroller |
| Soil Moisture Sensor | Detects soil moisture level |
| LDR Sensor | Detects surrounding light intensity |
| LCD I2C 16x2 | Displays sensor values |
| 4x4 Keypad | Selects displayed sensor data |
| Relay Module | Controls water pump |
| Water Pump | Waters the plant/greenhouse |
| LED | Provides lighting when the environment is dark |
| Jumper Wires | Circuit connection |
| Resistors | Supporting circuit components |

## Pin Configuration

| Component | Arduino Pin |
|---|---|
| LDR Sensor | A2 |
| Soil Moisture Sensor | A1 |
| LED 1 | 10 |
| LED 2 | 11 |
| Relay / Water Pump | 13 |
| Keypad Rows | 5, 4, 3, 2 |
| Keypad Columns | 9, 8, 7, 6 |
| LCD I2C | SDA/SCL |

## System Logic

- Press key `1` to display the soil moisture sensor value on the LCD.
- Press key `3` to display the LDR sensor value on the LCD.
- If the soil moisture value is above `700`, the relay activates the water pump.
- If the soil moisture value is less than or equal to `700`, the water pump turns off.
- If the LDR value is below `300`, the LED lighting turns on.
- If the LDR value is `300` or above, the LED lighting turns off.

## Project Structure

```text
embedded-iot-smart-greenhouse/
├── README.md
├── src/
│   └── smart_greenhouse.ino
├── docs/
│   └── explanation.md
└── assets/
    ├── circuit-diagram.png
    └── flowchart.png
```

## Required Libraries

This project uses the following Arduino libraries:

- Keypad
- Wire
- LiquidCrystal_I2C

`Wire` is usually included by default in the Arduino IDE.  
`Keypad` and `LiquidCrystal_I2C` may need to be installed through the Arduino Library Manager.

## How to Run

1. Open Arduino IDE.
2. Install the required libraries.
3. Open `src/smart_greenhouse.ino`.
4. Connect the hardware components according to the pin configuration.
5. Upload the code to Arduino Uno.
6. Open Serial Monitor to check sensor values.
7. Use keypad input to display selected sensor values on LCD.

## Skills Demonstrated

- Arduino programming
- Analog sensor reading
- Keypad input handling
- LCD I2C display
- Relay control
- LED control
- Sensor-based automation
- Embedded system logic
- Basic control system design
- Technical documentation

## Notes

This project was originally created as an academic project.  
The repository has been reorganized and documented as part of my technical portfolio for embedded systems and IoT-related roles.

---

# 組込みIoT スマート温室システム

Arduinoを使用したスマート温室システムです。  
土壌水分センサー、LDRセンサー、LCD I2C、キーパッド、リレー、LED、ウォーターポンプを使用し、簡単な自動制御を行います。

このプロジェクトは、大学時代の授業・課題で作成した組込みシステム関連の学習プロジェクトです。

---

## 日本語

## プロジェクト概要

このプロジェクトは、Arduinoを使用した簡易スマート温室自動制御システムです。  
土壌水分や周囲の明るさをセンサーで読み取り、その値に応じてウォーターポンプやLED照明を自動制御します。

使用している主な機能は以下の通りです。

- 土壌水分センサーによる土の状態の検出
- LDRセンサーによる明るさの検出
- LCD I2Cによるセンサー値の表示
- キーパッドによる表示内容の切り替え
- リレーによるウォーターポンプ制御
- 明るさに応じたLED照明制御

## 機能

- 土壌水分センサーの値を取得
- LDRセンサーで明るさを検出
- 選択したセンサー値をLCD I2Cに表示
- 土壌水分の状態に応じてリレー経由でウォーターポンプを制御
- 周囲の明るさに応じてLED照明を制御
- キーパッド入力により表示するセンサー値を切り替え

## 使用部品

| 部品 | 説明 |
|---|---|
| Arduino Uno | メインマイコン |
| 土壌水分センサー | 土の水分状態を検出 |
| LDRセンサー | 周囲の明るさを検出 |
| LCD I2C 16x2 | センサー値を表示 |
| 4x4 キーパッド | 表示するセンサー値を選択 |
| リレーモジュール | ウォーターポンプを制御 |
| ウォーターポンプ | 水やりを行う |
| LED | 暗い場合に点灯 |
| ジャンパーワイヤー | 回路接続 |
| 抵抗 | 補助部品 |

## ピン設定

| 部品 | Arduinoピン |
|---|---|
| LDRセンサー | A2 |
| 土壌水分センサー | A1 |
| LED 1 | 10 |
| LED 2 | 11 |
| リレー / ウォーターポンプ | 13 |
| キーパッド 行 | 5, 4, 3, 2 |
| キーパッド 列 | 9, 8, 7, 6 |
| LCD I2C | SDA/SCL |

## 制御ロジック

- キー `1` を押すと、土壌水分センサーの値をLCDに表示します。
- キー `3` を押すと、LDRセンサーの値をLCDに表示します。
- 土壌水分の値が `700` を超えると、リレーが作動してウォーターポンプを動かします。
- 土壌水分の値が `700` 以下の場合、ウォーターポンプを停止します。
- LDRの値が `300` 未満の場合、LED照明を点灯します。
- LDRの値が `300` 以上の場合、LED照明を消灯します。

## フォルダ構成

```text
embedded-iot-smart-greenhouse/
├── README.md
├── src/
│   └── smart_greenhouse.ino
├── docs/
│   └── explanation.md
└── assets/
    ├── circuit-diagram.png
    └── flowchart.png
```

## 必要なライブラリ

このプロジェクトでは、以下のArduinoライブラリを使用しています。

- Keypad
- Wire
- LiquidCrystal_I2C

`Wire` は通常Arduino IDEに標準で含まれています。  
`Keypad` と `LiquidCrystal_I2C` は、Arduino IDEのライブラリマネージャから追加する必要がある場合があります。

## 実行方法

1. Arduino IDEを開きます。
2. 必要なライブラリをインストールします。
3. `src/smart_greenhouse.ino` を開きます。
4. ピン設定に従って部品を接続します。
5. Arduino Unoにコードを書き込みます。
6. シリアルモニタでセンサー値を確認します。
7. キーパッドを使用して、LCDに表示するセンサー値を切り替えます。

## アピールできるスキル

- Arduinoプログラミング
- アナログセンサーの読み取り
- キーパッド入力処理
- LCD I2C表示
- リレー制御
- LED制御
- センサーを用いた自動制御
- 組込みシステムの基本ロジック
- 基本的な制御システム設計
- 技術ドキュメント作成

## 補足

このプロジェクトは、大学時代に作成した学習目的のプロジェクトです。  
現在は、組込みシステム・IoT関連の技術ポートフォリオとして、コードとドキュメントを整理しています。
