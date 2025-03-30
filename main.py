"""
舵机与 esp32 引脚接线图, 数据口方向为后 (tail)

    前 (head)
        -----               -----
        |  2  |             |  3  |
        |pin25|             |Pin18|
        ----- -----   ----- -----
            |  0  | |  1  |
            |Pin12| |Pin16|
             -----   -----
            |  4  | |  5  |
            |Pin13| |Pin17|
        ----- -----   ----- -----
        |  6  |             |  7  |
        |Pin26|             |Pin19|
        -----               -----
    后 (tail)
"""

import bluetooth
import utime
from dabble import Dabble
from esp32ble import BLESimplePeripheral
from quad import Quad

robot = Quad()
robot.init(12, 16, 25, 18, 13, 17, 26, 19)
robot.setTrims(0, 0, 0, 0, 0, 0, 0, 0)



def on_rx(v):
    print("收到命令:", v)

    if v == Dabble.up:
        print("前进")
        robot.forward()
    elif v == Dabble.down:
        print("后退")
        robot.backward()
    elif v == Dabble.left:
        print("左转")
        robot.turn_L()
    elif v == Dabble.right:
        print("右转")
        robot.turn_R()

    elif v == Dabble.triangle:
        print("上下")
        robot.up_down()
    elif v == Dabble.square:
        print("舞蹈")
        robot.dance()
    elif v == Dabble.circle:
        print("月球漫步")
        robot.moonwalk_L()
    elif v == Dabble.cross:
        print("撤退")
        robot.front_back()

    elif v == Dabble.start:
        print("回到初始位置")
        robot.home()
    elif v == Dabble.select:
        print("隐藏")
        robot.hide()


ble = bluetooth.BLE()
p = BLESimplePeripheral(ble, "MpyEsp32")
p.on_write(on_rx)
print("四足机器人BLE控制已启动, 等待Dabble App连接...")

while True:
    utime.sleep(0.2)
