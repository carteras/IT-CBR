using System;
using System.IO;

namespace ASCIIGame {
    /// <summary>
    /// ASCIIGame starter code. 
    /// Welcome to the starter code for an ascii game!
    /// This starter code has some features but is missing others. It also isn't beautiful 
    /// 
    /// Features: 
    /// <point>Reads a text file</point>
    /// <point>Renders text file as map</point>
    /// <point>Detects if there is amonster and tells you which way</point>
    /// <point>Takes user input and moves the player in response</point>
    /// 
    /// Todo:
    /// <point>Collision Detection - Mobile Objects (players and monsters) can't walk through walls</point>
    /// <point>A combat system</point>
    /// <point>an inventory</point>
    /// <point>items that can change aspects of the combat system</point>
    /// <point>Classes</point>
    /// <point>Doors/chests that can open or close</point>
    /// <point>Mobs that can move to nearby opponents. (simple AI)</point>
    /// <point>Objects!</point>
    /// <point>Class Inheritance!</point>
    /// <point>Beautiful design patterns!</point>
    /// 
    /// Known bugs: 
    /// <point>Players and monsters aren't known on the map. So you don't know if you are standing on a mob/door/chest.</point>
    /// <point>If you go north or west you get an exception</point>
    /// </summary>
    class Program {
        static void Main(string[] args) {
            // Players x and y positions are held in int
            int playerX = 3;                                                  
            int playerY = 3;
            int mobX = 15;
            int mobY = 3;

            // I need to know what kind of tile I am standing on. 
            char tile;

            //This path will read a map from your project directory
            var path = Path.Combine(Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName, "map.txt");
            string[] map = File.ReadAllLines(path);

            ConsoleKeyInfo user_input;
            Console.WriteLine("Press Q to quit");

            do {
                // Every time I start a loop, clear the screen. 
                Console.Clear();

                // Renders the map from the string[] map
                // I wonder if this should be in a function (or even better a Factory?)
                for (int y = 0; y < map.Length; y++) {
                    for (int x = 0; x < map[y].Length; x++) {
                        if (x == playerX && y == playerY) {
                            Console.Write("@");
                        } else if (x == mobX && y == mobY) {
                            Console.Write("&");
                        } else {
                            Console.Write(map[y][x]);
                        }
                    }
                    Console.Write("\r\n");
                }
                Console.WriteLine("Press, up, down, left, right or Q to quit");
                
                /*RenderMap(playerX, playerY, mobX, mobY, map);*/
                var deltaX = playerX - mobX;
                var deltaY = playerY - mobY;

                Console.Write("There is a noise from the ");

                // Is the mob north or south of me? 
                if (deltaY > 0) {
                    Console.Write(" North");
                } else if (deltaY < 0) {
                    Console.Write(" South");
                }

                // Is the mob west or east of me? 
                if (deltaX > 0) {
                    Console.Write(" West");
                } else if (deltaX < 0) {
                    Console.Write(" East ");
                }

                Console.Write(". ");

                // What is under neath me? 
                tile = map[playerY][playerX];
                Console.Write($"You are standing on {tile}");

                // Capture user input
                user_input = Console.ReadKey();
                if (user_input.Key == ConsoleKey.UpArrow) {
                    playerY--;
                } else if (user_input.Key == ConsoleKey.DownArrow) {
                    playerY++;
                } else if (user_input.Key == ConsoleKey.RightArrow) {
                    playerX++;
                } else if (user_input.Key == ConsoleKey.LeftArrow) {
                    playerX--;
                }
            } while (user_input.Key != ConsoleKey.Q);
        }
    }
}
