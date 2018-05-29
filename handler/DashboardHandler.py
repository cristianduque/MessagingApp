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
        return jsonify(Dashboard={"TrendingHash": self.appendName(trendhash), "TrendingUser": self.appendName(trenduser), "NumberOfLikes": numlike, "NumberOfDislikes": numdis, "NumberOfReplies": numr, "NumberOfMessages": numm})

    def appendName(self, m):
        result = []
        for r in m:
            result.append(self.maptoName(r))
        return result


    def maptoName(self, h):
        mapped = {"Name": h[0], "Count": h[1]}
        return mapped

