# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = []
        carryover = 0
        while l1.next and l2.next:
            element = (l1.val + l2.val + carryover) % 10
            sum.append(element)
            if (l1.val + l2.val) >= 10:
                carryover = 1
            else:
                carryover = 0
            l1 = l1.next
            l2 = l2.next

        #now we are at the last element of l1 or l2

        element = (l1.val + l2.val + carryover) % 10
        sum.append(element)
        if (l1.val + l2.val) >= 10:
            carryover = 1
        else:
            carryover = 0

        while l1.next:
            sum.append((element + carryover) % 10)
            if element + carryover >= 10:
                carryover = 1
            else:
                carryover = 0
            l1 = l1.next
        while l2.next: 
            sum.append((element + carryover) % 10)
            if element + carryover >= 10:
                carryover = 1
            else:
                carryover = 0
            l2 = l2.next

        #if remaining carryover, add it  
        if carryover:
            sum.append(carryover)

        #convert sum to a linked list
        sumLinkedList = [ListNode(0)]
        for i in range(len(sum)-1):
            sumLinkedList.append(ListNode(0))
            sumLinkedList[i].val = sum[i]
            sumLinkedList[i].next = sumLinkedList[i+1]
        sumLinkedList[len(sum)-1].val = sum[len(sum)-1]
        return sumLinkedList[0]
