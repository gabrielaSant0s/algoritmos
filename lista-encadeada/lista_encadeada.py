class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, element):
        # lista.append(5)
        if self.head:
            #inserção quando a lista já possui elementos
            #ponteiro que aponta para o próximo endereço de memória
            pointer = self.head

            while pointer.next:
                pointer = pointer.next
            
            pointer.next = Node(element)
        else:
            #Inserção do primeiro elemento da lista
            self.head = Node(element)
        
        self._size += 1
    
    def __len__(self):
        # len(lista)
        return self._size
    
    def __getitem__(self, index):
        # lista[0]
        pointer = self.head
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    def __setitem__(self, index, element):
        # lista[0] = 1
        pointer = self.head
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = element
        else:
            raise IndexError("list index out of range")
    
    def index(self, element):
        # Retorna o índice do elemento na lista
        # Algoritmo de busca linear em uma lista encadeada
        pointer = self.head
        cont = 0 
        while pointer:
            if pointer.data == element:
                return cont
            pointer = pointer.next
            cont+=1
        raise ValueError(f"{element} is not in list")
        
