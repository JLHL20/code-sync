/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode dum = new ListNode(0);
        ListNode current = dum;
        int carry = 0;

        while(l1 != null || l2 != null || carry != 0){

            int firstPointer = (l1 != null)  ? l1.val : 0;
            int secondPointer = (l2 != null) ? l2.val : 0;

            int sum = firstPointer + secondPointer + carry;

            carry = sum/10;
            int digit = sum % 10;

                        current.next = new ListNode(digit); // add node to result
            current = current.next;             // move result pointer

            if (l1 != null) l1 = l1.next; // move list pointers if possible
            if (l2 != null) l2 = l2.next;
        }

        return dum.next;
        }
    }