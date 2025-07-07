def pal(s, l, r):
    if l>=r:
        return True
    if s[l] != s[r]:
        return False
    return pal(s,l+1,r-1)


print(pal('abccba',0,5))
print(pal('abfccba',0,5))
print(pal('abf,;\'ccba',0,5))  # isalnum