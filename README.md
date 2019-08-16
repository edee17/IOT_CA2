**ST0324 Internet of Things CA2 Step-by-step Tutorial**

##### SCHOOL OF COMPUTING (SOC)

# IOT CA2 SmartCCTV

# Step-by-step Tutorial

ST 0324 Internet of Things (IOT)

## Table of Contents


- Section 1 Overview of SmartCCTV
- Section 2 Hardware requirements
- Section 3 Hardware setup
- Section 4 Create a “Thing”
- Section 5 DynamoDB Setup
- Section 6 AWS S3 Setup
- Section 7 Program setup
- Section 8 Web Interface setup
- Section 9 Expected outcome


## Section 1 Overview of SmartPark

### A. What is SmartCCTV about?

This application is inspired by an incident that happened to my uncle’s 2 Year Old child while he was in his room at Level 2 and my Uncle was at the Living Room which is at Level 1. So my uncle’s house is somewhat of a Smart Home where Lights are controlled by Motion Sensor but one day, while my uncle was at the Living Room, he heard a loud thud sound coming from Level 2 and to his horror, his baby was lying on the floor crying. So, this inspired me to create this application called ‘Smart CCTV’ where you can monitor the Temperature and Humidity of the room, Take a Photo of the room regularly and also sense if the Lighting is too dark or too bright.

### B. How does the final RPI set-up looks like?

```
Final Set-up
```

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/RPI_Setup.jpg "Optional title")

```
Overview of SmartCCTV
```

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/SystemArchitectureDiagram.jpg "Optional title")


### C. How does the web application look like?
![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/WebApp.jpg "Optional title")

## Section 2 Hardware Requirements

### A. Hardware checklist

##### 1 Light-Dependant Resistor (LDR)

a) Light-Dependant Resistor (LDR) is a photo conductive sensor. It is a variable resistor that changes it’s resistance in a proportion to the light exposed to it. Its resistance decreases with the intensity of light. In this case, the resistance is higher when it is dark. We will use this hardware to tell if the room is bright or dark.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/LDR.jpg "Optional title")

##### 1 Analog-to-Digital Converter

a) The MCP3008 is a low cost 8-channel 10-bit analog to digital converter.  The precision of this ADC is similar to that of an Arduino Uno, and with 8 channels you can read quite a few analog signals from the Pi.  This chip is a great option if you just need to read simple analog signals, like from a temperature or light sensor.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/MCP3008ADC.jpg "Optional title")

##### 2 10K Ω Resistors

a) Resistors are used to change the amount of current flowing through a part of the circuit. This is often used as a means of protecting components which cannot handle large currents.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/10KResistor.jpg "Optional title")

##### 1 DHT11 Sensor

a) The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/DHT11.jpg "Optional title")

## Section 3 Hardware setup

In this section, we will connect all the components shown in Section 2.

### Fritzing Diagram

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/FritzingDiagram_CA2.png "Optional title")
