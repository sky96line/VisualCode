using System;
using System.IO.Ports;

class ReadUSB
{
	static void Main(String[] args)
	{
		using (SerialPort port = new SerialPort("COM30"))
		{
			port.BaudRate = 115200;
			port.Parity = Parity.None;
			port.ReadTimeout = 10;
			port.StopBits = StopBits.One;

			port.Open();
			while(true)
			{
				try {
					Console.Write((char)port.ReadChar());
				}
	catch(Exception e) {Console.WriteLine(e);}
			}
		}
	}
}