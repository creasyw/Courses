#include <iostream>
using namespace std;

class Animal {
public:  
    virtual void speak()=0;
    virtual  void purr() { cout << "Purr\n"; }
};
class Cat : public Animal {
public:  
    void speak() { cout << "Meow\n";purr(); }
};
class Lion : public Cat {
public:  
    void speak() { cout << "ROAR\n"; }
    void purr() { cout << "ROAR\n"; }
};
int main() {
  Animal* c = new Cat();
  Cat napster;
  Lion googly;

  c->speak(); 
 
  napster.speak();
  googly.speak();
  return 0; 
}
