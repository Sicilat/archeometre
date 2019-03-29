//Initialisation des tableaux

double cap[3];

const float SOUND_SPEED = 340.0 / 1000;           /* Vitesse du son dans l'air en mm/us */
const byte TRIGGER_PIN = 2;                       // Broche TRIGGER
const byte ECHO_PIN = 4;                          // Broche ECHO
const unsigned long MEASURE_TIMEOUT = 25000UL;    // 25ms = ~8m à 340m/s
const int potA = 5;  //Défini le pin du potentiometre
const int potB = 4;
const int potC = 3;
const int btn = 5
const int L1 = 3;

double getUSvalue(){
	digitalWrite(TRIGGER_PIN, HIGH);
  	delayMicroseconds(10);
  	digitalWrite(TRIGGER_PIN, LOW);

  	long measure = pulseIn(ECHO_PIN, HIGH, MEASURE_TIMEOUT);
  	float distance_mm = measure / 2.0 * SOUND_SPEED;

  	float data = distance_mm / 1000.0, 2;
	return data;
}

void transmit_data(double cap[], double us){
	Serial.print('trsm');
	Serial.print(cap[0]);
	Serial.print(cap[1]);
	Serial.print(cap[2]);
	Serial.print(us);
}

double getRAcap(){
	int data = analogRead(potA);
	return data;
}

double getRBcap(){
	//Récupérer la valeur du capteur 2
	int data = analogRead(potB);
	return data;
}

double getRCcap(){
	//Récupérer la valeur du capteur 3
	int data = analogRead(potC);
	return data;
}

double get_cap(double cap[]){
	cap[0] = getRAcap();
	cap[1] = getRBcap();
	cap[2] = getRCcap();
	return cap;
}

void setup(){
	Serial.begin(9600);
	
	//Initialisation des capteurs US

	us = 0;
  
	//Initialisation du tableau des capteurs fils tendus
	
	cap[0] = 0;
	cap[1] = 0;
	cap[2] = 0;

  	pinMode(TRIGGER_PIN, OUTPUT);   //initialise les broches.
  	digitalWrite(TRIGGER_PIN, LOW);
  	pinMode(ECHO_PIN, INPUT);
  	pinMode(L1, OUTPUT); //L1 est une broche de sortie
  	pinMode(potA, INPUT);
  	pinMode(potB, INPUT);
  	pinMode(potC, INPUT);
}

void loop(){
	digitalWrite(L1, HIGH);
	if digitalRead(btn){
		transmit_data(get_cap(), getUSvalue())
	}
}
