import machine

# 사용할 핀 번호 입력
PIN_VMOT = 23

def motor():
    return machine.Pin(PIN_VMOT, machine.Pin.OUT)