using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace W3Objects
{
     class Car
    {
        public string Make { get; set; }
        public string Model { get; set; }

        public string Rego { get; set; }

        private int _year;

        public int Year
        {
            get { return _year; }
            set { _year = value; }
        }


        public int Odometer { set; get; }


        public Car(string i)
        {
            string[] input = i.Split(':');
            //VW:Tiguan:1234:123abc
            this.Make = input[0];
            this.Model = input[1];
            this.Year = Convert.ToInt32(input[2]);
            this.Rego = input[3];

        }
    }

    class Program
    {
        public static List<Car> cars;
        static void Main(string[] args)
        {
            cars = new List<Car>();
            for (int i = 0; i < 2; i++)
            {
                Console.WriteLine("Enter in car details Make:Model:Year:Rego");
                //VW:Tiguan:1234:123abc
                string userInput = Console.ReadLine();
                Car newCar = new Car(userInput);
                cars.Add(newCar);
            }

            foreach (Car car in cars)
            {
                Debug.WriteLine($"{car.Make}, {car.Model} {car.Year}");
            }

            //Car newCar = new Car("VW", "Tiguan", "123abc", 2021);
            //Console.WriteLine($"I own a {newCar.getYear()} {newCar.getMake()} {newCar.getModel()} it has {newCar.getOdometer()}km on the clock.");

        }
    }
}
