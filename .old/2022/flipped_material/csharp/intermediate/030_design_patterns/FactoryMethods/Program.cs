using System;

namespace FactoryMethods {
    public abstract class Dog {
        public string Name { get; set; }
        public string Type { get; set; }

        public abstract string describe();
    }

    class Greyhound : Dog {

        public Greyhound(string name) {
            Name = name;
            Type = "Greyhound";
        }

        public override string describe() {
            return $"Hey, my name is {Name} and I am a {Type}. I love everybody!";
        }

    }

    class Collie : Dog {
        public Collie(string name) {
            Name = name;
            Type = "Collie";
        }

        public override string describe() {
            return $"Hey, my name is {Name} and I am a {Type}. I am very excited!";
        }
    }
    public class Program {

        public static Dog DogFactory() {
            Dog myDog;
            Console.WriteLine("What is the name of your dog?");
            var DogName = Console.ReadLine();
            Console.WriteLine("Type 1 if your dog is a Greyhound");
            Console.WriteLine("Type 2 if your dog is a Collie");
            var Breed = Console.ReadLine();
            if (Breed.Equals("1")) {
                myDog = new Greyhound(DogName);
            } else {
                myDog = new Collie(DogName);
            }

            return myDog;
        }
        public static void Main(string[] args) {
            Dog myDog = DogFactory();            
            Console.WriteLine(myDog.describe());
        }
    }
}