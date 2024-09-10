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
   if (intensidadeLuz <= 33) {
    digitalWrite(LED_VERDE, HIGH);
    digitalWrite(LED_AMARELO, LOW);
    digitalWrite(LED_VERMELHO, LOW);
  } else if (intensidadeLuz <= 66) {
    digitalWrite(LED_AMARELO, HIGH);
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_VERMELHO, LOW);
    lcd.print("Ambiente a meia luz");
  } else {
    digitalWrite(LED_VERMELHO, HIGH);
    lcd.print("Ambiente muito claro");
    lcd.setCursor(0, 1);
  }

  if (temperatura >= 10 && temperatura <= 20) {
    digitalWrite(LED_VERDE, HIGH);
    digitalWrite(LED_AMARELO, LOW);
    digitalWrite(LED_VERMELHO, LOW);
    lcd.print("Temperatura OK:");
    lcd.print(temperatura);
  } else if (1 => temperatura && temperatura < 10 || temperatura > 20 && temperatura <= 30) {
    digitalWrite(LED_AMARELO, HIGH);
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_VERMELHO, HIGH);
    lcd.print(temperatura < 10 ? "Temperatura Baixa:" : "Temperatura Alta:");
    lcd.print(temperatura);
    lcd.setCursor(0, 1);
    lcd.scrollDisplayLeft();
  }
  } else if (temperatura < 1 ||  temperatura > 30) {
    digitalWrite(LED_AMARELO, HIGH);
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_VERMELHO, HIGH);
    lcd.print(temperatura < 1 ? "Temperatura Muito Baixa:" : "Temperatura Muito Alta:");
    lcd.print(temperatura);
    lcd.setCursor(0, 1);
    lcd.scrollDisplayLeft();
  }

  if (umidade >= 50 && umidade <= 100) {
    lcd.print("Umidade OK:");
    lcd.print(umidade);
  } else if (umidade < 30) {
    digitalWrite(LED_VERMELHO, HIGH);
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_AMARELO, LOW);
    lcd.print("Umidade Muito Baixa:");
    lcd.print(umidade);
  } else {
    digitalWrite(LED_VERMELHO, LOW);
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_AMARELO, HIGH);
    lcd.print("Umidade Baixa:");
    lcd.print(umidade);
  }
}
}