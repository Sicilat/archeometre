//Initialisation des tableaux

double us;
double pos[3];
double cap[3];

double getUSvalue(){
	return data;
}

double getZpos(double Rb, double Rc){
	return (((Rb * Rb) - (Rc * Rc) + 1) / 2);
}

double getXpos(double Ra, double Rb){
	return (((Ra * Ra) - (Rb * Rb) - 1) / (-2));
}

double getYpos(double Rb, double X, double Z){
	return (sqrt((Rb * Rb) - (X * X) - (Z * Z)));
}

void transmit_data(double cap[], double pos[], double us){
	//Transmettre les données à l'interface intermédiaire	
}

double get_pos(double pos[], double Rb, double Rc, double Ra){
	double X = getXpos(Ra, Rb);
	double Z = getZpos(Rb, Rc);
	double Y = getYpos(Rb, X, Y);
}

double getRAcap(){
	//Récupérer la valeur du capteur 1
	return data;
}

double getRBcap(){
	//Récupérer la valeur du capteur 2
	return data;
}

double getRCcap(){
	//Récupérer la valeur du capteur 3
	return data;
}

double get_cap(double cap[]){
	cap[0] = getRAcap();
	cap[1] = getRBcap();
	cap[2] = getRCcap();
	return cap;
}

void setup(){
	Serial.begin(115200);
	
	//Initialisation des capteurs US

	us = 0;
	
	//Initialisation du tableau de la position
	
	pos[0] = 0;
	pos[1] = 0;
	pos[2] = 0;
  
	//Initialisation du tableau des capteurs fils tendus
	
	cap[0] = 0;
	cap[1] = 0;
	cap[2] = 0;
}

void loop(){
	
}
