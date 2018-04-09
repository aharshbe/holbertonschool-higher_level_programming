#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linkedlist
 * @list: linked list to be checked
 * Return: 1 if there is a cycle and 0 if there is not
 */

int check_cycle(listint_t *list)
{
	int count = 0, store = 0, recall = 0;
	listint_t *h, *o;

	if (!list)
		return (0);
	h = o = list;
	while (h)
	{
		for (count = 0; count < store; count++, o = o->next)
		{
			if (h == o)
			{
				recall = 1;
				break;
			}
		}
		if (recall)
			return (1);
		store++, o = list, h = h->next;
	}
	return (0);
}
