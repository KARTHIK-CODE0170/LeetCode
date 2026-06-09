class Solution:
    def merge(self,arr,low,mid,high):
        left = low
        right = mid + 1
        cnt = 0

        #testing
        while left <= mid and right <= high:
            if arr[left] > (arr[right] * 2):
                cnt += (mid - left  + 1)
                right += 1  
            else:
                left += 1
            
        
        #sorting
        temp = list()
        left, right = low,mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(len(temp)):
            arr[i + low] = temp[i]
        return cnt
        
    def mergeSort(self,arr,low,high):
        cnt = 0
        if low < high:
            mid = (high - low) // 2 + low
            cnt += self.mergeSort(arr,low,mid)
            cnt += self.mergeSort(arr,mid + 1,high)
            cnt += self.merge(arr,low,mid,high)
        return cnt
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums) - 1)
        