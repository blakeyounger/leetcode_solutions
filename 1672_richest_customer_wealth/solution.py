class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        greatestWealth = 0
        for account in accounts:
            accountWealth = 0
            for bankAmount in account:
                accountWealth += bankAmount
            if accountWealth > greatestWealth:
                greatestWealth = accountWealth
            
        return greatestWealth
