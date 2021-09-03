using System;
using System.Collections.Generic;

namespace PatternsState {

public class Program {
        public static void Main(string[] args) {
            var quotes = new List<string>();
            quotes.Add("Be yourself; everyone else is taken - Oscar WIlde");
            quotes.Add("The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela");
            quotes.Add("A room without books is like a body without a soul. - Marcus Tullius Cicero");
            quotes.Add("The way to get started is to quit talking and begin doing. -Walt Disney");
            quotes.Add("Be the change that you wish to see in the world. - Mahatma Gandhi");
            quotes.Add("Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs");
            quotes.Add("If you tell the truth, you don't have to remember anything. - Mark Twain");

            for (int i = 0; i < quotes.Count; i++) {
                if (i % 2 == 0) {
                    Console.WriteLine(quotes[i].ToLower());
                } else {
                    Console.WriteLine(quotes[i].ToUpper());
                }
            }
        }
    }
}
