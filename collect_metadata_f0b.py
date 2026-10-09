"""Registered gds metadata transport only. No matrices, sample pages or values."""
import json,pathlib,datetime,hashlib,urllib.request,urllib.parse,time
root=pathlib.Path('metadata_f0b');root.mkdir(exist_ok=True);records=[]
base='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def fetch(endpoint,params,name,accession):
 url=base+endpoint+'?'+urllib.parse.urlencode(params);rec={'url':url,'attempts':[]};last=None
 for attempt in range(2):
  time.sleep(1);entry={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'attempt':attempt+1}
  try:
   with urllib.request.urlopen(url,timeout=45) as r:raw=r.read();entry['http_status']=r.status;entry['final_url']=r.url
   (root/f'{name}_{attempt+1}.json').write_bytes(raw);entry['sha256']=hashlib.sha256(raw).hexdigest();entry['bytes']=len(raw);last=json.loads(raw)
   if endpoint=='esearch.fcgi':
    assert isinstance(last['esearchresult']['idlist'],list) and last['esearchresult']['idlist'], 'No returned IDs'
   else:
    assert isinstance(last['result']['uids'],list)
    assert any(last['result'][uid].get('accession')==accession for uid in last['result']['uids']), 'No exact accession summary'
   entry['admission']='ENVELOPE-PASS';rec['attempts'].append(entry);return last,rec
  except Exception as e:entry['admission']='ADMISSION-FAILURE';entry['error']=str(e);rec['attempts'].append(entry)
 return None,rec
for i in range(5620,5629):
 acc=f'GSE{i}';entry={'accession':acc};search,trace=fetch('esearch.fcgi',{'db':'gds','term':acc+'[ACCN]','retmode':'json','retmax':20},acc+'_search',acc);entry['search']=trace
 ids=search['esearchresult']['idlist'] if search else []
 if ids:
  summary,trace=fetch('esummary.fcgi',{'db':'gds','id':','.join(ids),'retmode':'json'},acc+'_summary',acc);entry['summary']=trace
  matches=[summary['result'][uid] for uid in summary['result']['uids'] if summary['result'][uid].get('accession')==acc] if summary else []
  entry['exact_accession_matches']=matches;entry['semantic_admission']='EXACT-MATCH' if matches else 'ADMISSION-FAILURE'
 else:entry['semantic_admission']='ADMISSION-FAILURE';entry['reason']='No exact series metadata obtained'
 records.append(entry)
(root/'records.json').write_text(json.dumps(records,indent=2));print(json.dumps(records,indent=2))
