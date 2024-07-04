"""A simple library providing functions returning GCODE commands"""
def moveTopSpeed(x: int = 0, y: int = 0, z: int = 0) -> str:
  """Returns an instruction to move at top speed to the selected location. Used for positioning."""
  return "G00 X{xcoord} Y{ycoord} Z{zcoord}".format(xcoord=x,ycoord=y,zcoord=z)

def moveNormalSpeed(x: int = 0, y: int = 0, z: int = 0, s: int = 1000) -> str:
  """Returns an instruction to move at a selected speed to the selected location. Used for normal operation."""
  return "G01 X{xcoord} Y{ycoord} Z{zcoord} F{speed}".format(xcoord=x,ycoord=y,zcoord=z,speed=s)

def changePosMode(absMode = True) -> str:
  """Returns an instruction to change the positioning mode from absolute to relative or vice-versa, depending on the selected mode."""
  if absMode:
    return "G90"
  else:
    return "G91"

def changeUnitMode(mm = True) -> str:
  """Returns an instruction to change the unit mode from inches to millimetres or vice-versa, depending on the selected mode."""
  if mm:
    return "G21"
  else:
    return "G20"

