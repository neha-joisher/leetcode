public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        var res = new List<IList<int>>();
        for (int i=0;i<nums.Length;i++){
            if(i!=0 && nums[i-1]==nums[i]){
                continue;
            }
            int st=i+1;
            int end=nums.Length-1;
            while(st<end){
                if(nums[st]+nums[end]+nums[i]==0){
                    res.Add(new List<int>{nums[st],nums[end],nums[i]});
                    st++;
                    end--;
                    while(nums[st]==nums[st-1] && st<end){
                        st++;
                    }
                }else if(nums[st]+nums[end]+nums[i]<0){
                    st++;
                }else{
                    end--;
                }
            }
        }
        return res;
    }
}