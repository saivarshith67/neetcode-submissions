class MinStack {
public:
    stack<pair<int, int>> st;
    MinStack() {
    }
    
    void push(int val) {
        if(this->st.empty()){
            pair<int, int> pr;
            pr.first = val;
            pr.second = val;
            this->st.push(pr);
            return;
        }else{
            int stMin = st.top().second;
            pair<int, int> pr;
            pr.first = val;
            pr.second = min(stMin, val);
            this->st.push(pr);
            return;
        }
    }
    
    void pop() {
        st.pop();
    }
    
    int top() {
        return st.top().first;
    }
    
    int getMin() {
        return st.top().second;
    }
};
