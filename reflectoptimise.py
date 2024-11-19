from dataclasses import dataclass
import scipy
import numpy

@dataclass
class cubesat:
    volume: float
    mass: float
    cost: float
    
@dataclass
class launchvehicle:
    maxpayload: float
    costperkilo: float
    
cubesats = [cubesat(12000,2.72,4),      #12
            cubesat(16000,3.57,4.2),    #16
            cubesat(24000,5.28,5.5),    #24
            cubesat(36000,7.85,8.4),    #36
            cubesat(48000,10.42,10.8),  #48
            cubesat(60000,12.99,13),    #60 
            cubesat(72000,15.56,15.2)]  #72

lauchvehicles= [launchvehicle(800,	6000),   #SpaceX Rideshare
               launchvehicle(1000,	15000),  #Firefly Alpha
               launchvehicle(5000,	15000),  #Soyuz
               launchvehicle(2000,	19000),  #Vega
               launchvehicle(300,	24000)]  #Electron




