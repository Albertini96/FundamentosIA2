//
//  TemplateNode.cpp
//  ProgramacaoCientifica
//
//  Created by Guilherme Albertini on 24/07/19.
//  Copyright © 2019 Guilherme Albertini. All rights reserved.
//

#ifndef TemplateNode_hpp
#define TemplateNode_hpp

#include <stdio.h>
#include <iostream>

template <typename T>
class TemplateNode {
private:
    TemplateNode* nextNode;
    T content;
    
public:
    
    //Constructor and Destructors
    TemplateNode():content(NULL), nextNode(nullptr){}
    TemplateNode(T a):content(a), nextNode(nullptr){}
    TemplateNode(T a, TemplateNode* ne):content(a), nextNode(ne){}
    TemplateNode(TemplateNode* ne):content(NULL), nextNode(ne){}
    ~TemplateNode(){}
    
    //Get pointer to next linked TemplateNode
    TemplateNode* getNextNode(){
        return this->nextNode;
    };
    
    //Set the pointer to next linked TemplateNode
    bool setNextNode(TemplateNode* next){
        this->nextNode = next;
        return true;
    };
    
    //Return content of TemplateNode
    T getContent(){
        return this->content;
    };
    
};

#endif /* TemplateNode_hpp */



