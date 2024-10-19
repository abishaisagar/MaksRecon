import sublist3r

def get_subdomains(domain):
    subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, 
                                enable_bruteforce=False, engines=None, verbose=False, silent=True)
    return subdomains
