"""
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). You can walk back and forth between rooms freely.Return true if and only if you can enter every room.
Example 1:
Input: [[1],[2],[3],[]]
Output: True
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: False
Explanation: We can't enter the room with number 2.

Note:
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.

"""


def canVisitAllRooms(rooms):
  
 
  visited = {}#a dictionary to keep a check on all visited room
   #initialise them to False
  for key in range(0, len(rooms)):
    visited[key] = False

  print(len(rooms[1]))
  visited[0] = True #start room
  not_visited = []
  
  #to traverse through all the rooms
  for i in range(0, len(rooms)):
    not_visited = rooms[i]
    for j in range(0, len(not_visited)):
      if i != not_visited[j]:
        k = not_visited[j]
        visited[k] = True

  for key in visited:
    if visited[key] == False:
      return False
  return True


if __name__ == "__main__":
  rooms = [[1], [2], [3], []]
  print(canVisitAllRooms(rooms))









