def cl(l):
    return set(i.strip().lower() for i in l)

def rep(a,b,c):
    a,b,c=cl(a),cl(b),cl(c)
    u=a|b|c
    print("Total unique:",len(u))
    t=a&b&c
    print("All 3 days:",sorted(t))
    o=(a-(b|c))|(b-(a|c))|(c-(a|b))
    print("Exactly 1 day:",sorted(o))
    print("Day1&Day2 overlap:",len(a&b))
    print("Day2&Day3 overlap:",len(b&c))
    print("Day1&Day3 overlap:",len(a&c))
    print("\n--- Report ---")
    print("Unique:",len(u))
    print("All 3:",sorted(t))
    print("One day:",sorted(o))
    print("D1&D2:",sorted(a&b))
    print("D2&D3:",sorted(b&c))
    print("D1&D3:",sorted(a&c))

d1=["Alice@gmail.com","Bob@Gmail.com","alice@gmail.com","Charlie@yahoo.com"]
d2=["bob@gmail.com","david@outlook.com","Eve@Gmail.com"]
d3=["alice@gmail.com","eve@gmail.com","Frank@yahoo.com"]

rep(d1,d2,d3)
