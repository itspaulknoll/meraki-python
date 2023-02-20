import wx
import subprocess

class NetworkMetricsGUI(wx.Frame):
    def __init__(self, parent, title):
        super(NetworkMetricsGUI, self).__init__(parent, title=title, size=(800, 600))
        self.panel = wx.Panel(self, wx.ID_ANY)

        # Create a label to display the network metrics
        self.metrics_label = wx.StaticText(self.panel, wx.ID_ANY, "Click the button to get network metrics", pos=(20, 20))

        # Create a button to get the network metrics
        self.metrics_button = wx.Button(self.panel, wx.ID_ANY, "Get Metrics", pos=(20, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, self.metrics_button)

        # Create a button to quit the application
        self.quit_button = wx.Button(self.panel, wx.ID_ANY, "Quit", pos=(120, 50))
        self.Bind(wx.EVT_BUTTON, self.on_quit, self.quit_button)

    def on_click(self, event):
        # Run the ifconfig command to get network metrics
        ifconfig_output = subprocess.check_output(["ifconfig", "en0"])

        # Run the airport command to get wireless network metrics
        airport_output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"])

        # Combine the output of both commands into a string
        metrics_string = ifconfig_output.decode("utf-8") + "\n" + airport_output.decode("utf-8")

        # Create a multi-line text control to display the network metrics
        self.metrics_text = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(20, 100), size=(760, 480), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Set the font size of the text control
        font = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.metrics_text.SetFont(font)

        # Insert the network metrics into the text control
        self.metrics_text.SetValue(metrics_string)

    def on_quit(self, event):
        # Close the application
        self.Close(True)

app = wx.App()
frame = NetworkMetricsGUI(None, "Network Metrics")
frame.Show()
app.MainLoop()
