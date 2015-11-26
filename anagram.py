"""
bugs resolved:
1. result.append(sub) got "Nonetype cannot append error"
2. sub was not reset before the next iteration of for loop; result was wrong

"""

# produce anagrams
def anagrams(str):
    result=[]
  #  print type(result)
    result=permute_depth(result,str,str)
    return result

def permute_depth(result,str,remain,sub=""):
    print sub,remain, type(result),result
    
    if(len(sub) == len(str)):
        result.append(sub)
        return result
        
    for i in range(len(remain)):
        temp=sub
        sub=sub+remain[i]
        result = permute_depth(result,str,remain[0:i]+remain[i+1:],sub)
        print "result:",result,"sub:",sub, "remain:",remain
        sub=temp
    
    return result
        
        
        
    

def main():
    str='abc'
    remain = anagrams(str)
    print type(remain)
    print str
    print remain

if __name__ == '__main__':
    main()
