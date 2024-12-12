#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

Ed.Drive(Ed.FORWARD, Ed.SPEED_8, 36)
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_6, 70)

Ed.Drive(Ed.FORWARD, Ed.SPEED_6, 16)
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_8, 104)
Ed.Drive(Ed.FORWARD, Ed.SPEED_8, 39)

Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_6, 65)
Ed.Drive(Ed.FORWARD, Ed.SPEED_8, 15)

Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_8, 60)
Ed.Drive(Ed.FORWARD, Ed.SPEED_6, 13)
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_8, 60)
Ed.Drive(Ed.FORWARD, Ed.SPEED_6, 13)
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_8, 60)
Ed.Drive(Ed.FORWARD, Ed.SPEED_6, 13)

Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_8, 98)
Ed.Drive(Ed.FORWARD, Ed.SPEED_7, 38)

Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_6, 100)
Ed.Drive(Ed.FORWARD, Ed.SPEED_6, 30)
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_6, 105)
Ed.Drive(Ed.FORWARD, Ed.SPEED_10, 40)
