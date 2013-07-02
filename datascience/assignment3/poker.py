# Python Mapper() : Given unique 5-card hand (csv string), return the made hand.
# e.g. 'flush', 'straight', etc  
def Mapper(jsmr_context, dataline): 
  cards = dataline.split(',')  # 5 cards like 'QH' (for Q of hearts) 

  # Get counts of all faces and suits. 
  counts = ({ 
      '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'T':0, 
      'J':0, 'Q':0, 'K':0, 'A':0, 
      'S':0, 'C':0, 'D':0, 'H':0 
    }) 
  for card in cards: 
    face = card[0] 
    suit = card[1] 
    counts[face] += 1 
    counts[suit] += 1 

  is_flush = ( 
      (counts['S'] == 5) or 
      (counts['C'] == 5) or 
      (counts['D'] == 5) or 
      (counts['H'] == 5)) 

  is_straight = False 
  straightrunfaces = 'A23456789TJQKA';  # note: ace ('A') appears twice
  for i in range(0, 10): 
    if (counts[straightrunfaces[i]] and 
        counts[straightrunfaces[i+1]] and 
        counts[straightrunfaces[i+2]] and 
        counts[straightrunfaces[i+3]] and 
        counts[straightrunfaces[i+4]]): 
      is_straight = True 
      break 

  is_4handstraight = False 
  for i in range(0, 11): 
    if (counts[straightrunfaces[i]] and 
        counts[straightrunfaces[i+1]] and 
        counts[straightrunfaces[i+2]] and 
        counts[straightrunfaces[i+3]]): 
      is_4handstraight = True 
      break 

  is_quad, is_trip, is_pair, is_two_pair = False, False, False, False 
  faces = 'A23456789TJQK' 
  for i in range(0, len(faces)): 
    face_count = counts[faces[i]] 
    if face_count == 4: 
      is_quad = True 
    elif face_count == 3: 
      is_trip = True 
    elif face_count == 2: 
      if is_pair:  # saw another pair before? 
        is_two_pair = True 
      is_pair = True 
 
  # Emit output: a (stringized) count of '1' for the detected hand.
  if is_straight and is_flush: 
    jsmr_context.Emit('straightflush', '1') 
  elif is_quad: 
    jsmr_context.Emit('4ofakind', '1') 
  elif is_trip and is_pair: 
    jsmr_context.Emit('fullhouse', '1') 
  elif is_flush: 
    jsmr_context.Emit('flush', '1') 
  elif is_straight: 
    jsmr_context.Emit('straight', '1') 
  elif is_4handstraight:
    jsmr_context.Emit('4cardstraight', '1')
  elif is_trip: 
    jsmr_context.Emit('3ofakind', '1') 
  elif is_two_pair: 
    jsmr_context.Emit('2pair', '1') 
  elif is_pair: 
    jsmr_context.Emit('pair', '1') 
  else: 
    jsmr_context.Emit('highcard', '1') 
