const int tempPin = A0; // Pin for temperature sensor (LM35)
const int ldrPin = A1;  // Pin for LDR sensor
int celsius = 0;
int baselineTemp = 0;

// Parâmetros de calibração para turbidez (valores de exemplo)
const float maxTurbidity = 100; // Valor máximo de turbidez em NTU
const int maxLDRValue = 1023;   // Valor máximo possível do LDR (10-bit ADC)

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial
}

void loop() {
  // Leitura da temperatura do sensor LM35
  baselineTemp = 40;
  int tempValue = analogRead(tempPin);
  celsius = map(((tempValue - 20) * 3.04), 0, 1023, -40, 125);

  // Leitura dos valores do pH no potenciometro
  int sensorValue = analogRead(A2);
  float pH = sensorValue * (14.0/1023.0);
  
  // Leitura da turbidez do sensor LDR
  int ldrValue = analogRead(ldrPin);
  // Calculo da turbidez: valor máximo de turbidez menos a proporcionalidade inversa do valor do LDR
  float turbidity = maxTurbidity * (1.0 - (float)ldrValue / maxLDRValue);

  // Determina a qualidade da turbidez
  String turbidityQuality;
  if (turbidity <= 2) {
    turbidityQuality = "Excelente";
  } else if (turbidity <= 5) {
    turbidityQuality = "Mediana";
  } else {
    turbidityQuality = "Ruim";
  }
  // Determine temperature quality
  String temperatureQuality;
  if (celsius >= 20 && celsius <= 25) {
    temperatureQuality = "Ideal";
  } else if ((temperature >= 15 && temperature < 20) || (temperature > 25 && temperature <= 30)) {
    temperatureQuality = "Boa";
  } else {
    temperatureQuality = "Ruim";
  }

  // Determine pH quality
  String pHQuality;
  if (pH >= 6.5 && pH <= 8.5) {
    pHQuality = "Ideal";
  } else if ((pH >= 6.0 && pH < 6.5) || (pH > 8.5 && pH <= 9.0)) {
    pHQuality = "Boa";
  } else {
    pHQuality = "Ruim";
  }

  // Imprime os valores de temperatura e turbidez no Monitor Serial
  Serial.print("Temperatura: ");
  Serial.print(celsius);
  Serial.print(" C\t");
  Serial.print(temperatureQuality);
  Serial.print(")\t");
  Serial.print("Turbidez: ");
  Serial.print(turbidity);
  Serial.print(" NTU\t");
  Serial.print("Qualidade H2O: ");
  Serial.println(turbidityQuality);
  Serial.println("\t");
  Serial.println("pH: \t");
  Serial.println(pH);
  Serial.print(pHQuality);
  Serial.print(")\t");
  
  

  delay(2000); // Aguarda 2 segundos antes da próxima leitura
}
