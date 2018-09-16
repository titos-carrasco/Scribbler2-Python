#include <SoftwareSerial.h>
SoftwareSerial S2Serial( D2, D3, true, 256 );

#include <ESP8266WiFi.h>
String MySSID = String( "NodeMCU-" ) + String( ESP.getChipId() );
#define MyPASS  "1234567890"
#define MyIP    IPAddress( 192, 168, 145, 1 )
#define MyMask  IPAddress( 255, 255, 255, 0 )
#define MyGw    MyIP
#define MyPort  1500
WiFiServer server( MyPort );

byte ledState = 0;
unsigned long lastBlink = 0;

void setup() {
  // para debug
  Serial.begin( 115200 );
  Serial.println();
  pinMode( LED_BUILTIN, OUTPUT );

  // conexión con el S2 a través de la puerta RS232
  S2Serial.begin( 38400 );
  
  // configurando el ESP8266 como AP
  //ESP.eraseConfig();
  Serial.println( "Ajustando valores del ESP8266..." );
  WiFi.mode( WIFI_OFF );
  WiFi.disconnect();
  WiFi.softAPdisconnect();
  WiFi.setPhyMode( WIFI_PHY_MODE_11B );
  delay( 2000 );

  Serial.print( "Configurando AP... " );
  WiFi.mode( WIFI_AP );
  WiFi.softAPConfig( MyIP, MyGw, MyMask );
  WiFi.softAP( MySSID.c_str(), MyPASS );
  Serial.print( MySSID );
  Serial.print( ", " );
  Serial.println( MyPASS );
  delay( 2000 );

  Serial.println( "Inicializando Server..." );
  server.begin();

  Serial.print( "Esperando conexiones en " );
  Serial.print( WiFi.softAPIP() );
  Serial.print( ":" );
  Serial.print( MyPort );
  Serial.println( "..." );
  Serial.print( "Ejecute socat:$ socat -d -d pty,raw,echo=0 tcp4:" );
  Serial.print( WiFi.softAPIP() );
  Serial.print( ":" );
  Serial.println( MyPort );
}

void loop() {
  // para indicar que estamos vivos
  unsigned long t = millis();
  if( t - lastBlink >= 1000UL ){
    ledState = ledState ? LOW : HIGH;
    digitalWrite( LED_BUILTIN, ledState );
    lastBlink = t;
  }

  // Espera por una conexión
  delay(10);
  WiFiClient client = server.available();
  if( !client ) return;
 
  Serial.println( "Conexión Establecida..." );
  while( client.connected() ){
    while( client.available() )
      S2Serial.write( client.read() );
    yield();
    while( S2Serial.available() )
      client.write( S2Serial.read() );
    yield();
  }    

  Serial.println( "Desconectado!!!" );
  Serial.print( "Esperando conexiones en " );
  Serial.print( WiFi.softAPIP() );
  Serial.print( ":" );
  Serial.print( MyPort );
  Serial.println( "..." );
}

