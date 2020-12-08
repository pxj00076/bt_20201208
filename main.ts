bluetooth.startAccelerometerService()
bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showIcon(IconNames.Heart)
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    basic.showIcon(IconNames.House)
})
