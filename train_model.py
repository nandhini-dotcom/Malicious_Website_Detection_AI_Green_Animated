from pathlib import Path
import random, joblib
from sklearn.ensemble import RandomForestClassifier
BASE=Path(__file__).resolve().parent
random.seed(42)
X=[]; y=[]
for i in range(3600):
    malicious=i%2==0
    if malicious:
        length=random.randint(55,180); dots=random.randint(3,8); hy=random.randint(1,8); digits=random.randint(3,15); at=random.choice([0,1,1]); q=random.randint(1,8); eq=random.randint(1,10); amp=random.randint(1,7); slash=random.randint(2,12); https=random.choice([0,0,1]); ip=random.choice([0,1]); kw=1; host=random.randint(12,65); tail=random.randint(15,100)
    else:
        length=random.randint(15,70); dots=random.randint(1,3); hy=random.randint(0,2); digits=random.randint(0,5); at=0; q=random.randint(0,2); eq=random.randint(0,2); amp=random.randint(0,2); slash=random.randint(1,6); https=1; ip=0; kw=0; host=random.randint(8,35); tail=random.randint(3,40)
    X.append([length,dots,hy,digits,at,q,eq,amp,slash,https,ip,kw,host,tail]); y.append(int(malicious))
model=RandomForestClassifier(n_estimators=180,max_depth=10,class_weight='balanced',random_state=42)
model.fit(X,y)
(BASE/'model').mkdir(exist_ok=True)
joblib.dump({'model':model},BASE/'model'/'model.joblib')
print('Model trained successfully:',BASE/'model'/'model.joblib')
