from pathlib import Path
import re, math, joblib
BASE=Path(__file__).resolve().parent.parent
MODEL=BASE/'model'/'model.joblib'
def features(url):
    u=url.lower()
    host=u.split('://')[-1].split('/')[0]
    return [[len(url),url.count('.'),url.count('-'),sum(c.isdigit() for c in url),
             url.count('@'),url.count('?'),url.count('='),url.count('&'),url.count('/'),
             int(u.startswith('https://')),int(re.match(r'https?://(?:\d{1,3}\.){3}\d{1,3}',u or '') is not None),
             int(any(k in u for k in ['login','verify','secure','account','update','free','bonus','bank','confirm'])),
             len(host),len(u.split('/')[-1])]]
def predict(url):
    bundle=joblib.load(MODEL)
    X=features(url)
    p=float(bundle['model'].predict_proba(X)[0][1])
    label='MALICIOUS' if p>=0.5 else 'BENIGN'
    conf=p if label=='MALICIOUS' else 1-p
    risk='HIGH' if conf>=.80 and label=='MALICIOUS' else ('MEDIUM' if label=='MALICIOUS' else 'LOW')
    return label,round(conf*100,2),risk
