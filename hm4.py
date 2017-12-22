import json
with open("C:\\Users\\lucad\\OneDrive\\ADM\Homework 4\\full_dblp.json","r",encoding="utf-8") as f:
    data=json.load(f)

data[0]

# create a dict where each key is an author_id and each value is its list of id_publication_int

D={} 

for i in data:
    for j in i['authors']:
        D[j['author_id']]=[]        
        
for i in data:
    for j in i['authors']:
        D[j['author_id']].append(i['id_publication_int'])
            
# define Jaccard similarity

def js(a,b):
    union=set(a+b)
    intersection=[]
    for i in a:
        if i in b:
            intersection.append(i)
    return len(intersection)/len(union)

# create a graph where each author is a node and each edge exists if the two authors have at least a common publication; then attribute a mass for each edge and id, conferences and publications for each node

import networkx as nx
G=nx.Graph()

for i in data:
    for j in i['authors']:
        G.add_node(j['author_id'],id=j['author_id'],id_conferences=[],id_publications=[])
    for u in i['authors']:
        for v in i['authors']:
            if u['author_id']!=v['author_id'] and u['author_id'] not in G.neighbors(v['author_id']):
                G.add_edge(u['author_id'],v['author_id'])
                G[u['author_id']][v['author_id']]['weight']=1-js(D[u['author_id']],D[v['author_id']])

for i in data:
    for j in i['authors']:
        G.node[j['author_id']]['id_conferences'].append(i['id_conference_int'])
        G.node[j['author_id']]['id_publications'].append(i['id_publication_int'])

G.node
nx.info(G)
G.degree()
G.adj
nx.draw(G,node_shape='.',node_size=5)

# =============================================================================
# 
# =============================================================================

# given a conference in input, return the subgraph induced by the set of authors who published at the input conference at least once. Once you have the graph, compute some centralities measures (degree, closeness, betweeness) and plot them.

conference=int(input()) # write an id_conference_int in input (16501)

lst1=[]
for i in data:
    for j in i['authors']:
        if i['id_conference_int']==conference:
            lst1.append(j['author_id']) 

G2=nx.subgraph(G,lst1)
nx.draw(G2,node_shape='.',node_size=5)

# degree centrality

from operator import itemgetter
lst2=sorted(G2.degree(),key=itemgetter(1),reverse=True)
print('The node with highest value of degree is',lst2[0][0],'with degree =',lst2[0][1])

# closeness centrality

node=int(input('Insert a node: '))
d=0
for i in G2.node:
    if node in list(nx.ego_graph(G2,i,len(G2.node))):
        d+=nx.shortest_path_length(G2,node,i)
print('The closeness Centrality of the input node',node,'is: ',1/d)

# given in input an author and an integer d, get the subgraph induced by the nodes that have hop distance (i.e., number of edges) at most equal to d with the input author. Then, visualize the graph.

author=int(input()) # write an author_id in input (Aris=256176)
d=int(input()) # pivot for the hop distance

G3=nx.ego_graph(G,author,d)
nx.draw(nx.ego_graph(G,author,d),node_shape='.',node_size=5)

# =============================================================================
# 
# =============================================================================

# Write a Python software that takes in input an author (id) and returns the weight of the shortest path that connects the input author with Aris. Here, as a measure of distance you use the weight w(a1,a2) defined previously.

aris=author
authorX=int(input()) # 519479

def sp(G,a1,a2=aris): # weight of the shortest path (Dijkstra)
    lst=nx.dijkstra_path(G,a1,a2,weight='weight')
    sum_weight=0
    i=0
    while i<len(lst)-1:
        sum_weight+=G[lst[i]][lst[i+1]]['weight']
        i+=1
    return sum_weight

sp(G,authorX,aris)

# Write a Python software that takes in input a subset of nodes (cardinality smaller than 21) and returns, for each node of the graph, its GroupNumber, defined as follow: GroupNumber(v) = min {ShortestPath(v,u)}, where v is a node in the graph and I is the set of input nodes u's. You must implement from scratch the algorithm to compute the shortest path. Moreover, if you can, try to think if there is a way to exploit the properties of the shortest path algorithm to avoid performing the same computations multiple times.

I=[] # 256176, 519479
n=0
while n<20:
    I.append(int(input('Write an author_id or "stop" to break the loop: ')))
    if input=='stop': # write "stop" to stop if I want |I|<21
        break
    n+=1

I=list(set(I)) # to remove duplicate nodes



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
    
GroupNumber(G,I)