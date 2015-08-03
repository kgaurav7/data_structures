#include <stdlib.h>
#include "bst.h"
#include <stdio.h>


typedef struct Node Node;

struct Node{
    int key;
    int value;
    int count;
    Node *left;
    Node *right;
};

static Node *root;
static void printLeftView(Node *x);
static void printRightView(Node *x);

static Node* getNode(Node* x, int key)
{
      while(x != NULL)
      {
          if(key < x->key) x = x->left;
          else if(key > x->key) x = x->right;
          else return x;
      }

      return NULL;
}

int get(int key)
{
    Node* match = getNode(root, key);
    if(match) return match->value;

    return -1;
}

static int sizeNode(Node *x)
{
    if(x == NULL) return 0;

    return x->count;
}

int sizeTree()
{
    return sizeNode(root);
}

static Node* putNode(Node* x, int key, int value)
{
    if(x == NULL) { 
        x = (Node *) malloc(sizeof(Node));
        x->key = key;
        x->value = value;
        x->count = 1;
        
        return x;
    }

    if(key < x->key) x->left = putNode(x->left, key, value);
    else if(key > x->key) x->right= putNode(x->right, key, value);
    else x->value = value;

   x->count = 1 + sizeNode(x->left) + sizeNode(x->right);

   return x;
}

void put(int key, int value)
{
    root = putNode(root, key, value);
}

Node* findFloorNode(Node* x, int key)
{
    if(x == NULL)
        return NULL;

    if(key == x->key)
        return x;

    if(key < x->key)
        return findFloorNode(x->left, key);

    Node* t = findFloorNode(x->right, key);
    if(t != NULL) return t;
   
    return x;
}

int bstfloor(int key)
{
    Node* x = findFloorNode(root, key);
 
    if(x == NULL) return -1;
    
    return x->key;
}

int rankNode(Node* x, int key)
{
    if(x == NULL) return 0;

    if(key < x->key) return rankNode(x->left, key);
    else if(key > x->key) return 1 + sizeNode(x->left) + rankNode(x->right, key);
    else return sizeNode(x);
}



int rank(int key)
{
    return rankNode(root, key);
}

static int htTree(Node *x)
{
    if(x == NULL) return 0;
  
    int left = 1 + htTree(x->left);
    int right = 1 + htTree(x->right);

    return left > right ? left : right;
}

int height()
{
    return htTree(root);
}

static void printLeftView(Node *x)
{
    if(x == NULL) return;
 
    printLeftView(x->left);
    printf("%d ", x->key);
}

static void printRightView(Node *x)
{
    if(x == NULL) return;
 
    printf("%d ", x->key);
    printRightView(x->right);
}

void prtTopView(Node *x)
{
    printLeftView(x->left);
    printf("%d ", x->key);
    printRightView(x->right);
}

void topView()
{
    prtTopView(root);
}
