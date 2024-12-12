import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.INCH 
Ed.Tempo = Ed.TEMPO_MEDIUM 
for _ in range(20): 
Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 1) 
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_2, 20)  
