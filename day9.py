"""
Hunt a new Apartment:
You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimize its location. 
You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment.
The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question.
For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.
In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.
Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

sample output:
3 
Explanation
At index 3, the farthest you'd have to walk to reach a gym, school, or a store is 1 block; at any other index, you'd have to walk farther
"""

def apartmentHunting(blocks, reqs):
  cost = [{} for i in range (len(blocks))]
  Totalcost = float('inf')
  r = float('inf')
  for i in range(0, len(blocks)):
    for key in reqs:
      if blocks[i][key] is True:#if the requirement is True i.e. in the block then cost is zero
        cost[i][key] = 0
      if blocks[i][key] is not True:#if the requirement is False i.e. in the block then calculate the minimum cost
       for j in range(0, len(blocks)):
         if blocks[j][key] == True:# when the requirement is True then compare the current distance with that of initial found distance, and find the minimum
           if abs(j-i) < r:
             r = abs(j-i)
       cost[i][key] = r
       r = float('inf')
  
  l = []
 #convert dictionary to list
  for i in range (0, len(cost)):
    values = []
    for key in reqs:
      values.append(cost[i][key])

    l.append(values)

  # compare the max of each inner list with the total cost, if less then set that value
  for i in range(0, len(l)):

   if max(l[i]) < Totalcost:
     
     Totalcost = max(l[i])
     k = i
  return k
 
  
blocks = [
 {"gym": False, "school": True, "store": False},
 {"gym": True, "school": False, "store": False},
 {"gym": True, "school": True, "store": False},
 {"gym": False, "school": True, "store": False},
 {"gym": False, "school": True, "store": True}
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))