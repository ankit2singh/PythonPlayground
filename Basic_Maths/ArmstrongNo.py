def problemstatement():
 '''
Example 1:
Input:N = 153
Output:True
Explanation: 13+53+33 = 1 + 125 + 27 = 153
Example 2:
Input:N = 371
Output: True
Explanation: 33+53+13 = 27 + 343 + 1 = 371
'''


def checkArmstrong(n):
    org = n
    power = len(str(n))
    final_no = 0
    while(n>0):
        k = n%10  # 153 -> 3
        final_no += k**power  # 0+9
        n = n//10  # n = 15
        # return final_no
    
    if final_no == org:
      return True 
    else :
      return False
    
print(checkArmstrong(1533)) #
