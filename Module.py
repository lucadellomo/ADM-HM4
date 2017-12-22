def js(a,b): # jacard similarity
    union=set(a+b)
    intersection=[]
    for i in a:
        if i in b:
            intersection.append(i)
    return len(intersection)/len(union)

def sp(G,a1,a2=aris): # weight of the shortest path (Dijkstra)
    lst=nx.dijkstra_path(G,a1,a2,weight='weight')
    sum_weight=0
    i=0
    while i<len(lst)-1:
        sum_weight+=G[lst[i]][lst[i+1]]['weight']
        i+=1
    return sum_weight

def GroupNumber(G,I):
    I=list(set(I)) # to remove duplicate nodes    
    for v in G.node:
        m=list(range(100))
        for u in I:
            if u in list(nx.ego_graph(G,v,len(G.node))):
                if nx.shortest_path_length(G,v,u)<=len(m):
                    m=nx.shortest_path(G,v,u)
        if m!=list(range(100)):
            print('GropuNumber of',v,'is:',m)
