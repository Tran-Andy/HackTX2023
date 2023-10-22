void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

int LightSensor()
{
  int lightValue = analogRead(A0);

  Serial.print("Light Intensity: ");
  Serial.println(lightValue);

  delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:
    LightSensor();

}
