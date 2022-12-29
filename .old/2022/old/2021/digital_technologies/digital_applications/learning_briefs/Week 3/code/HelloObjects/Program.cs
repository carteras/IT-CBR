using System;
using System.Collections.Generic;

namespace HelloObjects {
    // name 
    // barkSound
    // breed
    class Dog {
        public string Name { get; set; }
        public string Bark { get; set; }

        public string Breed { get; set; }

        public Dog(string name, string bark, string breed) {
            this.Name = name;
            this.Bark = bark;
            this.Breed = breed;
        }

        public string describe() {
            return $"This dog's name is: {this.Name} they are a {this.Breed}. They barks! {this.Bark}, {this.Bark}!";
        }


    }
    class Program {
        static List<Dog> dogs;
        static Random rand; 
        static void Main(string[] args) {
            dogs = new List<Dog>();
            rand = new Random();
            
            var dogNames = new List<string> {"Sam", "Max", "Ranger", "Charlie" };
            var barks = new List<string> { "woof", "yip" };
            var breeds = new List<string> { "Greyhound", "Border Collie" };

            for (int i = 0; i < 10; i++) {
                var nameIndex = rand.Next(dogNames.Count);
                var barksIndex = rand.Next(barks.Count);
                var breedsIndex = rand.Next(breeds.Count);
                dogs.Add(new Dog(dogNames[nameIndex], barks[barksIndex], breeds[breedsIndex]));
            }

            for (int j = 0; j < 10; j++) {
                foreach (Dog dog in dogs) {
                    Console.WriteLine(dog.describe());
                }
                Console.WriteLine(j);
            }
        }
    }
}
