class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        else:
            # counting the length of the linked list
            count = 0
            head1 = head
            slow, fast = None, head
            # reversing the linked list till the middle
            while head1:
                count += 1
                head1 = head1.next
            if count % 2:
                # if length is odd
                count = count // 2
                while count > 0:
                    temp = fast.next
                    fast.next = slow
                    slow = fast
                    fast = temp
                    count -= 1
                fast = fast.next  # if length is odd skip the middle element

                # slow is going back and fast is going forward and we compare each node's value
                while fast:
                    if slow.val == fast.val:
                        slow = slow.next
                        fast = fast.next

                    else:
                        return False
                return True

            else:
                count = count // 2
                # reversing the linkedlist till middle
                while count > 0:
                    temp = fast.next
                    fast.next = slow
                    slow = fast
                    fast = temp
                    count -= 1

                while fast:
                    if slow.val == fast.val:
                        slow = slow.next
                        fast = fast.next

                    else:
                        return False
                return True
