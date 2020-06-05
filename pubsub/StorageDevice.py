import paho.mqtt.client as paho
import time
import random
from datetime import datetime


DelayInPackets = 30  # defines the delay among each packet while sending to cloud 
DeviceName = "BrevarageDevice001" # name of the simulated device device 


def on_publish(client, userdata, mid):
     
     """
     This method execute after one message is published to the MQTT broker
     
     prints the number of message published 

     """
     
     print(" Message published : "+ str(mid)+"\n")


def date_time_now():
    """ 
    Returns the current date and time as a string 
    
    This is returned in the form defined by an explicit format string

    Returns
    -------
    date_time : str
        A string with the specified date time format

    """

    now = datetime.utcnow()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return date_time

def simulated_packet():

    """
    The method "simulated_packet" generates simulated values like the read device, 
    this generates simulated temperature , humidity, weight, heatbeat status, in this way 
    we replicate the real device, 

    return : dictionary data type  
    """
    
    simulatedTemp = random.randint(1,7)  # generates integer between 1 to 7 
    simulatedHumidity = random.randint(10,30) # generates integer between 10 to 30 
    weightOnboard = random.randint(20,40) # generates integer between 20 to 40 
    heatbeat = "0n" # sets the default heartbeat to on  
    
    # creates the "telemetryMessage"  dictionary object  that contains all the details along with deviceName and Timestamp 

    telemetryMessage = {"Temperature": simulatedTemp, "Humidity" : simulatedHumidity, 
                        "WeightOnbaord" : weightOnboard , "Heartbeat" : heatbeat,
                        "TimeStamp" : date_time_now() , "DeviceID" : DeviceName }


    return telemetryMessage # returns "telemetryMessage" dictionary 


def storage_device_init():

    """
    The method "storage_device_init" takes the simulated values dictionary and
    publish the message to broker, this include connection with the client, 
    it starts an infinite loop. 
    """

    client = paho.Client()  # creates the MQTT clinet 
    client.on_publish = on_publish # sets the callback method 
    client.connect("broker.mqttdashboard.com", 1883) # connection with the MQTT Broker 
    client.loop_start() # initiate the client 

    while True:
        
        publishMessage = simulated_packet() # gets the simulated message 
        print("The simulated message from storage device \n") 
        print(publishMessage) # prints the message 
        print("\n")
        (rc, mid) = client.publish("storageDevice/simulator", str(publishMessage), qos=1) # publish the message 
        
        time.sleep(DelayInPackets) # wait before executing the loop again 

if __name__ == "__main__":

    storage_device_init() 
