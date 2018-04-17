#include "lists.h"
/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i[1024], j = 0, l = 0, k = 0, r = 0;

	if (!head)
		return (1);

	for ( ; *head; *head = (*head)->next, j++, l++)
		i[j] = (*head)->n;
	l--;
	for ( ; l; k++, l--)
	{
		if (i[k] == i[l])
			r = 1;
		else
			r = 0;
	}
	return (r);
}
