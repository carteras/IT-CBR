using System;
using System.Collections.Generic;

namespace Composition {
    public enum FighterClass {
        Knight,
        Ninja,
        Samurai,
        Assassin,
        Viking,
        Mamluk
    }
    public class Fighter {
        public string Name { get; set; }
        public int Damage { get; set; }
        
        public int Health { get; set; }

        public int Armour { get; set; }

        public FighterClass FighterClass {get;set;} 

        public Fighter(string name, FighterClass fighterClass) {
            Name = name;
            Damage = 1;
            Health = 10;
            FighterClass = fighterClass;
        }


        public int  Attack() {
            return Damage;
        }

        public void RecieveDamage(int damage) {
            Health -= damage;
        }
    }

    public class FightPit {
        List<Fighter> fighters;

        public FightPit() {
            fighters = new List<Fighter>();
        }

        public void AddFighter(Fighter f) {
            fighters.Add(f);
        }

        public Boolean StillFighting() {
            if (fighters.Count > 0) {
                return true;
            }
            return false;
        }

        public string Fight() {
            // return a string
            var random = new Random();
            
            Fighter f1 = fighters[random.Next(fighters.Count)];
            Fighter f2 = fighters[random.Next(fighters.Count)];
   
            f2.RecieveDamage(f1.Attack());

            return $"{f1.Name} attacks {f2.Name} for {f1.Damage}. {f2.Name} has {f2.Health} remaining";
        }

        public string CleanUp() {
            List<string> output = new List<String>();
            List<Fighter> remaining = new List<Fighter>();
            foreach (Fighter f in fighters) {
                if (f.Health > 0) {
                    remaining.Add(f);
                } else {
                    output.Add(f.Name);
                }
            }
            fighters = remaining;
            if (output.Count > 1) return $"{string.Join(",", output.ToArray())} are dead.";
            if (output.Count == 1) return $"{string.Join(",", output.ToArray())} is dead.";
            return "Nobody died this round!";

        }
    }

    public class Program {

        public static void Main(string[] args) {
            FightPit pit = new FightPit();
            pit.AddFighter(new Fighter("Ada", FighterClass.Knight));
            pit.AddFighter(new Fighter("Bob", FighterClass.Ninja));
            pit.AddFighter(new Fighter("Charles", FighterClass.Assassin));
            pit.AddFighter(new Fighter("Eva", FighterClass.Samurai));
            pit.AddFighter(new Fighter("Fred", FighterClass.Viking));
            pit.AddFighter(new Fighter("Georgia", FighterClass.Mamluk));

            while (pit.StillFighting()) {
                Console.WriteLine(pit.Fight());
                Console.WriteLine(pit.CleanUp());
            }
            
        }
    }
}
