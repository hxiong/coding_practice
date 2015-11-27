"""
bugs resolved:
1. result.append(sub) got "Nonetype cannot append error"
2. sub was not reset before the next iteration of for loop; result was wrong
"""

# produce anagrams
def anagrams(str):
    result_d=[]
    # breadth first
    result_b=[]
    node_tp=("",str)
    nodes_q=[node_tp]
    rtn_tp=(result_b,nodes_q)     # permute_breadth return value
    
  #  print type(result)
    result_d=permute_depth(result_d,str,str)
    
    rtn_tp = permute_breadth(rtn_tp,str)
    result_b = rtn_tp[0]
    
    print "result_d:",result_d
    print "result_b:", result_b
    

def permute_breadth(rtn_tp,str):   #node_tp(sub,remaining)
    if(len(rtn_tp[1]) == 0):
        return rtn_tp
    
    #pop one from nodes_q
    nodes_q = rtn_tp[1]
    node_tp = nodes_q[0]
    del nodes_q[0]
    
    if(len(node_tp[0]) == len(str)):
        rtn_tp[0].append(node_tp[0])
        return rtn_tp
    
    remain=node_tp[1]
    sub = node_tp[0]
    
    for i in range(len(remain)):
        temp = sub
        temp2 = remain
        
        sub = sub + remain[i]
        remain = remain[:i]+remain[i+1:]
        nodes_q.append((sub,remain))
        
        sub=temp
        remain = temp2
    
    rtn_tp = permute_breadth(rtn_tp,str)
    return rtn_tp
    
        

def permute_depth(result,str,remain,sub=""):
  #  print sub,remain, type(result),result
    
    if(len(sub) == len(str)):
        result.append(sub)
        return result
        
    for i in range(len(remain)):
        temp=sub
        sub=sub+remain[i]
        result = permute_depth(result,str,remain[0:i]+remain[i+1:],sub)
     #   print "result:",result,"sub:",sub, "remain:",remain
        sub=temp
    
    return result
        
        
        
    

def main():
    str='abc'
    anagrams(str)
   

if __name__ == '__main__':
    main()
