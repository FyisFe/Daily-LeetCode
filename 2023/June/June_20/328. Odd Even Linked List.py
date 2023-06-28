class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Check if linked list is empty or contains only one node
        if not head or not head.next:
            return head

        odd = head  # Pointer to the first odd node
        even = head.next  # Pointer to the first even node
        even_head = even  # Pointer to the head of even nodes

        # Traverse the linked list in pairs of odd and even nodes
        while even and even.next:
            # Connect the next odd node with the current odd node
            odd.next = even.next
            odd = odd.next

            # Connect the next even node with the current even node
            even.next = odd.next
            even = even.next

        # Connect the last odd node with the head of even nodes
        odd.next = even_head

        return head
