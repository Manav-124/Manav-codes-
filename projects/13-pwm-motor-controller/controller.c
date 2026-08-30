/* PWM motor control reference model with direction and safe duty limiting. */
#include <stdint.h>

typedef enum { MOTOR_STOP, MOTOR_FORWARD, MOTOR_REVERSE } direction_t;
typedef struct { direction_t direction; uint8_t duty_percent; } motor_command_t;

motor_command_t command_motor(int requested_speed) {
    motor_command_t cmd;
    if (requested_speed == 0) return (motor_command_t){MOTOR_STOP, 0};
    cmd.direction = requested_speed > 0 ? MOTOR_FORWARD : MOTOR_REVERSE;
    int magnitude = requested_speed > 0 ? requested_speed : -requested_speed;
    cmd.duty_percent = (uint8_t)(magnitude > 100 ? 100 : magnitude);
    return cmd;
}

int main(void) { motor_command_t cmd = command_motor(72); return cmd.duty_percent == 72 ? 0 : 1; }
