#include "lists.h"

/**
 * check_cycle - function entry
 * Description: Function that checks if a singly linked list has a cycle in it
 * @list: head address of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *one_step = list;
	listint_t *two_step = list->next;

	if (one_step == NULL || two_step == NULL)
		return (0);

	while (two_step != NULL && two_step->next != NULL)
	{
		if (one_step == two_step)
			return (1);

		one_step = one_step->next;
		two_step = two_step->next->next;
	}
	return (0);
}
