#include <ArduinoJson.h>
const int TAMANHO =50; //define o buffer

////// Sensor DHT

#include"DHT.h"
#define DHTPIN 7; //define o pino usado no arduino
#define DHTTYPE DHT11;
DHT dht (DHTPIN, DHTTYPE);

//// Outras declarações
#define led 13

void setup()
{
  //inicializa o sensor
  dht.begin();

//inializa a comunicação serial

digitalWrite(led,LOW)
}
void loop()
{
  StaticJsonDocument<TAMANHO> json; //aloca o buffer para objeto json

  //faz a leitura da tempreratura 
  float temp = dht.readTemperature();

  //faz a leitura da umidade
  float umi = dht.readHumidity();

  //formato de escrita json
  json["temperatura"] = temp;
  json["umidade"] = umi;

  serializeJson(json.Serial);
  serial.println();

  //delay
  delay(500)
  digitalWrite()
}

//ler o bagulho do professor de como instalar um servidor no teams, sobre o checkpoint 4, usar virtual box (por conta dp linux), ubutunu 22
//sudo docker , vê os servidores....

