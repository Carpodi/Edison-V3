#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.INCH
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

# Turn 90 degrees to the right from point 0
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)  

# Turn 90 degrees to return to point 0
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 90) 

# Turn 180 degrees to the left
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 180)  

# Turn 180 degrees to return to point 0
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 180)
# --- Made by Carpodi | carpodi.is-a.dev ---
