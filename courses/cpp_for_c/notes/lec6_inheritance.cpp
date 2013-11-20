

class student { 
  public: 
  enum year { fresh, soph, junior, senior, grad }; 
  student(char* nm, int id, double g, year x); 
  void print() const; //??? What does this mean 
  protected: 
  int student_id; 
  double gpa; 
  year y; 
  char name[30]; 
  }; 

class grad_student : public student {//public - subtype 
  public: 
  enum support { ta, ra, fellowship, other }; 
  grad_student(char* nm, int id, double g, 
                     l  year x, support t, char* d, char* th); 
  void print() const; 
  protected: 
  support s; 
  char dept[10]; 
  char thesis[80]; 
  }; 

