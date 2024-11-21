from dataclasses import dataclass
import scipy
import numpy

@dataclass
class cubesat:
    volume: float        #Units
    structuremass: float #kg
    cost: float          #thousands of dollars
    
@dataclass
class launchvehicle:
    maxpayload: float  #kg
    costperkilo: float #thousands of dollars
    
@dataclass
class mirror:
    size: float          #m
    area: float          #m^2
    effectivearea: float #m^2
    totalmass: float     #kg
    totalvolume: float   #Units
    
@dataclass
class attitudecontrolsystem:
    name: str
    mass: float   #kg
    volume: float #Units
    power: float  #W
     
@dataclass#god help me
class attitudecontrolsystemstruct:
    reactionwheel: attitudecontrolsystem = attitudecontrolsystem("Reaction Wheel (single)",0.375,0.068,1.9)
    magnetorquersystem: attitudecontrolsystem = attitudecontrolsystem("Magnetorquer system",	0.5,	0.4,	1)
    gpsreciever: attitudecontrolsystem = attitudecontrolsystem("GPS Receiver",	0.024,	0.03,	0.125)
    startracker: attitudecontrolsystem = attitudecontrolsystem("Star tracker (single)",	0.28,	0.25,	0.7)
    sunsensor: attitudecontrolsystem = attitudecontrolsystem("Sun sensor (single)",	0.01,	0,	0.01)
    inertialmeasurementunit: attitudecontrolsystem = attitudecontrolsystem("Inertial Measurement Unit (IMU)",	0.15,	0.025,	0.2)

acs = attitudecontrolsystemstruct()
            
@dataclass
class communicationandobdh:
    mass: float   #kg
    volume: float #Units
    power: float  #W

totalcomms = communicationandobdh(0.675, 0.6, 5.55)



cubesats = [cubesat(12,2.72,4000),    #12U
            cubesat(16,3.57,4200),    #16U
            cubesat(24,5.28,5500),    #24U
            cubesat(36,7.85,8400),    #36U
            cubesat(48,10.42,10800),  #48U
            cubesat(60,12.99,13000),  #60U
            cubesat(72,15.56,15200)]  #72U

lauchvehicles = [launchvehicle(800,6000),    #SpaceX Rideshare
                 launchvehicle(1000,15000),  #Firefly Alpha
                launchvehicle(5000,15000),   #Soyuz
                launchvehicle(2000,19000),   #Vega
                launchvehicle(300,24000)]    #Electron

mirrors = [launchvehicle(5, 	25, 	19.6,	2.09,	2.0),#see first value
           launchvehicle(6, 	36, 	28.3,	2.33,	2.5),
           launchvehicle(7, 	49,     38.5,	2.6,	3.0),
           launchvehicle(8, 	64,	    50.3,	2.89,	3.5),
           launchvehicle(9, 	81,	    63.6,	3.2,	4.5),
           launchvehicle(10,	100,	78.5,	3.54,	5.0),
           launchvehicle(12,	144,	113.1,	4.29,	7.0),
           launchvehicle(14,	196,	153.9,	5.12,	9.0),
           launchvehicle(16,	256,	201.1,	6.06,	11.0),
           launchvehicle(18,	324,	254.5,	7.1,	13.5),
           launchvehicle(20,	400,	314.2,	8.23,	16.5),
           launchvehicle(25,	625,	490.9,	11.47,	25.0),
           launchvehicle(30,	900,	706.9,	15.31,	35.0),
           launchvehicle(35,	1225,	962.1,	19.76,	47.0),
           launchvehicle(40,	1600,	1256.6,	24.8,	60.5)]

attitudecontrolsystems = [acs.reactionwheel, #kinda obvious
                          acs.magnetorquersystem,
                          acs.gpsreciever,
                          acs.startracker,
                          acs.sunsensor,
                          acs.inertialmeasurementunit,]


    
    

