from fastapi import FastAPI
import whois
import socket

app = FastAPI()

@app.get('/')
def info(domain: str):
    try:
        domain_info = whois.whois(domain)
        ip = socket.gethostbyname(domain)


        # Extract individual items from domain_info
        domain_names = domain_info.domain_name
        registrar = domain_info.registrar
        whois_server = domain_info.whois_server
        updated_date = domain_info.updated_date
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date
        name_servers = domain_info.name_servers
        status = domain_info.status
        emails = domain_info.emails
        dnssec = domain_info.dnssec
        name = domain_info.name
        org = domain_info.org
        address = domain_info.address
        city = domain_info.city
        state = domain_info.state
        registrant_postal_code = domain_info.registrant_postal_code
        country = domain_info.country

        # Return items one by one
        return {
            "IP": ip,
            "Domain Name": domain_names,
            "Registrar": registrar,
            "WHOIS Server": whois_server,
            "Updated Date": updated_date,
            "Creation Date": creation_date,
            "Expiration Date": expiration_date,
            "Name Servers": name_servers,
            "Status": status,
            "Emails": emails,
            "DNSSEC": dnssec,
            "Name": name,
            "Organization": org,
            "Address": address,
            "City": city,
            "State": state,
            "Registrant Postal Code": registrant_postal_code,
            "Country": country
        }
    except whois.parser.PywhoisError as e:
        return str(e)

# Usage Example
# Access the endpoint at http://localhost:8000/?domain=example.com
