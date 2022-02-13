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

# Worker thread only calls htmlParser.getUrls()
# Seen is kept in main thread, no lock needed.

from concurrent import futures

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getHostname(url):
            return url.split('/')[2]

        seen = {startUrl}
        hostname = getHostname(startUrl)

        with futures.ThreadPoolExecutor(max_workers=10) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])

            while tasks:
                urls = tasks.popleft().result()

                for url in urls:
                    if url in seen or hostname != getHostname(url):
                        continue

                    seen.add(url)
                    tasks.append(executor.submit(htmlParser.getUrls, url))

        return list(seen)

# Follow-ups
# 1. Assume we have 10000 nodes and 1 billion URLs to crawl. We will deploy the same software onto each node. The software can know all the
# nodes. We have to minimize communication between machines and make sure each node does equal amount of work.
#
# SQS queue, asychronously process URLs in to_do queue, apply visibility timeout when one consumer gets to it and change its state to
# in_progress, after a while, delete the URL message upon completion, otherwise, move it to dead queue.
#
# 2. What if one node fails or does not work?
#
# The message under processing by this node will timeout and be moved to a dead queue, then it will be retried later on.
# Or, we can do re-processing (i.e. move them back to to_do queue).
#
# 3. How do you know when the crawler is done?
#
# to_do queue and dead queue are both cleared.
