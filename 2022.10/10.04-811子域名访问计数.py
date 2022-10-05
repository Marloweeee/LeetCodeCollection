from typing import List
from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        http_dic=Counter()
        for item in cpdomains:
            times,http=item.split(' ')
            http_dic[http] += int(times)
            while '.' in http:
                http=http[http.index('.')+1:]
                http_dic[http]+=int(times)
        return [f'{times} {domain}' for domain,times in http_dic.items()]



if __name__ == '__main__':
    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))