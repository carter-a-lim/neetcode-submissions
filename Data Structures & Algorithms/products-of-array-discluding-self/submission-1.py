class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply for big sum; if count(0) > 2: return all 0, else get prod of everything else & ret 0s
        zeros = 0
        product = 1
        ret=[]

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        if zeros > 1:
            return [0] * len(nums)

        if zeros == 1:
            for num in nums:
                if num == 0:
                    ret.append(product)
                else: ret.append(0)

        if zeros == 0:
            for num in nums:
                    ret.append(int(product / num))

        return ret

