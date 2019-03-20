#define MOTOR 3
#define POTEN 4
#define RPI0 5
#define RPI1 6
#define MAX_WRITE 1024

void setup() {
	pinMode(4, OUTPUT);
//	pinMode(POTEN, INPUT);
	pinMode(RPI0, INPUT);
	pinMode(RPI1, INPUT);
}

void loop() {/*
	int input = getRPiInput();
	input = 0; // temporary to override the input

	switch(input) {
	case 0:
		setToPosition(0.5, 0.05);
		break;
	case 1:
		useSelector(7, 10);
		break;
	}*/

	digitalWrite(4, HIGH);
}

void setToPosition(int position, int tolerance) {
	position /= MAX_WRITE;
	tolerance /= MAX_WRITE;
	int current = digitalRead(POTEN);
	
	while(!(current < position + tolerance && current > position - tolerance)) {
		if(current < position)
			analogWrite(MOTOR, 120);
		else if(current > position)
			analogWrite(MOTOR, -120);
	}
}

void useSelector(int positions, int force) {
	int intervals[positions + 1];
	int position;
	int value = digitalRead(POTEN);

	for(int i = 0; i < positions + 1; i++) {
		intervals[i] = i / MAX_WRITE;

		if(value / MAX_WRITE < i && value / MAX_WRITE > (i - 1))
			position = i;
	}

	int delta = value - (position * MAX_WRITE);
	if(delta < 0)
		analogWrite(MOTOR, 10 * delta);
	else
		analogWrite(MOTOR, -10 * delta);
}

int getRPiInput() {
	int twos = digitalRead(RPI0);
	int ones = digitalRead(RPI1);

	return pow(2, twos) + pow(2, ones);
}

