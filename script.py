import time
import board
import adafruit_bme680
import datetime
#Initialisieren
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# Kalibrierung mit lokalem Druck auf Höhe des Meeresspiegels
#bme680.sea_level_pressure = 1013.25
#zeit
zeit = datetime.datetime.now()
#listen für Werte
tmp = []
gas = []
hum = []
dru = []
for i in range(0,5):
#Erster ausgelesener werd ist immer falsch Bsp. hum immer 100%, werden daher vernachlässigt
	if i>0:
		tmp.append(bme680.temperature)
		gas.append(bme680.gas)
		hum.append(bme680.relative_humidity)
		dru.append(bme680.pressure)
	else:
		(bme680.temperature)
		(bme680.gas)
		(bme680.relative_humidity)
		(bme680.pressure)
	time.sleep(1)
#Durchschnitswerte
tmp_avg = sum(tmp)/len(tmp)
gas_avg = sum(gas)/len(gas)
hum_avg = sum(hum)/len(hum)
dru_avg = sum(dru)/len(dru)
#Werte in datei schreiben
with open('data.txt','a') as d: 
	d.write(zeit.strftime("%d/%m/%Y %H:%M:%S"))
	d.write("; Tmp: %0.1f C; " % tmp_avg)
	d.write("Gas: %d ohm; " % gas_avg)
	d.write("Hum: %0.1f %%; " % hum_avg)
	d.write("Dru: %0.3f hPa;\n" % dru_avg)
