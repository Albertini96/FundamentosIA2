//
//  TemplateDynamicStack.h
//  ProgramacaoCientifica
//
//  Created by Guilherme Albertini on 28/07/19.
//  Copyright © 2019 Guilherme Albertini. All rights reserved.
//

#ifndef TemplateDynamicStack_h
#define TemplateDynamicStack_h

#include "TemplateLDE.h"

template <typename T>
class TemplateDynamicStack : public TemplateLDE<T>{
public:
    
    //Constructor and Destructors
    TemplateDynamicStack():TemplateLDE<T>(){};
    ~TemplateDynamicStack(){};
    
    //Push a new element on the stack
    bool push(T a){
        return this->insertNodeBack(a);
    };
    //Pop the top element of the stack
    T pop(){
        return this->removeBackNode();
    };
    //Check if stack is empty
    bool isStackEmpty(){
        return this->isEmpty();
    };
    //Prints top element on console
    void top(){
        this->peekBack();
    };
};


#endif /* TemplateDynamicStack_h */


