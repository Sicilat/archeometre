//Initialisation des tableaux

double cap[3];

const float SOUND_SPEED = 340.0 / 1000;           /* Vitesse du son dans l'air en mm/us */
const byte TRIGGER_PIN = 2;                       // Broche TRIGGER
const byte ECHO1_PIN = 4;                          // Broche ECHO
const byte ECHO2_PIN = 5;
const byte ECHO3_PIN = 6;
const unsigned long MEASURE_TIMEOUT = 25000UL;    // 25ms = ~8m à 340m/s
const int potA = 5;  //Défini le pin du potentiometre
const int potB = 4;
const int potC = 3;
const int btn = 7;
const int L1 = 3;
const int L2 = 4;
const int L3 = 1;
double distance_mm;

double getUSvalue(float distance_mm){
    digitalWrite(TRIGGER_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, LOW);

   
    long measure1 = pulseIn(ECHO1_PIN, HIGH, MEASURE_TIMEOUT);
    distance_mm1 = measure1 / 2.0 * SOUND_SPEED;
    long measure2 = pulseIn(ECHO2_PIN, HIGH, MEASURE_TIMEOUT);
    distance_mm2 = measure2 / 2.0 * SOUND_SPEED;
    long measure3 = pulseIn(ECHO3_PIN, HIGH, MEASURE_TIMEOUT);
    distance_mm3 = measure3 / 2.0 * SOUND_SPEED;

    float data = (distance_mm1 + distance_mm2 + distance_mm3) / 3;
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

int get_cap(double cap[]){
  cap[0] = getRAcap();
  cap[1] = getRBcap();
  cap[2] = getRCcap();
  return cap;
}

void setup(){
  Serial.begin(9600);
  
  //Initialisation des capteurs US

  double us = 0;
  
  //Initialisation du tableau des capteurs fils tendus
  
  cap[0] = 0;
  cap[1] = 0;
  cap[2] = 0;

    pinMode(TRIGGER_PIN, OUTPUT);   //initialise les broches.
    digitalWrite(TRIGGER_PIN, LOW);
    pinMode(ECHO1_PIN, INPUT);
    pinMode(ECHO2_PIN, INPUT);
    pinMode(ECHO3_PIN, INPUT);
    pinMode(L1, OUTPUT); //L1 est une broche de sortie
    pinMode(L2, OUTPUT);
    pinMode(L3, OUTPUT);
    pinMode(potA, INPUT);
    pinMode(potB, INPUT);
    pinMode(potC, INPUT);
    pinMode(btn, INPUT);
}

void loop(){
  digitalWrite(L1, HIGH);
  digitalWrite(L2, HIGH);
  digitalWrite(L3, HIGH);
  if (digitalRead(btn) == 0){
    transmit_data(get_cap(cap), getUSvalue(distance_mm));
    delay(1000)
  }
}
