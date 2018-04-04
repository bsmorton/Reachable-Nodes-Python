# Submitter: bmorton(Morton, Brad)
import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    f=file.readlines()
    d={line[0]:set({}) for line in f}
    for line in f: 
        d[line[0]].add(line[2])
    file.close()
    return d
        


def graph_as_str(graph : {str:{str}}) -> str:
    r=sorted([[key,[val for val in graph[key]]]for key in graph.keys()])
    s=''
    for item in r: s+='  {} -> {}\n'.format(item[0],sorted(item[1]))
    return s

       
def reachable(graph : {str:{str}}, start : str) -> {str}:
        p=set()
        l=[start]
        if start not in graph.keys():
            return None
        while len(l)!=0:
            q=l.pop()
            p.add(q)
            if graph.get(q)!=None:                
                for item in graph.get(q):
                    if item not in p:
                        l.append(item)
        return p
            
    
        





if __name__ == '__main__':
    # Write script here
    file=input('Enter the name of any file with a graph:')
    graph=read_graph(open(file))
    print()
    print('Graph: source -> [destination] edges')
    print(graph_as_str(graph))
    print()
    while True:
        n=input('Enter the name of any starting node:')
        if n=='quit':
            break
        if reachable(graph,n)==None:
            print('Entry Error: '+n+';  Illegal: not a source node\nPlease enter a legal String')
        else:
            print('From e the reachable nodes are',reachable(graph,n))
        print()
    
    #reachable(read_graph(open('graph2.txt')), 'a')          
    # For running batch self-tests
    print()
    #import driver
    #driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    #driver.driver()
