def findMergeNode(headA, headB):
    curA = headA
    curB = headB
    lenA = lenB = 0
    while curA:
        lenA += 1
        curA = curA.next
    while curB:
        lenB += 1
        curB = curB.next
    if lenA > lenB:
        for i in range(lenA - lenB):
            headA = headA.next
    else:
        for i in range(lenB - lenA):
            headB = headB.next
    while headA and headB:
        if headA == headB:
            return headA.data
        headA = headA.next
        headB = headB.next


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