class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)  # Sort the citations in descending order
        h_index = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index