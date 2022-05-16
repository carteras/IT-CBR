using System;
using System.Collections.Generic;

namespace DogPark {

    abstract class Dog {
        public string Name { get; set; }
        public string BarkSound { get; set; }

        public string Bark() {
            return $"{Name} barks at you! {BarkSound} {BarkSound}";
        }
    }


    class Greyhound : Dog {

        public Greyhound(string name) {
            Name = name;
            BarkSound = "yep";
        }
 
        
    }

    class Poodle : Dog {

        public Poodle(string name) {
            Name = name;
            BarkSound = "woof";
        }
     
    }

    class DogPark {
        List<Dog> dogs = new List<Dog>();
        
        public void AddDog(Dog d) {
            dogs.Add(d);
        }

        public void run() {
            foreach (Dog d in dogs) {
                Console.WriteLine(d.Bark());
            }
        }
    }
    class Program {
        static void Main(string[] args) {
            DogPark dp = new DogPark();
            dp.AddDog(new Greyhound("Sam"));

            dp.run();
        }
    }
}
