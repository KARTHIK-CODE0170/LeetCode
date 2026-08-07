class Solution {
public:
    void check(string s,int left,int right,int arr[3]){
        int maxi = 1;
        // if(right == s.size())
        while(left >= 0 and right < s.size()){
            if(s[left] != s[right]){
                // return -1;
                break;
            }
            maxi = max(maxi,right - left + 1);
            left -= 1;
            right += 1;
        }
        arr[0] = left + 1;
        arr[1] = right - 1;
        arr[2] = maxi;
        // return arr;
    }
    string longestPalindrome(string s) {
        string res = "";
        int maxi = 0;
        int arr[3];
        for(int i = 0;i < s.size();i += 1){
            check(s,i,i,arr);
            if(arr[2] > maxi){
                res = s.substr(arr[0],arr[2]);
                maxi = arr[2];
            }
            check(s,i,i + 1,arr);
            if(arr[2]>maxi){
                res = s.substr(arr[0],arr[2]);
                maxi = arr[2];
            }
        }
        return res;
    }
};