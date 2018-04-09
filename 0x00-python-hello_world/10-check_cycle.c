#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linkedlist
 * @list: linked list to be checked
 * Return: 1 if there is a cycle and 0 if there is not
 */

int check_cycle(listint_t *list)
{
	int s[1024];
	int i = 0, k = 0, recall = 0;

	while (list)
	{
		s[k] = list->n;
		k++;
		while (s[i])
		{
			if (s[i] == list->next->n)
			{
				recall = 1;
				break;
			}
			i++;
		}
		if (recall)
			return (1);
		list = list->next;
	}
	return (0);
}
