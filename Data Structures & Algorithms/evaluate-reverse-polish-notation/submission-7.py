class Solution:
    @staticmethod
    def perform_operation(arg1, arg2, operator) -> int:
        match operator:
            case "+":
                return arg1 + arg2
            case "-":
                return arg2 - arg1

            case "*":
                return arg1 * arg2

            case "/":
                return int(arg2 / arg1)

        return 0


    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        st = []
        for token in tokens:
            if token in ops:
                arg1 = st.pop()
                arg2 = st.pop()
                val = Solution.perform_operation(arg1, arg2, token)
                st.append(val)

            else:
                # guarenteed that token is integer
                st.append(int(token))


        return st[-1]
                
        