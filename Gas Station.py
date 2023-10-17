class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total_gas, current_gas, start = 0, 0, 0

        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start = i + 1
                current_gas = 0

        return start if total_gas >= 0 else -1
