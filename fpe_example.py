import csv
import pyffx

f = open('/tmp/data/MOCK_DATA.csv')
wf = open('/tmp/data/encrypted_MOCK_DATA.csv','w')
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
  fnameencryp = e.encrypt(fname)
  e = pyffx.String(b'secret-key', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- .@0123456789,\'', length=lnamelen)
  lnameencryp = e.encrypt(lname)
  e = pyffx.String(b'secret-key', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- .@0123456789,\'', length=emaillen)
  emailencryp = e.encrypt(email)
  e = pyffx.String(b'secret-key', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- .@0123456789,\'', length=companylen)
  companyencryp = e.encrypt(company)
  wf.write(row[0]+ ",\"" + fnameencryp + "\",\"" + lnameencryp + "\",\"" + emailencryp + "\",\"" + companyencryp + "\"" + "\r\n")
  
wf.close();
f.close();
print 'finished'