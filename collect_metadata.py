"""DOC-2-091 F0: brief series HTML only; never fetch values or sample pages."""
import hashlib,json,datetime,pathlib,re,urllib.request,html,time
out=pathlib.Path('metadata');out.mkdir(exist_ok=True);records=[]
for i in range(5620,5629):
 accession=f'GSE{i}';url=f'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={accession}';record={'accession':accession,'url':url,'fetched_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'errors':[]}
 for attempt in range(2):
  try:
   with urllib.request.urlopen(url,timeout=45) as r:
    raw=r.read();record['http_status']=r.status
   text=raw.decode('utf-8',errors='replace');(out/(accession+'.html')).write_bytes(raw)
   record['sha256']=hashlib.sha256(raw).hexdigest();record['bytes']=len(raw)
   visible=html.unescape(re.sub('<[^>]*>',' ',text));visible=re.sub(r'\s+',' ',visible)
   record['visible_text']=visible;record['gsm_ids']=sorted(set(re.findall(r'GSM\d+',text)));record['gpl_ids']=sorted(set(re.findall(r'GPL\d+',text)))
   record['matrix_links']=re.findall(r'href=["\']([^"\']*series_matrix[^"\']*)',text)
   break
  except Exception as e:
   record['errors'].append({'attempt':attempt+1,'error':str(e)})
   if attempt==0:time.sleep(2)
 records.append(record)
(out/'records.json').write_text(json.dumps(records,indent=2));print(json.dumps([{k:v for k,v in r.items() if k!='visible_text'} for r in records],indent=2))
