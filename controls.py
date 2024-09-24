import vgamepad as vg
import time

# some VARS
ax_min = -10
ax_max = 10
stick_min = -32768
stick_max = 32768

# Emulate XBox 360 gamepad
gamepad = vg.VX360Gamepad()

# press a button to wake the device up
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(0.5)
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(0.5)

# some vars
steering_turned = False


def gas_hold():
    gamepad.right_trigger(value=200)
    gamepad.update()


def gas_release():
    gamepad.right_trigger(value=0)
    gamepad.update()


def brake_hold():
    gamepad.left_trigger(value=150)
    gamepad.update()


def brake_release():
    gamepad.left_trigger(value=0)
    gamepad.update()


def control_steering(ax_y: float):
    global stick_max

    tilt = (stick_max * (abs(ax_y) / 10))

    if ax_y < 0:
        # LEFT
        gamepad.left_joystick(x_value=-int(tilt), y_value=0)
    else:
        # RIGHT
        gamepad.left_joystick(x_value=int(tilt), y_value=0)

    gamepad.update()


def _control_steering(ax_y: float):
    global steering_turned

    if ax_y < -3 and not steering_turned:
        # left
        # ahk.key_down("a")
        print("Steer LEFT")
        steering_turned = True
    elif ax_y > 3 and not steering_turned:
        # right
        # ahk.key_down("d")
        print("Steer RIGHT")
        steering_turned = True
    elif (ax_y > -3 and ax_y < 3) and steering_turned:
        release_steering()
        print("Steer RELEASE")


def release_steering():
    global steering_turned

    #ahk.key_up("a")
    #ahk.key_up("d")
    steering_turned = False
