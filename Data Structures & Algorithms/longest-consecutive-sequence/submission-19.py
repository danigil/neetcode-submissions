class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in [0,1]:
            return len(nums)

        nums_uniq = set(nums)
        nums_d = {k:k+1 for k in nums_uniq if k+1 in nums_uniq}
        # print(nums_d)

        already_visited = set()

        longest = 1
        for k,v in nums_d.items():
            if k in already_visited:
                continue

            # print(f'k: {k}')

            curr = k
            curr_longest = 1
            while (next_one := nums_d.get(curr, None)) is not None:
                # print(f'next: {next_one}') 
                curr_longest += 1
                longest = max(longest, curr_longest)
                already_visited.add(curr)
                curr = next_one
        

        # nums = set(nums)
        # already_checked = set()

        # longest = 1
        # for num in nums:
        #     curr_longest = 1
        #     while num not in already_checked and num+1 in nums and curr_longest < len(nums):
        #         curr_longest+=1
        #         if curr_longest > longest:
        #             longest = curr_longest
        #         already_checked.add(num)
        
        # return longest
        return longest

        