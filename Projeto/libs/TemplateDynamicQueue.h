//
//  TemplateDynamicQueue.h
//  ProgramacaoCientifica
//
//  Created by Guilherme Albertini on 28/07/19.
//  Copyright © 2019 Guilherme Albertini. All rights reserved.
//

#ifndef TemplateDynamicQueue_h
#define TemplateDynamicQueue_h

#include "TemplateLDE.h"

template <typename T>
class TemplateDynamicQueue : public TemplateLDE<T>{
public:
    
    //Constructor and Destructors
    TemplateDynamicQueue():TemplateLDE<T>(){};
    ~TemplateDynamicQueue(){};
    
    //Enqueue an element on queue
    bool enqueue(T a){
        return this->insertNodeBack(a);
    };
    //Dequeue an element on queue
    T dequeue(){
        return this->removeFrontNode();
    };
    //Check whether the queue is empty
    bool isQueueEmpty(){
        return this->isEmpty();
    }
    //Print front element on console
    void front(){
        this->peekFront();
    }
    
};

#endif /* TemplateDynamicQueue_h */


