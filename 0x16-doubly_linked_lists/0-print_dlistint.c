#include "lists.h"
/**
 * print_dlistint - Short description, single line
 * @h: head of ddl list
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t size = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		size++;
	}
	return (size);
}
