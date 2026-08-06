class Solution {
public:
    bool check(int n,int t){
        int mul = 1;
        int temp = n;
        while(temp > 0){
            mul *= (temp % 10);
            temp = temp / 10;
        }
        return mul % t == 0;
    }
    int smallestNumber(int n, int t) {
        for(int i = n;i <= (n + t);i += 1){
            if(check(i,t)){
                return i;
            }
        }
        return 0;
    }
};