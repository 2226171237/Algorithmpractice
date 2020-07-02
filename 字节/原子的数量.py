'''
给定一个化学式formula（作为字符串），返回每种原子的数量。
原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。
例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，
跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），
跟着它的数量（如果数量大于 1），以此类推。

示例 1:
输入:
formula = "H2O"
输出: "H2O"
解释:
原子的数量是 {'H': 2, 'O': 1}。
示例 2:
输入:
formula = "Mg(OH)2"
输出: "H2MgO2"
解释:
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
示例 3:
输入:
formula = "K4(ON(SO3)2)2"
输出: "K4N2O14S4"
解释:
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
注意:
所有原子的第一个字母为大写，剩余字母都是小写。
formula的长度在[1, 1000]之间。
formula只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-atoms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        arrFormula=[]
        result=dict()
        i=0
        while i<len(formula):
            # 括号
            if formula[i] in '()':
                arrFormula.append(formula[i])
                i+=1
                continue
            # 数字
            num=0
            while i<len(formula) and 0<=ord(formula[i])-ord('0')<=9:
                num=num*10+ord(formula[i])-ord('0')
                i+=1
            if num!=0:
                arrFormula.append(num)
            # 原子
            if i<len(formula) and'A'<=formula[i]<='Z':
                s=formula[i]
                i+=1
                while i<len(formula) and 'a'<=formula[i]<'z':
                    s+=formula[i]
                    i+=1
                result[s]=0
                arrFormula.append(s)
        stack=[]
        i=0
        while i<len(arrFormula):
            x=arrFormula[i]
            if x=='(':
                stack.append(x)
                i+=1
            if x==')':
                beta=1 if i+1>=len(arrFormula) or not isinstance(arrFormula[i+1],int) else arrFormula[i+1]
                tmpstack=[]
                while stack[-1]!='(':
                    num=stack.pop()
                    alpha=stack.pop()
                    num=num*beta
                    tmpstack.append(num)
                    tmpstack.append(alpha)
                stack.pop()
                while len(tmpstack):
                    stack.append(tmpstack.pop())
                i+=1 if beta==1 else 2
            if isinstance(x,str) and x not in '()':
                stack.append(x)
                beta=1 if i+1>=len(arrFormula) or not isinstance(arrFormula[i+1],int) else arrFormula[i+1]
                stack.append(beta)
                i += 1 if beta == 1 else 2
        i=0
        while i<len(stack):
            result[stack[i]]+=stack[i+1]
            i+=2
        keys=sorted(result.keys())
        s=''
        for x in keys:
            s+=x
            if result[x]>1:
                s+=str(result[x])
        return s


if __name__ == '__main__':
    s=Solution()
    print(s.countOfAtoms("H2O"))
