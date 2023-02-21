import wx
import subprocess


class NetworkMetricsGUI(wx.Frame):
    def __init__(self, parent, title):
        super(NetworkMetricsGUI, self).__init__(parent, title=title, size=(800, 600))

        panel = wx.Panel(self)

        # Create a label to display the network metrics
        self.metrics_label = wx.StaticText(panel, -1, "Click the button to get network metrics", style=wx.ALIGN_CENTER)
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.metrics_label.SetFont(font)

        # Create a text control to display the network metrics
        self.metrics_text = wx.TextCtrl(panel, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)

        # Create a button to get the network metrics
        self.metrics_button = wx.Button(panel, label="Get Metrics")
        self.metrics_button.Bind(wx.EVT_BUTTON, self.get_metrics)

        # Create a button to quit the application
        self.quit_button = wx.Button(panel, label="Quit")
        self.quit_button.Bind(wx.EVT_BUTTON, self.OnQuit)

        # Create a horizontal box sizer for the buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddStretchSpacer()
        button_sizer.Add(self.metrics_button, 0, wx.ALL|wx.EXPAND, 10)
        button_sizer.Add(self.quit_button, 0, wx.ALL|wx.EXPAND, 10)
        button_sizer.AddStretchSpacer()

        # Create a vertical box sizer for the panel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.metrics_label, 0, wx.ALL|wx.EXPAND, 10)
        sizer.Add(self.metrics_text, 1, wx.ALL|wx.EXPAND, 10)
        sizer.Add(button_sizer, 0, wx.ALL|wx.EXPAND, 10)
        panel.SetSizerAndFit(sizer)

        self.Centre()
        self.Show()

    def get_metrics(self, event):
        # Run the ifconfig command to get network metrics
        ifconfig_output = subprocess.check_output(["ifconfig", "-a"]).decode("utf-8")

        # Run the netstat command to get network connection metrics
        netstat_output = subprocess.check_output(["netstat", "-an"]).decode("utf-8")

        # Combine the output of both commands into a string
        metrics_string = "ifconfig:\n" + ifconfig_output + "\nnetstat:\n" + netstat_output

        # Update the text control to display the network metrics
        self.metrics_text.SetValue(metrics_string)

    def OnQuit(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    frame = NetworkMetricsGUI(None, "Network Metrics")
    app.MainLoop()
