import tensorflow as tf
from imageai.Prediction.Custom import CustomImagePrediction
import os
import wx


execution_path = os.getcwd()
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("idenprof_061-0.7933.h5")
prediction.setJsonPath("idenprof_model_class.json")
prediction.loadModel(num_objects=10)

def predictor(file):
    predictions, probabilities = prediction.predictImage(file, result_count=3)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
       print(eachPrediction , " : " , eachProbability)
 
def upload_image():
    if __name__ == "__main__":
        app = wx.PySimpleApp()
    wildcard = "Python source (*.py)|*.py|" \
            "Compiled Python (*.pyc)|*.pyc|" \
            "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), 
            "", wildcard, wx.FD_OPEN)
    if dialog.ShowModal() == wx.ID_OK:
       file=dialog.GetPath()
    predictor(file)
    dialog.Destroy()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          "Image Prediction")
        p = wx.Panel(self)
        btn = wx.Button(p, -1, "Choose Image")
        self.Bind(wx.EVT_BUTTON, self.OnAddItem, btn)
    def OnAddItem(self, event):
        upload_image()
    def OnExit(self, event):
        self.Close()
        
    

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()