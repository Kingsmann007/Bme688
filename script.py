import time
import board
import adafruit_bme680
import datetime
#initial setup
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
#zeit
zeit = datetime.datetime.now()
#lists for values
tmp = []
gas = []
hum = []
dru = []
for i in range(0,5):
#hum is always 100% the first time getting data
#the first reading will therfore be disregarded
	if i>0:
		tmp.append(bme680.temperature)
		gas.append(bme680.gas)
		hum.append(bme680.relative_humidity)
		dru.append(bme680.pressure)
	else:
		bme680.temperature
		bme680.gas
		bme680.relative_humidity
		bme680.pressure
	time.sleep(0.5)
#claculating averages
tmp_avg = sum(tmp)/len(tmp)
gas_avg = sum(gas)/len(gas)
hum_avg = sum(hum)/len(hum)
dru_avg = sum(dru)/len(dru)
#writing data to file
file = "data/"
file += zeit.strftime("%Y%m%d.txt")
with open(file ,'a') as d: 
	d.write(zeit.strftime("%d/%m/%Y %H:%M:%S"))
	d.write("; Tmp: %0.1f C; " % tmp_avg-1)
	d.write("Gas: %d ohm; " % gas_avg)
	d.write("Hum: %0.1f %%; " % hum_avg-5)
	d.write("Dru: %0.3f hPa;\n" % dru_avg)