from dao.DashboardDAO import DashboardDAO
from flask import jsonify

class DashboardHandler:
    def dashboard(self):
        dao = DashboardDAO()
        trendhash = dao.trendHash()
        trenduser = dao.trendUser()
        numlike = dao.numlike()
        numdis = dao.numdislike()
        numr = dao.numreply()
        numm = dao.nummessage()
        mapped = []

        return jsonify(Dashboard={"TrendingHash": self.appendName(trendhash), "TrendingUser": self.appendName(trenduser), "NumberOfLikes": self.appendCount(numlike), "NumberOfDislikes": self.appendCount(numdis), "NumberOfReplies": self.appendCount(numr), "NumberOfMessages": self.appendCount(numm)})

    def appendName(self, m):
        result = []
        for r in m:
            result.append(self.maptoName(r))
        return result

    def appendCount(self, m):
        result = []
        for r in m:
            result.append(self.mapNumCount(r))
        return result

    def maptoName(self, h):
        mapped = {"Name": h[0], "Date": h[1], "Count": h[2]}
        return mapped

    def mapNumCount(self, m):
        return {"Count": m[0], "Date": m[1]}

