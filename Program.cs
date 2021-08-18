using System;
using System.Timers;
using System.IO;
using System.Collections;
// using System.Text.Json;
using Newtonsoft.Json.Linq;
using System.Text.RegularExpressions;


namespace Typing_App
{
    interface UploadToJson
    {
        void uploadtojson();
    }
    interface showResult
    {
        void ShowResult();
    }

    public abstract class Grade : UploadToJson, showResult
    {
        private ArrayList badWords = new ArrayList();
        private ArrayList badChars = new ArrayList();
        private int chars;
        private int backTime;
        private int testTime;


        public float Per()
        {
            // StreamReader jsonfile = new StreamReader(@"Databases\Database.json");
            // string data = jsonfile.ReadToEnd();
            // JObject AnalysingResults = JObject.Parse(JArray.Parse(data)[2].ToString());
            // JObject lettersPerWords = JObject.Parse(AnalysingResults["Analysing Results"]["Advanced Datas"].ToString());
            // float CharsPerWord = lettersPerWords["Letters Per Words"].ToObject<float>();
            // return CharsPerWord;
            return 5;
        }

        public Grade(ArrayList _badWords, ArrayList _badChars, int _chars, int _backTime, int _testTime)
        {
            badWords = _badWords;
            badChars = _badChars;
            chars = _chars;
            backTime = _backTime;
            testTime = _testTime;
        }
        public ArrayList BadWords { get { return badWords; } set { badWords = value; } }
        public ArrayList BadChars { get { return badChars; } set { badChars = value; } }
        public int Chars { get { return chars; } set { chars = value; } }
        public int BackTime { get { return backTime; } set { backTime = value; } }
        public int TestTime { get { return testTime; } set { testTime = value; } }

        public int GoodChars(){
            return Chars - badChars.Count;
        }
        public double Accuracy()
        {

            return Convert.ToDouble(GoodChars()) /
                Convert.ToDouble(Chars);
        }
        public double Backspace_Freq()
        {
            return Convert.ToDouble(BackTime) /
                Convert.ToDouble(Chars);
        }
        public virtual float wpm()
        {
            return 0;
        }
        public float cpm()
        {
            return Chars / TestTime;
        }
        public void ShowResult()
        {
            Console.WriteLine(
                "WPM: " + (float)((int)(wpm() * 10)) / 10 + ",  CPM: " + (float)((int)(cpm() * 10)) / 10 +
                ",  Accuracy: " + Convert.ToDouble(Convert.ToInt32(Accuracy() * 1000)) / 10 + "%" +
                ",  BackSpace Frequency: " + Convert.ToDouble(Convert.ToInt32(Backspace_Freq() * 1000)) / 10 + "%");
        }
        public void uploadtojson()
        {
            var json_element = new Json_element
            {
                DateTime = DateTime.Now.ToString()
                    .Replace("\u4E0B\u5348", "P.M.").Replace("\u4E0A\u5348", "A.M."),
                TestLength = TestTime,
                TotalChars = Chars,
                GoodChars = GoodChars(),
                TotalBack = BackTime,
                WrongWords = (string[])BadWords.ToArray(typeof(string)),
                WrongChars = (string[])BadChars.ToArray(typeof(string))
            };
            string json = System.Text.Json.JsonSerializer.Serialize(json_element);
            File.AppendAllText(@"Databases\TypingPracticeRecords.json", "," + json + "]  ");
        }
    }
    public class Json_element
    {
        public string DateTime { get; set; }
        public int TestLength { get; set; }
        public int TotalChars { get; set; }
        public int GoodChars { get; set; }
        public int TotalBack { get; set; }
        public string[] WrongWords { get; set; }
        public string[] WrongChars { get; set; }
    }
    public class Common_Calculate_Way : Grade
    {
        public Common_Calculate_Way(ArrayList _badWords, ArrayList _badChars, int _chars, int _backTime, int _testTime)
                                                       : base( _badWords, _badChars, _chars, _backTime, _testTime)
        {
            TestTime = _testTime;
            BadWords = _badWords;
            Chars = _chars;
            BackTime = _backTime;
        }

        public override float wpm()
        {
            return cpm() / Per();
        }
    }
    public class For_Long_Time_Test : Grade
    {
        public For_Long_Time_Test( ArrayList _badWords, ArrayList _badChars, int _chars, int _backTime, int _testTime)
                                                     : base(_badWords, _badChars, _chars, _backTime, _testTime)
        {
            TestTime = _testTime;
            BadWords = _badWords;
            BadChars = _badChars;
            Chars = _chars;
            BackTime = _backTime;
        }
        public override float wpm()
        {
            return GoodChars() / TestTime;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            ushort TestTime = 1;
            void Exception()
            {
                try
                {
                    Console.WriteLine("How long do you want this test be ?\n");
                    Console.Write("Please Enter (minute): (Ex: 3)");
                    TestTime = Convert.ToUInt16(Console.ReadLine());
                }
                catch (IOException e)
                {
                    Console.Error.WriteLine("\n" + e.Message + "系統將自動判定為 1");
                }
                catch (OutOfMemoryException e)
                {
                    Console.Error.WriteLine("\n" + e.Message + "系統將自動判定為 1");
                }
                catch (ArgumentException e)
                {
                    Console.Error.WriteLine("\n" + e.Message + "系統將自動判定為 1");
                }
                catch (FormatException e)
                {
                    Console.Error.WriteLine("\n" + e.Message + "系統將自動判定為 1");
                }
                catch (System.OverflowException e)
                {
                    Console.Error.WriteLine("\n" + e.Message + "系統將自動判定為 1");
                }
                finally
                {
                    if (TestTime == 0)
                    {
                        Console.Error.WriteLine("不可為 0");
                        Exception();
                    }
                    else
                    {
                        Console.WriteLine("\nThis test is going to be " + TestTime +
                            " minites long. Press Enter to continue.");
                        Console.ReadLine();
                        Console.WriteLine("Ok, Let's Go !");
                    }
                }
            }

            Exception();
            StreamReader _preWord = new StreamReader(@"Databases\TypingPracticeRecords.json");
            string AllJsonContent = _preWord.ReadToEnd();
            _preWord.Close();
            StreamWriter preWork = new StreamWriter(@"Databases\TypingPracticeRecords.json");
            preWork.Write(AllJsonContent.Remove(AllJsonContent.Length - 3));
            preWork.Close();


            For_Long_Time_Test _g = new For_Long_Time_Test(new ArrayList(), new ArrayList(), 0, 0, TestTime);
            Common_Calculate_Way g = new Common_Calculate_Way(new ArrayList(), new ArrayList(), 0, 0, TestTime);

            Timer timer = new Timer(1000);
            timer.Elapsed += new ElapsedEventHandler(Timesup);
            timer.AutoReset = true;
            timer.Interval = TestTime * 1000 * 60;
            timer.Enabled = true;

            void Timesup(object source, ElapsedEventArgs e)
            {
                Console.WriteLine();
                Console.WriteLine("-------------------------------------------" +
                    "------------------------------------------------------------------");
                Console.WriteLine(".");
                Console.WriteLine(".");
                Console.WriteLine(".");
                g.ShowResult();
                g.uploadtojson();
                timer.Close();
                Console.Read();
            }

            ArrayList recordRandom = new ArrayList();
            ArrayList word = new ArrayList();

            int state = 1;


            StreamReader jsonfile = new StreamReader(@"Databases\Database.json");
            string data = jsonfile.ReadToEnd();
            JObject Dictionary = JObject.Parse(JArray.Parse(data)[0].ToString());
            JArray arrs = (JArray)Dictionary["Words List"];
            string[] arr = arrs.ToObject<string[]>();

            DateTime now = DateTime.Now;
            string Now = now.ToString();
            int secondNow = now.Second;
            int minuteNow = now.Minute;
            int hourNow = now.Hour;
            int yearNow = now.Year;
            int randomSeed = secondNow * yearNow * hourNow / minuteNow;

            createLine();
            input();

            void createLine()
            {
                recordRandom.Clear();
                recordRandom.Add("");
                Console.WriteLine();
                int i = 10;
                Random r = new Random(randomSeed / i * state + TestTime);
                int n = r.Next(Array.IndexOf(arr, "1980s"));
                while (i != 0)
                {
                    Console.Write("\u001b[1m" + arr[n] + "\u001b[0m      ");
                    recordRandom.Add(arr[n]);
                    n += 1;
                    i--;
                }
                Console.WriteLine();
            }


            void checkResultByChar(string Result, string standard)
            {
                if (standard.Length == Result.Length)
                {
                    for (int i = 0; i < Result.Length; i++)
                    {
                        if (standard[i] == Result[i])
                        {
                            g.BadChars.Add(standard[i].ToString());
                        }
                    }
                }
                if (Result.Length > standard.Length)
                {
                    while (Result.Length != standard.Length) standard += "!";
                    for (int i = 0; i < Result.Length; i++)
                    {
                        if (Result[i] != standard[i])
                        {
                            if (standard[i] != '!') g.BadChars.Add(standard[i].ToString());
                            else if (standard[i] == '!') g.BadChars.Add("Spaces");
                        }
                    }
                }
                if (Result.Length < standard.Length)
                {
                    while (Result.Length != standard.Length) Result += "!";
                    for (int i = 0; i < standard.Length; i++)
                    {
                        if (standard[i] != Result[i])
                        {
                            g.BadChars.Add(standard[i].ToString());
                        }
                    }
                }
            }


            void input()
            {
                ConsoleKeyInfo k = Console.ReadKey();
                if (k.KeyChar == ' ')
                {
                    string result = "";
                    foreach (char element in word) result += element.ToString();
                    g.Chars += result.Length + 1;
                    string standard(int n)
                    {
                        return Convert.ToString(recordRandom[n]);
                    }
                    if (state % 10 == 0)
                    {
                        string Standard = standard(10);
                        if (result == Standard)
                        {
                            Console.Write(" \u001b[38;5;82m(O)\u001b[0m ");
                        }
                        else
                        {
                            Console.Write(" \u001b[38;5;160m(X)\u001b[0m ");
                            g.BadWords.Add(Standard);
                            checkResultByChar(result, Standard);

                        }
                        Console.WriteLine();
                        createLine();
                    }
                    else
                    {
                        string Standard = standard(state % 10);
                        if (result == Standard)
                        {
                            Console.Write(" \u001b[38;5;82m(O)\u001b[0m ");
                        }
                        else
                        {
                            Console.Write(" \u001b[38;5;160m(X)\u001b[0m ");
                            g.BadWords.Add(Standard);
                            checkResultByChar(result, Standard);

                        }
                    }
                    word.Clear();
                    state++;
                    input();
                }
                else if (k.Key == ConsoleKey.Backspace)
                {
                    if (word.Count > 0)
                    {
                        string letters = "qwertyuiopasdfghjklzxcvbnm";
                        string symbols = "1234567890`~!@#$%^&*()_+-=[]{};':\"\\|/?,.<>QWERTYUIOPASDFGHJKLZXCVBNM";
                        foreach (char ch in letters)
                        {
                            if (ch.ToString() == word[word.Count - 1].ToString())
                            {
                                g.BadChars.Add(word[word.Count - 1].ToString());
                            }
                        }
                        foreach (char ch in symbols)
                        {
                            if(ch.ToString() == word[word.Count - 1].ToString())
                            {
                                g.BadChars.Add("Symbols");
                            }
                        }
                        word.RemoveAt(word.Count - 1);
                        g.BackTime++;
                    }
                    input();
                }
                else
                {
                    word.Add(k.KeyChar);
                    input();
                }
            }
        }
    }
}
