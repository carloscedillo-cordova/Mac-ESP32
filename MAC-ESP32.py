import network

# Crear una instancia de la interfaz de red Wi-Fi
wifi = network.WLAN(network.STA_IF)

# Activar la interfaz Wi-Fi
wifi.active(True)

# Obtener la dirección MAC de la interfaz Wi-Fi
mac_address = wifi.config('mac')

# Mostrar la dirección MAC
print("Dirección MAC de tu ESP32:", mac_address)