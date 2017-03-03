friendsCount <- read.csv('./fb.mlnFriends.csv', head=TRUE, sep=',')
plot(friendsCount$FriendsCount, xlab='Friends', ylab='Number of friends', main='')
text(100, 120, 'Dr. Nelson has 165 friends')
abline(h=165, v=0)

summary(friendsCount$FriendsCount)
sd(friendsCount$FriendsCount)

friendsCount <- read.csv('./twitter.mlnFriends.csv', head=TRUE, sep=',')
plot(friendsCount$FriendsCount, log='y', xlab='Followers', ylab='Number of Folowers', main='Dr. Nelson\'s Twitter Follower vs Number of Followers')
text(100, 10, 'Dr. Nelson has 304 Followers')
abline(h=30, v=0)

summary(friendsCount$FriendsCount)
sd(friendsCount$FriendsCount)