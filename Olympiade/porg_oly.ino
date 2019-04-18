double cap;

const float SOUND_SPEED = 340.0 / 1000;           /* Vitesse du son dans l'air en mm/us */
const byte TRIGGER_PIN = 2;                       // Broche TRIGGER
const byte ECHO1_PIN = 4;
const unsigned long MEASURE_TIMEOUT = 25000UL;    // 25ms = ~8m à 340m/s
const int potA = 5;
const int btn = 7;
const int L1 = 3;
double distance_mm;

double getUSvalue(float distance_mm){                 //Récupère les valeurs des capteurs ultrason en mètres
    digitalWrite(TRIGGER_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, LOW);
    double distance_mm1;
    
    long measure1 = pulseIn(ECHO1_PIN, HIGH, MEASURE_TIMEOUT);
    distance_mm1 = measure1 / 2.0 * SOUND_SPEED / 1000;

    float data = distance_mm1;
  return data;
}

void transmit_data(double cap, double us){          //Envoie les données dans le serial
  Serial.println("trsm");
  Serial.println(cap);
  Serial.println(us);
}

double getRAcap(){                //Récupère la valeur du capteur fil tendu
  int a = 0;
  double data = 0;
  for (int i = 0; i < 1000; i++){
    data += analogRead(potA);
    a++;
  }
  data = data / a;
  return data;
}

int get_cap(double cap){            //Récupère la valeur du capteur fil tendu
  cap = getRAcap();
  return cap;
}

void setup(){
  Serial.begin(9600);
  double us = 0;
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
  if (digitalRead(btn) == 1){               //Si l'utilisateur appuie sur le bouton alors la transmission des données commence
    transmit_data(get_cap(cap), getUSvalue(distance_mm));
    delay(100);
  }
}
