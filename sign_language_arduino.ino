void setup() {
  // put your setup code here, to run once:

  Serial.begin (9600);
  pinMode ( A0, INPUT );
  pinMode ( A1, INPUT );
  pinMode ( A2, INPUT );
  pinMode ( A3, INPUT );
  pinMode ( A4, INPUT );
  pinMode ( A5, INPUT );
  pinMode ( A6, INPUT );
  pinMode ( A7, INPUT );
  pinMode ( A8, INPUT );
  pinMode ( A9, INPUT );
  pinMode ( A10, INPUT );
}


int arr[11];
char buf[60];

void loop() {
  // put your main code here, to run repeatedly:
  arr[0] = analogRead(A0);
  arr[1] = analogRead(A1);
  arr[2] = analogRead(A2);
  arr[3] = analogRead(A3);
  arr[4] = analogRead(A4);
  arr[5] = analogRead(A5);
  arr[6] = analogRead(A6);
  arr[7] = analogRead(A7);
  arr[8] = analogRead(A8);
  arr[9] = analogRead(A9);   
  arr[10] = analogRead(A10);
  sprintf(buf,"%d|%d|%d|%d|%d|%d|%d|%d|%d|%d|%d",arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9], arr[10]);
  Serial.println(buf);
  delay(1000);

}
