import dns.resolver

class DNSRecon:
    def __init__(self, domain):
        self.domain = domain
        self.records = ['A', 'AAAA', 'MX', 'NS', 'TXT']
        
    def run(self):
        results = {}
        for record_type in self.records:
            try:
                answers = dns.resolver.resolve(self.domain, record_type)
                results[record_type] = [str(rdata) for rdata in answers]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
                results[record_type] = []
            except Exception as e:
                results[record_type] = [f"Error: {str(e)}"]
                
        return results
