lcd1602.set_address(lcd1602.I2C_ADDR.ADDR1)
lcd1602.clear()
agvgimothta = 0
thermedafous = 0
humidity = 0
temperature = 0

def on_forever():
    global humidity, temperature, agvgimothta, thermedafous
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P11, True, False, True)
    humidity = dht11_dht22.read_data(dataType.HUMIDITY)
    temperature = dht11_dht22.read_data(dataType.TEMPERATURE)
    if humidity != -999 and temperature != -999:
        pass
    serial.write_value("hunidity", humidity)
    serial.write_value("temperature", temperature)
    basic.show_number(humidity)
    basic.show_number(temperature)
    if temperature > 10 and temperature < 15:
        pins.analog_write_pin(AnalogPin.P6, 1)
    else:
        pins.analog_write_pin(AnalogPin.P6, 0)
    lcd1602.clear()
    lcd1602.put_string("humidity", 0, 0)
    lcd1602.put_number(humidity, 12, 0)
    lcd1602.put_string("temperature", 0, 1)
    lcd1602.put_number(temperature, 12, 1)
    agvgimothta = pins.analog_read_pin(AnalogReadWritePin.P0)
    basic.show_number(agvgimothta)
    serial.write_value("Agogimotita", agvgimothta)
    basic.pause(500)
    thermedafous = Environment.ds18b20_temp(DigitalPin.P5, Environment.ValType.DS18B20_TEMPERATURE_C)
    serial.write_value("therm edaf", thermedafous)
    basic.pause(1000)
basic.forever(on_forever)
