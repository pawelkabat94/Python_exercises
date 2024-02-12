isAutomaticMode = False
print("Automatic Mode:",isAutomaticMode)
# automatic mode is on

is80PercentLight = False
print("Is the light good:",is80PercentLight)
# is the level of day-light above 80%

isDirectLight = True
print("Is sun low:",isDirectLight)
# is the Sun ligthing directly into the driver's face

isRainy = True
print("Is Rainy:",isRainy)
# is it rainy, foggy or other weather conditions are present

turnthelights = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("Turn the lights on:",turnthelights)