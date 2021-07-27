using System;
using System.Collections.Generic;

namespace HelloObjects
{

    class Dog
    {
        

        public string Name { get; set; }
        public int NumTreats { get; set; }

        public Dog(string name) {
            this.Name = name;
            this.NumTreats = 0;
        }

        public string bark()
        {
            return $"{this.Name} barks. Woof Woof!";
        }

        public void eatTreat()
        {
            this.NumTreats++;
        }
    }
    class Program
    {
        static List<Dog> dogs;
        static void Main(string[] args)
        {
            dogs = new List<Dog>();
            dogs.Add(new Dog("Sam"));
            dogs.Add(new Dog("Max"));
            dogs.Add(new Dog("Ranger"));

            foreach (Dog dog in dogs)
            {
                Console.WriteLine(dog.bark());
            }

            dogs[0].eatTreat();
            Console.WriteLine(dogs[0].NumTreats);
        }
    }
}
