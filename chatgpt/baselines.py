import wx
import os
import subprocess

class NetworkMetrics(wx.Frame):
    def __init__(self, *args, **kw):
        super(NetworkMetrics, self).__init__(*args, **kw)
        
        # Initialize UI
        self.InitUI()
        
    def InitUI(self):
        # Set up main panel
        panel = wx.Panel(self)

        # Add output text control
        self.output = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY)

        # Add interface button
        intf_btn = wx.Button(panel, label="Interfaces")
        intf_btn.Bind(wx.EVT_BUTTON, self.OnInterfaces)

        # Add ping button
        ping_btn = wx.Button(panel, label="Ping")
        ping_btn.Bind(wx.EVT_BUTTON, self.OnPing)

        # Add speedtest button
        speedtest_btn = wx.Button(panel, label="Speedtest")
        speedtest_btn.Bind(wx.EVT_BUTTON, self.OnSpeedtest)

        # Add wireless environment info button
        wifi_btn = wx.Button(panel, label="Wireless Environment")
        wifi_btn.Bind(wx.EVT_BUTTON, self.OnWifi)

        # Add quit button
        quit_btn = wx.Button(panel, label="Quit")
        quit_btn.Bind(wx.EVT_BUTTON, self.OnQuit)

        # Set up sizer for main panel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.output, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(intf_btn, 0, wx.ALL, 5)
        sizer.Add(ping_btn, 0, wx.ALL, 5)
        sizer.Add(speedtest_btn, 0, wx.ALL, 5)
        sizer.Add(wifi_btn, 0, wx.ALL, 5)
        sizer.Add(quit_btn, 0, wx.ALL, 5)

        # Set sizer for panel and show UI
        panel.SetSizer(sizer)
        self.Show(True)

    def OnInterfaces(self, e):
        # Get network interface information
        result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
        output = result.stdout.decode()

        # Set output text
        self.output.SetValue(output)

    def OnPing(self, e):
        # Prompt user for ping address
        address = wx.GetTextFromUser('Enter IP or address to ping:', 'Ping', '')

        # Execute ping command and set output text
        result = subprocess.run(['ping', '-c', '4', address], stdout=subprocess.PIPE)
        output = result.stdout.decode()
        self.output.SetValue(output)

    def OnSpeedtest(self, e):
        # Execute speedtest command and set output text
        result = subprocess.run(['speedtest-cli'], stdout=subprocess.PIPE)
        output = result.stdout.decode()
        self.output.SetValue(output)

    def OnWifi(self, e):
        # Get wireless environment information
        result = subprocess.run(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
        output = result.stdout.decode()

        # Set output text
        self.output.SetValue(output)

    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    NetworkMetrics(None, title='Network Metrics')
    app.MainLoop()
