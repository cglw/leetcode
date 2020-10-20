package common;

/**
 * Created by chengang on 2020/10/16.
 * 1.定义一个dfs，计算0，到数组长度l的函数
 * 2.写一个分割函数partition，传入左右index,找到分割点，（可以利用最后一个点作为pivot）
 * 3.分别计算左边界，右边界
 */
public class QuickSort {
    //插入排序 相当于插牌
    //选择排序 相当于选两个位置牌进行交换
    //排序的swap 函数最好不用位运算,除非判断不是自己
    public static void main(String[] args) {
        int[]nums=new int[]{2,4,2,5,1};

        new QuickSort().quickSort(nums);
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }

    }
    int index;
    int ans=0;

    public void quickSort(int[]nums){
        index=nums.length-2;
        dfs(nums,0,nums.length-1);
        System.out.println("result=====>"+ans);

    }
    public void dfs(int[]nums,int p,int r){
        if(p>r)return;
        //获得分割点
        int q=partition(nums,p,r);

        if(q==index){
            System.out.println("index"+nums[q]);
            ans=nums[q];
            return;
        }

        //分割点左右排序
        dfs(nums,p,q-1);
        dfs(nums,q+1,r);

    }

    private int partition(int[] nums, int p, int r) {
        int pivot=nums[r];
        int start=p;
        for (int i = start; i <r ; i++) {
            if(nums[i]<pivot){
                swap(nums,start,i);
                start+=1;
            }
        }

        swap(nums,start,r);
        return start;
    }

    public void swap(int[]nums,int p,int q){
        if(p==q){
            return;
        }
        nums[p]=nums[p]^nums[q];
        nums[q]=nums[p]^nums[q];
        nums[p]=nums[p]^nums[q];

    }


}
