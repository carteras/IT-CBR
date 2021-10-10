using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace Testing {

    public abstract class HelloWorld {
        public abstract string SayIt();
    }

    public class Normal : HelloWorld {
        public override string SayIt() {
            return "Hello, World!";
        }
    }

    public class Lazy : HelloWorld {
        public override string SayIt() {
            return "hello world";
        }
    }


    public class Thing {
        public HelloWorld Foo { get; set; }

        public Thing(HelloWorld hw) {
            Foo = hw;
        }

        public string SayIt() {
            return Foo.SayIt();
        }

    }

    
    public class Program {

        public static void Main(string[] args) {
            Thing t = new Thing(new Normal());
            Debug.WriteLine(t.SayIt());
            t.Foo = new Lazy();
            Debug.WriteLine(t.SayIt());
        }
    }
}
