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

## Section 4 Create a “Thing”

#### Setting Up Your “Thing”

a) First, navigate to AWS website and click on services and search for IOT Core.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/AWS_Services.PNG "Optional title")

b) In the manage console, select things and choose register a thing.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/RegisterAThing.png "Optional title")

c) Select Create a single thing.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreateAThing.png "Optional title")

d) Enter a name for your thing, MyRaspberryPi. Click next.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/AddDeviceToThing.png "Optional title")

e) Click create certificate. Download all four files. As for the root CA, download the Root CA1 certificate file.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CertificateCreated.png "Optional title")

f) Rename the four files accordingly.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CertificateName.png "Optional title")

g) Copy these four files into the same directory in the raspberry pi.

h) Click Activate.

i) Click register thing.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/RegisterThing.png "Optional title")

j) Navigate to policies under the secure section. Click create a policy.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/NavigateToPolicies.png "Optional title")

k) Enter a name for your policy.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreatePolicy.png "Optional title")

l) Navigate to certificates under secure section. Select the certificate you created previously, and click attach policy. Attach the policy that you have just created.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/AttachPolicy.png "Optional title")

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/PolicyAttached.png "Optional title")

m) Select the certificate you created previously again, and click attach thing. Attach the thing you created previously.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/AttachThing.png "Optional title")

#### Create AWS Role

a) Click on IAM service.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/AWS_Services.PNG "Optional title")

b) Click Create Role, choose AWS Service, then IOT.

c) On this page, input a name.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreateRole.png "Optional title")

d) Copy and Paste the REST API endpoint of the Thing and also the ARN into a Notepad.

## Section 5 DynamoDB Setup

#### DynamoDB

a) First, navigate to DynamoDB within the AWS website by clicking on services, then DynamoDB. Click create table.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/AWS_Services.PNG "Optional title")

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreateDynamoDB.png "Optional title")

b) Enter the table name and other info as stated below, then click create.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreateDynamoDBInfo.png "Optional title")

e) Next, navigate back to IoT Core within the AWS website by clicking on services, then IoT Core. Click Act, then create button at the top right corner.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/NavigateToRule.png "Optional title")

f) Create the rule.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreateRule.png "Optional title")

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/RuleQueryStatement.png "Optional title")

g) In Set one or more actions, choose Add action, then select "Split messages into multiple columns of DynamDB table (DynamoDBv2).

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/SetAction.png "Optional title")

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/SplitMessage.png "Optional title")

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/SplitMessageInfo.png "Optional title")

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/SplitMessageInfo2.png "Optional title")

## Section 6 AWS S3 Setup

I used AWS S3 to recognize if there is any object blocking the camera.

#### Creation of S3 Bucket

a) In the AWS console, search for S3

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/AWS_Services.PNG "Optional title")

b) Click Create Bucket.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreateBucket.png "Optional title")

c) Enter the details as shown below

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/CreateBucketInfo.png "Optional title")

## Section 7 Program Setup

The following installation are needed to run the files.

### A. Installing Necessary Libraries

a) Install flask.

```
sudo pip install flask
```

b) Install Gevent.

```
sudo pip install gevent
```

c) Install awscli.

```
sudo pip install awscli
```

d) Install botocore.

```
sudo pip install botocore
```

e) Install Boto3

```
sudo pip install boto3
```

f) Install Paho-MQTT

```
sudo pip install paho-mqtt
```

g) Upgrade

```
sudo pip install --upgrade --force-reinstall pip==9.0.3
sudo pip install AWSIoTPythonSDK --upgrade --disable-pip-version-check
sudo pip install --upgrade pip
```

### B. aws_pubsub_edited.py

This python file is needed to subscribe the LDR Sensor to MQTT and also store its values into DynamoDB.

### C. dynamodb.py

This python file will get and send the light values to the web page. The program will subscribe to topic sensors/lights. Once it receives the light values from topic sensors/lights, it will access the DynamoDB table called iotdata and retrieve the light values.

### D. picam_s3_rekognition_1_server.py

This python file host the web page. The web page will enable us to take photo of the surroundings, check temperature and humidity and also light values.

## Section 9 Web interface setup

The following files are required to get the style of the webpage.

![Alt text](https://github.com/edee17/IOT_CA2/blob/master/README(IMAGES)/WebAppSetup.png "Optional title")

## Section 10 Expected outcome

To test if the program works, you can visit this link here! https://youtu.be/UBYAjOURmOw
