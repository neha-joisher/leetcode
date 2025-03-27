class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
            XOR stands for "exclusive OR", and it's a bitwise operation.

            It compares two bits:

            Returns 1 if the bits are different

            Returns 0 if the bits are the same

            \U0001f9ee XOR Truth Table
            A	B	A ⊕ B (A XOR B)
            0	0	0
            0	1	1
            1	0	1
            1	1	0
        '''
        res=0 #0^n=n
        for num in nums:
            res=res^num
        return res

                    