####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Collude, then alternate every 2 rounds'
strategy_description = 'Collude first and the after alternate every two rounds.'
    
def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'c'
  elif len(my_history)%3 == 0:
    return 'b'
  else:
    return 'c'
    
    #history: a string with one letter (c or b) per round that has been played with this opponent.
    #their_history: a string of the same length as history, possibly empty. 
    #The first round between these two players is my_history[0] and their_history[0]
    #The most recent round is my_history[-1] and their_history[-1]
    
    #Returns 'c' or 'b' for collude or betray.
    #'''
    
    # This player always colludes.
    #return 'c'

  #''' Arguments accepted: my_history, their_history are strings.
  #my_score, their_score are ints.
  #Make my move.
  #Returns c or b. 
  #'''

