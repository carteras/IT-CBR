using System;

namespace TestRevision {

    class Foo {
        public string WhatClassIsThis() {
            return "This is Foo!";
        }

        public string SpecialFooFunction() {
            return "This is a special function in Foo";
        }
    }

    class Baz {
        public string WhatClassIsThis() {
            return "This is Baz";
        }

        public string SpecialBazFunction() {
            return "this is a special function in Baz";
        }
    }

    class Bar{
        private Foo _ClassA = new Foo();
        private Baz _ClassB = new Baz();

        public string WhatClassIsThis() {
            return $"Hey, let's check in with {_ClassA.WhatClassIsThis()} and {_ClassB.WhatClassIsThis()}";
        }

        public string SpecialFooFunction() {
            var data = _ClassA.SpecialFooFunction();
            return data + " this is the child class C doing stuff with foo";
        }
    }

    class Program {
        
        static void Main(string[] args) {
            var someObject = new Bar();
            Console.WriteLine(someObject.WhatClassIsThis());
            Console.WriteLine(someObject.SpecialFooFunction());

        }
    }
}
