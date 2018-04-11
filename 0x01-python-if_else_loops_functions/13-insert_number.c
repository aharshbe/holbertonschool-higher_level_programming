#include "lists.h"
/**
 * insert_node - singly linked list
 * @head: pointer to head of linked list
 * @number: number to be inserted
 * Return: New nodes address or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *tmp_head;

	if (!head)
		return (NULL);

	new = malloc(sizeof(*head));
	if (!new)
		return (NULL);

	current = *head;
	new->n = number;
	tmp_head = NULL;

	if (current)
	{
		if (current->n > number)
		{
			tmp_head = current->next;
			*head = new;
			new->next = tmp_head;
			return (new);
		}
	}

	while (current && number > current->n)
	{
		tmp_head = current;
		current = current->next;
	}
	if (!(!tmp_head))
	{
		tmp_head->next = new;
		new->next = current;
	}
	else
		*head = new;
	return (new);	
}
