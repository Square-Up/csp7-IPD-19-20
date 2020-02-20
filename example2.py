####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'Collude, Collude until betrayed'
strategy_description = 'First round collude, then if they have c as their most recent move, collude. Otherwise betray'
    
def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return'c'
  elif 'c' in their_history:
    return 'c'
  else:
    return 'b'