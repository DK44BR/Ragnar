#include <Arduino.h>
#include "RagnarCore.h"


RagnarCore Ragnar;


unsigned long inicio;


void RagnarCore::begin(){

    inicio = millis();

    Serial.println();
    Serial.println("==============================");
    Serial.println("       RAGNAR ESP32 CORE");
    Serial.println("==============================");

    Serial.println("Versao: 0.3");
    Serial.println("Status: ONLINE");

    Serial.println("==============================");

}



void RagnarCore::heartbeat(){

    Serial.println("[RAGNAR] Heartbeat");

    Serial.print("Uptime: ");
    Serial.print((millis() - inicio) / 1000);
    Serial.println("s");


    Serial.print("Memoria: ");
    Serial.println(ESP.getFreeHeap());

}
