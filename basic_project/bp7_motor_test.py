import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# Control M2 motor
L_IN1 = 20
L_IN2 = 21
L_PWM1 = 0
# Control M1 motor
L_IN3 = 22
L_IN4 = 23
L_PWM2 = 1
# Control M3 motor
R_IN1 = 24
R_IN2 = 25
R_PWM1 = 12
# Control M4 motor
R_IN3 = 26
R_IN4 = 27
R_PWM2 = 13

GPIO.setmode(GPIO.BCM)  # use BCM numbers
#set the MOTOR Driver Pin OUTPUT mode
GPIO.setup(L_IN1,GPIO.OUT)
GPIO.setup(L_IN2,GPIO.OUT)
GPIO.setup(L_PWM1,GPIO.OUT)

GPIO.setup(L_IN3,GPIO.OUT)
GPIO.setup(L_IN4,GPIO.OUT)
GPIO.setup(L_PWM2,GPIO.OUT)

GPIO.setup(R_IN1,GPIO.OUT)
GPIO.setup(R_IN2,GPIO.OUT)
GPIO.setup(R_PWM1,GPIO.OUT)

GPIO.setup(R_IN3,GPIO.OUT)
GPIO.setup(R_IN4,GPIO.OUT)
GPIO.setup(R_PWM2,GPIO.OUT)


GPIO.output(L_IN1,GPIO.LOW)
GPIO.output(L_IN2,GPIO.LOW)
GPIO.output(L_IN3,GPIO.LOW)
GPIO.output(L_IN4,GPIO.LOW)

GPIO.output(R_IN1,GPIO.LOW)
GPIO.output(R_IN2,GPIO.LOW)
GPIO.output(R_IN3,GPIO.LOW)
GPIO.output(R_IN4,GPIO.LOW)


freq = 1000
#set pwm frequence to 1000hz
pwm_FR = GPIO.PWM(R_PWM1, freq/10)
pwm_BR = GPIO.PWM(R_PWM2, freq/10)
pwm_FL = GPIO.PWM(L_PWM1, freq/10)
pwm_BL = GPIO.PWM(L_PWM2, freq/10)

#set inital duty cycle to 0
pwm_FR.start(0)
pwm_FL.start(0)
pwm_BR.start(0)
pwm_BL.start(0)

try:
    while True:
        GPIO.output(L_IN1,GPIO.LOW)  #Front Left forward
        GPIO.output(L_IN2,GPIO.HIGH)
        pwm_FL.ChangeDutyCycle(50)
        GPIO.output(L_IN3,GPIO.HIGH)  #Back left forward
        GPIO.output(L_IN4,GPIO.LOW)
        pwm_BL.ChangeDutyCycle(50)
        GPIO.output(R_IN1,GPIO.HIGH)  #Front Right forward
        GPIO.output(R_IN2,GPIO.LOW)
        pwm_FR.ChangeDutyCycle(50)
        GPIO.output(R_IN3,GPIO.LOW)  #Back Right forward
        GPIO.output(R_IN4,GPIO.HIGH)
        pwm_BR.ChangeDutyCycle(50)

except KeyboardInterrupt:
    print("User interrupt keyboard")

finally:
    #stop pwm
    pwm_FR.stop()
    pwm_FL.stop()
    pwm_BR.stop()
    pwm_BL.stop()
    time.sleep(1)

    GPIO.cleanup()  #release all GPIO
