class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"[Node with value {self.value}]"


def print_linked_list(head: Node):
    cur = head
    while cur is not None:
        print(cur)
        cur = cur.next


def reverse_linked_list(head):
    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def bubble_sort_linked_list(head):
    current = head
    while True:
        is_swapped = False
        while current.next:
            current_next = current.next
            if current.value > current_next.value:
                current.value, current_next.value = current_next.value, current.value
                is_swapped = True
            current = current_next

        if not is_swapped:
            break
        current = head

    return head


if __name__ == "__main__":
    lst = Node(1, Node(6, Node(3, Node(9, Node(0)))))
    print("список")
    print_linked_list(lst)
    print("развернутый список")
    rev_lst = reverse_linked_list(lst)
    print_linked_list(rev_lst)
    print("сортированный список")
    print_linked_list(bubble_sort_linked_list(rev_lst))
