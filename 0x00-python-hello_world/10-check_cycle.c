#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linkedlist
 * @list: linked list to be checked
 * Return: 1 if there is a cycle and 0 if there is not
 */

int check_cycle(listint_t *list)
{
	listint_t *h, *o;

	if (!list && !list->next)
		return (0);
	h = list, o = h->next;
	while (o->next && o->next->next && o->next->next->next)
	{
		if (h == o)
			return (1);
		h = h->next, o = o->next->next->next;
	}
	return (0);
}
