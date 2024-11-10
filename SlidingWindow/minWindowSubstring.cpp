class Solution {
public:

    bool check(vector<int>&s_map, vector<int>&t_map){
        //everything in t should be in s
        //but if s has anything extra, then its not the problem
        for(int i=0;i<128;i++){
            if(t_map[i]>s_map[i]){
                return false;
            }
        }
        return true;
    }
    string minWindow(string s, string t) {
        
        //save t in a map/array/list
        vector<int>t_map(128, 0);
        vector<int>s_map(128, 0);

        //iterating t and saving in t_map
        for(char &ch:t){
            t_map[ch]+=1;
        }
        
        //start my window translation
        int start=0;
        int ans_start=-1; //just the final ans index
        int ans_length=INT_MAX; //important to initalise to a very large number
        for(int i=0;i<s.size();i++){
            char ch = s[i];
            //expand
            s_map[ch]+=1;

            //shrink
            //if current availabiloity(s_map) of the start charcter is extra than the requirement(t_map), then i can shrink
            while (s_map[s[start]]>t_map[s[start]]){
                s_map[s[start]]--;
                start+=1;
            }

            //update
            if(check(s_map, t_map)){
                //cout<<i<<endl;
                int curr_size = i-start+1;
                if (curr_size<ans_length){
                    ans_length=curr_size;
                    ans_start=start;
                }
            }
        }
        //ans_start, ans_length-> generate my substring
        if(ans_start==-1) return "";
        string ans = s.substr(ans_start, ans_length);
        return ans;
    }
};


// s = "ADOBECODEBANC", t = "ABC"
// one of the option = ADOBEC = 6
// one of the other option BANC = 4
// min sized substring with all characters of t

// //compare whether I have found one of the answer options or not
// in T:
// 1 a, 1b, 1c

// in substring of S:
// ADOBE
// 1D 1 A 1 O...

// //shrink only when i have extra than the requirement
// //1a 1b 1c

// s = "ADOBECODEBANC"
// current window:
// ADOBEC
// BANC
// 1a 2b 1c

// ans = BANC
