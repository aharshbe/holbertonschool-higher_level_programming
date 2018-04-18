#include "lists.h"
/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int l = 0, k = 0, s = 0;
	listint_t *tmp;
	int i[BUF];

	tmp = *head;
	if (!*head)
		return (1);
	for ( ; tmp; tmp = tmp->next, l++, s++)
	{
		if (l == 1)
			return (1);
		i[s] = tmp->n;
	}
	s = --l;
	for ( ; s >= l / 2; k++, s--)
	{
		if (i[k] != i[s])
			return (0);
	}
	return (1);
}
