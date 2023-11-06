algorithm#include <DHT.h>
#define DHTPIN 7 
#define DHTTYPE DHT11 

DHT dht(DHTPIN, DHTTYPE);

float umbralTemperatura = 28.0; ///TEMPERATURA NIVEL FUEGO
int M1derecho=2;
int M1izquierdo=3;
int M2derecho=4;
int M2izquierdo=5;
int Control1 = 9;   
int Control2 = 10;   
int  alarma = 6;  ////PIN DE LA ALARMA LED

void setup() {
  Serial.begin(9600);
    pinMode(M1derecho,OUTPUT);
  pinMode(M1izquierdo,OUTPUT);
  pinMode(M2derecho,OUTPUT);
  pinMode(M2izquierdo,OUTPUT);
  pinMode(Control1, OUTPUT);
  pinMode(Control2, OUTPUT);
  pinMode(alarma, OUTPUT);
  dht.begin();
}

void loop() {
  float temperatura = dht.readTemperature();
  if (!isnan(temperatura)) {
    Serial.print("Temperatura: ");
    Serial.println(temperatura);
    if (temperatura < umbralTemperatura) {
    Avanzar();
    delay(4000);
    Parar();
    delay(3000);
    Girar();
    delay(1000);
    Avanzar();
    delay(4000); 
    Parar();
    delay(4000);
    Girar();
    delay(500);
    }
    
    else {
    Parar();
    delay(1000);
    Girar();
    digitalWrite(alarma,HIGH);
    }
  }
}

  void Avanzar(){           
digitalWrite(M1derecho,1);
digitalWrite(M1izquierdo,0);
digitalWrite(M2derecho,0);
digitalWrite(M2izquierdo,1);
  analogWrite(Control1,50);
  analogWrite(Control2,45);      
  }
  void Girar(){          
digitalWrite(M1derecho,1);
digitalWrite(M1izquierdo,0);
digitalWrite(M2derecho,1);
digitalWrite(M2izquierdo,0);
 analogWrite(Control1,50);
  analogWrite(Control2,45);     
  }
  void Parar(){         
digitalWrite(M1derecho,0);
digitalWrite(M1izquierdo,0);
digitalWrite(M2derecho,0);
digitalWrite(M2izquierdo,0); 
 analogWrite(Control1,0);
  analogWrite(Control2,0); 
  }