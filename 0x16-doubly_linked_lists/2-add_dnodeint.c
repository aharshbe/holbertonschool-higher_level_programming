#include "lists.h"
/**
 * add_dnodeint - Add a new node at the start of the list
 * @h: head of ddl list
 * @n: member for new node to add
 * Return: the address for new element or null if failed
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;

	if (!*head)
	{
		new->prev = NULL;
		new->next = NULL;
		*head = new;
		return (new);
	}
       	(*head)->prev = new;
	new->next = *head;
	new->prev = NULL;
	*head = new;
	return (new);
}
