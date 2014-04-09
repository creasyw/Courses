/*
 *  The scanner definition for COOL.
 */

/*
 *  Stuff enclosed in %{ %} in the first section is copied verbatim to the
 *  output, so headers and global definitions are placed here to be visible
 * to the code in the file.  Don't remove anything that was here initially
 */
%{
#include <cool-parse.h>
#include <stringtab.h>
#include <utilities.h>
#include <string.h>

/* The compiler assumes these identifiers. */
#define yylval cool_yylval
#define yylex  cool_yylex

/* Max size of string constants */
#define MAX_STR_CONST 1025
#define YY_NO_UNPUT   /* keep g++ happy */

extern FILE *fin; /* we read from this file */

/* define YY_INPUT so we read from the FILE fin:
 * This change makes it possible to use this scanner in
 * the Cool compiler.
 */
#undef YY_INPUT
#define YY_INPUT(buf,result,max_size) \
    if ( (result = fread( (char*)buf, sizeof(char), max_size, fin)) < 0) \
        YY_FATAL_ERROR( "read() in flex scanner failed");

char string_buf[MAX_STR_CONST]; /* to assemble string constants */
char *string_buf_ptr;

extern int curr_lineno;
extern int verbose_flag;

extern YYSTYPE cool_yylval;

/*
 *  Add Your own definitions here
 */



%}

/*
 * Define names for regular expressions here.
 */

DARROW          =>
LE      <=
ASSIGN      <-
DIGIT   [0-9]
LETTER  [a-zA-Z:_]
SPACE   [ \t\f\r]
NEWLINE [\n]
%%

 /* 
  * single line comments
  */
"--"[^\n]*  {
        printf("matching comment %s\n",yytext);
        /*do nothing, consume the comments */
        }




 /*
  *  Nested comments
  *  
  */


 /*
  *  The multiple-character operators.
  */

{DARROW}        { return (DARROW); }
{LE}            { return LE; }
{ASSIGN}        {return ASSIGN;}

 /*
  * Keywords are case-insensitive except for the values true and false,
  * which must begin with a lower-case letter.
  */

class   {return CLASS;}
else    {return ELSE;}
fi  {return FI;}
if  {return IF;}
in  {return IN;}
inherits    {return INHERITS;}
let {return LET;}
loop    {return LOOP;}
pool    {return POOL;}
then    {return THEN;}
while   {return WHILE;}
case    {return CASE;}
esac    {return ESAC;}
of  {return OF;}
new {return NEW;}
isvoid  {return ISVOID;}

t[Rr][Uu][Ee]   { 
        cool_yylval.boolean=1;
            return BOOL_CONST;
        }

f[aA][lL][sS][eE]   {
            cool_yylval.boolean=0;
            return BOOL_CONST;
            }

"+" {return '+';} /* for expressions, not implemented yet do nothing for now */
"-" {return '-';} /* for expressions, not implemented yet do nothing for now*/
";" {return ';';}
"{" {return '{';} /* begin scope do nothing for now*/
"}" {return '}';} /* end scope do nothing for now*/
"." {return '.';}
"(" {return '(';}
")" {return ')';}
":" {return ':';}

 /* 
  * IntConst
  */
{DIGIT}*        {
                /*not sure if we should use inttable.add_string() or inttable.addint() look sour*/
                cool_yylval.symbol = inttable.add_string(yytext);
                return INT_CONST;
                }


{SPACE}

 /*
  *  String constants (C syntax)
  *  Escape sequence \c is accepted for all characters c. Except for 
  *  \n \t \b \f, the result is c.
  *
  */
\"[^"\0\t\f]*\"?    {
        /*printf("string const:%s",yytext);*/
        std::string s1(yytext);
        std::string s2 = s1.substr(1,strlen(yytext)-2);
        char *type = new char[s2.length()];
        /*printf("stripped str const:%s",type);*/
        strcpy(type,s2.c_str());
        cool_yylval.symbol = stringtable.add_string(type);
        return STR_CONST;
        }

 /*
  * Identifiers, there are 2 types, a string identifier and a typeid identifier. 
  * A typeid identifier starts with a : followed by whitespace and a series of letters
  * A string identifier is just a series of letters. These 2 rules have to work simultaenously
  * put the colon rule first, should be a longest subsequence match
  * the above rule is wrong, make the colon a char return, then 
  * make everything else a id_table token
  */




 /*  TYPEID starts with upper case?
  *  a class starts with upper case like type 
  *  OBJECTID starts with lower case? 
  *
  */
[a-z]{LETTER}*       {
        /*printf("id:%s \n",yytext);*/
        cool_yylval.symbol=idtable.add_string(yytext);
        return OBJECTID;
        }

[A-Z]{LETTER}*  {
                 /*printf("upper case:%s",yytext);*/
                 cool_yylval.symbol=idtable.add_string(yytext);
         return TYPEID;
                }

{NEWLINE}    {curr_lineno++;}

<<EOF>>

 .  { //this is 2 chars, one for end of string char and one for the char being tokenized which has no match

       char *tp = new char[2];
        strcpy(tp,yytext);
       cool_yylval.error_msg=tp;
       return ERROR;
    }

%%
