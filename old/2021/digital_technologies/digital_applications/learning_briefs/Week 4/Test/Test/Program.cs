using System;
using System.Collections.Generic;
namespace Demo {
    class Program {
        static void Main(string[] args) {
            var random = new Random();
            var names = new List<string> { "ada", "bob", "charlie", "erin" };
            var place = new List<string> { "to the shops", "school", "to work", "home" };
            Console.WriteLine($"{names[random.Next(names.Count)]} went {place[random.Next(place.Count)]}");
        }
    }
}