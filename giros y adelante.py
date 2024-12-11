#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.INCH
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------


# Moverse hacia adelante
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 4) 
# Girar hacia la izquierda 
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 80)
#Hacia adelante
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 3) 
# Enderezarse 
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 80)
# Hacia adelante
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 6) 
