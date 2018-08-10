import time
import datetime
import numpy as np

#from w1thermsensor import W1ThermSensor
#imports, all essential, all already installed on the Pi. If using a new pi to install
#a module type "sudo apt-get install python3-modulename" you will need an internet connection


#Sets the LED pins, if the wiring for the LEDs is changed these pins will be incorrect

def inputno(g, a, lim1, lim2):
#This defines the function used to check user inputs are within range and of correct data type
    if g == 1:
        while True:
            try:
                h = int(input(a))
                if lim1 <= h <= lim2:
                    return h
                else:
                    print('x')
            except ValueError:
                print('x')
                continue
#If a wrong value is entered the Red LED will flash
                
def temperatures():
#Temperature probe management, this will not break and manages any exceptions, if the incorrect
    data = [(time.time()-start_time)]
    d = time.time()
    block = [1,2,3,4]
    for sensor in block:
        data.append(sensor)
    data.insert(1,(time.time()-start_time))
    y = (time.time()-d)
#For each available sensor the data from the sensor will be printed into the data list, this
#will cycle for as many sensors. The final insertion of the time ensures that the correct
#time corresponding to the final probe entering its data into the list is recorded
    return(y,data)
	
Menu = '0'
while Menu != 'q':
    Menu = input('Press 1 to begin log, press q to quit: ')

#Menu setup allowing the program to be run multiple times without turning the pi off
    now = datetime.datetime.now()
    if Menu == '1':
        frequency = inputno(1,'Frequency of data reading: ',1,100)
        length = int((inputno(1,'Run test for how many minutes: ',1,1500))*60/frequency)
#All relevant parameters, with incorrect user input checking
        i = 0
        start_time = time.time()
        array = np.zeros(6)
#sets up final array for data printing 
        try:
            while i <= length:
#When recording the red light shows
                z = temperatures()
                array = np.vstack([array,z[1]])
                time.sleep(frequency-z[0])
                i += 1
#Uses the temperature function to read the temperatures and insert them into the array, at 
#the frequency specified by the user
        except KeyboardInterrupt:
            pass            
#Allows the user to manually terminate the logging but preserve the data
        np.savetxt('Temperature Log-'+now.strftime("%Y-%m-%d %H-%M")+'.txt', array,fmt='%+3.3f')
#Final data printing into a file named with the time and date, final light switching to show the
#program has finished.			
			
		
			
		

	

	
	