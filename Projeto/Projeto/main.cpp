//
//  main.cpp
//  Projeto
//
//  Created by Guilherme Albertini on 17/03/20.
//  Copyright © 2020 Guilherme Albertini. All rights reserved.
//

#include <iostream>
//#include "Stack.hpp"
#include "TemplateLDE.h"
#include "Tree.h"
#include "Jar.h"

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    
    Jar start_state = Jar(0, 0);
    Jar final_state = Jar(1, 2);
    
    Tree<Jar> arvore(start_state);
    arvore.dfs_traversal(final_state);
//    arvore.bfs_traversal(final_state);
    
    return 0;
}
