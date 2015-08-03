#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node
{
    int data;
    Node *link;
} *head;

Node *reverseList(Node *head)
{
    if(head == NULL) 
        return NULL;

    if(head->link == NULL)
        return head;

    Node* newHead = reverseList(head->link);

    Node *x = head->link;

    x->link = head;
    head->link = NULL;

    return newHead;
}


int main()
{
    int i;

    for(i = 0; i < 5; i++)
    {
        Node * temp = (Node *) malloc(sizeof(Node));
       
        temp->data = i;
        Node* prevHead = head;
        head = temp;
        head->link = prevHead;
    }

    Node *ptr = head;
    for(i = 0; i < 5; i++)
    {
        printf("%d ", ptr->data);
        ptr = ptr->link;
    }

    printf("\n");

    head = reverseList(head);

   ptr = head;
    for(i = 0; i < 5; i++)
    {
        printf("%d ", ptr->data);
        ptr = ptr->link;
    }
}

