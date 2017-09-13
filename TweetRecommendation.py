class Solution(object):
    def tweetRecommendation(self, followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
        follows = {}    # {userId: ''}, use blank string as placeholder
        potential_tweets = {}   # {tweetId: count}
        res = []
        for edge in followGraph_edges:
            if edge[0] == targetUser:
                follows.setdefault(edge[1], '')
        for edge in likeGraph_edges:
            if edge[0] in follows:
                potential_tweets.setdefault(edge[1], 0)
                potential_tweets[edge[1]] += 1
        for tweet in potential_tweets:
            if potential_tweets[tweet] >= minLikeThreshold:
                res.append(tweet)
        return res
        
followGraph_edges = [('A','B'), ('A','C'), ('B','C')]
likeGraph_edges = [('A','T1'), ('B', 'T1'), ('C', 'T1'), ('C','T2')]
targetUser = 'A'
minLikeThreshold = 1
test = Solution()
print test.tweetRecommendation(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold)
