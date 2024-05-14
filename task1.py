class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node

        self.head = prev

    def insertion_sort(self):
        if not self.head:
            return

        dummy = ListNode()
        dummy.next_node = self.head
        current = self.head.next_node
        last_sorted = self.head

        while current:
            if current.value < last_sorted.value:
                prev = dummy
                while prev.next_node and prev.next_node.value < current.value:
                    prev = prev.next_node

                last_sorted.next_node = current.next_node
                current.next_node = prev.next_node
                prev.next_node = current
                current = last_sorted.next_node
            else:
                last_sorted = current
                current = current.next_node

        self.head = dummy.next_node

    def merge_sorted_lists(self, l1, l2):
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.value < l2.value:
                current.next_node = l1
                l1 = l1.next_node
            else:
                current.next_node = l2
                l2 = l2.next_node
            current = current.next_node

        current.next_node = l1 or l2

        return dummy.next_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next_node
        print("None")

# Приклад використання:
sll = SinglyLinkedList()

# Вставляємо вузли в кінець списку
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)

print("Список після вставки в кінець:")
sll.print_list()

# Вставляємо вузли на початок списку
sll.insert_at_beginning(77)
sll.insert_at_beginning(5)

print("Список після вставки на початок:")
sll.print_list()


# Реверсуємо список
sll.reverse()
print("Реверсований список:")
sll.print_list()

# Сортуємо список за допомогою сортування вставками
sll.insertion_sort()
print("Відсортований список за допомогою сортування вставками:")
sll.print_list()

# Створюємо два відсортованих списки
sll1 = SinglyLinkedList()
sll1.insert_at_end(1)
sll1.insert_at_end(2)
sll1.insert_at_end(3)

sll2 = SinglyLinkedList()
sll2.insert_at_beginning(0)
sll2.insert_at_beginning(7)

# Сортуємо списки
sll1.insertion_sort()
sll2.insertion_sort()

# Об'єднуємо відсортовані списки
print("Об'єднання двох відсортованих списків:")
merged_head = sll.merge_sorted_lists(sll1.head, sll2.head)
merged_list = SinglyLinkedList()
merged_list.head = merged_head
merged_list.print_list()



