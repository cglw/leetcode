package bytedance;

/**
 * Created by chengang on 2020/10/15.
 */
public class maxSubArray_53 {
    public static void main(String[] args) {

    }

    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int ans = dp[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = (dp[i - 1] < 0 ? 0 : dp[i - 1]) + nums[i];
            ans = Math.max(ans, dp[i]);
        }
        return ans;
    }
}
