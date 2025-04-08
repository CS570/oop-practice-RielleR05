from motor import Motor

class Robot:
    def __init__(self,color,name):
        self.name = name
        self.color = color
        self.left_motor = Motor()
        self.right_motor = Motor()
    def set_speed(self, speed):
        if speed < 0:
            speed = 0
        if speed >1:
            speed =1
    def reverse(self):
        self.left_motor.set_speed(-1)
        self.right_motor.set_speed(-1)
    def drive_forward(self,speed):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)
    def turn_left(self):
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(1)
    def turn_right(self):
        self.left_motor.set_speed(1)
        self.right_motor.set_speed(0)

