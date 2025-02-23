lcd1602.setAddress(lcd1602.I2C_ADDR.addr1)
lcd1602.clear()
let agvgimothta = 0
let thermedafous = 0
let humidity = 0
let temperature = 0
basic.forever(function on_forever() {
    
    dht11_dht22.queryData(DHTtype.DHT11, DigitalPin.P11, true, false, true)
    humidity = dht11_dht22.readData(dataType.humidity)
    temperature = dht11_dht22.readData(dataType.temperature)
    if (humidity != -999 && temperature != -999) {
        
    }
    
    serial.writeValue("hunidity", humidity)
    serial.writeValue("temperature", temperature)
    basic.showNumber(humidity)
    basic.showNumber(temperature)
    if (temperature > 10 && temperature < 15) {
        pins.analogWritePin(AnalogPin.P6, 1)
    } else {
        pins.analogWritePin(AnalogPin.P6, 0)
    }
    
    lcd1602.clear()
    lcd1602.putString("humidity", 0, 0)
    lcd1602.putNumber(humidity, 12, 0)
    lcd1602.putString("temperature", 0, 1)
    lcd1602.putNumber(temperature, 12, 1)
    agvgimothta = pins.analogReadPin(AnalogReadWritePin.P0)
    basic.showNumber(agvgimothta)
    serial.writeValue("Agogimotita", agvgimothta)
    basic.pause(500)
    thermedafous = Environment.Ds18b20Temp(DigitalPin.P5, Environment.ValType.DS18B20_temperature_C)
    serial.writeValue("therm edaf", thermedafous)
    basic.pause(1000)
})
