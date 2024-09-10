#include <DHT11.h>
#include <LiquidCrystal.h>

// Definindo a qual pino os Leds estão ligados:
int LED_PIN_RED = 12;
int LED_PIN_YELLOW = 11;
int LED_PIN_GREEN = 10;
int BUZZER = 13;
int LDR_PIN = A0;
DHT11 dht11(2);

// Definindo os pinos do LCD
const int rs = 9;
const int rw = 8;
const int en = 7;
const int d4 = 6;
const int d5 = 5;
const int d6 = 4; 
const int d7 = 3;

LiquidCrystal lcd(rs, rw, en, d4, d5, d6, d7);

unsigned long previousMillis = 0;
const long interval = 1500; // Intervalo de tempo desejado em milissegundos para o buzzer

void setup() {
  Serial.begin(9600);
  pinMode(LDR_PIN, INPUT);
  lcd.begin(16, 2);

  // Define os LED's e o Buzzer como output
  pinMode(LED_PIN_RED, OUTPUT);
  pinMode(LED_PIN_YELLOW, OUTPUT);
  pinMode(LED_PIN_GREEN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}

void loop() { 
  unsigned long currentMillis = millis();
  float IntensidadeLuz;
  int temperatura = 0
  int umidade = 0
  float result = dht11.readTemperatureHumidity(temperatura, umidade);
  int ValorLDR = analogRead(LDR_PIN);
  IntensidadeLuz = map(ValorLDR, 0, 1023, 0, 100);

  if (result == 0) {
      Serial.print("Temperature: ");
      Serial.print(temperature);
      Serial.print(" °C\tHumidity: ");
      Serial.print(humidity);
      Serial.println(" %");
  }
  // Mostra os valores no LCD
  lcd.setCursor(0, 0);
  lcd.print("Temp:");
  lcd.print(temperatura);
  lcd.print("C");
  lcd.setCursor(0, 1);
  lcd.print("umidade:");
  lcd.print(umidade);
  lcd.print('%');

  // Estabelecendo condicionais dos Leds baseados nos valores percentuais do LDR:
  if (IntensidadeLuz < 100 && temperatura < 100 && umidade < 100) {
    analogWrite(LED_PIN_RED, 0); 
    analogWrite(LED_PIN_YELLOW, 0); 
    analogWrite(LED_PIN_GREEN, 255); // Faz com que o Led verde brilhe
  } 
  else if (IntensidadeLuz < 60 || temperatura < 60 || umidade < 60) {
    analogWrite(LED_PIN_RED, 0);
    analogWrite(LED_PIN_YELLOW, 255); // Faz com que o Led amarelo brilhe
    analogWrite(LED_PIN_GREEN, 0);
    if (currentMillis - previousMillis >= interval) {
      tone(BUZZER, 400, 1500);
      previousMillis = currentMillis;
    }
  } 
  else if (IntensidadeLuz < 40 || temperatura < 40 || umidade < 40) {
    analogWrite(LED_PIN_RED, 255); // Faz com que o Led vermelho brilhe
    analogWrite(LED_PIN_YELLOW, 0); 
    analogWrite(LED_PIN_GREEN, 0); 
    if (currentMillis - previousMillis >= interval) {
      tone(BUZZER, 400, 1500);
      previousMillis = currentMillis;
    }
  }

  // Mostra os valores no Serial Monitor
  Serial.println(IntensidadeLuz);
  Serial.print(F("Umidade: "));
  Serial.print(umidade);
  Serial.print(F(" Temperatura: "));
  Serial.print(temperatura);
  Serial.println(F("°C "));
}

//comentar o erro do professor no Display do tinkercad (colocou o 5v e o GND nos lugares errados)
//wokwi.com/projects/395835804219402241

