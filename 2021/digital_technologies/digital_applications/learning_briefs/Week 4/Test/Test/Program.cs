using System;
using System.Collections.Generic;
namespace Test {

    abstract class Foo{
        public string Thing { get; set; }

        public abstract string describe();
    }

    class Bar: Foo {
        public Bar() {
            Thing = "What?";
        }

        public override string describe() {
            return $"{Thing} is in Bar";
        }
    }

    class Boo: Foo {
        public Boo() {
            Thing = "What what?";
        }
        public override string describe() {
            return $"I am not bar, I am boo {Thing}";
        }
    }
    class Program {
        static void Main(string[] args) {
            var foos = new List<Foo>();
            foos.Add(new Bar());
            foos.Add(new Boo());

            foreach (Foo f in foos) {
                Console.WriteLine(f.describe());
            }
        }
    }
}
