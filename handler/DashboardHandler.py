from dao.DashboardDAO import DashboardDAO
from flask import jsonify

class DashboardHandler:
    def dashboard(self):
        dao = DashboardDAO().dashboardInfo()
        if dao == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped = self.mappedDashboard(dao)
        return jsonify(Dashboard=mapped)

    def mappedDashboard(self, d):
        activeUsers = []
        for u in d[5]:
            activeUsers.append(self.mapToDict(u))
        trendHash = []
        for h in d[4]:
            trendHash.append(self.maptoDicHash(h))
        return {'Number Of Dislikes': d[0][0], 'Number Of Likes': d[1][0], 'Number Of Messages': d[2][0], 'Numbers Of Replies': d[3][0], 'Trending Hashtags': trendHash, 'Active Users': activeUsers}

    def mapToDict(self, row):
        result = {'username': row[0]}
        return result

    def maptoDicHash(self, h):
        mapped = {'Hashtag': h[0]}
        return mapped
