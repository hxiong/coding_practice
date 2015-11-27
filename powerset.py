"""
prompt: Given a set S, return the power set P(S), which is        
           a set of all subsets of S.                                
                                                                      
    Input:  A String                                                 
    Output: An Array with the power set of the input string           
                                                                      
    Example: S = "abc", P(S) = ['', 'a', 'b','c','ab','ac','bc','abc']                                                               *
                                                                      
    Note: There should not be any duplicates in the power set         
          ('ab' and 'ba' are considered the same), and it will always
          begin with an empty string ('')                             
                                               
"""

def power_set(str):
    result=[]
    result = permute_powerset(result,str,str)
    print result


def permute_powerset(result,str,remain,sub=""):
    result.append(sub)
      
    for i in range(len(remain)):
        temp=sub
        sub=sub+remain[i]
        result = permute_powerset(result,str,remain[i+1:],sub)
        sub=temp            
    
    return result       
        
        
def main():
    str='abcd'
    power_set(str)
   

if __name__ == '__main__':
    main()
