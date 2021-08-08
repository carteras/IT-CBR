using System;
using System.Collections.Generic;
namespace Test {


    class Program {

        public static string foo(List<string> f) {
            string foo = "";
            foreach (String s in f) {
                foo += s;
            }
            return foo;
        }
        static void Main(string[] args) {

            var tt = new List<string>();
            tt.Add("foo");
            tt.Add("bar");
            Console.WriteLine(foo(tt));
            
        }
    }
}
