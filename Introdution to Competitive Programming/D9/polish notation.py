class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        items = []

        for i in tokens:
            try:
                int(i)
                isNum = True
            except:
                isNum = False
            if isNum:
                items.append(int(i))
            if not isNum:
                x = items.pop()
                y = items.pop()
                oprator = i
                if oprator == "+":
                    result = (x+y)
                    items.append(result)
                elif oprator == "-":
                    result = (y-x)
                    items.append(result)
                elif oprator == "*":
                    result = (x*y)
                    items.append(result)
                elif oprator == "/":
                    result =(y/x)
                    items.append(int(result))
        return items.pop()
