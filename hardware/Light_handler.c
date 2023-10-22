#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>

#define MAX_BUFFER_SIZE 128

typedef struct{
    char *value;
    char *time;
}data_t;

void load_data(data_t *light, char *value_triggered)
{
    
    light->value = value_triggered;
    while(!isdigit(*(light->value)))
        light->value++;

    time_t current_time;
    struct tm *time_info;

    time(&current_time);
    time_info = localtime(&current_time);
    light->time = asctime(time_info);
    strtok(light->time, "\n");

}

void getAlert(char* data)
{
    char raw_data[MAX_BUFFER_SIZE] = {0};
    FILE *serial = fopen("/dev/cu.usbmodem1101", "r");
    if (!serial) {
        fprintf(stderr, "Failed to open serial port.\n");
        return;
    }

    data_t *light = calloc(1, sizeof(data_t));


    while (1) {
        if (fgets(raw_data, MAX_BUFFER_SIZE, serial) != NULL) {
            strtok(raw_data, "\n");
            strtok(raw_data, "\r");
            load_data(light, raw_data);
            strcat(data, "value'");
            strcat(data, light->value);
            strcat(data, "'time'");
            strcat(data, light->time);
            fclose(serial);
            return;
        }
    }

    return;
}

int main() {
    int arduino_fd;
    struct termios serial;
    char buffer[64];

    // Open the serial port (replace "/dev/ttyUSB0" with the correct device name)
    arduino_fd = open("/dev/ttyUSB0", O_RDWR | O_NOCTTY);
    if (arduino_fd == -1) {
        perror("Failed to open the Arduino serial port");
        return 1;
    }

    // Configure the serial port
    tcgetattr(arduino_fd, &serial);
    cfsetospeed(&serial, B9600); // Set the baud rate to match Arduino's Serial.begin
    serial.c_cflag |= (CLOCAL | CREAD);
    tcsetattr(arduino_fd, TCSANOW, &serial);

    while (1) {
        ssize_t n = read(arduino_fd, buffer, sizeof(buffer) - 1);
        if (n > 0) {
            buffer[n] = '\0';
            printf("Received from Arduino: %s", buffer);
        }
    }

    close(arduino_fd);

    return 0;
}
