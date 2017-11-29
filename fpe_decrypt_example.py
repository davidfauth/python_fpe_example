 
import csv
import pyffx

f = open('/tmp/data/encrypted_MOCK_DATA.csv')
wf = open('/tmp/data/unencrypted_MOCK_DATA.csv','w')
csv_f = csv.reader(f)
wf.write("id,first_name,last_name,email,company" + "\r\n")

next(csv_f, None)  # skip the headers

for row in csv_f:
  
  fname = row[1]
  lname = row[2]
  email = row[3]
  company=row[4]
  fnamelen = len(fname)
  lnamelen = len(lname)
  emaillen = len(email)
  companylen = len(company)
  e = pyffx.String(b'secret-key', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- .@0123456789,\'', length=fnamelen)
  fnamedecrypt = e.decrypt(fname)
  e = pyffx.String(b'secret-key', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- .@0123456789,\'', length=lnamelen)
  lnamedecrypt = e.decrypt(lname)
  e = pyffx.String(b'secret-key', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- .@0123456789,\'', length=emaillen)
  emaildecrypt = e.decrypt(email)
  e = pyffx.String(b'secret-key', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- .@0123456789,\'', length=companylen)
  companydecrypt = e.decrypt(company)
  wf.write(row[0]+ ",\"" + fnamedecrypt + "\",\"" + lnamedecrypt + "\",\"" + emaildecrypt + "\",\"" + companydecrypt + "\"" + "\r\n")
  
wf.close();
f.close();
print 'finished'