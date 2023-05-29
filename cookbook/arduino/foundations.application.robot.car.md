


```cpp
// Define motor pins
#define MOTOR_LEFT_1 2   // Control pin for left motor, forward direction
#define MOTOR_LEFT_2 3   // Control pin for left motor, backward direction
#define MOTOR_RIGHT_1 4  // Control pin for right motor, forward direction
#define MOTOR_RIGHT_2 5  // Control pin for right motor, backward direction

// Define sensor pins
#define TRACKER_LEFT 7   // Input pin for left line tracker sensor
#define TRACKER_RIGHT 6  // Input pin for right line tracker sensor
#define MOTOR_STATE 8    // Input pin for reading motor state (on/off)
#define THROTTLE_IN A0   // Analog input pin for reading the throttle (speed control)
#define THROTTLE_OUT_LEFT 9   // PWM output pin for setting speed (speed control)
#define THROTTLE_OUT_RIGHT 10  // PWM output pin for setting speed (speed control)

// Define states
#define STOP 0     // Motors stopped
#define FORWARD 1  // Moving forward
#define REVERSE 2  // Moving backwards
#define LEFT 3     // Turning left
#define RIGHT 4    // Turning right

int state = STOP;  // Initialize the state of the robot as stopped

int speed;
int motorOn;
int lineLeft;
int lineRight;

void setup() {
  Serial.begin(115200);

  // Set motor pins as OUTPUTs
  pinMode(MOTOR_LEFT_1, OUTPUT);
  pinMode(MOTOR_LEFT_2, OUTPUT);
  pinMode(MOTOR_RIGHT_1, OUTPUT);
  pinMode(MOTOR_RIGHT_2, OUTPUT);
  pinMode(THROTTLE_OUT_LEFT, OUTPUT);
  pinMode(THROTTLE_OUT_RIGHT, OUTPUT);

  // Set sensor pins as INPUTs
  pinMode(TRACKER_RIGHT, INPUT);
  pinMode(TRACKER_LEFT, INPUT);
  pinMode(MOTOR_STATE, INPUT);
  pinMode(THROTTLE_IN, INPUT);
}

/*
 * powerMotor function powers the motor in one direction.
 * It sets one pin to HIGH (power on) and the other pin to LOW (power off).
 */
void powerMotor(int positive, int negative) {
  digitalWrite(positive, HIGH);
  digitalWrite(negative, LOW);
}

/*
 * goForward checks if line is detected by either sensor.
 * If line is detected by left sensor, it returns RIGHT. 
 * If line is detected by right sensor, it returns LEFT.
 * If the line is detected by both sensors, it returns STOP.
 * Otherwise, it powers both motors to move forward and returns FORWARD.
 */
int goForward(int lineLeft, int lineRight) {
  if (lineLeft && lineRight) return STOP;
  if (lineLeft) return RIGHT;
  if (lineRight) return LEFT;
  powerMotor(MOTOR_LEFT_1, MOTOR_LEFT_2);
  powerMotor(MOTOR_RIGHT_1, MOTOR_RIGHT_2);
  return FORWARD;
}

/*
 * goBackward powers the motors in opposite direction.
 * If the line is not detected by either sensor, it returns FORWARD.
 * If the line is detected by either sensor, it returns appropriate turn.
 */
int goBackward(int lineLeft, int lineRight) {
  if (!lineLeft && !lineRight) return FORWARD;
  if (lineLeft) return RIGHT;
  if (lineRight) return LEFT;
  powerMotor(MOTOR_LEFT_2, MOTOR_LEFT_1);
  powerMotor(MOTOR_RIGHT_2, MOTOR_RIGHT_1);
  return REVERSE;
}

/*
 * turnLeft turns the robot to the left until it finds the line.
 * If the line is not detected by either sensor, it returns FORWARD.
 * If the line is detected by both sensors, it returns STOP.
 * If the line is detected by left sensor, it returns RIGHT.
 */
int turnLeft(int lineLeft, int lineRight) {
  if (!lineLeft && !lineRight) return FORWARD;
  if (lineLeft && lineRight) return STOP;
  if (lineLeft) return RIGHT;
  powerMotor(MOTOR_LEFT_2, MOTOR_LEFT_1);
  powerMotor(MOTOR_RIGHT_1, MOTOR_RIGHT_2);
  return LEFT;
}

/*
 * turnRight turns the robot to the right.
 * If the line is not detected by either sensor, it returns FORWARD.
 * If the line is detected by both sensors, it returns STOP.
 * If the line is detected by right sensor, it returns LEFT.
 */
int turnRight(int lineLeft, int lineRight) {
  if (!lineLeft && !lineRight) return FORWARD;
  if (lineLeft && lineRight) return STOP;
  if (lineRight) return LEFT;
  powerMotor(MOTOR_LEFT_1, MOTOR_LEFT_2);
  powerMotor(MOTOR_RIGHT_2, MOTOR_RIGHT_1);
  return RIGHT;
}

/*
 * stop function stops the movement of the robot by turning off both motors
 * If the line is not detected by either sensor, it returns FORWARD.
 * If the line is detected by either sensor, it returns appropriate turn.
 * If the line is detected by both sensors, it returns STOP.
 */
int stop(int lineLeft, int lineRight) {
  if (!lineLeft && !lineRight) return FORWARD;
  if (lineRight) return LEFT;
  if (lineLeft) return RIGHT;
  digitalWrite(MOTOR_LEFT_1, LOW);
  digitalWrite(MOTOR_LEFT_2, LOW);
  digitalWrite(MOTOR_RIGHT_1, LOW);
  digitalWrite(MOTOR_RIGHT_2, LOW);
  return STOP;
}

// setSpeed sets both motors to the same speed
void setSpeed(int speed) {
  analogWrite(THROTTLE_OUT_LEFT, speed);
  analogWrite(THROTTLE_OUT_RIGHT, speed);
}

/*
 * loop function runs continuously after the setup function has completed.
 * It controls the movement of the robot.
 * It reads the state of the motors, the line tracker sensors, and the throttle, 
 * and updates the state of the robot accordingly.
 */
void loop() {
  motorOn = digitalRead(MOTOR_STATE);
   
  if (!motorOn) return;

  lineLeft = digitalRead(TRACKER_LEFT);
  lineRight = digitalRead(TRACKER_RIGHT);

  // THROTTLE is an analog input, so use analogRead() instead of digitalRead()
  speed = analogRead(THROTTLE_IN);  
  speed = map(speed, 0, 1024, 0, 255);
  setSpeed(speed);
  
  // Depending on the current state of the robot, call the appropriate function
  if (state == FORWARD) {
    state = goForward(lineLeft, lineRight);
  } else if (state == LEFT){
    state = turnLeft(lineLeft, lineRight);
  } else if (state == RIGHT){
    state = turnRight(lineLeft, lineRight);
  } else if (state == REVERSE){
    state = goBackward(lineLeft, lineRight);
  }else if (state == STOP){
    state = stop(lineLeft, lineRight);
  }
  Serial.println();
  // If the robot is stopped, it doesn't move.
  // (You don't seem to have a 'stop' function, so this will cause an error.)
}
  ```