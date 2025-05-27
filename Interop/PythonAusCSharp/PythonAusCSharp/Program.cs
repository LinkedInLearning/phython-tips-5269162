using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PythonAusCSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            

            string pythonCode = "3 + 4 * (2 - 1)";
            var psi = new ProcessStartInfo
            {
                FileName = "python", // Oder "python" je nach System
                Arguments = $"eval.py \"{pythonCode}\"",
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            var process = Process.Start(psi);
            string output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();

            Console.WriteLine("Ergebnis von Python eval(): " + output);

        }
    }
}
