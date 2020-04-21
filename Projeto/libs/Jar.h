//
//  Jar.h
//  Projeto
//
//  Created by Guilherme Albertini on 17/03/20.
//  Copyright © 2020 Guilherme Albertini. All rights reserved.
//

#ifndef Jar_h
#define Jar_h
#include <iostream>
#include "TemplateLDE.h"

class Jar {

private:
    int JarA;
    int JarB;
    int LimitA;
    int LimitB;
    
public:
    
    Jar(){}
    
    Jar(int a, int b){
        this->JarA = a;
        this->JarB = b;
        this->LimitA = 3;
        this->LimitB = 4;
    }
    
    void printState(){
        std::cout<< "Jar A -> " << this->JarA << std::endl;
        std::cout<< "Jar B -> " << this->JarB << std::endl;
        std::cout<<std::endl;
    }
    
    TemplateLDE<Jar> getPossibleMoves(){
        TemplateLDE<Jar> possibleMoves;
        
    //        Encher a jarra de 3
        if(this->JarA < this->LimitA)
            possibleMoves.insertNodeFront(Jar(this->LimitA, this->JarB));
    //        Encher a jarra de 4
        if(this->JarB < this->LimitB)
            possibleMoves.insertNodeFront(Jar(this->JarA, this->LimitB));
    //        Esvaziar a jarra de 3
        if(this->JarA > 0)
            possibleMoves.insertNodeFront(Jar(0, this->JarB));
    //        Esvaziar a jarra de 4
        if(this->JarB > 0)
            possibleMoves.insertNodeFront(Jar(this->JarA, 0));
    //        Transferir de 3 para 4
        if(this->JarB < this->LimitB && this->JarA > 0){
            int transf = 0;
            transf = this->LimitB - this->JarB;
            
            
            if(transf > this->JarA){
                possibleMoves.insertNodeFront(Jar(0, this->JarB + transf));
            }else{
                possibleMoves.insertNodeFront(Jar(this->JarA - transf, this->JarB + transf));
            }
            
        }
        
        //        Transferir de 4 para 3
        if(this->JarA < this->LimitA && this->JarB > 0){
            int transf = 0;
            transf = this->LimitA - this->JarA;
            
            if(transf > this->JarB){
                possibleMoves.insertNodeFront(Jar(this->JarA + transf, 0));
            }else{
                possibleMoves.insertNodeFront(Jar(this->JarA + transf, this->JarB - transf));
            }
        }
        
        return possibleMoves;
    }
    
    bool equalTo(Jar test){
        return this->JarB == test.JarB &&
                this->JarA == test.JarA;
    }
    
    bool isAnswer(Jar test){
        return this->JarB == test.JarB;
    }
    
};

#endif /* Jar_h */
