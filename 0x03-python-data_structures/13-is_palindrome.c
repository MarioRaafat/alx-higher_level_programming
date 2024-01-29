#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t** head)
{
    listint_t* top = *head;
    listint_t* rear = *head;
    listint_t* temp = *head;
    int len = 1;

    while (rear->next) {
        rear = rear->next;
        len++;
    }

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);

    for(int i = 0; i < len/2; i++)
    {
        if (rear->n == top->n)
        {
            len -= 2;
            rear = temp;
            top = top->next;
            for (int j = 0; j < (len + i); j++)
                rear = rear->next;
        }
        else
            return 0;
    }
    return 1;
}
