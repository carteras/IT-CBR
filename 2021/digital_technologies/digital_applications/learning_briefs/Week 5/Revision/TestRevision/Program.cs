using System;

namespace TestRevision {
    class Program {
        enum Level {
            Awesome = 1,
            Cool = 2,
        }
        static void Main(string[] args) {
            var foo = Level.Cool;

            Console.WriteLine((int)foo) ;

        }
    }
}
