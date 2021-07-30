using System;
using System.Collections.Generic;

namespace Foo {

    class Dog {
        public string Name { get; set; }
        public string BarkNoise { get; set; }
        public string Breed { get; set; }

        public Dog(string name, string bark, string breed) {
            this.Name = name;
            this.BarkNoise = bark;
            this.Breed = breed;
        }

        public string describe() {
            return $"This dog's name is {this.Name}, they are a {this.Breed}. They go {this.BarkNoise}";
        }

    }
    class Program {
        static List<Dog> dogs;
        static void Main(string[] args) {
            dogs = new List<Dog>();
            dogs.Add(new Dog("Sam", "woof", "Greyhound"));
            dogs.Add(new Dog("Max", "yip", "Poodle"));

            foreach (Dog dog in dogs) {
                Console.WriteLine(dog.describe());
            }
        }
    }
}
