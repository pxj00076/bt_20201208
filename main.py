
bluetooth.start_accelerometer_service()

def on_bluetooth_connected():
    basic.show_icon(IconNames.HEART)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.HOUSE)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)
