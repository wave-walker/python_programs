def checkanagrams(s1, s2):
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")
def main():
    s1=input("enter forst str: ")
    s2=input("enter forst str: ")
    checkanagrams(s1, s2)
if __name__=='__main__':
    main()