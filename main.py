
def count_batteries_by_usage(cycles):
  #initilize 3 counter variables
  low=0
  medium=0
  high=0
       	#classifying them based on the given condiions of being low medium and high
  for batcharge in cycles:
    #ittirate through each value in the list
    if (batcharge<310) :
      low+=1
    elif (batcharge >309) and (batcharge < 930):
      medium+=1
    else (batcharge >929):
      high+=1
      
      
 #return the values based on the classification information   
  return {
    "lowCount": low,
    "mediumCount": medium,
    "highCount": high
  }

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")
    
  #edge or boundary conditions
  counts = count_batteries_by_usage([100, 309, 310, 929, 900, 930])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 2)
  assert(counts["highCount"] == 2)
  print("Done counting :)")
 # a custom to take input from the user
def take_inputs():
  n=int(input("Enter the number of batteries you want check efficiency cycle "))
  cycles=[]
  print("Enter the cycles")
  for cycle in range(0,n):
    cycles.append(int(input()))
  return cycles
  
  


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
