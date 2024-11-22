class Twitter(object):
    def __init__(self):
        self.users = defaultdict(set)
        self.followers = defaultdict(set)
        self.reputation = 0

    def postTweet(self, userId, tweetId):
        self.reputation += 1
        self.users[userId].add((tweetId, self.reputation))

    def getNewsFeed(self, userId):
        tweets = list(self.users[userId])
        followees = self.followers[userId]

        for user_id in followees:
            tweets += self.users[user_id]

        most_recent_Tweets = sorted(
            tweets, key=lambda posts: posts[1], reverse=True)[:10]

        return [post[0] for post in most_recent_Tweets]

    def follow(self, followerId, followeeId):
        self.followers[followerId].add(
            followeeId if followerId != followeeId else None)

    def unfollow(self, followerId, followeeId):
        self.followers[followerId] -= {followeeId}
