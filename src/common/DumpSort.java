package common;

import java.util.Arrays;

/**
 * Created by chengang on 2020/10/19.
 * 堆是一种二叉树，大顶堆具有每个父亲节点大于等于子节点，
 * 1.构建大顶堆,i/2 开始到0   先左边再右边，swap 然后继续调整，非叶子节点开始进行调整
 * 2.每次取出堆的头部，然后继续调整，这是一个for循环
 */
public class DumpSort {

    public static void main(String[] args) {
        int[] arr = {7, 6, 7, 11, 5, 12, 3, 0, 1};
        System.out.println("排序前：" + Arrays.toString(arr));
        int sort = sort(arr, 3);
        System.out.println("排序前：" + Arrays.toString(arr));
        System.out.println(sort);
    }

    public static int sort(int[] arr, int k) {
        //构建大顶堆
        int heapSize = arr.length;
        buildMaxHeap(arr, heapSize);
        System.out.println("----" + arr[0]);
        for (int i = arr.length - 1; i >= 1; i--) {
            if (arr.length - i == k) {
                System.out.println("---->");
                return arr[0];
            }
            swap(arr, 0, i);
            --heapSize;
            //重写调整
            adjust(arr, 0, heapSize);

        }
        return arr[arr.length-k];

    }

    public static void buildMaxHeap(int[] arr, int heapSize) {
        //从第一个不是叶子
        for (int i = heapSize / 2; i >= 0; i--) {
            adjust(arr, i, heapSize);
        }

    }


    public static void adjust(int[] arr, int i, int heapSize) {
        int l = 2 * i + 1, r = l + 1, largest = i;
        if (l < heapSize && arr[l] > arr[largest]) {
            largest = l;
        }
        if (r < heapSize && arr[r] > arr[largest]) {
            largest = r;
        }
        //需要交换
        if (largest != i) {
            //交换以后必须重写调整
            swap(arr, i, largest);
            //继续调整,在顶部
            adjust(arr, largest, heapSize);
        }

    }

    /**
     * 交换元素
     *
     * @param arr
     * @param a
     * @param b
     */
    public static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }


}
