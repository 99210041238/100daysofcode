public class SearchInsertPosition {
    public static void main(String[] args) {
        int a[]={1,3,4,6};
        int key =5;
        int ans =find(a, key);
        System.out.println(ans);
    }

    static int find(int a[], int key) {
        int s = 0;
        int e = a.length - 1;
        while (s <= e) {
            int mid = s + (e - s) / 2;
            if (a[mid] == key) {
                return mid;
            } else if (a[mid] > key) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        for (int i = 0; i <= a.length; i++) {
            if (a[i] - key == 1) {
                return i;
            }
        }
        return -1; // Return -1 if key is not found
    }
}
