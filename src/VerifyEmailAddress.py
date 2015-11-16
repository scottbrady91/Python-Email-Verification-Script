import re
import socket
import smtplib
import dns.resolver

# Address used for SMTP MAIL FROM command  
fromAddress = 'corn@bt.com'

# Simple Regex for syntax checking
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

# Email address to verify
inputAddress = input('Please enter the emailAddress to verify:')
addressToVerify = str(inputAddress)

# Syntax check
match = re.match(regex, addressToVerify)
if match == None:
	print('Bad Syntax')
	raise ValueError('Bad Syntax')

# Get domain for DNS lookup
splitAddress = addressToVerify.split('@')
domain = str(splitAddress[1])
print('Domain:', domain)

# MX record lookup
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

# Get local server hostname
host = socket.gethostname()

# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail(fromAddress)
code, message = server.rcpt(str(addressToVerify))
server.quit()

#print(code)
#print(message)

# Assume SMTP response 250 is success
if code == 250:
	print('Success')
else:
	print('Bad')