#include "lists.h"
/**
 * insert_node - singly linked list
 * @head: pointer to head of linked list
 * @number: number to be inserted
 * Return: New nodes address or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *new_head, *tmp_head;

	if (!*head)
		return (NULL);

	new_node = malloc(sizeof(*head));
	if (!new_node)
		return (NULL);
	new_head = *head;
	new_node->n = number;

	while (new_head)
	{
		if (new_node->n > new_head->n)
		{
			if (new_node->n < new_head->next->n)
			{
				tmp_head = new_head->next;
				new_head->next = new_node;
				new_node->next = tmp_head;
				return (new_node);
			}
			else
			{
				new_head = new_head->next;
			}
		}
		new_head = new_head->next;
	}
	return (NULL);
}
