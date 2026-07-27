#include <Arduino.h>
#include "RagnarCore.h"



void setup(){

    Serial.begin(115200);

    delay(1000);

    Ragnar.begin();

}



void loop(){

    Ragnar.heartbeat();

    delay(5000);

}
