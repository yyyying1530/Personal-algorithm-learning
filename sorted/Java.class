import java.util.Arrays;

public class Sort {

    public Sort(){}

    public int[] selection_sort(int[] arr){
        int n = arr.length;
        for (int i = 0; i < n; i++){
            int minindex = i;
            for (int j = i + 1; j < n; j++){
                if (arr[j] < arr[minindex]){
                    minindex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minindex];
            arr[minindex] = temp;
        }
        return arr;
    }

    public int[] bubble_sort(int[] arr){
        int n = arr.length;
        boolean swapped = true;
        while (swapped){
            swapped = false;
            for (int i = 0; i < n-1; i++){
                if (arr[i] > arr[i+1]){
                    swapped = true;
                    int temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                }
            }
        }
        return arr;
    }

    public int[] insertion_sort(int[] arr){
        int n = arr.length;
        for (int i = 1; i < n; i++){
            int temp = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > temp){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
        return arr;
    }

    public int[] counting_sort(int[] arr){
        int n = arr.length;
        int maxnum = Arrays.stream(arr).max().getAsInt();
        int[] buf = new int[maxnum + 1];
        int[] ans = new int[n];
        for(int i : arr) {
            buf[i] += 1;
        }
        for(int i = 1; i<=maxnum; i++){
            buf[i] += buf[i-1];
        }
        for(int i : arr){
            ans[buf[i]-1] = i;
            buf[i]--;
        }
        return ans;
    }
}
