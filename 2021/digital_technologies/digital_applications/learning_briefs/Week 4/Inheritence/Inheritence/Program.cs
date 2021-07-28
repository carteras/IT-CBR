using System;
using System.Collections.Generic;

namespace Inheritence
{

    abstract class User {
        public string Name { get; set; }
        public User(string name) {
            Name = name;
        }

        public abstract string Describe();
    }

    class Student : User {
        public int Age { get; set; }
        public Student(string name, int age) : base(name) {
            Name = name;
            Age = age;
        }

        public override string Describe() {
            return $"This is {this.Name} and they are {this.Age} years old";
        }
    }

    class Teacher : User {
        public int Salary { get; set; }

        public Teacher(string name, int salary) : base(name) {
            Name = name;
            Salary = salary;
        }
        public override string Describe() {
            return $"This is {this.Name} and he earns ${this.Salary}";
        }
    }
    class Program {
        static List<User> users;
        public static void Main(string[] args)
        {
            users = new List<User>();
            users.Add(new Student("Ada", 16));
            users.Add(new Teacher("Adam", 110000));

            foreach (User user in users) {
                Console.WriteLine(user.Describe());
            }
        }
    }
}
