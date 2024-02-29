#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>

const struct gpio_dt_spec bmp180 = GPIO_DT_SPEC_GET(DT_NODELABEL(bmp180), gpios);
const struct gpio_dt_spec dht11 = GPIO_DT_SPEC_GET(DT_NODELABEL(dht11), gpios);
const struct gpio_dt_spec rain_sensor = GPIO_DT_SPEC_GET(DT_NODELABEL(rain_sensor), gpios);

int main(void) {

        if (!device_is_ready(bmp180.port)) {
                printk("BMP180 is not ready\n");
        }

        if (!device_is_ready(dht11.port)) {
                printk("DHT11 is not ready\n");
        }

        if (!device_is_ready(rain_sensor.port)) {
                printk("Rain sensor is not ready\n");
        }

        gpio_pin_configure_dt(&bmp180, GPIO_INPUT);
        gpio_pin_configure_dt(&dht11, GPIO_INPUT);
        gpio_pin_configure_dt(&rain_sensor, GPIO_INPUT);

        while (1) {
                int bmp180_value = gpio_pin_get(bmp180.port, bmp180.pin);
                int dht11_value = gpio_pin_get(dht11.port, dht11.pin);
                int rain_sensor_value = gpio_pin_get(rain_sensor.port, rain_sensor.pin);
                printk("BMP180: %d\n", bmp180_value);
                printk("DHT11: %d\n", dht11_value);
                printk("Rain sensor: %d\n", rain_sensor_value);
                k_sleep(K_MSEC(1000));
        }

}
