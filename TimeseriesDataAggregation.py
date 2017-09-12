class Solution(object):
    def TimeAggregation(self, data):
        data = data.split('\n')
        # extract start year, month and end year, month
        self.start_year = data[0].split(',')[0].strip().split('-')[0]
        self.start_month = data[0].split(',')[0].strip().split('-')[1]
        self.end_year = data[0].split(',')[1].strip().split('-')[0]
        self.end_month = data[0].split(',')[1].strip().split('-')[1]
        
        res = {}    # the structure of res = {year: {month: {type: count} } }

        # extract the year, month, engagement type and count
        for i in range(2, len(data)-1):
            year = data[i].split(',')[0].strip().split('-')[0]
            month = data[i].split(',')[0].strip().split('-')[1]
            e_type = data[i].split(',')[1].strip()
            count = data[i].split(',')[2].strip()
            # if date is within the interval, add data into dict
            if self.dateInInterval(year, month):
                res.setdefault(year, {})
                res[year].setdefault(month, {})
                res[year][month].setdefault(e_type, 0)
                res[year][month][e_type] += int(count)
        s = ''  # output string
        for year in res:
            for month in res[year]:
                s += year + '-' + month
                for e_type in res[year][month]:
                    count = res[year][month][e_type]
                    s += ', ' + e_type + ', ' + str(count)
                s += '\n'
        return s
    
    def dateInInterval(self, year, month):
        start = self.start_year + self.start_month
        end = self.end_year + self.end_month
        if year + month >= start and year + month <= end:
            return True
        return False

    # def dateInInterval(self, year, month):
    #     if year == self.start_year:
    #         if month >= self.start_month:
    #             return True
    #     elif year > self.start_year and year < self.end_year:
    #         return True
    #     elif year == self.end_year:
    #         if month <= self.end_month:
    #             return True
    #     else:
    #         return False
    #     return False
        
data = '\
2015-08, 2016-04\n\
\n\
2015-08-15, clicks, 635\n\
2016-03-24, app_installs, 683\n\
2015-04-05, favorites, 763\n\
2016-01-22, favorites, 788\n\
2015-12-26, clicks, 525\n\
2016-06-03, retweets, 101\n\
2015-08-10, retweets, 100\n\
'
test = Solution()
print test.TimeAggregation(data)

