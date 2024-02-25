public class peakelement {
        public static void main(String[] args) {
            int a[] = {1,2,3,0,5,6,4};
            int ans = peak(a);
            System.out.println(ans);
        }
    
        static int peak(int a[]) {
            int s = 0;
            int e = a.length - 1;
    
            while (s <= e) {
                int mid = s + (e - s) / 2;
    
                if ((mid == 0 || a[mid] >= a[mid - 1]) && (mid == a.length - 1 || a[mid] >= a[mid + 1])) {
                    return mid;
                } else if (a[mid - 1] > a[mid]) {
                    e = mid - 1;
                } else {
                    s = mid + 1;
                }
            }
            return -1;
        }
    }
