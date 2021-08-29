using System;
using System.Collections.Generic;

namespace PatternsState {

    public class StateContext {
        private CaseState _State;

        public StateContext() {
            _State = new LowerCaseState();
        }

        public void SetState(CaseState State) {
            _State = State;
        }

        public void WriteOut(String Phrase) {
            _State.WriteOut(this, Phrase);
        }
    }


    public abstract class CaseState {
        public abstract void WriteOut(StateContext Context, String Phrase);
    }

    public class LowerCaseState : CaseState {
        public override void WriteOut(StateContext Context, string Phrase) {
            Console.WriteLine(Phrase.ToLower());
            Context.SetState(new UpperCaseState());
        }
    }

    public class UpperCaseState : CaseState {
        public override void WriteOut(StateContext Context, string Phrase) {
            Console.WriteLine(Phrase.ToUpper());
            Context.SetState(new MockingCaseState());
        }
    }

    public class MockingCaseState : CaseState {
        public override void WriteOut(StateContext Context, string Phrase) {
            for (int i = 0; i < Phrase.Length; i++) {
                if (i % 2 == 0) {
                    Console.Write(char.ToUpper(Phrase[i]));
                } else {
                    Console.Write(Phrase[i]);
                }
            }
            Console.WriteLine();
            Context.SetState(new LowerCaseState());
        }
    }

class Program {
        static void Main(string[] args) {
            var quotes = new List<string>();
            quotes.Add("Be yourself; everyone else is taken - Oscar WIlde");
            quotes.Add("The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela");
            quotes.Add("A room without books is like a body without a soul. - Marcus Tullius Cicero");
            quotes.Add("The way to get started is to quit talking and begin doing. -Walt Disney");
            quotes.Add("Be the change that you wish to see in the world. - Mahatma Gandhi");
            quotes.Add("Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs");
            quotes.Add("If you tell the truth, you don't have to remember anything. - Mark Twain");


            StateContext context = new StateContext();

            foreach (string quote in quotes) {
                context.WriteOut(quote);
            }
        }
    }
}
1