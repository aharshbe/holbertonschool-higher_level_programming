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

	new->n = number;
	tmp_head = NULL;
	current = *head;

	while (current && number >= current->n)
	{
		tmp_head = current;
		current = current->next;
	}
	new->next = current;

	if (tmp_head != NULL)
		tmp_head->next = new;
	else
		*head = new;
	return (new);
}
