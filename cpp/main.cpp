#include <iostream>
#include <string>
#include <vector>
#include "./LinkedList/LinkedList.h"

using namespace std;

int main()
{
	vector<int> testCase;
	testCase.push_back(3);
	testCase.push_back(4);
	testCase.push_back(5);
/*
	for(int i = 0; i < v.size(); i++) {
		v.push_back(testCase[i])
	}

	ListNode ll = LLFactory->ConstructLL(v);
	cout << LLFactory->PrintLL(ll) << endl
*/
	ListNode* dummy = new ListNode();

	ListNode* index = dummy;

	for(int i = 0; i < testCase.size(); i++) {
		ListNode* node = new ListNode(testCase[i]);
		index->next = node;
		index = index->next;
	}

	string retVal = "";

	index = dummy->next;

	while (index != NULL) {
		retVal.append(to_string(index->val)).append(" -> ");
		index = index->next;
	}

	retVal.append("end");
	cout << retVal << endl;

	return 0;
}