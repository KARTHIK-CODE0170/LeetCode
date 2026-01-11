class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /*
        int left = 0, right = 0;
        int maxi = 0;
        unordered_map<char, int> mp;
        while (right < s.size())
        {

            if(mp.find(s[right]) != mp.end() && mp[s[right]] >= left)
            {
                left = mp[s[right]] + 1;
                // maxi = max(maxi,right - left + 1);
                mp[s[right]] = right;
            }
        mp[s[right]] = right;
        maxi = max(maxi,right - left + 1);
        right++;
    }
    return maxi;*/

        unordered_map<char, int> mp;
        int left = 0, right = 0;
        int maxi = 0;
        while (right < s.size()) {
            mp[s[right]]++;
            // cnt++;
            if (mp.size() == right - left + 1) {
                maxi = max(maxi, right - left + 1);
            }
            while (mp.size() < right - left + 1) {
                mp[s[left]]--;
                if (mp[s[left]] == 0) {
                    mp.erase(s[left]);
                }
                left++;
            }
            right++;
        }
        return maxi;
    }
};