class Solution:
    def maximumWealth(self,accounts):
        max_wealth = 0  # Initialize max_wealth to 0
        # ToDo: Write Your Code Here.
        current_wealth = 0
        for account in range(len(accounts)):
            #print(f"this is the Account: {i}, {accounts[i]}")
            current_wealth = sum(accounts[account])
            max_wealth = max(current_wealth, max_wealth)

    def maximumWealth(self, accounts):
        max_wealth = 0  # Initialize max_wealth to 0
        # Loop through each customer's accounts
        for customer in accounts:
            wealth = sum(customer)  # Sum up the customer's wealth using the sum function
            # Update max_wealth if the current customer's wealth is greater
            if wealth > max_wealth:
                max_wealth = wealth
        # Return the maximum wealth found
        return max_wealth

