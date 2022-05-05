def line_up(hints):
    line = []
    for hint in hints:
        line.append(hint.split(' ')[0]) #get first colour from hint
        line.append(hint.split(' ')[2]) #get second colour from hint
        line.append(hint.split(' ')[5]) #get their relation
    
    # rearrange every couple of colurs such that the 
    # second one is on the left related to the first one
    for i in range(2,len(line),3): 
        if line[i] == 'right':
            a = line[i-2]
            line[i-2]=line[i-1]
            line[i-1] = a
            line[i] = 'left'
    #generate a dictionary with 0 value for each colour key
    colours = dict.fromkeys(line,0)
    del colours['left'] #remove unnecessary key
    
    #each time some colour is on the right it gets +1 to its value
    #we repeat it as many times as many colours we have
    #this generates a unique value to each colour
    for i in range(len(colours)):
        for j in range(2,len(line),3):
            if colours[line[j-2]] <= colours[line[j-1]]:
                colours[line[j-2]] += 1
    
    colours = {v: k for k, v in colours.items()} #swap keys and values
    
    out = []
    
    #fill return list based on the values at the color keys
    for i in range(len(colours)): 
        out.append(colours.get(i))  
    
    return out
