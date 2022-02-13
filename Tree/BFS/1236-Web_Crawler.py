# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        queue = deque([startUrl])
        seen = {startUrl}
        domain = startUrl[7:].split('/')[0]
        res = []

        while queue:
            url = queue.popleft()
            res.append(url)
            urls = htmlParser.getUrls(url)

            for u in urls:
                if u in seen:
                    continue

                if u[7:].split('/')[0] != domain:
                    continue

                queue.append(u)
                seen.add(u)

        return res
