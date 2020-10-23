#include <string>
#include "./LinkedList.h"

ListNode::ListNode () {
	this->val = 0;
	this->next = NULL;
}

ListNode::ListNode (int val) {
	this->val = val;
	this->next = NULL;
}

/*
ListNode LLFactory::ConstructLL(vector<int> LL){
	ListNode* dummy = ListNode();
	ListNode* index = dummy;

	for(int i = 0; i < LL.size(); i++) {
		ListNode node(LL[i]);
		index->next = node;
		index = index->next;
	}

	return dummy->next;
}

string LLFactory::PrintLL(ListNode LL) {
	string retVal = "";

	ListNode index = LL;

	while (index.next) {
		retVal.append(to_string(index.val)).append(" -> ");
	}
	retVal.append("end");
	return retVal;
}
*/