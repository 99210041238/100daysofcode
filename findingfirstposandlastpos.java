public class findingfirstposandlastpos {
        public static void main(String[] args) {
            int a[] = {5, 7, 7, 8, 8, 8, 9, 10};
            int target = 8;
            int[] result = findFirstAndLastPos(a, target);
            if (result[0] == -1) {
                System.out.println(-1);
            } else {
                System.out.println(result[0]);
                System.out.println(result[1]);
            }
        }
    
        static int[] findFirstAndLastPos(int a[], int target) {
            int first_pos = findFirstPos(a, target);
            int last_pos = findLastPos(a, target);
            return new int[]{first_pos, last_pos};
        }
    
        static int findFirstPos(int[] a, int target) {
            int s = 0;
            int e = a.length - 1;
            while (s <= e) {
                int mid = s + (e - s) / 2;
                if (a[mid] == target) {
                    e = mid - 1;
                    return mid;
                } else if (a[mid] < target) {
                    s = mid + 1;
                } else {
                    e = mid - 1;
                }
            }
            return -1;
        }
    
        static int findLastPos(int a[], int target) {
            int s = 0;
            int e = a.length - 1;
            while (s <= e) {
                int mid = s + (e - s) / 2;
                if (a[mid] == target) {
                    s = mid + 1;
                    return mid;
                } else if (a[mid] < target) {
                    s = mid + 1;
                } else {
                    e = mid - 1;
                }
            }
            return -1;
        }

    
}
