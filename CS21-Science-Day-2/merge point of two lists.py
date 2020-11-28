def findMergeNode(headA, headB):
    curA = headA   1
    curB = headB   1
    lenA = lenB = 0  1
    while curA:  n1+1
        lenA += 1  n1
        curA = curA.next n1
    while curB:  n2+1
        lenB += 1  n2
        curB = curB.next  n2
    if lenA > lenB:   1
        for i in range(lenA - lenB): n1-n2+1
            headA = headA.next 1 n1-n2
    else:
        for i in range(lenB - lenA): n2-n1+1
            headB = headB.next  n2-n1
    while headA and headB:
        if headA == headB:  
            return headA.data   1
        headA = headA.next    1
        headB = headB.next    1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count - 1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
     
        
    Then time complexity is     O(n1+n2) where n1 and n2 are number of nodes of the two linked list
