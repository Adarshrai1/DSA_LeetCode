class Solution:
    def sortByBits(self, arr):
        def custom_key(num):
            return (bin(num).count('1'), num)

        # Sort the array using the custom sorting key function
        arr.sort(key=custom_key)

        return arr  #Adarshrai