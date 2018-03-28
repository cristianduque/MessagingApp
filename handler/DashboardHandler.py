from dao.DashboardDAO import DashboardDAO
from flask import jsonify

class DashboardHandler:
    def dashboard(self):
        dao = DashboardDAO().dashboardInfo()
        mapped = self.mappedDashboard(dao)
        return jsonify(Dashboard=mapped)

    def mappedDashboard(self, d):
        activeUsers = []
        for u in d[5]:
            activeUsers.append(self.mapToDict(u))
        trendHash = []
        for h in d[4]:
            trendHash.append(self.maptoDicHash(h))
        return {'Number Of Dislikes': d[0], 'Number Of Likes': d[1], 'Number Of Messages': d[2], 'Numbers Of Replies': d[3], 'Trending Hashtags': trendHash, 'Active Users': activeUsers}

    def mapToDict(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4]}
        return result

    def maptoDicHash(self, h):
        mapped = {'HashtagId': h[0], 'Hashtag': h[1]}
        return mapped
