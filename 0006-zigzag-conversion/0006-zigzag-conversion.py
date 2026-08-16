class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        
        result=[""]*numRows
        cur_row=0
        step=1

        for ch in s:
            result[cur_row]+=ch

            if cur_row==0:
                step=1
            elif cur_row == numRows -1:
                step=-1
            cur_row+=step
        return ''.join(result)