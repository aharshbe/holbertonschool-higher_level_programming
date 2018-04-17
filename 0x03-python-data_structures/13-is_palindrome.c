#include "lists.h"
/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i[1 << 10], l = 0, k = 0, r = 0, s = 0;
	const listint_t *tmp;

	if (!*head)
		return (1);
	tmp = *head;

	for ( ; tmp; tmp = tmp->next, l++)
		;
	if (l == 1)
		return (1);
	tmp = *head;
	for ( ; tmp; tmp = tmp->next, s++)
		i[s] = tmp->n;
	s = --l;
	for ( ; s >= (l / 2); k++, s--)
	{
		if (i[k] != i[s])
			break;
		r = 1;
	}
	return (r);
}
