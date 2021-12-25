class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {
            'Jan' : '01',
            'Feb' : '02',
            'Mar' : '03',
            'Apr' : '04',
            'May' : '05',
            'Jun' : '06',
            'Jul' : '07',
            'Aug' : '08',
            'Sep' : '09',
            'Oct' : '10',
            'Nov' : '11',
            'Dec' : '12'
        }

        tokens = date.split(" ")
        date = None

        if len(tokens[0]) == 4:
            date = tokens[0][:len(tokens[0]) - 2]
        else:
            date = '0' + tokens[0][:len(tokens[0]) - 2]

        month = month_map[tokens[1]]
        year = tokens[2]

        return '-'.join([year, month, date])
