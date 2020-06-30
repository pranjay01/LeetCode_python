# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        sumval = 0
        print(l1)
        print(l2)
        itr1 = ListNode()
        itr2 = ListNode()
        prev = ListNode()
        #result = ListNode()
        #result=l1
        itr1 = l1
        itr2 = l2
        carry = 0
        while itr1 and itr2:
            #print(itr.val*(pow(10,i)))
            sumval = itr1.val + itr2.val + carry
            if sumval <= 9:
                carry = 0
                itr1.val=sumval
                prev =itr1
                itr1=itr1.next
                itr2=itr2.next
            else:
                carry = 1
                itr1.val=sumval-10
                prev =itr1
                itr1=itr1.next
                itr2=itr2.next
           
        if not(itr1) and itr2:
            itr1.next=itr2
            if carry ==1:
                while(itr2.val<9 and itr2 and carry==1):
                    sumval = itr2.val + carry
                    if sumval <= 9:
                        carry = 0
                        itr2.val=sumval                        
                    else:
                        carry = 1
                        itr2.val=sumval-10
                        prev =itr2
                        itr2=itr2.next
                
        elif carry==1 and itr1 and not(itr2): 
            
            while(itr1.val<9 and itr1 and carry==1):      

                sumval = itr1.val + carry
                if sumval <= 9:
                    carry = 0
                    itr1.val=sumval                        
                else:
                    carry = 1
                    itr1.val=sumval-10
                    prev =itr1
                    itr1=itr1.next

            
                
        if carry==1:
            n = ListNode(1)
            prev.next=n
        
        return l1

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()