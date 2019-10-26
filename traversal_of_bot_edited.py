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
	time_move=300*dist/circum_wheel
	forward(left_wheel,200)
	backward(right_wheel,200)
	wp.delay(int(time_move))
	off_motor(left_wheel)
	off_motor(right_wheel)
def turn_angle(deg,dir='clock'):
	angle_to_rot=deg
	len_to_move=(2*3.14*dist_between_wheels)*angle_to_rot/360
	time_move=300*len_to_move/circum_wheel
	if dir=='clock':
		forward(left_wheel,200)
		wp.delay(int(time_move))
		off_motor(left_wheel)
	else:
		backward(right_wheel,200)
		wp.delay(int(time_move))
		off_motor(right_wheel)


#program:

left_wheel=Motor(23,24,25)
right_wheel=Motor(17,27,22)
circum_wheel=23.1
dist_between_wheels=17.9

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
