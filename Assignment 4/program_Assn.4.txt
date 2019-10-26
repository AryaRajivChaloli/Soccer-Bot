#importing files:

import wiringpi as wp
wp.wiringPiSetupGpio()



#function definitions:

def Motor(x,y,pwm):
	wp.pinMode(x,1)
	wp.pinMode(y,1)
	wp.pinMode(pwm,1)
	wp.softPwmCreate(pwm,0,100)
	return x,y,pwm
def forward(motor,speed):
	(x,y,pwm)=motor
	wp.digitalWrite(x,1)
	wp.digitalWrite(y,0)
	wp.softPwmCreate(pwm,speed)
def backward(motor,speed):
	(x,y,pwm)=motor
	wp.digitalWrite(x,0)
	wp.digitalWrite(y,1)
	wp.softPwmCreate(pwm,speed)
def off_motor(motor):
	(x,y,pwm)=motor
	wp.digitalWrite(x,0)
	wp.digitalWrite(y,0)
def move_dist(dist):
	time_left=300*dist/circum_left
	time_right=300*dist/circum_right
	forward(left_wheel,200)
	backward(right_wheel,200)
	wp.delay(time_left)
	off_motor(left_wheel)
	wp.delay(time_right-time_left)
	off_motor(right_wheel)
def turn_angle(deg,dir='clock'):
	if dir=='clock':
		part_of_rot=circum_left*60/360
		time_left=300*part_of_rot
		forward(left_wheel,200)
		wp.delay(time_left)
		off_motor(left_wheel)
	else:
		part_of_rot=circum_right*60/360
		time_right=300*part_of_rot
		forward(right_wheel,200)
		wp.delay(right_left)
		off_motor(right_wheel)


#program:

left_wheel=Motor(23,24,25)
right_wheel=Motor(17,27,22)
circum_left=22.75
circum_right=22.18

#1.moving 50cm forward:
move_dist(50)

#2.turning 60 deg.:
turn_angle(60,'clock')

#3.moving 30cm forward:
move_dist(30)

#4.turning 180-32.54292 deg:	
turn_angle(180-32.54292,'clock')

#5.moving 70cm forward:
move_dist(70)
