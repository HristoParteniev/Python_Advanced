counter = 0

for c in range(1,48):
    for b in range (1,c):
        for a in range (1,b):
            if a * a * b * b == c * c:
                counter +=1
                print(f" {a}, {b}, {c}, total combinations: {counter}")
                
################## 2nd solution ###############
second_counter = 0

for f in range(1,48):
    for e in range (1,f):
        for d in range (1,e):
            if d * d * e * e == f * f: 
                second_counter +=1               
                print(f" {d}, {e}, {f}")

print(f"Count of Pythagorean triples: {second_counter}")
                

