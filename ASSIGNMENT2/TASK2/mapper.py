#!/usr/bin/env python3

import sys,json

def dot(a,b):
    val=0
    for x,y in zip(a,b):
        val+=x*y
    return val

def get_similarity(a,b):
    similarity=dot(a,b)/(dot(a,a)*dot(b,b))**0.5
    return similarity


initial_pagerank={}

with open(sys.argv[1]) as v:
    for line in v:
        a,b=line.strip().split(',')
        a,b=int(a),float(b)
        initial_pagerank[a]=b
with open(sys.argv[2]) as embed:
    vectors=json.load(embed)

for y in sys.stdin:
    page,pointers=y.strip().split('?')
    pointers=eval(pointers)
    contri=initial_pagerank.pop(int(page))/len(pointers)
    from_vector=vectors[str(page)]
    M={i:contri*get_similarity(from_vector,vectors[str(i)]) for i in pointers}
    print(page,M,sep="?")
