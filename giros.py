#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.INCH
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

# Gira 90 grados a la derecha desde el punto 0
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)  

# Gira 90 grados para volver al punto 0
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 90) 

# Gira 180 grados a la izquierda
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 180)  

# Gira 180 grados para volver al punto 0
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 180)  
