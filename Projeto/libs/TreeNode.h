//
//  TreeNode.h
//  ProgramacaoCientifica
//
//  Created by Guilherme Albertini on 25/07/19.
//  Copyright © 2019 Guilherme Albertini. All rights reserved.
//

#ifndef TreeNode_h
#define TreeNode_h

#include "TemplateLDE.h"

template <typename T>
class TreeNode {
private:
    TreeNode<T>* parentNode;
    TemplateLDE<TreeNode<T>*>* childrenNodes;
    T content;
    
public:
    
    TreeNode(){
        this->childrenNodes = new TemplateLDE<TreeNode<T>*>();
    }
    TreeNode(T content){
        this->childrenNodes = new TemplateLDE<TreeNode<T>*>();
        this->content = content;
    }
    
    //Get depth of node
    int getDepth(){
        TreeNode<T>* current_node = this;
        int depth = 0;
        
        while(current_node->getParent() != nullptr){
            current_node = current_node->getParent();
            depth++;
        }
        
        return depth;
    }
    
    //Return pointer to parent
    void setParent(TreeNode<T>* parent){
        this->parentNode = parent;
    }
    
    //Set content of node
    void setContent(T content){
        this->content = content;
    }
    
    //Get content of node
    T getContent(){
        return this->content;
    }
    
    //Return pointer to parent
    TreeNode<T>* getParent(){
        return this->parentNode;
    }
    
    //Return pointer to list of children
    TemplateLDE<TreeNode<T>*>* getChildrenList(){
        return this->childrenNodes;
    }
    
    //Insert Child
    void insertChild(T content){
        TreeNode<T>* child = new TreeNode<T>();
        child->setContent(content);
        child->setParent(this);
        childrenNodes->insertNodeFront(child);
    }
};

#endif /* TreeNode_h */

