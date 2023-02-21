import wx
import os
import subprocess
import threading

class NetworkMetrics(wx.Frame):
    def __init__(self, *args, **kw):
        super(NetworkMetrics, self).__init__(*args, **kw)
        
        # Initialize UI
        self.InitUI()
        
    def InitUI(self):
    # Set up main panel
        panel = wx.Panel(self)

        # Set up splitter window
        splitter = wx.SplitterWindow(panel, style=wx.SP_LIVE_UPDATE)

        # Set up left panel for buttons
        left_panel = wx.Panel(splitter)
        intf_btn = wx.Button(left_panel, label="Interfaces")
        intf_btn.Bind(wx.EVT_BUTTON, self.OnInterfaces)
        ping_btn = wx.Button(left_panel, label="Ping")
        ping_btn.Bind(wx.EVT_BUTTON, self.OnPing)
        speedtest_btn = wx.Button(left_panel, label="Speedtest")
        speedtest_btn.Bind(wx.EVT_BUTTON, self.OnSpeedtest)
        wifi_btn = wx.Button(left_panel, label="Wireless Environment")
        wifi_btn.Bind(wx.EVT_BUTTON, self.OnWifi)
        loadtest_btn = wx.Button(left_panel, label="Load Test")
        loadtest_btn.Bind(wx.EVT_BUTTON, self.OnLoadTest)
        quit_btn = wx.Button(left_panel, label="Quit")
        quit_btn.Bind(wx.EVT_BUTTON, self.OnQuit)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.AddSpacer(5)
        left_sizer.Add(intf_btn, 0, wx.EXPAND | wx.ALL, 5)
        left_sizer.AddSpacer(5)
        left_sizer.Add(ping_btn, 0, wx.EXPAND | wx.ALL, 5)
        left_sizer.AddSpacer(5)
        left_sizer.Add(speedtest_btn, 0, wx.EXPAND | wx.ALL, 5)
        left_sizer.AddSpacer(5)
        left_sizer.Add(wifi_btn, 0, wx.EXPAND | wx.ALL, 5)
        left_sizer.AddSpacer(5)
        left_sizer.Add(loadtest_btn, 0, wx.EXPAND | wx.ALL, 5)
        left_sizer.AddSpacer(5)
        left_sizer.Add(quit_btn, 0, wx.EXPAND | wx.ALL, 5)
        left_panel.SetSizer(left_sizer)

        # Set up right panel for output
        right_panel = wx.Panel(splitter)
        self.output = wx.TextCtrl(right_panel, style=wx.TE_MULTILINE|wx.TE_READONLY)
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer.Add(self.output, 1, wx.EXPAND | wx.ALL, 5)
        right_panel.SetSizer(right_sizer)

        # Set up splitter window
        splitter.SplitVertically(left_panel, right_panel, 200)

        # Set up sizer for main panel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND | wx.ALL, 5)

        # Set sizer for panel and show UI
        panel.SetSizer(sizer)
        self.Show(True)

    def OnInterfaces(self, e):
    # Define function to run ifconfig command
        self.output.SetValue("Running a command please wait...")
        def run_ifconfig():
            result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
            output = result.stdout.decode()
            wx.CallAfter(self.output.SetValue, output) # Update UI with output

    # Start thread to run ifconfig command
        thread = threading.Thread(target=run_ifconfig)
        thread.start()
    
    def OnPing(self, e):
        # Prompt user for ping address
        self.output.SetValue("Running a command please wait...")
        address = wx.GetTextFromUser('Enter IP or address to ping:', 'Ping', '')
        # Execute ping command and set output text
        result = subprocess.run(['ping', '-c', '4', address], stdout=subprocess.PIPE)
        output = result.stdout.decode()
        self.output.SetValue(output)

    def OnSpeedtest(self, e):
    # Define function to run speedtest command
        def speed_test():
            wx.CallAfter(self.output.SetValue, "Running a command please wait...") # Update UI with status message
            result = subprocess.run(['speedtest-cli'], stdout=subprocess.PIPE)
            output = result.stdout.decode()
            wx.CallAfter(self.output.SetValue, output) # Update UI with output

    # Start thread to run command
        thread = threading.Thread(target=speed_test)
        thread.start()

    def OnWifi(self, e):
        self.output.SetValue("Running a command please wait...")
        # Get wireless environment information
        result = subprocess.run(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
        output = result.stdout.decode()

        # Set output text
        self.output.SetValue(output)

    def OnLoadTest(self, e):
        def load_test():
        # Execute load/stress test command and set output text
            wx.CallAfter(self.output.SetValue, "Running a command please wait...") # Update UI with status message
            result = subprocess.run(['ping', '-c', '100', '-i', '0.1', '1.1.1.1'], stdout=subprocess.PIPE)
            output = result.stdout.decode()
            wx.CallAfter(self.output.SetValue, output) # Update UI with output
    # Start thread to run command
        thread = threading.Thread(target=load_test)
        thread.start()

    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    NetworkMetrics(None, title='Network Metrics')
    app.MainLoop()
