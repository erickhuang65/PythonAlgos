class Solution:
    def containsDuplicate(self, nums):
      # check for edge cases
      # if nums array is null return False
      if nums is None or len(nums) == 0:
          return False
      
      # BRUTE FORCE APPORACH: compare each element to all other in the array
      for i in range(len(nums)):
           for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                     return True
      return False
    
    # def contains_duplicate(self, nums):
    #     unique_set = set() # Use set to store unique elements
        
    #     for x in nums:
    #     if x in unique_set: # If the set already contains the current element, return True
    #         return True
    #     unique_set.add(x) # Add the current element to the set

    #     return False # Return False if no duplicates found

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3, 4]
    print(sol.containsDuplicate(nums1))