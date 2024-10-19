import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from subdomain import get_subdomains

def check_reachability(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=5)
        if response.status_code == 200:
            return subdomain, "active"
    except requests.RequestException:
        pass
    return subdomain, "not active"

def run_recon(domain):
    print(f"Starting recon for {domain}...")

    # Get subdomains
    subdomains = get_subdomains(domain)
    print(f"Subdomains found: {subdomains}")  # Debug print

    if not subdomains:
        print("No subdomains found.")
        return

    print("Checking reachability of subdomains...")
    reachable_subdomains = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_subdomain = {executor.submit(check_reachability, subdomain): subdomain for subdomain in subdomains}
        
        for future in as_completed(future_to_subdomain):
            subdomain, status = future.result()
            print(f"{subdomain} - {status}")
            reachable_subdomains.append(f"{subdomain} - {status}")

    # Write results to a file
    with open(f"{domain}_reachable_subdomains.txt", "w") as f:
        for result in reachable_subdomains:
            f.write(result + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 maksrecon.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    run_recon(domain)
