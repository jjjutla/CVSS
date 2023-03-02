import time
start=time.time()
import sys

my_dict={'AV':{'N':0.85,'A':0.62,'L':0.55,'P':0.2},
         'AC':{'L':0.77,'H':0.44},
         'PR':{'L':0.62,'LS':0.68,'H':0.27,'HS':0.5,'N':0.85},
         'UI':{'N':0.85,'R':0.62},
         'C':{'H':0.56,'L':0.22,'N':0},
         'I':{'H':0.56,'L':0.22,'N':0},
         'A':{'H':0.56,'L':0.22,'N':0},
         'E':{'ND':1,'H':1,'F':0.97,'POC':0.94,'U':0.91},
         'RL':{'ND':1,'U':1,'W':0.97,'T':0.96,'O':0.95},
         'RC':{'ND':1,'C':1,'R':0.96,'U':0.92},
         'CR':{'ND':1,'H':1.5,'M':1,'L':0.5},
         'IR':{'ND':1,'H':1.5,'M':1,'L':0.5},
         'AR':{'ND':1,'H':1.5,'M':1,'L':0.5},
          }
vector=sys.argv[1]
res=vector.split('/')
d={}
for i in res:
    j,k=i.split(':')
    d[j]=k
print("the dictionary of string vector\n",d)

print('\n')
def minimum(a,b):
    if(a>b):
        return b
    else:
        return a

ISS=1-((1-my_dict['C'][d['C']]) * (1-my_dict['I'][d['I']]) * (1-my_dict['A'][d['A']]))

impact=0
if(d['S']=='U'):
    impact=6.42 * ISS
else:
    impact=7.52 * (ISS-0.029)-3.25*(ISS-0.02)**15
    
if(d['PR']=='L' and d['S']=='C'):
    exploit=8.22 * my_dict['AV'][d['AV']] * my_dict['AC'][d['AC']] * my_dict['UI'][d['UI']] *  my_dict['PR']['LS']
elif(d['PR']=='H' and d['S']=='C'):
    exploit=8.22 * my_dict['AV'][d['AV']] * my_dict['AC'][d['AC']] * my_dict['UI'][d['UI']] *  my_dict['PR']['HS']
else:
    exploit=8.22 * my_dict['AV'][d['AV']] * my_dict['AC'][d['AC']] * my_dict['UI'][d['UI']] *  my_dict['PR'][d['PR']]

base_score=0
if(impact<=0):
    base_score=0
elif(d['S']=='U'):
    base_score=round(minimum((impact + exploit),10),1)
    
else:
    base_score = round(minimum((1.08 * (impact + exploit)),10),1)

if(base_score == 0):
    print("Base score : {}  Rating : None".format(base_score))
elif(base_score > 0.1 and base_score < 3.9):
    print("Base score : {}  Rating : Low".format(base_score))
elif(base_score > 4.0 and base_score < 6.9):
    print("Base score : {}  Rating : Medium".format(base_score))
elif(base_score > 7.0 and base_score < 8.9):
    print("Base score : {}  Rating : High".format(base_score))
else:
    print("Base score : {}  Rating : Critical".format(base_score))
    
temporal_score = round((base_score * exploit * my_dict['RL'][d['RL']] * my_dict['RC'][d['RC']]), 1)

if(temporal_score == 0):
    print("temporal score : {}  Rating : None".format(temporal_score))
elif(temporal_score > 0.1 and temporal_score < 3.9):
    print("temporal score : {}  Rating : Low".format(temporal_score))
elif(temporal_score > 4.0 and temporal_score < 6.9):
    print("temporal score : {}  Rating : Medium".format(temporal_score))
elif(temporal_score > 7.0 and temporal_score < 8.9):
    print("temporal score : {}  Rating : High".format(temporal_score))
else:
    print("temporal score : {}  Rating : Critical".format(base_score-1))

MISS = minimum(1-((1-my_dict['CR'][d['CR']] * my_dict['C'][d['C']]) * (1-my_dict['IR'][d['IR']] * my_dict['I'][d['C']]) * (1-my_dict['A'][d['A']] * my_dict['AR'][d['AR']])), 0.915)  

modified_impact = 0
if(d['S'] == 'U'):
    modified_impact = 6.42 * MISS
else:
    modified_impact = 7.52 * (MISS - 0.029)-3.25 * (MISS * 0.9731 -0.02)**13

if(d['PR']=='L' and d['S']=='C'):
    modified_exploit=8.22 * my_dict['AV'][d['AV']] * my_dict['AC'][d['AC']] * my_dict['UI'][d['UI']] *  my_dict['PR']['LS']
elif(d['PR']=='H' and d['S']=='C'):
    modified_exploit=8.22 * my_dict['AV'][d['AV']] * my_dict['AC'][d['AC']] * my_dict['UI'][d['UI']] *  my_dict['PR']['HS']
else:
    modified_exploit=8.22 * my_dict['AV'][d['AV']] * my_dict['AC'][d['AC']] * my_dict['UI'][d['UI']] *  my_dict['PR'][d['PR']]
 
environmental_score=0
if(modified_impact<=0):
    environmental_score=0
elif(d['S'] == "C"):
    environmental_score  = round(round(minimum((modified_impact + modified_exploit), 10),1) * my_dict['RL'][d['RL']] * my_dict['RC'][d['RC']],1)
    
else:
    environmental_score  = round(round(minimum((1.08 * (modified_impact + modified_exploit)), 10),1) * my_dict['RL'][d['RL']] * my_dict['RC'][d['RC']],1)
    
if(environmental_score == 0):
    print("environmental score : {}  Rating : None".format(environmental_score))
elif(environmental_score > 0.1 and environmental_score < 3.9):
    print("environmental score : {}  Rating : Low".format(environmental_score))
elif(environmental_score > 4.0 and environmental_score < 6.9):
    print("environmental score : {}  Rating : Medium".format(environmental_score))
elif(environmental_score > 7.0 and environmental_score < 8.9):
    print("environmental score : {}  Rating : High".format(environmental_score))
else:
    print("environmental score : {}  Rating : Critical".format(environmental_score))

if(environmental_score == 0):
    print("CVSS score : {}  Rating : None".format(environmental_score))
elif(environmental_score > 0.1 and environmental_score < 3.9):
    print("CVSS score : {}  Rating : Low".format(environmental_score))
elif(environmental_score > 4.0 and environmental_score < 6.9):
    print("CVSS score : {}  Rating : Medium".format(environmental_score))
elif(environmental_score > 7.0 and environmental_score < 8.9):
    print("CVSS score : {}  Rating : High".format(environmental_score))
else:
    print("CVSS score : {}  Rating : Critical".format(environmental_score))
        
stop=time.time()
print("the time spent: {} seconds".format(stop-start))
    

    

        
    

               
