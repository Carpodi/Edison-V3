#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.INCH
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

# Move forward
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 4) 
# Turn left
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 80)
# Move forward
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 3) 
# Straighten up
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 80)
# Move forward
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 6)
