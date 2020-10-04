#include <iostream>
using namespace std;

/*This program shows the implementation of both the recursive binary search function as well as iterative binary search.
 User enters an array of 10 numbers in ascending order.
 Binary Search (both recursive and iterative) returns the location of the key if present, otherwise returns -1 */

int recursiveBinarySearch(int arr[], int left, int right, int key)
{
    if (left<=right) {
        int mid = left + (right - left) / 2;
        
        // If element to search is equal to the current middle element, return it
        if (arr[mid] == key)
            return mid;
        
        // If element to search is smaller than middle value, then it can only be present in left subarray
        if (arr[mid] > key)
            return recursiveBinarySearch(arr, left, mid - 1, key);
        
        // If element to search is larger than middle value, then it can only be present in right subarray
        return recursiveBinarySearch(arr, mid + 1, right, key);
    }
    
    //Element is not found in the array
    return -1;
}

int iterativeBinarySearch(int arr[], int left, int right, int key)
{
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // If element to search is equal to the current middle element, return it
        if (arr[mid] == key) {
            cout << "Middle value is now  " << arr[mid] << " . Element found!" <<endl;
            return mid;
        }
        
        // If element to search is smaller than middle value, then it can only be present in left subarray
        if (arr[mid] >key) {
            cout << "Middle value is now " << arr[mid] << endl;
            cout << "have to search the left half now" <<endl;
            cout << endl;
            right = mid - 1;
        }
        
        // If element to search is larger than middle value, then it can only be present in right subarray
        else {
            cout << "Middle value is now " << arr[mid] << endl;
            cout << "have to search the right half now" <<endl;
            cout << endl;
            left = mid + 1;
        }
    }
    
    //Element is not found in the array
    return -1;
}

int main() {
    int size = 10;
    int arr[size];
    cout << "Enter a list of 10 numbers in ascending order to perform Binary Search : ";
    for (int i=0; i<10; i++){
        cin >> arr[i];
    }
    cout << endl;
    int key;
    cout << "Please enter a number from the list to search: " << endl;
    cin >> key;
    cout << "Displaying the Working of Binary Search: " <<endl;
    int res = iterativeBinarySearch(arr, 0, size-1, key);
    int res2 = recursiveBinarySearch(arr, 0, size-1, key);
    (res == -1)||(res2==-1) ? cout << "Element not found in array"
    : cout << "Element found at index " << res+1;
    return 0;
} 
