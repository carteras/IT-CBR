using System;

namespace FactoryMethods {


    class Program {

        public abstract class Dog {
            public string Name { get; set; }
            public string Type { get; set; }

            public abstract string describe();
        }

        class Greyhound: Dog {

            public Greyhound(string name) {
                Name = name;
                Type = "Greyhound";
            }

            public override string describe() {
                return $"Hey, my name is {Name} and I am a {Type}. I love everybody!";
            }

        }

        class Collie: Dog {
            public Collie(string name) {
                Name = name;
                Type = "Collie";
            }

            public override string describe() {
                return $"Hey, my name is {Name} and I am a {Type}. I am very excited!";
            }
        }


        public static Dog GetDog() {
            Console.WriteLine("What is your dog's name?");
            var DogName = Console.ReadLine();
            Console.WriteLine("Press 1 for Greyhound.");
            Console.WriteLine("Press 2 for Collie.");
            var DogType = Console.ReadLine();
            if (DogType.Equals("1")) {
                return new Greyhound(DogName);
            }
            return new Collie(DogName);
        }

        
        static void Main(string[] args) {
            var sam = GetDog();
            var max = GetDog();
            Console.WriteLine(sam.describe());
            Console.WriteLine(max.describe());
        }
    }
}
