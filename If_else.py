#Likes and Shares promo

minLikes = 500
minShares = 100

numLikes = 800
numShares = 99

if numLikes >= minLikes and numShares >= minShares:
    print("You're entitled to get 10% promo.")
elif numLikes >= minLikes and numShares <= minShares:
    print ("You don't have enough shares")
elif numLikes <= minLikes and numShares >= minShares:
    print ("You don't have enough likes")
else:
    print("Sorry, you are not entitled to get 10% promo.")


#Pizza promo

isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = True

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print ("You receive the coupon for free burger!")
else:
    print ("Sorry, you are not entitled to take part in free burger promo.") 


#Disk size

DiskSize = 100
DiskSizeUsed = 90
FileSize = 20

if DiskSize - DiskSizeUsed >= FileSize:
    print ("You can save the file, there is enough space on disk.")
else: 
    print ("Disk space is not enough, you cannot download the file.")


#Engine check
isCheckCompleted = True

print ("Engine check is completed" if isCheckCompleted else "Engine check is not yet completed.")

#InfluenzaCheck

musclePain = False
Fever = True
Weakness = False

if musclePain and Fever and Weakness:
    print ("You might have influenza")
elif Weakness and (not Fever or not musclePain):
    print ("This might be just muscle issue, go rest.")
else:
    print ("This might be only sickness")
