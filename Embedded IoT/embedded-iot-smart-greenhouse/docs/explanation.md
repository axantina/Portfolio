# Project Explanation

## English

## 1. Project Overview

This project is an Arduino-based automatic greenhouse system developed as an academic embedded systems project.

The system uses an Arduino Uno as the main microcontroller to control input and output devices. The main input sensors are a soil moisture sensor and an LDR sensor. Based on the sensor readings, the system controls a water pump through a relay and turns LED lighting on or off.

The purpose of this project is to demonstrate a basic embedded automation system using analog sensors, actuator control, and simple decision-making logic.

---

## 2. Hardware Components

The circuit consists of the following components:

| Component | Quantity / Specification | Function |
|---|---:|---|
| Arduino Uno | 1 | Main microcontroller |
| Soil moisture sensor | 1 | Measures soil moisture level |
| LDR sensor | 1 | Detects light intensity |
| LED | 2 | Provides lighting when the environment is dark |
| Water pump | 6V | Waters the greenhouse/plant automatically |
| LCD I2C | 1 | Displays sensor values |
| Resistor | 220 Ohm × 3 | Supporting components for the circuit |
| Keypad | 1 | Selects which sensor value is shown on the LCD |
| Battery clip | 2 | Power connection for external components |
| Relay | 5V | Controls the water pump |
| Jumper wires | As needed | Circuit connections |

---

## 3. Pin Configuration

| Arduino Pin | Connected Component |
|---|---|
| A1 | Soil moisture sensor input |
| A2 | LDR sensor input |
| A4 / A5 | LCD I2C |
| 2, 3, 4, 5, 6, 7, 8, 9 | Keypad |
| 10, 11 | LED output |
| 13 | Relay and water pump control |

---

## 4. Soil Moisture Sensor Logic

The soil moisture sensor is used to measure the moisture level of the soil in the greenhouse.  
The sensor value determines whether the relay and water pump should be turned on or off.

The sensor provides an analog input value between `0` and `1023`.

### Condition

| Sensor Value | Soil Condition | Relay / Water Pump |
|---:|---|---|
| `<= 700` | Moist / high moisture | Water pump OFF |
| `> 700` | Dry / low moisture | Water pump ON |

If the soil moisture value is `700` or lower, the soil is considered moist enough, so the relay turns off the water pump.

If the soil moisture value is higher than `700`, the soil is considered dry, so the relay activates the water pump. The water pump will turn off again when the soil moisture value returns to `700` or lower.

### Voltage Interpretation

The soil moisture sensor uses 5V input and produces an analog value from `0` to `1023`.

If the sensor value is `700`, the approximate input voltage is:

`700 / 1024 × 5V = 3.4V`

This means:

- Input voltage below approximately `3.4V` indicates high soil moisture.
- Input voltage above approximately `3.4V` indicates low soil moisture or dry soil.

---

## 5. LDR Sensor Logic

The LDR sensor is used to detect the light condition inside the greenhouse.  
It helps determine whether the LED lighting should be turned on or off.

The sensor provides an analog input value between `0` and `1023`.

### Condition

| Sensor Value | Light Condition | LED |
|---:|---|---|
| `< 300` | Dark / night condition | LED ON |
| `>= 300` | Bright / daytime condition | LED OFF |

If the LDR value is below `300`, the environment is considered dark, so the Arduino sends a HIGH signal to pins `10` and `11` to turn on the LEDs.

If the LDR value is `300` or higher, the environment is considered bright, so the Arduino sends a LOW signal to pins `10` and `11` to turn off the LEDs.

### Voltage Interpretation

The LDR sensor uses 5V input and produces an analog value from `0` to `1023`.

If the sensor value is `300`, the approximate input voltage is:

`300 / 1024 × 5V = 1.4V`

This means:

- Input voltage below approximately `1.4V` indicates a dark condition.
- Input voltage above approximately `1.4V` indicates a bright condition.

---

## 6. LCD and Keypad Function

The LCD I2C is used to display sensor values.

The keypad is used to select which sensor value appears on the LCD.

| Keypad Input | LCD Display |
|---|---|
| `1` | Soil moisture sensor value |
| `3` | LDR sensor value |

When key `1` is pressed, the LCD displays the soil moisture sensor value.  
When key `3` is pressed, the LCD displays the LDR sensor value.

---

## 7. System Workflow

1. Arduino reads the soil moisture sensor value from pin `A1`.
2. Arduino reads the LDR sensor value from pin `A2`.
3. The user can press the keypad to display selected sensor data on the LCD.
4. If key `1` is pressed, the soil moisture value is displayed.
5. If key `3` is pressed, the LDR value is displayed.
6. If the soil moisture value is above `700`, the relay activates the water pump.
7. If the soil moisture value is `700` or lower, the water pump turns off.
8. If the LDR value is below `300`, the LEDs turn on.
9. If the LDR value is `300` or higher, the LEDs turn off.
10. The system continuously repeats this process.

---

## 8. Skills Demonstrated

This project demonstrates the following skills:

- Arduino programming
- Analog sensor reading
- Soil moisture sensor usage
- LDR sensor usage
- Relay control
- Water pump control
- LED output control
- LCD I2C display
- Keypad input handling
- Basic embedded system logic
- Sensor-based automation
- Technical documentation

---

## 9. Notes

This project was originally created as a university coursework project.  
The documentation and source code have been reorganized as part of a technical portfolio for embedded systems and IoT-related roles.

---

# プロジェクト説明

## 日本語

## 1. プロジェクト概要

このプロジェクトは、大学時代の授業・課題で作成したArduinoベースの自動温室システムです。

Arduino Unoをメインマイコンとして使用し、入力センサーと出力機器を制御します。主な入力センサーは土壌水分センサーとLDRセンサーです。センサーの値に応じて、リレーを通してウォーターポンプを制御し、LED照明の点灯・消灯を行います。

このプロジェクトの目的は、アナログセンサー、アクチュエータ制御、簡単な条件分岐ロジックを使った基本的な組込み自動制御システムを示すことです。

---

## 2. 使用部品

回路は以下の部品で構成されています。

| 部品 | 数量・仕様 | 役割 |
|---|---:|---|
| Arduino Uno | 1 | メインマイコン |
| 土壌水分センサー | 1 | 土の水分状態を測定 |
| LDRセンサー | 1 | 明るさを検出 |
| LED | 2 | 暗い場合に照明として点灯 |
| ウォーターポンプ | 6V | 温室・植物への自動給水 |
| LCD I2C | 1 | センサー値を表示 |
| 抵抗 | 220Ω × 3 | 回路補助部品 |
| キーパッド | 1 | LCDに表示するセンサー値を選択 |
| バッテリークリップ | 2 | 外部電源接続 |
| リレー | 5V | ウォーターポンプを制御 |
| ジャンパーワイヤー | 必要数 | 回路接続 |

---

## 3. ピン設定

| Arduinoピン | 接続部品 |
|---|---|
| A1 | 土壌水分センサー入力 |
| A2 | LDRセンサー入力 |
| A4 / A5 | LCD I2C |
| 2, 3, 4, 5, 6, 7, 8, 9 | キーパッド |
| 10, 11 | LED出力 |
| 13 | リレー・ウォーターポンプ制御 |

---

## 4. 土壌水分センサーの制御ロジック

土壌水分センサーは、温室内の土の水分状態を測定するために使用します。  
センサーの値によって、リレーとウォーターポンプのON/OFFを制御します。

センサーは `0` から `1023` のアナログ値を出力します。

### 条件

| センサー値 | 土の状態 | リレー / ウォーターポンプ |
|---:|---|---|
| `<= 700` | 湿っている / 水分が多い | ウォーターポンプ OFF |
| `> 700` | 乾いている / 水分が少ない | ウォーターポンプ ON |

土壌水分センサーの値が `700` 以下の場合、土は十分に湿っていると判断し、ウォーターポンプを停止します。

土壌水分センサーの値が `700` を超えた場合、土が乾いていると判断し、リレーを作動させてウォーターポンプを動かします。土壌水分の値が再び `700` 以下になると、ウォーターポンプを停止します。

### 電圧の考え方

土壌水分センサーは5Vで動作し、`0` から `1023` のアナログ値を出力します。

センサー値が `700` の場合、入力電圧の目安は以下の通りです。

`700 / 1024 × 5V = 3.4V`

つまり、

- 入力電圧が約 `3.4V` 未満の場合、土壌水分が高い状態
- 入力電圧が約 `3.4V` を超える場合、土壌水分が低い、または乾燥している状態

と判断します。

---

## 5. LDRセンサーの制御ロジック

LDRセンサーは、温室内の明るさを検出するために使用します。  
この値に応じて、LED照明を点灯または消灯します。

センサーは `0` から `1023` のアナログ値を出力します。

### 条件

| センサー値 | 明るさの状態 | LED |
|---:|---|---|
| `< 300` | 暗い / 夜間 | LED ON |
| `>= 300` | 明るい / 昼間 | LED OFF |

LDRセンサーの値が `300` 未満の場合、周囲が暗いと判断し、Arduinoがピン `10` と `11` にHIGH信号を出力してLEDを点灯します。

LDRセンサーの値が `300` 以上の場合、周囲が明るいと判断し、Arduinoがピン `10` と `11` にLOW信号を出力してLEDを消灯します。

### 電圧の考え方

LDRセンサーは5Vで動作し、`0` から `1023` のアナログ値を出力します。

センサー値が `300` の場合、入力電圧の目安は以下の通りです。

`300 / 1024 × 5V = 1.4V`

つまり、

- 入力電圧が約 `1.4V` 未満の場合、暗い状態
- 入力電圧が約 `1.4V` を超える場合、明るい状態

と判断します。

---

## 6. LCDとキーパッドの機能

LCD I2Cはセンサー値を表示するために使用します。

キーパッドは、LCDに表示するセンサー値を選択するために使用します。

| キーパッド入力 | LCD表示 |
|---|---|
| `1` | 土壌水分センサーの値 |
| `3` | LDRセンサーの値 |

キー `1` を押すと、LCDに土壌水分センサーの値を表示します。  
キー `3` を押すと、LCDにLDRセンサーの値を表示します。

---

## 7. システムの流れ

1. Arduinoがピン `A1` から土壌水分センサーの値を読み取ります。
2. Arduinoがピン `A2` からLDRセンサーの値を読み取ります。
3. ユーザーはキーパッドを押して、LCDに表示するセンサー値を選択できます。
4. キー `1` が押された場合、土壌水分センサーの値を表示します。
5. キー `3` が押された場合、LDRセンサーの値を表示します。
6. 土壌水分の値が `700` を超えた場合、リレーが作動してウォーターポンプを動かします。
7. 土壌水分の値が `700` 以下の場合、ウォーターポンプを停止します。
8. LDRの値が `300` 未満の場合、LEDを点灯します。
9. LDRの値が `300` 以上の場合、LEDを消灯します。
10. システムはこの処理を繰り返します。

---

## 8. アピールできるスキル

このプロジェクトでは、以下のスキルを示しています。

- Arduinoプログラミング
- アナログセンサーの読み取り
- 土壌水分センサーの使用
- LDRセンサーの使用
- リレー制御
- ウォーターポンプ制御
- LED出力制御
- LCD I2C表示
- キーパッド入力処理
- 組込みシステムの基本ロジック
- センサーを用いた自動制御
- 技術ドキュメント作成

---

## 9. 補足

このプロジェクトは、大学時代に作成した学習目的のプロジェクトです。  
現在は、組込みシステム・IoT関連の技術ポートフォリオとして、ドキュメントとソースコードを整理しています。
