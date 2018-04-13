#include "lists.h"
/**
 * dlistint_len - Short description, single line
 * @h: head of ddl list
 * Return: the number of nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t size = 0;

	while (h)
	{
		h = h->next;
		size++;
	}
	return (size);
}
