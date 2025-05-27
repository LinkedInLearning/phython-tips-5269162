using System;
using System.Windows.Forms;

namespace WinFormInterop
{
    public class MainForm : Form
    {
        private Button button;
        private Label label;

        public MainForm()
        {
            this.Text = "WinForms aus Python";
            this.Width = 300;
            this.Height = 200;

            label = new Label();
            label.Text = "Starttext";
            label.Top = 30;
            label.Left = 30;
            label.Width = 200;

            button = new Button();
            button.Text = "Klick mich!";
            button.Top = 70;
            button.Left = 30;
            button.Click += (sender, e) => label.Text = "Button wurde geklickt!";

            this.Controls.Add(label);
            this.Controls.Add(button);
        }

        public void ShowForm()
        {
            Application.Run(this);
        }
    }
}
