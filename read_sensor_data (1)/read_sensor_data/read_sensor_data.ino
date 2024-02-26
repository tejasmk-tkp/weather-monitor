#include <DHT11.h>
#include <Wire.h>
#include <Adafruit_BMP085.h>

DHT11 dht11(3);

Adafruit_BMP085 bmp;

int rain_sensor = 5;

void setup() {

    Serial.begin(9600);

    pinMode(rain_sensor, INPUT);
    
    if (!bmp.begin()) {
    Serial.println("Could not find a valid BMP085 sensor, check wiring!");
    while (1); // This will halt the program if BMP sensor is not found
  }

}

void loop() {
    int temperature = 0;
    int humidity = 0;

    // Attempt to read the temperature and humidity values from the DHT11 sensor.
    int result = dht11.readTemperatureHumidity(temperature, humidity);

    // Check the results of the readings.
    // If the reading is successful, print the temperature and humidity values.
    // If there are errors, print the appropriate error messages.
    if (result == 0) {
        Serial.print("Temperature: ");
        Serial.print(temperature);
        Serial.print(" °C\tHumidity: ");
        Serial.print(humidity);
        Serial.println(" %");
    } else {
        // Print error message based on the error code.
        Serial.println(DHT11::getErrorString(result));
    }

      Serial.print("Temperature = ");
  Serial.print(bmp.readTemperature());
  Serial.println(" *C");
   
  Serial.print("Pressure = ");
  Serial.print(bmp.readPressure());
  Serial.println(" Pa");

  Serial.print("Altitude = ");
  Serial.print(bmp.readAltitude());
  Serial.println(" meters");

  Serial.print("Pressure at sealevel (calculated) = ");
  Serial.print(bmp.readSealevelPressure());
  Serial.println(" Pa");

  // Assuming sea level pressure in hectopascals
  float seaLevelPressure_hPa = 1013.25; // Example value, replace with actual sea level pressure at your location
  Serial.print("Real altitude = ");
  Serial.print(bmp.readAltitude(seaLevelPressure_hPa * 100)); // Convert hPa to Pa
  Serial.println(" meters");

  int value = analogRead(rain_sensor);//read value
  Serial.print("Value : ");
  Serial.println(value);
}
