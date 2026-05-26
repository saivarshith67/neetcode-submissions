class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
            } else {
                // Before accessing st.top(), check if the stack is empty
                if (st.empty()) return false;

                char top = st.top();
                if ((ch == ')' && top == '(') ||
                    (ch == ']' && top == '[') ||
                    (ch == '}' && top == '{')) {
                    st.pop(); // Matched pair
                } else {
                    return false; // Mismatched pair
                }
            }
        }

        // If the stack is empty, all brackets matched
        return st.empty();
    }
};
