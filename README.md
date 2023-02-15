# changedns

1. Domain name from Godaddy, at the developer's page, apply for a public key and secret key pair,write them down.
2. Run this script every 12 hours to keep your domain linking to newest public IP.
3. NAT your public IP port 80 to internal port 80 on your home (wireless) router.
4. Run Apache2 and listen 80 on 0.0.0.0 at your internal server or PC or raspberry.
