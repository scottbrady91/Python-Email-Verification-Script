# Python-Email-Verification-Script
A simple script for email address verification using syntax, DNS and mailbox verification

Accompanying article available on: [https://www.scottbrady91.com/Email-Verification/Python-Email-Verification-Script](https://www.scottbrady91.com/Email-Verification/Python-Email-Verification-Script)

This script uses Python 3 and dnspython3

## Warnings and Disclaimers
Whilst this process will get you up and running, you need to be aware of the following:
- Do this too much and you will get put on a naughty list (e.g. Spamhaus), especially if you are using a dynamic IP address from your ISP.
- B2C addresses: this does not work very well against the big boys who have their own procedures and spam rules (e.g.hotmail and yahoo).
- Incorrect results: some mail servers will give you incorrect results, for instance catch-all servers, which will accept all incoming email addresses, often forwarding incoming emails to a central mailbox. Yahoo addresses displays this catch-all behavior.
