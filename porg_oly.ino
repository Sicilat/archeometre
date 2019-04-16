double cap;

const float SOUND_SPEED = 340.0 / 1000;           /* Vitesse du son dans l'air en mm/us */
const byte TRIGGER_PIN = 2;                       // Broche TRIGGER
const byte ECHO1_PIN = 4;
const unsigned long MEASURE_TIMEOUT = 25000UL;    // 25ms = ~8m à 340m/s
const int potA = 5;
const int btn = 7;
const int L1 = 3;
double distance_mm;

double getUSvalue(float distance_mm){
    digitalWrite(TRIGGER_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, LOW);
    double distance_mm1;
    
    long measure1 = pulseIn(ECHO1_PIN, HIGH, MEASURE_TIMEOUT);
    distance_mm1 = measure1 / 2.0 * SOUND_SPEED / 1000;

    float data = distance_mm1;
  return data;
}

void transmit_data(double cap, double us){
  Serial.println("trsm");
  Serial.println(cap);
  Serial.println(us);
}

double getRAcap(){
  int a = 0;
  double data = 0;
  Serial.println("get rAcap")
  for (int i = 0; i < 1000; i++){
    data += analogRead(potA);
    a++;
  }
  Serial.println("data full")
  Serial.println(data)
  data = data / a;
  Serial.println(data)
  return data;
}

int get_cap(double cap){
  cap = getRAcap();
  return cap;
}

void setup(){
  Serial.begin(9600);
  
  //Initialisation des capteurs US

  double us = 0;
  
  //Initialisation du tableau des capteurs fils tendus
  
  cap = 0;

  pinMode(TRIGGER_PIN, OUTPUT);   //initialise les broches.
  digitalWrite(TRIGGER_PIN, LOW);
  pinMode(ECHO1_PIN, INPUT);
  pinMode(L1, OUTPUT);
  pinMode(potA, INPUT);
  pinMode(btn, INPUT);
}

void loop(){
  digitalWrite(L1, HIGH);
  if (digitalRead(btn) == 0){
    transmit_data(get_cap(cap), getUSvalue(distance_mm));
    delay(100);
  }
}
